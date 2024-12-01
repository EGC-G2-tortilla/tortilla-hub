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


def resolve_user(commit):
    # Intentar obtener el nombre de usuario del autor del commit
    if commit.author:
        user_login = commit.author.login
        # Excluir usuarios específicos
        if user_login and any(excluded_user.lower() in user_login.lower() for excluded_user in EXCLUDED_USERS):
            return None
        return user_login
    else:
        # Si el autor no está disponible, usar el nombre y correo del commit
        email = commit.commit.author.email
        name = commit.commit.author.name
        key = (email, name)
        if key in user_cache:
            return user_cache[key]
        # Excluir si el nombre o el correo contienen usuarios excluidos
        combined_info = (email + name).lower()
        if any(excluded_user.lower() in combined_info for excluded_user in EXCLUDED_USERS):
            user_cache[key] = None
            return None
        if "bot" in combined_info:
            user_cache[key] = None
            return None
        # Intentar buscar el usuario en GitHub por nombre
        try:
            users = g.search_users(f'"{name}" in:name')
            for user in users:
                user_login = user.login
                if any(excluded_user.lower() in user_login.lower() for excluded_user in EXCLUDED_USERS):
                    user_cache[key] = None
                    return None
                user_cache[key] = user_login
                return user_login
        except Exception:
            pass
        # Como último recurso, usar el nombre del autor si no está en la lista de excluidos
        if any(excluded_user.lower() in name.lower() for excluded_user in EXCLUDED_USERS):
            user_cache[key] = None
            return None
        user_cache[key] = name
        return name


# Obtener estadísticas de commits con barra de progreso
def get_commit_stats():
    contributors = defaultdict(int)
    commits = list(gh_repo.get_commits())
    for commit in tqdm(commits, desc="Procesando commits para estadísticas de commits"):
        user = resolve_user(commit)
        if user:
            contributors[user] += 1
    return contributors


# Obtener líneas de código (LoC) con barra de progreso
def get_loc_stats():
    contributor_loc = defaultdict(lambda: [0, 0])  # Añadidas, eliminadas
    commits = list(gh_repo.get_commits())
    for commit in tqdm(commits, desc="Procesando commits para estadísticas de líneas de código"):
        user = resolve_user(commit)
        if not user:
            continue
        stats = commit.stats
        added = stats.additions
        deleted = stats.deletions
        contributor_loc[user][0] += added
        contributor_loc[user][1] += deleted
    return contributor_loc


# Obtener issues asignadas con barra de progreso
def get_assigned_issues():
    issues = list(gh_repo.get_issues(state="all", assignee="*"))
    issue_stats = defaultdict(int)
    for issue in tqdm(issues, desc="Procesando issues asignadas"):
        user = issue.assignee.login
        # Excluir bots y usuarios específicos
        if user and "bot" not in user.lower() \
                and not any(excluded_user.lower() in user.lower() for excluded_user in EXCLUDED_USERS):
            issue_stats[user] += 1
    return issue_stats


# Generar estadísticas
commit_stats = get_commit_stats()
loc_stats = get_loc_stats()
issue_stats = get_assigned_issues()

# Crear directorio de salida si no existe
os.makedirs('output', exist_ok=True)

# Guardar estadísticas en archivos JSON
with open('output/commit_stats.json', 'w') as f:
    json.dump(commit_stats, f)

with open('output/loc_stats.json', 'w') as f:
    json.dump(loc_stats, f)

with open('output/issue_stats.json', 'w') as f:
    json.dump(issue_stats, f)

# Visualización de estadísticas
sns.set(style="whitegrid")

# Commits por contribuidor
top_committers = sorted(commit_stats.items(), key=lambda x: x[1], reverse=True)[:13]
users, commits = zip(*top_committers)

plt.figure(figsize=(12, 6))
sns.barplot(x=list(users), y=list(commits), palette='viridis')
plt.title('Top 13 Contribuidores por Número de Commits')
plt.xlabel('Usuario')
plt.ylabel('Número de Commits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/commits_per_user.png')
plt.close()

# Líneas de código netas por contribuidor
if loc_stats:
    top_loc_contributors = sorted(
        loc_stats.items(), key=lambda x: sum(x[1]), reverse=True
    )
    users, loc = zip(*top_loc_contributors)
    added = [lines[0] for lines in loc]
    deleted = [lines[1] for lines in loc]
    net = [a - d for a, d in zip(added, deleted)]
    plt.figure(figsize=(12, 6))
    sns.barplot(x=list(users), y=net, palette='coolwarm')
    plt.title('Líneas de Código Netas por Contribuidor')
    plt.xlabel('Usuario')
    plt.ylabel('Líneas de Código Netas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/loc_per_user.png')
    plt.close()

# Issues asignadas
if issue_stats:
    top_issue_contributors = sorted(
        issue_stats.items(), key=lambda x: x[1], reverse=True
    )
    users, issues = zip(*top_issue_contributors)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=list(users), y=list(issues), palette='magma')
    plt.title('Número de Issues Asignadas por Usuario')
    plt.xlabel('Usuario')
    plt.ylabel('Issues Asignadas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/issues_per_user.png')
    plt.close()

# Salida ordenada
print("\nCommits por contribuidor:")
top_committers = sorted(commit_stats.items(), key=lambda x: x[1], reverse=True)[:13]
for user, commits in top_committers:
    print(f"  {user}: {commits}")

print("\nLíneas de código por contribuidor:")
if loc_stats:
    top_loc_contributors = sorted(
        loc_stats.items(), key=lambda x: sum(x[1]), reverse=True
    )
    for user, loc in top_loc_contributors:
        print(f"  {user}: {loc[0]} líneas añadidas, {loc[1]} líneas eliminadas")
else:
    print("  No se encontraron datos de líneas de código.")

print("\nIssues asignadas:")
if issue_stats:
    top_issue_contributors = sorted(
        issue_stats.items(), key=lambda x: x[1], reverse=True
    )
    for user, issues in top_issue_contributors:
        print(f"  {user}: {issues}")
else:
    print("  No se encontraron issues asignadas.")
