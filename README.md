<div align="center">
  <img src="https://www.uvlhub.io/static/img/logos/logo-light.svg" alt="Logo">
</div>

<div align="center">
  <h1>TORTILLA-HUB</h1>
  <h3 style="font-style: italic; font-weight: normal;">
    A fork of the UVLHub project by DiversoLab: tortilla-hub is a repository of feature models in UVL format integrated with Zenodo and flamapy following Open Science principles.
  </h3>

  <p>
    <img src="https://github.com/EGC-G2-tortilla/tortilla-hub/actions/workflows/tests.yml/badge.svg?branch=main" alt="Pytest Testing Suite">
    <img src="https://github.com/EGC-G2-tortilla/tortilla-hub/actions/workflows/commits.yml/badge.svg?branch=main" alt="Commits Syntax Checker">
  </p>

  <p>
    <img src="https://img.shields.io/github/last-commit/EGC-G2-tortilla/tortilla-hub?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/EGC-G2-tortilla/tortilla-hub?style=default&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/EGC-G2-tortilla/tortilla-hub?style=default&color=0080ff" alt="repo-language-count">
  </p>

</div>

## Table of Contents

- [Overview](#overview)
- [Project Documentation](#project-documentation)
- [Project Structure](#project-structure)
  - [Project Index](#project-index)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Testing](#testing)
- [Acknowledgments](#acknowledgments)

---

# Overview

Tortilla-hub is a fork of the UVLHub project by DiversoLab, created for the Evolution and Configuration Management (Evolución y Gestión de la configuración - EGC) course in the Software Engineering degree at the University of Seville.

This project serves as a repository for feature models in UVL format, integrated with Zenodo and Flamapy. It includes various modifications made by students of the course, providing hands-on experience in a continuous integration and deployment environment. Students have practiced automating tests and checks using GitHub Actions and collaborating effectively within multiple teams.

---

# Project Documentation

Tortilla-hub is a proyect made by two teams: tortilla-hub-1 and tortilla-hub-2. You can find all our documentation on the ``/docs`` folder in our common proyect. 

There you may find our commmon working policy checking ``/docs/Acta fundacional.md`` and our specific group documentation in our respective group folder.

---

# Project Structure

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

## Project Index

  <details>
    <summary><b>__root__</b></summary>
    <blockquote>
      <table>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
          <td>- Requirements.txt specifies the project's dependencies<br>- It lists numerous Python packages, including Flask for web framework, SQLAlchemy for database interaction, pytest for testing, and several libraries related to  feature modeling (flamapy-*)<br>- These packages provide the necessary tools and components for building and running the application.</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/setup.py'>setup.py</a></b></td>
          <td>- setup.py configures the Rosemary project for installation<br>- It defines the project's metadata, lists dependencies (Click and python-dotenv), and specifies the command-line interface (rosemary) entry point, enabling users to easily interact with the UVLHub development environment via the command line.</td>
        </tr>
      </table>
    </blockquote>
  </details>
  <details>
    <summary><b>migrations</b></summary>
    <blockquote>
      <table>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/script.py.mako'>script.py.mako</a></b></td>
          <td>- The script generates Alembic migration scripts for database schema changes.</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/env.py'>env.py</a></b></td>
          <td>- env.py configures Alembic, a database migration tool, within a Flask application</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/alembic.ini'>alembic.ini</a></b></td>
          <td>- The alembic.ini file configures Alembic, a database migration tool, for the project</td>
        </tr>
      </table>
      <details>
        <summary><b>versions</b></summary>
        <blockquote>
          <a>This folder will contain the successive versions of the migrations made for the Flask project's database. The most recent one will have the highest version number.</a>
          <table>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/versions/002.py'>002.py</a></b></td>
              <td>❯ ...</td>
            </tr>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/migrations/versions/001.py'>001.py</a></b></td>
              <td>❯ ...</td>
            </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details>
    <summary><b>rosemary</b></summary>
    <blockquote>
      <table>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/cli.py'>cli.py</a></b></td>
          <td>- Rosemary/cli.py provides a command-line interface (CLI) for streamlining project development<br>- It integrates various commands, including database management, testing, environment setup, code quality checks, and deployment aids<br>- The CLI acts as a central access point, simplifying common development tasks and improving workflow efficiency within the larger Rosemary project.</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/rosemary/__main__.py'>__main__.py</a></b></td>
          <td>- Rosemary's __main__.py serves as the application's entry point.</td>
        </tr>
      </table>
      <details>
        <summary><b>templates</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>commands</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details>
    <summary><b>docker</b></summary>
    <blockquote>
      <table>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.prod.ssl.yml'>docker-compose.prod.ssl.yml</a></b></td>
          <td>- The docker-compose.prod.ssl.yml file configures a production environment using Docker Compose<br>- It orchestrates the deployment of a web application, a MariaDB database, an Nginx reverse proxy, and Watchtower for automated container updates<br>- The configuration specifies container images, environment variables, port mappings, and volume mounts for persistent data and application resources.</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.dev.yml'>docker-compose.dev.yml</a></b></td>
          <td>- The docker-compose.dev.yml file configures a multi-container development environment<br>- It defines services for a web application, a MariaDB database, and an Nginx reverse proxy<br>- The configuration facilitates local development by linking these services, managing environment variables, and setting up necessary volumes and networks for seamless interaction<br>- The setup enables developers to run and test the application locally.</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.prod.webhook.yml'>docker-compose.prod.webhook.yml</a></b></td>
          <td>- The docker-compose.prod.webhook.yml file configures a production environment for a web application using Docker Compose<br>- It defines services for the application itself, a MariaDB database, and an Nginx web server, orchestrating their interactions and resource allocation<br>- The configuration includes environment variables, port mappings, volume mounts for persistent data and scripts, and ensures automatic restarts<br>- The setup facilitates deployment and management of the application within a containerized infrastructure.</td>
        </tr>
        <tr>
          <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/docker-compose.prod.yml'>docker-compose.prod.yml</a></b></td>
          <td>- Docker Compose orchestrates a production environment<br>- It defines and manages four containers: a web application, a MariaDB database, an Nginx reverse proxy, and a Watchtower for automated container updates<br>- The configuration maps local directories to containers, enabling persistent storage and deployment of application code, scripts, and configurations<br>- The setup ensures high availability and simplified deployment.</td>
        </tr>
      </table>
      <details>
        <summary><b>images</b></summary>
        <a>This folder will contain the latest Docker images of the webhoock, database, prodcution and development application, and necessary test environments. </a>
        <blockquote>
          <table>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.prod'>Dockerfile.prod</a></b></td>
              <td>❯ ...</td>
            </tr>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.webhook'>Dockerfile.webhook</a></b></td>
              <td>❯ ...</td>
            </tr>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.mariadb'>Dockerfile.mariadb</a></b></td>
              <td>❯ ...</td>
            </tr>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.render'>Dockerfile.render</a></b></td>
              <td>❯ ...</td>
            </tr>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.locust'>Dockerfile.locust</a></b></td>
              <td>❯ ...</td>
            </tr>
            <tr>
              <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/docker/images/Dockerfile.dev'>Dockerfile.dev</a></b></td>
              <td>❯ ...</td>
            </tr>
          </table>
        </blockquote>
      </details>
      <details>
        <summary><b>nginx</b></summary>
        <a>This folder will contain the latest Docker images of the Nginx reverse proxy, and a Watchtower for automated container updates. </a>
        <blockquote>
          <a>...</a>
          <details>
            <summary><b>html</b></summary>
            <blockquote>
              <a>...</a>
            </blockquote>
          </details>
        </blockquote>
      </details>
      <details>
        <summary><b>entrypoints</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details>
    <summary><b>vagrant</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/04_install_dependencies.yml'>04_install_dependencies.yml</a></b></td>
        <td>- The Ansible playbook configures the system to support the project's Python 3.12 environment.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/02_install_mariadb.yml'>02_install_mariadb.yml</a></b></td>
        <td>- The Ansible playbook 02_install_mariadb.yml sets up a MariaDB database server<br>- It installs MariaDB and the necessary Python library, starts and enables the service, configures the root password, and creates specified databases and a user with appropriate privileges.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/01_setup.yml'>01_setup.yml</a></b></td>
        <td>- `vagrant/01_setup.yml prepares the system for provisioning by updating the apt package cache.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/03_mariadb_scripts.yml'>03_mariadb_scripts.yml</a></b></td>
        <td>- The vagrant/03_mariadb_scripts.yml Ansible playbook configures and initializes the MariaDB database.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/06_utilities.yml'>06_utilities.yml</a></b></td>
        <td>- Ansible's 06_utilities.yml configures the Vagrant user environment.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/00_main.yml'>00_main.yml</a></b></td>
        <td>❯ ...</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/Vagrantfile'>Vagrantfile</a></b></td>
        <td>- The Vagrantfile configures a virtual machine using Ubuntu, setting up network ports, syncing folders, and provisioning via Ansible<br>- It loads environment variables from a .env file, making them accessible to the Ansible playbook and the virtual machine's shell environment<br>- This ensures consistent configuration and deployment across different environments.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/vagrant/05_run_app.yml'>05_run_app.yml</a></b></td>
        <td>❯ ...</td>
      </tr>
      </table>
    </blockquote>
  </details>
  <details>
    <summary><b>scripts</b></summary>
    <blockquote>
      <table>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/restart_container.sh'>restart_container.sh</a></b></td>
        <td>❯ Restarts the Docker container running the Flask app. </td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/wait-for-db.sh'>wait-for-db.sh</a></b></td>
        <td>❯ Waits for the database service to be up before starting the Flask app. </td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/init-testing-db.sh'>init-testing-db.sh</a></b></td>
        <td>❯ Waits for the database service to be up before starting the Flask app, likely using a connection check loop.</td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/ssl_renew.sh'>ssl_renew.sh</a></b></td>
        <td>❯ Renews SSL certificates. </td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/git_update.sh'>git_update.sh</a></b></td>
        <td>❯ Updates the project repository by pulling the latest changes from Git. </td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/ssl_setup.sh'>ssl_setup.sh</a></b></td>
        <td>❯ Sets up SSL certificates and configures the Flask app with Nginx. </td>
      </tr>
      <tr>
        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/scripts/clean_docker.sh'>clean_docker.sh</a></b></td>
        <td>❯ Cleans up unused Docker containers, images, volumes, and networks.</td>
      </tr>
      </table>
    </blockquote>
  </details>
  <details>
    <summary><b>core</b></summary>
    <blockquote>
      <a>The core folder contains the core logic of the application: application setup,  configurations, selenium configuration, serialicers and decorators, base templates, etc.</a>
      <details>
        <summary><b>bootstraps</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>selenium</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>configuration</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>blueprints</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>serialisers</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>decorators</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>locust</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>resources</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>managers</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>repositories</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>seeders</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>environment</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
      <details>
        <summary><b>services</b></summary>
        <blockquote>
          <a>...</a>
        </blockquote>
      </details>
    </blockquote>
  </details>
  <details>
    <summary><b>app</b></summary>
    <a>The app folder cotains all the application logic: all the data models, the repositories and servers of the differrent modules, and the html files for the applications views. </a>
    <blockquote>
      <details>
        <summary><b>templates</b></summary>
        <a>Base templates for the html files and common error pages. </a>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/base_template.html'>base_template.html</a></b></td>
            <td>❯ The base template that provides the layout (e.g., navigation, header, footer) for other pages. Other templates extend this. </td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/500.html'>500.html</a></b></td>
            <td>❯ Displays the 500 Internal Server Error page, shown when the server encounters an unexpected condition. </td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/404.html'>404.html</a></b></td>
            <td>❯ Renders the 404 Not Found page, displayed when a resource (e.g., URL) does not exist. </td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/401.html'>401.html</a></b></td>
            <td>❯ A 401 Unauthorized error page, shown when the user is not authenticated. </td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/templates/400.html'>400.html</a></b></td>
            <td>❯ Handles the 400 Bad Request error, usually caused by invalid client input. </td>
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
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/pytest.ini'>pytest.ini</a></b></td>
            <td>❯ ...</td>
          </tr>
          </table>
          <details>
            <summary><b>webhook</b></summary>
            <a>This folder contains the logic related to handling webhooks (HTTP callbacks triggered by external services to notify your of certain events).</a>
            <blockquote>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/webhook/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/flamapy/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
              <a>The auth folder is dedicated to handling authentication and authorization functionalities. It contains code that manages user login, registration, password management, and permissions.</a>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/templates/auth/provide_email.html'>provide_email.html</a></b></td>
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/auth/templates/auth/login_form.html'>login_form.html</a></b></td>
                        <td>❯ ...</td>
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
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/hubfile/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
              <a>This folder contains all the object modelling and business logic related to the datasets, which are one of the core elements of the uvl repository. </a>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/api.py'>api.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              </table>
              <details>
                <summary><b>uvl_examples</b></summary>
                <blockquote>
                  <table>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file6.uvl'>file6.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file7.uvl'>file7.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file5.uvl'>file5.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file4.uvl'>file4.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file1.uvl'>file1.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file3.uvl'>file3.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file2.uvl'>file2.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file9.uvl'>file9.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file12.uvl'>file12.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file8.uvl'>file8.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file10.uvl'>file10.uvl</a></b></td>
                    <td>❯ ...</td>
                  </tr>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/uvl_examples/file11.uvl'>file11.uvl</a></b></td>
                    <td>❯ ...</td>
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
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/templates/dataset/view_dataset.html'>view_dataset.html</a></b></td>
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/dataset/templates/dataset/list_datasets.html'>list_datasets.html</a></b></td>
                        <td>❯ ...</td>
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
              <a>This folder contains all the data modelling and business logic behind the FeatureModel objects. </a>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/featuremodel/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/explore/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
              <a> The profile folder handles user-related functionalities that allow users to view, update, and manage their personal data. </a>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/profile/templates/profile/summary.html'>summary.html</a></b></td>
                        <td>❯ ...</td>
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
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
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
              <a>The comunnity folder contains all the data modelling, route, business logic and views of the communities. </a>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/seeders.py'>seeders.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
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
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/community_members.html'>community_members.html</a></b></td>
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/community.html'>community.html</a></b></td>
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/index.html'>index.html</a></b></td>
                        <td>❯ ...</td>
                      </tr>
                      <tr>
                        <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/community/templates/community/create_community.html'>create_community.html</a></b></td>
                        <td>❯ ...</td>
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
              <a> The fakenodo folder contains all the services and models necessary to works with a mocked version of Zenodo. this will help to simulate as many calls to the Zenodyo API as they are necessary to test the application. </a>
              <table>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/services.py'>services.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/models.py'>models.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/forms.py'>forms.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/repositories.py'>repositories.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              <tr>
                <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/routes.py'>routes.py</a></b></td>
                <td>❯ ...</td>
              </tr>
              </table>
              <details>
                <summary><b>templates</b></summary>
                <blockquote>
                  <table>
                  <tr>
                    <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/app/modules/fakenodo/templates/index.html'>index.html</a></b></td>
                    <td>❯ ...</td>
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
  <details>
    <summary><b>.github</b></summary>
    <a>It contains configuration files and scripts related to continuous integration (CI) and continuous deployment (CD). It includes YAML files that define workflows for GitHub Actions. </a>
    <blockquote>
      <details>
        <summary><b>workflows</b></summary>
        <blockquote>
          <table>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/deployment_on_dockerhub.yml'>deployment_on_dockerhub.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/codacy.yml'>codacy.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/render.yml'>render.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/versioning.yml'>versioning.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/lint.yml'>lint.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/commits.yml'>commits.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/merge-migrations.yml'>merge-migrations.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/tests.yml'>tests.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/workflows/automatic_pr.yml'>automatic_pr.yml</a></b></td>
            <td>❯ ...</td>
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
            <td>❯ ...</td>
          </tr>
          <tr>
            <td><b><a href='https://github.com/EGC-G2-tortilla/tortilla-hub.git/blob/master/.github/ISSUE_TEMPLATE/reportar_incidencia.yml'>reportar_incidencia.yml</a></b></td>
            <td>❯ ...</td>
          </tr>
          </table>
        </blockquote>
      </details>
    </blockquote>
</details>

---

# Getting Started

## Prerequisites

Before getting started with tortilla-hub.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip / Pip3


## Installation

Install tortilla-hub.git using one of the following methods:

**Deploy on Docker:**
1. Clone the tortilla-hub.git repository:
```sh
❯ git clone https://github.com/EGC-G2-tortilla/tortilla-hub.git
```

2. Navigate to the project directory:
```sh
❯ cd tortilla-hub
```

3. Install docker and docker-compose:
**Using ``pip``** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ sudo apt update
❯ sudo apt install docker-ce docker-ce-cli containerd.io -y
❯ sudo apt install docker-compose-plugin -y
❯ sudo docker --version
❯ docker compose version
```

4. Deploy in develop:
**Using ``Docker``** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2496ED.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)
```sh
❯ docker compose -f docker/docker-compose.dev.yml up -d 
```

5. To shut down the project:
**Using ``Docker``** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2496ED.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)
```sh
❯ ddocker compose -f docker/docker-compose.dev.yml down
```

For more detailed information check https://docs.uvlhub.io/installation/installation_with_docker. 


**Deploy locally:**

For more detailed information check https://docs.uvlhub.io/installation/manual_installation.



## Testing

To run the tests we should deploy the projcet locally: https://docs.uvlhub.io/installation/manual_installation.

**Unit tests**
Run the unit test suite using the following command:
```sh
❯ rosemary test
```

If you want to run specific test modules:
```sh
❯ rosemary test <module name>
```

**Frontend tests using Selenium**
Run the unit test suite using the following command:
```sh
❯ rosemary selenium
```

If you want to run specific test modules:
```sh
❯ rosemary selenium <module name>
```

**Load tests using Locust**
Run the unit test suite using the following command:
```sh
❯ rosemary locust
```

If you want to run specific test modules:
```sh
❯ rosemary locust <module name>
```

---


# Acknowledgments

In this section you can find all the contributors of each team:


**Tortilla Hub 1:**

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/DelfinSR">
                <img src="https://avatars.githubusercontent.com/u/91948384?v=4" width="100px;" alt="Delfín Santana Rubio"/>
                <br />
                <sub><b>Delfín Santana Rubio</b></sub>
            </a>
        </td>
               <td align="center">
            <a href="https://github.com/antoniommff">
                <img src="https://avatars.githubusercontent.com/u/91947070?v=4" width="100px;" alt="Antonio Macías Ferrera"/>
                <br />
                <sub><b>Antonio Macías Ferrera</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/guaridpin">
                <img src="https://avatars.githubusercontent.com/u/114622587?v=4" width="100px;" alt="Guadalupe Ridruejo Pineda"/>
                <br />
                <sub><b>Guadalupe Ridruejo Pineda</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/josemicpy">
                <img src="https://avatars.githubusercontent.com/u/62075385?v=4" width="100px;" alt="José Miguel Iborra"/>
                <br />
                <sub><b>José Miguel Iborra</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/danvelcam">
                <img src="https://avatars.githubusercontent.com/u/93273683?v=4" width="100px;" alt="Daniel Vela Camacho"/>
                <br />
                <sub><b>Daniel Vela Camacho</b></sub>
            </a>
        </td>
                      <td align="center">
            <a href="https://github.com/Letee2">
                <img src="https://avatars.githubusercontent.com/u/91889823?v=4" width="100px;" alt="Pablo Fernández Pérez"/>
                <br />
                <sub><b>Pablo Fernández Pérez</b></sub>
            </a>
        </td>
                      <td align="center">
            <a href="https://github.com/benjimrfl">
                <img src="https://avatars.githubusercontent.com/u/91946757?v=4" width="100px;" alt="Benjamín Ignacio Maureira Flores"/>
                <br />
                <sub><b>Benjamín Ignacio Maureira Flores</b></sub>
            </a>
        </td>
</table>


**Tortilla Hub 2:**

<table>
                <td align="center">
            <a href="https://github.com/DaniFdezCab">
                <img src="https://avatars.githubusercontent.com/u/92794081?v=4" width="100px;" alt="Daniel Fernández Caballero"/>
                <br />
                <sub><b>Daniel Fernández Caballero</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/manbarjim2">
                <img src="https://avatars.githubusercontent.com/u/80253313?v=4" width="100px;" alt="Manuel Francisco Barcia Jiménez"/>
                <br />
                <sub><b>Manuel Francisco Barcia Jiménez</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/rgavira123">
                <img src="https://avatars.githubusercontent.com/u/91947011?v=4" width="100px;" alt="Ramón Gavira Sánchez"/>
                <br />
                <sub><b>Ramón Gavira Sánchez</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/rafpulcif">
                <img src="https://avatars.githubusercontent.com/u/91948036?v=4" width="100px;" alt="Rafael Pulido Cifuentes"/>
                <br />
                <sub><b>Rafael Pulido Cifuentes</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/Danielruizlopezcc">
                <img src="https://avatars.githubusercontent.com/u/91948447?v=4" width="100px;" alt="Daniel Ruiz López"/>
                <br />
                <sub><b>Daniel Ruiz López</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/albcarsic">
                <img src="https://avatars.githubusercontent.com/u/91947046?v=4" width="100px;" alt="Alberto Carmona Sicre"/>
                <br />
                <sub><b>Alberto Carmona Sicre</b></sub>
            </a>
        </td>
    </tr>
</table>

---

