import os
import json
from collections import defaultdict
from github import Github
from git import Repo
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

# Repositorio local y token de acceso personal
REPO_PATH = "."
GITHUB_TOKEN = os.getenv("STATISTICS")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")

# API Client para GitHub
g = Github(GITHUB_TOKEN)
gh_repo = g.get_repo(REPO_NAME)
local_repo = Repo(REPO_PATH)

# Caché para mapear correos electrónicos a nombres de usuario
user_cache = {}

# Lista de usuarios a excluir (nombres de usuario y nombres de autor)
EXCLUDED_USERS = ["github-actions[bot]", "semantic-release-bot"]

# Lista de usuarios permitidos
INCLUDED_USERS = ["DelfinSR", "Pablo Fernández", "Letee2", "guaridpin", "Danielruizlopezcc", "rafpulcif",
                  "josemicpy", "danvelcam", "benjimrfl", "Alberto Carmona Sicre",
                  "manbarjim2", "DaniFdezCab", "antoniommff", "rgavira123", "albcarsic"]


def resolve_user(commit):
    if commit.author:
        user_login = commit.author.login
        if user_login and user_login in INCLUDED_USERS:
            return user_login
    else:
        email = commit.commit.author.email
        name = commit.commit.author.name
        key = (email, name)
        if key in user_cache:
            return user_cache[key]
        if name not in INCLUDED_USERS:
            user_cache[key] = None
            return None
        user_cache[key] = name
        return name


def get_commit_stats():
    """
    Obtiene el número de commits aportados por cada contribuidor.
    """
    contributors = defaultdict(int)
    commits = list(gh_repo.get_commits())
    with tqdm(total=len(commits), desc="Procesando commits", dynamic_ncols=True, leave=False) as pbar:
        for commit in commits:
            user = resolve_user(commit)
            if user:
                contributors[user] += 1
            pbar.update(1)
    return contributors


def get_loc_stats():
    """
    Obtiene las líneas de código añadidas por cada contribuidor,
    excluyendo los commits que sean merges de pull requests.
    """
    contributor_loc = defaultdict(lambda: [0, 0])  # Añadidas, eliminadas
    commits = list(gh_repo.get_commits())

    with tqdm(total=len(commits), desc="Procesando líneas de código", dynamic_ncols=True, leave=False) as pbar:
        for commit in commits:
            # Filtrar commits que sean merges de pull requests
            if "Merge pull request" in commit.commit.message or "Merge branch" in commit.commit.message:
                pbar.update(1)
                continue

            user = resolve_user(commit)
            if not user:
                pbar.update(1)
                continue

            # Obtener estadísticas del commit
            stats = commit.stats
            added = stats.additions
            deleted = stats.deletions
            contributor_loc[user][0] += added
            contributor_loc[user][1] += deleted

            pbar.update(1)

    return contributor_loc


def get_assigned_issues():
    """
    Obtiene las estadísticas de issues asignadas, considerando que
    una issue puede tener múltiples contribuidores asignados.
    """
    issues = list(gh_repo.get_issues(state="all"))
    issue_stats = defaultdict(int)
    with tqdm(total=len(issues), desc="Procesando issues asignadas", dynamic_ncols=True, leave=False) as pbar:
        for issue in issues:
            assignees = issue.assignees  # Obtiene una lista de todos los asignados a la issue
            if not assignees:
                pbar.update(1)
                continue  # Saltar issues sin asignados
            for assignee in assignees:
                user = assignee.login
                if user and user in INCLUDED_USERS:  # Validar que el usuario esté permitido
                    issue_stats[user] += 1
            pbar.update(1)
    return issue_stats


print("\nEstadísticas de contribución para el proyecto Tortilla-hub:")

commit_stats = get_commit_stats()
loc_stats = get_loc_stats()
issue_stats = get_assigned_issues()

os.makedirs('output', exist_ok=True)

with open('output/commit_stats.json', 'w') as f:
    json.dump(commit_stats, f)

with open('output/loc_stats.json', 'w') as f:
    json.dump(loc_stats, f)

with open('output/issue_stats.json', 'w') as f:
    json.dump(issue_stats, f)


sns.set(style="whitegrid")

top_committers = sorted(commit_stats.items(), key=lambda x: x[1], reverse=True)[:13]
users, commits = zip(*top_committers)

plt.figure(figsize=(16, 6))
sns.barplot(x=list(users), y=list(commits), palette='viridis', hue=list(users), dodge=False)
plt.title('Contribuidores por Número de Commits')
plt.xlabel('Usuario')
plt.ylabel('Número de Commits')
plt.xticks(rotation=45)
plt.legend([], [], frameon=False)
plt.tight_layout()
plt.savefig('output/commits_per_user.png')
plt.close()

if loc_stats:
    top_loc_contributors = sorted(
        loc_stats.items(), key=lambda x: sum(x[1]), reverse=True
    )
    users, loc = zip(*top_loc_contributors)
    added = [lines[0] for lines in loc]
    deleted = [lines[1] for lines in loc]
    net = [a - d for a, d in zip(added, deleted)]
    plt.figure(figsize=(16, 6))
    sns.barplot(x=list(users), y=net, palette='coolwarm', hue=list(users), dodge=False)
    plt.title('Líneas de Código Netas por Contribuidor')
    plt.xlabel('Usuario')
    plt.ylabel('Líneas de Código Netas')
    plt.xticks(rotation=45)
    plt.legend([], [], frameon=False)
    plt.tight_layout()
    plt.savefig('output/loc_per_user.png')
    plt.close()

if issue_stats:
    top_issue_contributors = sorted(
        issue_stats.items(), key=lambda x: x[1], reverse=True
    )
    users, issues = zip(*top_issue_contributors)
    plt.figure(figsize=(16, 6))
    sns.barplot(x=list(users), y=list(issues), palette='magma', hue=list(users), dodge=False)
    plt.title('Número de Issues Asignadas por Usuario')
    plt.xlabel('Usuario')
    plt.ylabel('Issues Asignadas')
    plt.xticks(rotation=45)
    plt.legend([], [], frameon=False)
    plt.tight_layout()
    plt.savefig('output/issues_per_user.png')
    plt.close()


print("\nCommits por contribuidor:")
for user, commits in top_committers:
    print(f"  {user}: {commits}")

print("\nLíneas de código netas por contribuidor:")
for user, loc in top_loc_contributors:
    print(f"  {user}: {loc[0]} añadidas, {loc[1]} eliminadas (netas: {loc[0] - loc[1]})")

print("\nIssues asignadas:")
for user, issues in top_issue_contributors:
    print(f"  {user}: {issues}")
