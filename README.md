<div style="text-align: center;">
  <img src="https://www.uvlhub.io/static/img/logos/logo-light.svg" alt="Logo">
</div>

<p style="text-align: center;">
  <h1 align="center">TORTILLA-HUB</h1>
</p>
<p style="text-align: center;">
  <em><code>❯ A fork of the UVLHub project by DiversoLab: tortilla-hub is a repository of feature models in UVL format integrated with Zenodo and flamapy following Open Science principles. </code></em>
</p>
<p style="align: center;">

  <a href="">[![Pytest Testing Suite](https://github.com/diverso-lab/uvlhub/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/diverso-lab/uvlhub/actions/workflows/tests.yml)</a>

  <a href="">[![Commits Syntax Checker](https://github.com/diverso-lab/uvlhub/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/diverso-lab/uvlhub/actions/workflows/commits.yml)</a>

</p>

<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
  <!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Documentation](#-project-documentation)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>❯ REPLACE-ME</code>

---

##  Project Structure

```sh
└── tortilla-hub.git/
    ├── .github/
    │   ├── ISSUE_TEMPLATE/
    │   └── workflows/
    ├── CHANGELOG.md
    ├── README.md
    ├── app/
    │   ├── modules/
    │   ├── static/
    │   └── templates/
    ├── core/
    │   ├── ...
    ├── docker/
    │   ├── ...
    ├── docs/
    │   ├── Acta fundacional.md
    │   ├── tortilla-hub-1/
    │   └── tortilla-hub-2/
    ├── migrations/
    │   ├── ...
    ├── requirements.txt
    ├── rosemary/
    │   ├── commands/
    │   └── templates/
    ├── scripts/
    │   ├── ...
    └── vagrant/
        ├── ...
```


###  Project Index
<details open>
  <summary><b><code>TORTILLA-HUB.GIT/</code></b></summary>
  <details> <!-- __root__ Submodule -->
    <summary><b>__root__</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
        <td>- Requirements.txt specifies the project's dependencies<br>- It lists numerous Python packages, including Flask for web framework, SQLAlchemy for database interaction, pytest for testing, and several libraries related to  feature modeling (flamapy-*)<br>- These packages provide the necessary tools and components for building and running the application.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/setup.py'>setup.py</a></b></td>
        <td>- `setup.py` configures the Rosemary project for installation<br>- It defines the project's metadata, lists dependencies (Click and python-dotenv), and specifies the command-line interface (`rosemary`) entry point, enabling users to easily interact with the UVLHub development environment via the command line.</td>
      </tr>
      </table>
    </blockquote>
  </details>
  <details> <!-- migrations Submodule -->
    <summary><b>migrations</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/script.py.mako'>script.py.mako</a></b></td>
        <td>- The script generates Alembic migration scripts for database schema changes<br>- It defines upgrade and downgrade functions to manage database evolution,  integrating with SQLAlchemy for database interactions<br>- The generated scripts are part of the project's database migration system, ensuring consistent and controlled schema updates across different database versions.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/env.py'>env.py</a></b></td>
        <td>- `env.py` configures Alembic, a database migration tool, within a Flask application<br>- It bridges Alembic with Flask-SQLAlchemy, dynamically determining the database URL and connection<br>- The script executes database migrations, either offline using a URL or online via a live database connection, preventing unnecessary migrations when the schema is unchanged<br>- This ensures database schema synchronization throughout the application's lifecycle.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/alembic.ini'>alembic.ini</a></b></td>
        <td>- The `alembic.ini` file configures Alembic, a database migration tool, for the project<br>- It specifies logging levels for SQLAlchemy, Alembic, and Flask-Migrate, ensuring proper tracking of database schema changes<br>- This facilitates database version control and smooth deployment across different environments by managing database schema evolution.</td>
      </tr>
      </table>
      <details>
        <summary><b>versions</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/versions/002.py'>002.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/versions/001.py'>001.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details> <!-- rosemary Submodule -->
    <summary><b>rosemary</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/cli.py'>cli.py</a></b></td>
        <td>- Rosemary/cli.py provides a command-line interface (CLI) for streamlining project development<br>- It integrates various commands, including database management, testing, environment setup, code quality checks, and deployment aids<br>- The CLI acts as a central access point, simplifying common development tasks and improving workflow efficiency within the larger Rosemary project.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/__main__.py'>__main__.py</a></b></td>
        <td>- Rosemary's `__main__.py` serves as the application's entry point<br>- It initializes and runs the command-line interface (CLI), providing the primary user interaction mechanism for the entire rosemary application<br>- The CLI handles user commands, orchestrating the execution of the application's core functionalities<br>- Essentially, it acts as the main interface for interacting with the rosemary project.</td>
      </tr>
      </table>
      <details>
        <summary><b>templates</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_templates_index.html.j2'>module_templates_index.html.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_repositories.py.j2'>module_repositories.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_forms.py.j2'>module_forms.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_tests_test_unit.py.j2'>module_tests_test_unit.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_scripts.js.j2'>module_scripts.js.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_tests_locustfile.py.j2'>module_tests_locustfile.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_init.py.j2'>module_init.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_routes.py.j2'>module_routes.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_tests_test_selenium.py.j2'>module_tests_test_selenium.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_seeders.py.j2'>module_seeders.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_models.py.j2'>module_models.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/templates/module_services.py.j2'>module_services.py.j2</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>commands</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/update.py'>update.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/db_migrate.py'>db_migrate.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/clear_cache.py'>clear_cache.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/route_list.py'>route_list.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/db_reset.py'>db_reset.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/env.py'>env.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/compose_env.py'>compose_env.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/coverage.py'>coverage.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/selenium.py'>selenium.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/test.py'>test.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/clear_log.py'>clear_log.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/make_module.py'>make_module.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/db_seed.py'>db_seed.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/info.py'>info.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/linter.py'>linter.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/clear_uploads.py'>clear_uploads.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/locust.py'>locust.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/db_console.py'>db_console.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/commands/module_list.py'>module_list.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details> <!-- docker Submodule -->
    <summary><b>docker</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.prod.ssl.yml'>docker-compose.prod.ssl.yml</a></b></td>
        <td>- The docker-compose.prod.ssl.yml file configures a production environment using Docker Compose<br>- It orchestrates the deployment of a web application, a MariaDB database, an Nginx reverse proxy, and Watchtower for automated container updates<br>- The configuration specifies container images, environment variables, port mappings, and volume mounts for persistent data and application resources.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.dev.yml'>docker-compose.dev.yml</a></b></td>
        <td>- The `docker-compose.dev.yml` file configures a multi-container development environment<br>- It defines services for a web application, a MariaDB database, and an Nginx reverse proxy<br>- The configuration facilitates local development by linking these services, managing environment variables, and setting up necessary volumes and networks for seamless interaction<br>- The setup enables developers to run and test the application locally.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.prod.webhook.yml'>docker-compose.prod.webhook.yml</a></b></td>
        <td>- The `docker-compose.prod.webhook.yml` file configures a production environment for a web application using Docker Compose<br>- It defines services for the application itself, a MariaDB database, and an Nginx web server, orchestrating their interactions and resource allocation<br>- The configuration includes environment variables, port mappings, volume mounts for persistent data and scripts, and ensures automatic restarts<br>- The setup facilitates deployment and management of the application within a containerized infrastructure.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.prod.yml'>docker-compose.prod.yml</a></b></td>
        <td>- Docker Compose orchestrates a production environment<br>- It defines and manages four containers: a web application, a MariaDB database, an Nginx reverse proxy, and a Watchtower for automated container updates<br>- The configuration maps local directories to containers, enabling persistent storage and deployment of application code, scripts, and configurations<br>- The setup ensures high availability and simplified deployment.</td>
      </tr>
      </table>
      <details>
        <summary><b>images</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.prod'>Dockerfile.prod</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.webhook'>Dockerfile.webhook</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.mariadb'>Dockerfile.mariadb</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.render'>Dockerfile.render</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.locust'>Dockerfile.locust</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.dev'>Dockerfile.dev</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>nginx</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/nginx/nginx.prod.ssl.conf.template'>nginx.prod.ssl.conf.template</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/nginx/nginx.dev.conf'>nginx.dev.conf</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/nginx/nginx.prod.conf'>nginx.prod.conf</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/nginx/nginx.prod.no-ssl.conf.template'>nginx.prod.no-ssl.conf.template</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
          <details>
            <summary><b>html</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/nginx/html/502_dev.html'>502_dev.html</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/nginx/html/502_prod.html'>502_prod.html</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
            </blockquote>
          </details>
        </blockquote>
      </details>
      <details>
        <summary><b>entrypoints</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/entrypoints/development_entrypoint.sh'>development_entrypoint.sh</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/entrypoints/production_entrypoint.sh'>production_entrypoint.sh</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/entrypoints/render_entrypoint.sh'>render_entrypoint.sh</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details> <!-- vagrant Submodule -->
    <summary><b>vagrant</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/04_install_dependencies.yml'>04_install_dependencies.yml</a></b></td>
        <td>- The Ansible playbook configures the system to support the project's Python 3.12 environment<br>- It adds necessary repositories, installs Python 3.12 and related packages,  installs pip and setuptools, creates a virtual environment, and installs project dependencies specified in requirements.txt, ensuring a consistent development environment.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/02_install_mariadb.yml'>02_install_mariadb.yml</a></b></td>
        <td>- The Ansible playbook `02_install_mariadb.yml` sets up a MariaDB database server<br>- It installs MariaDB and the necessary Python library, starts and enables the service, configures the root password, and creates specified databases and a user with appropriate privileges<br>- Finally, it cleans up temporary files<br>- This ensures a functional MariaDB instance is ready for application use.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/01_setup.yml'>01_setup.yml</a></b></td>
        <td>- `vagrant/01_setup.yml` prepares the system for provisioning by updating the apt package cache<br>- Within the larger project's infrastructure setup, this Ansible playbook ensures all target hosts have access to the latest package information, a crucial prerequisite for subsequent configuration and software installation tasks<br>- It streamlines the initial system preparation phase.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/03_mariadb_scripts.yml'>03_mariadb_scripts.yml</a></b></td>
        <td>- The `vagrant/03_mariadb_scripts.yml` Ansible playbook configures and initializes the MariaDB database<br>- It sets permissions for database setup scripts, waits for the database to become available, and then executes scripts to initialize the main and test databases, using environment variables for database credentials and paths<br>- This ensures the database is ready for the application.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/06_utilities.yml'>06_utilities.yml</a></b></td>
        <td>- Ansible's `06_utilities.yml` configures the Vagrant user environment<br>- It modifies the `.bashrc` file to automatically activate a virtual environment and change the working directory upon login<br>- This ensures consistent project setup and simplifies the user experience within the Vagrant environment, contributing to the overall project's automation and reproducibility.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/00_main.yml'>00_main.yml</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/Vagrantfile'>Vagrantfile</a></b></td>
        <td>- The Vagrantfile configures a virtual machine using Ubuntu, setting up network ports, syncing folders, and provisioning via Ansible<br>- It loads environment variables from a `.env` file, making them accessible to the Ansible playbook and the virtual machine's shell environment<br>- This ensures consistent configuration and deployment across different environments.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/05_run_app.yml'>05_run_app.yml</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      </table>
    </blockquote>
  </details>
  <details> <!-- scripts Submodule -->
    <summary><b>scripts</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/restart_container.sh'>restart_container.sh</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/wait-for-db.sh'>wait-for-db.sh</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/init-testing-db.sh'>init-testing-db.sh</a></b></td>
        <td>- The script initializes a MariaDB test database<br>- It leverages environment variables to connect to the MariaDB server and creates the specified test database, ensuring it's configured with the correct character set and granting all privileges to the designated test user<br>- This setup facilitates automated testing within the broader project by providing a dedicated, clean database environment.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/ssl_renew.sh'>ssl_renew.sh</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/git_update.sh'>git_update.sh</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/ssl_setup.sh'>ssl_setup.sh</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/clean_docker.sh'>clean_docker.sh</a></b></td>
        <td><code>❯ REPLACE-ME</code></td>
      </tr>
      </table>
    </blockquote>
  </details>
  <details> <!-- core Submodule -->
    <summary><b>core</b></summary>
    <blockquote>
      <details>
        <summary><b>bootstraps</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/bootstraps/locustfile_bootstrap.py'>locustfile_bootstrap.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>selenium</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/selenium/common.py'>common.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>configuration</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/configuration/configuration.py'>configuration.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>blueprints</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/blueprints/base_blueprint.py'>base_blueprint.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>serialisers</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/serialisers/serializer.py'>serializer.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>decorators</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/decorators/decorators.py'>decorators.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>locust</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/locust/common.py'>common.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>resources</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/resources/generic_resource.py'>generic_resource.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>managers</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/managers/module_manager.py'>module_manager.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/managers/config_manager.py'>config_manager.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/managers/logging_manager.py'>logging_manager.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/managers/error_handler_manager.py'>error_handler_manager.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>repositories</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/repositories/BaseRepository.py'>BaseRepository.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>seeders</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/seeders/BaseSeeder.py'>BaseSeeder.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>environment</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/environment/host.py'>host.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>services</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/core/services/BaseService.py'>BaseService.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details> <!-- app Submodule -->
    <summary><b>app</b></summary>
    <blockquote>
      <details>
        <summary><b>templates</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/base_template.html'>base_template.html</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/500.html'>500.html</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/404.html'>404.html</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/401.html'>401.html</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/400.html'>400.html</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>modules</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/conftest.py'>conftest.py</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/pytest.ini'>pytest.ini</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
          <details>
            <summary><b>webhook</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>webhook</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/templates/webhook/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>flamapy</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>flamapy</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/templates/flamapy/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>auth</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>auth</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/templates/auth/signup_form.html'>signup_form.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/templates/auth/provide_email.html'>provide_email.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/templates/auth/login_form.html'>login_form.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>hubfile</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>hubfile</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/templates/hubfile/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>dataset</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/api.py'>api.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>uvl_examples</b></summary>
                <blockquote>
                  <table>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file6.uvl'>file6.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file7.uvl'>file7.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file5.uvl'>file5.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file4.uvl'>file4.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file1.uvl'>file1.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file3.uvl'>file3.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file2.uvl'>file2.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file9.uvl'>file9.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file12.uvl'>file12.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file8.uvl'>file8.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file10.uvl'>file10.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file11.uvl'>file11.uvl</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  </table>
                </blockquote>
              </details>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>dataset</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/templates/dataset/upload_dataset.html'>upload_dataset.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/templates/dataset/view_dataset.html'>view_dataset.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/templates/dataset/list_datasets.html'>list_datasets.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>featuremodel</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>featuremodel</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/templates/featuremodel/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>explore</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>explore</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/templates/explore/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>public</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/public/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>public</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/public/templates/public/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>profile</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>profile</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/templates/profile/edit.html'>edit.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/templates/profile/summary.html'>summary.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>team</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/team/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>team</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/team/templates/team/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>community</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/seeders.py'>seeders.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <details>
                    <summary><b>community</b></summary>
                    <blockquote>
                      <table>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/community_info.html'>community_info.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/community_members.html'>community_members.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/community.html'>community.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/index.html'>index.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/create_community.html'>create_community.html</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                      </tr>
                      </table>
                    </blockquote>
                  </details>
                </blockquote>
              </details>
            </blockquote>
          </details>
          <details>
            <summary><b>fakenodo</b></summary>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/services.py'>services.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/repositories.py'>repositories.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/routes.py'>routes.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <table>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/templates/index.html'>index.html</a></b></td>
                    <td><code>❯ REPLACE-ME</code></td>
                  </tr>
                  </table>
                </blockquote>
              </details>
            </blockquote>
          </details>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details> <!-- .github Submodule -->
    <summary><b>.github</b></summary>
    <blockquote>
      <details>
        <summary><b>workflows</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/deployment_on_dockerhub.yml'>deployment_on_dockerhub.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/codacy.yml'>codacy.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/render.yml'>render.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/versioning.yml'>versioning.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/lint.yml'>lint.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/commits.yml'>commits.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/merge-migrations.yml'>merge-migrations.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/tests.yml'>tests.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/automatic_pr.yml'>automatic_pr.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>ISSUE_TEMPLATE</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/ISSUE_TEMPLATE/generic_issue.yml'>generic_issue.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/ISSUE_TEMPLATE/reportar_incidencia.yml'>reportar_incidencia.yml</a></b></td>
            <td><code>❯ REPLACE-ME</code></td>
          </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
  </details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with tortilla-hub.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip / Pip3


###  Installation

Install tortilla-hub.git using one of the following methods:

**Build from source:**

1. Clone the tortilla-hub.git repository:
```sh
❯ git clone https://github.com/EGC-G2-tortilla/tortilla-hub.git
```

2. Navigate to the project directory:
```sh
❯ cd tortilla-hub.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run tortilla-hub.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Documentation


---
##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
