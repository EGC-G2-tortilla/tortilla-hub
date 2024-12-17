# TORTILLA-HUB-1

* Grupo 2  
* Curso escolar: 2024/2025  
* Asignatura: Evolución y Gestión de la Configuración

## Miembros

| Miembro | Implicación |
| :---- | :---- |
| Fernández Pérez, Pablo | 10 |
| Iborra Conejo, José Miguel | 6 |
| Macías Ferrera, Antonio | 10 |
| Maureira Flores, Benjamín Ignacio | 7 |
| Ridruejo Pineda, Guadalupe | 10|
| Santana Rubio, Delfín | 10 |
| Vela Camacho, Daniel | 10 |

## Índice

[Indicadores del Proyecto](#indicadores-del-proyecto)

[Descripción de los Work Items implementados](#descripción-de-los-work-items-implementados)

[Integración con otros equipos](#integración-con-otros-equipos)

[Resumen Ejecutivo (800 palabras)](#resumen-ejecutivo-\(800-palabras\))

[Descripción del sistema (1500 palabras)](#descripción-del-sistema-\(1500-palabras\))

[Visión global del proceso de desarrollo (1500 palabras)](#visión-global-del-proceso-de-desarrollo-\(1500-palabras\))

[Entorno de desarrollo (800 palabras)](#entorno-de-desarrollo-\(800-palabras\))

[Ejercicio de propuesta de cambio](#ejercicio-de-propuesta-de-cambio)

[Conclusiones y trabajo futuro](#conclusiones-y-trabajo-futuro)

# Indicadores del Proyecto

| Miembro del equipo | Horas | Commits | LoC | Test | Issues | Work Item |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Fernández Pérez, Pablo | 13h | 40  |+1090 -322   |  | 16 | Upload, analyse and repair UVL |
| Iborra Conejo, José Miguel | 14h 13min |24  |+4074 -823  |  |5  | Rate datasets / models |
| Macías Ferrera, Antonio |28h 13min  |57  |+12940 -4462  |  |17  | Dashboard |
| Maureira Flores, Benjamín Ignacio |20h 41min  |27  |+13418 -74  |  |8  | Sync with github/gitlab |
| Ridruejo Pineda, Guadalupe | 36h 8min |  |  |  |  | Improve UI |
| Santana Rubio, Delfín |16h 57min  |90  |+5833 -2684  | 52 |26  | Create communities |
| Vela Camacho, Daniel |21h 3min  |58  |+2863 -1530  |  |25  | Staging area |
| **TOTAL** |  |  |  |  |  |  |


# Descripción de los Work Items implementados

## **1. Upload, Analyse, and Repair UVL:**
Esta funcionalidad permite a los usuarios cargar archivos UVL (Universal Variability Language) y verificar su validez sintáctica. Si se detectan errores, el sistema indica la línea exacta donde ocurren, ayudando al usuario a corregirlos. Esto resuelve una necesidad clave: evitar que los usuarios suban archivos UVL con errores cuando cargan un nuevo dataset a UVLHub. Anteriormente, no existía un sistema de comprobación, lo que dificultaba la detección de errores. 

## **2. Rate Datasets:**
Se ha desarrollado un sistema de calificación para que los usuarios puedan evaluar datasets. Esta funcionalidad incluye:

- Sistema de valoración mediante estrellas: Los usuarios pueden asignar una puntuación a un dataset y actualizarla si lo desean.

- Cálculo y visualización de estadísticas: Se muestra la puntuación media y el número total de calificaciones para cada dataset, ofreciendo a otros usuarios información relevante sobre la calidad del contenido.

## **3. Dashboard:**
Se ha modificado la pantalla principal ("Home") para mostrar datos y estadísticas relevantes sobre los datasets. Esta vista inicial permite a los usuarios logueados tener una visión general del contenido más destacado y del estado de los datasets disponibles en el sistema. Dentro de este DAshboard, podremos visualizar un rankin de los datasets más descargados, los últimos subidos, los autores más populares y otras estadísitcas de la web.

## **4. Sync with GitHub/GitLab:**
Se ha implementado la sincronización con plataformas como GitHub y GitLab para facilitar la gestión de modelos UVL. Los usuarios pueden iniciar sesión en estas plataformas desde la vista de "Upload Dataset" y, al cargar un dataset a Zenodo, también pueden subirlo automáticamente a un repositorio personal en GitHub o GitLab, integrando ambas plataformas en el flujo de trabajo.

## **5. Improve UI:**
Se ha mejorado la interfaz de usuario para que la enumeración del contenido de los datasets sea lo más similar posible a la experiencia ofrecida por GitHub. Este cambio busca mejorar la usabilidad, basándose en el principio de previsibilidad, facilitando la navegación y el uso intuitivo del sistema.

## **6. Create Communities:**
Se ha introducido la funcionalidad de comunidades en UVLHub.io, permitiendo a los usuarios:

- Crear y listar comunidades.
- Solicitar unirse a una comunidad y, tras la aprobación del administrador, integrarse a ella.
- Subir datasets específicos a comunidades.
- Cada comunidad cuenta con un administrador que gestiona las solicitudes de para unirse a una comunidad, asegurando un control adecuado sobre los miembros y el contenido compartido. El administrador es quien crea la comunidad.

## **7. Staging Area:**
Se ha diseñado una "zona de preparación" que permite a los usuarios gestionar sus datasets antes de publicarlos en plataformas como Zenodo o Fakenodo. Esta área ofrece:

- Selección de datasets: Los usuarios pueden decidir qué datasets quieren publicar y cuáles mantener en estado privado.
- Edición previa a la publicación: Se permite realizar modificaciones en los metadatos, corregir errores o ajustar cualquier aspecto del dataset antes de su publicación final.
- Indicador de estado: Cada dataset tiene un indicador que muestra si está listo para ser publicado, en proceso de revisión o pendiente de ajustes.

Esta funcionalidad proporciona flexibilidad, control y asegura que el contenido cumpla con los estándares de calidad antes de hacerse público.


# Integración con otros equipos 

Este proyecto es el resultado de la colaboración entre los equipos **Tortilla-Hub-1** (nuestro equipo) y **Tortilla-Hub-2**. 

Desde el inicio, se celebró una reunión conjunta en la que se definieron los acuerdos fundamentales que guiarían todo el desarrollo del proyecto. En esta reunión, se tomaron las siguientes decisiones clave:

- **Asignación de Work Items:** Se estableció claramente qué _Work Items_ serían responsabilidad de cada equipo.
- **Uso de un repositorio común:** Se decidió trabajar desde el principio en un repositorio compartido ([tortilla-hub](https://github.com/EGC-G2-tortilla/tortilla-hub)) para minimizar posibles errores y conflictos durante la integración de los subproyectos.
- **Definición de pautas de trabajo:** Todas las normas y directrices relacionadas con la gestión del repositorio y del código fuente quedaron documentadas en el ([Acta de Constitución](https://github.com/EGC-G2-tortilla/tortilla-hub/blob/main/docs/Acta%20fundacional.md)), garantizando un desarrollo ordenado y coordinado. Estas pautas han sido cumplidas satisfactoriamente por ambos equipos.

Guadalupe Ridruejo Pineda asumió el rol de coordinadora, asegurando una correcta sincronización entre los equipos. Además, se mantuvo una comunicación diaria a través de un grupo común de **WhatsApp**, lo que facilitó una colaboración fluida y eficiente a lo largo de todo el proyecto. 

# Resumen Ejecutivo

Tortilla-hub es un fork del proyecto UVLHub de DiversoLab, creado para la asignatura Evolución y Gestión de la configuración (EGC) del grado en Ingeniería del Software de la Universidad de Sevilla desarrollado gracias a la colaboración de dos equipos: **tortilla-hub-1** y **tortilla-hub-2**.

Este proyecto sirve como repositorio de modelos de características en formato UVL, integrado con Zenodo y Flamapy. Incluye varias modificaciones realizadas por los estudiantes del curso, lo que proporciona experiencia práctica en un entorno de implementación e integración continua. Los estudiantes han practicado la automatización de pruebas y verificaciones mediante GitHub Actions y han colaborado de manera eficaz dentro de varios equipos. 

Tortilla-hub-1 ha realizado una serie de contribuciones al proyecto para mejorar y ampliar su funcionalidad entre las que se incluyen: calificación y publicación de datasets, carga y verificación de datasets, integración con plataformas externas como GitHub y GitLab, la creación y gestión de comunidades. Además, se han añadido modificaciones en el diseño y la interfaz de la aplicación web para mantener altos estándares de usabilidad y eficiencia.

El proyecto incluye, además, funcionalidades clave como _staging area_ para gestionar datasets antes de su publicación definitiva, un dashboard interactivo para visualizar estadísticas y datos relevantes, y mecanismos de validación automática de UVLs para garantizar y consistencia de los datos. Asimismo, se han integrado flujos de trabajo automatizados para la integración continua y el despliegue continuo, tal y como se detallarán en los apartados siguiente.

# Descripción del sistema

Más allá de los cambios realizados para poder cumplir con las funcionalidades esperadas de los WIs elegidos, los miembros del equipo han desarrollado código que afecta a otras partes del proyecto, como workflows de CI en Github Actions, playbooks para el despliegue de Vagrant, entre otros. 
A continuación, quedan enumerados y explicados, por cada miembro, aquellos cambios adicionales implementados.

## Pablo Fernández Pérez

### Descripción técnica del *Work Item*: Subida y validación de archivos UVL

Se implementó un sistema para la validación de archivos **UVL** durante la carga de nuevos datasets en **UVLHub**. Esta mejora evita la subida de archivos con errores de sintaxis mediante un método que analiza archivos con extensión `.uvl` en el momento de la subida del mismo. Si el archivo contiene errores de sintaxis, se notifica al usuario indicando la línea y el tipo de error.

Esta implementación se integró con los módulos `flamapy` y `dataset` (vistas).
 
Esta nueva funcionalidad mejoró la calidad de los datos ingresados y agilizó la corrección de errores por parte de los usuarios al recibir feedback inmediato.

### Pruebas realizadas
  - Test **unitarios** con Pytest (6): se rueban todas las posibles variantes de archivos UVL y sus casuísticas de error.
  - Test de **interfaz** con Selenium (1): se comprueba la presencia de las modificaciones realizadas en la UX.
  - Test de **carga** con Locust (1): se comprueba el rendimiento del servidor de cara a un escenario de múltiples peticiones de subir archivo UVL.

### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. Workflow de versionado automático

Este workflow realiza una la asignación de versiones en el proyecto y mantiene un historial organizado a través de un archivo `CHANGELOG.md`, permitiendo así una mejor trazabilidad de versiones y posibilidad de volver a estados estables mediante *tags*. A continuaci´r

- Cada commit en la rama `main` se categoriza siguiendo el siguiente estándar semántico:
  - **feat:** Incremento en la versión *minor* (ej. 1.1.0).
  - **fix:** Incremento en la versión *patch* (ej. 1.0.1).
  - **docs** y **chore:** La versión no se modifica (ej. permanece en 1.0.0).
- Los cambios se recopilan automáticamente en el `CHANGELOG.md`.

#### 2. Workflow de sincronización de ramas (*PR main <- develop*) (junto con Delfín Santana Rubio)

Este workflow se encarga de automatizar la integración diaria de los cambios de la rama `develop` en `main`. Se detectó que la ausencia de integraciones frecuentes generaba _Pull Requests_ conflictivas con cambios acumulados de múltiples ramas. Mediante este workflow se consigue mantener la rama `main` en un esatdo estable y actualizado sin comprometer la integridad del proyecto, reduciendo conflictos al integrar cambios de forma continua.
Este workflow fue implementado en la versión 1.5.0 del proyecto y está programado para ejecutarse diaramente.
La PR resultante debe ser revisada y validada manualmente antes del *merge* pro un meimbro de **tortilla-hub**.

#### 3. Despliegue con Vagrant: Integración de Prometheus y Grafana

Se trata de un _playbook_ que tiene como objetivo monitorizar el desempeño del sistema desplegado en una **Máquina Virtual (MV)** de Vagrant en tiempo real con métricas como el **% de uso de CPU**. Para ello, se ha creado un **playbook adicional** que instala y configura las siguientes herramientas: 
  1. **Prometheus:** Recolecta y almacena métricas en una base de datos de series temporales (*TSDB*).
  2. **Grafana:** Proporciona una interfaz visual para conectar con Prometheus y crear *dashboards* interactivos.

De esta forma se facilita el monitoreo y análisis de rendimiento del sistema desplegado proporcionando herramientas visuales para la toma de decisiones en entornos de desarrollo y producción.


## José Miguel Iborra Conejo

### Descripción técnica del *Work Item*: Valorar datasets

Todo el sistema se ha desarrollado dentro del módulo `dataset`. Con esta implementación, se permite que los usuarios puedan valorar y ver el desempeño de los datasets en la plataforma de manera intuitiva y funcional desde la vista de detalle de los mismos. En la parte superior derecha de la pantalla, se han situado 5 estrellas para permitir valorar los datasets y permitir que los usuarios vean estadísticas de valoración realizadas por otros usuarios.

### Pruebas realizadas
  - Tests **unitarios** con Pytest (6): se verifica la validación de lógica de negocio en el servicio de calificaciones evaluando todas las posibles interacciones del usuario (calificaciones válidas, entradas inválidas, duplicaciones, etc.). También se probaron límites en valores de rating (de 1 a 5) y manejo de errores con valores no válidos o tipos incorrectos.
  - Tests de **interfaz** con Selenium (4): se verifica que las calificaciones otorgadas por un usuario autenticado se actualizan correctamente, que se muestran las restricciones correspondientes al intentar calificar sin autenticación, la persistencia de calificaciones al refrescar la página y la actualización del promedio de calificaciones y conteo correcto de ratings al realizar una nueva valoración.

## Antonio Macías Ferrera

### Descripción técnica del *Work Item*: Dashboard

La funcionalidad desarrollada en el módulo `dataset` incluye gráficas de barras interactivas que muestran un ranking con los datasets más descargados, destacando el nombre del dataset y el número de descargas, otro con los cuatro autores más populares ordenador por el número de publicaciones, así como un listado con los cuatro últimos datasets subidos, ordenados de más a menos reciente. 
Para manetener la coherencia estética de la vista de la página principal, se tuvo que reubicar el panel de estadísticas de UVLHub; como el número total de datasets y modelos, la cantidad de datasets vistos, entre otros indicadores, para adaptarlo al nuevo 'layout' de la pantalla del "Home".

### Pruebas realizadas

  - Test **unitarios** con Pytest (12): se han realizado 6 tests de repositorio (3 positivos y 3 negativos) que prueban que se obtienen de manera correcta los datos necesarios para mostrar en el dashboard y otros 6 tests (3 positivos y 3 negativos) que prueban la obtención correcta de los datos en el servicio.

  - Tests de **interfaz** con Selenium (1): se ha comprobado que se muestran todos los elementos del Dashboard en la pantalla 'Home'.

  - Test de **carga** con Locust (3): se ha probado que tanto la vista como los botones de descargar y explorar los datasets se muestran y funcionan correctamente ante múltiples peticiones concurrentes.

### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. README.md

Se creó un archivo README para el repositorio **tortilla-hub** con una guía completa para la instalación, uso y ejecución de pruebas del proyecto; además de incluir los enlaces al proyecto desplegado en Render y Docker y un esquema desplegable e interactivo para conocer la estructura del proyecto Flask.

El README incluye una introducción con una descripción general del proyecto y su propósito, instrucciones detalladas para la instalación, desde cómo clonar el repositorio hasta la configuración del entorno necesario, y una guía para la ejecución de las pruebas unitarias, de carga y de frontend. Además, se detalla la estructura del proyecto, desglosando las carpetas y archivos principales. También se incluye información sobre la licencia del proyecto, enlaces relevantes a documentación externa y una lista con los principales contribuidores del proyecto.

#### 2. Despliegue con Docker

Se modificaron los scripts de construcción proporcionados en el proyecto original para construir y desplegar correctamente la aplicación utilizando Docker. Para ello, se creó un repositorio remoto en Docker Hub para almacenar la última versión de la imagen. 

#### 3. CD con Docker (junto con Guadalupe Ridruejo Pineda)

Se ha implementado un workflow automatizado en GitHub Actions para la construcción, etiquetado y despliegue de imágenes Docker de la aplicación tras cada push a la rama principal.

El workflow construye la imagen Docker y la etiqueta de forma automática, incluyendo versiones específicas asociadas a los tags de versión del repositorio. Posteriormente, la imagen es publicada en el repositorio DockerHub del proyecto.

Una vez publicada, la imagen se despliega en un servidor externo alojado en una Raspberry Pi, donde se ejecuta el proyecto mediante Docker Compose. Finalmente, el contenedor se expone a través de una dirección DNS pública, permitiendo el acceso a la aplicación. 

Desafortunadamente, durante la configuración de la Raspberry Pi 4 proporcionada, surgieron diversos problemas técnicos. Inicialmente, fue necesario reformatear la tarjeta SD de 64 GB debido a que la partición existente estaba inservible y mostraba menos almacenamiento del real. Posteriormente, tras instalar el sistema operativo Ubuntu Server, se tuvo que configurar manualmente las claves SSH para el acceso remoto, ya que no venían preinstaladas por defecto. Además, para garantizar un acceso seguro, se configuró un servidor DNS HTTPS donde se alojó la dirección IP pública del router al que estaba conectada la Raspberry Pi, evitando así el acceso directo mediante una simple IPv4 pública no segura.

Una vez resueltos estos problemas iniciales y conseguido ejecutar el workflow, surgieron nuevas limitaciones relacionadas con el consumo de recursos. El sistema operativo Ubuntu Server resultó ser demasiado pesado, agotando la memoria RAM de la Raspberry Pi e impidiendo la correcta ejecución del workflow. Para solucionar esto, se reinstaló un sistema operativo más ligero, Raspberry Pi OS, que permitió un mejor rendimiento y estabilidad en el proceso de despliegue.

## Benjamín Ignacio Maureira Flores

### Descripción técnica del *Work Item*: Sincronización con GitHub y GitLab

Integrando los módulos `auth` y `dataset`, se consiguió que al iniciar sesión en GitHub o en GitLab pudieran subirse modelos UVL a repositorios del usuario. Esto se hace desde la vista de _upload dataset_, para que una vez subido el dataset a Zenodo, también pueda subirse a alguna de las plataformas deseadas.

Usando como base el trabajo de Ramón Gavira de Tortilla-Hub-2, que implementaban la opción _multiple login_, se añadieron unos botones en la vista mencionada anteriormente para poder loguearse en los servicios indicados si no se había hecho previaente. Una vez iniciada la sesión, se obtiene el _access_token_ y en la vista aparece un desplegable para marcar el repositorio destino donde subir los modelos UVL. Estos modelos se suben uno a uno al repositorio, para evitar problemas de compatibilidad con las API.

### Pruebas realizadas

- Tests **unitarios** con Pytest (10): se han probado el _signup_ y el _login_ de Github y Gitlab y la obtención de los repositorios destino, mockeando respuestas de la API y probando casos positivos y negativos. 

### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. Plabybook con Vagrant

Se añadió un playbook a Vagrant llamado _08_tests.yml_ con el objetivo de lanzar los tests unitarios utilizando Rosemary CLI para comprobar el correcto funcionamiento de los tests en la máquina virtual, y también ejecutar los tests de carga con Locust. Una vez se ejecutan estos tests, los resultados se almacenan en una carpeta en la raíz del proyecto llamada _locustresults_, donde pueden verse los archivos .csv que genera la prueba.


## Guadalupe Ridruejo Pineda

### Descripción técnica del *Work Item*: Mejorar la interfaz de usuario

La tarea consistió principalmente en modificar la vista de detalle del módulo `dataset`, reestructurando los elementos y ajustando el estilo para asemejarlo a la estética de GitHub, con el objetivo de mejorar la usabilidad. Se dio mayor relevancia a los ficheros, ubicándolos en la parte central de la vista, mientras que la información relacionada se situó a la derecha y las publicaciones relacionadas en la sección inferior. Además, se implementó un buscador para facilitar la navegación entre los ficheros, y las opciones de valorar y explorar otros datasets se reubicaron en la parte superior derecha.

### Pruebas realizadas

- Tests de **interfaz** con Selenium (7): se han realizado pruebas que verifiquen que todos los elementos necesarios se muestran en la pantalla correctamente y funcionan según lo esperado.
- Tests de **carga** con Locust (2): se han implementado pruebas que simulan el comportamiento de la plataforma ante múltiples peticiones de visualización y descarga de datasts.

### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. Documentación del proyecto

Se elaboró la documentación del proyecto Tortilla-hub-1, que incluyó el Diario de Equipo y el Documento del Proyecto. La redacción de este último se completó gracias a la colaboración de Antonio Macías.

Además, se redactó el documento más importante, el Acta Fundacional, que sirvió como eje central para la gestión del repositorio y del código fuente del proyecto.

#### 2. Workflow de estadísticas del repositorio

Motivado por la necesidad de conocer el progreso del equipo y mantener la información actualizada de las aportaciones realizadas, se elaboró un workflow que mediante librerías de python (gitpython pyyaml requests python-dotenv PyGithub tqdm matplotlib seaborn) calcula las contribuciones evaluadas en el proyecto: número de commits, líneas de código aportadas e issues creadas por cada contribuidor y generas gráficas y archivos `.json` para visualizar los datos de una forma más clara y sintetizada.

Las estadísticas ofrecidas por GitHub solo mostraban las contribuciones que ya estuvieran presentes en la rama `main`, lo que no reflejaba las aportaciones reales de ambos equipos al proyecto durante su desarrollo.

#### 3. CD con Docker (junto con Antonio Macías Ferrera)

Concreatemente, se realizaron las tareas correspondientes a la configuración del servidor y a la gestión de la red para el acceso al servidor. 


## Delfín Santana Rubio

### Descripción técnica del *Work Item*: Crear comunidades

Se creó el módulo `community`, así como el módulo `community_join_request`, que gestiona las solicitudes para unirse a una comunidad. Por otro lado, se modificaron las rutas, modelo, repositorio, seeders y servicio del módulo `dataset` para así poder utilizar los datasets (subir y listar) en las comunidades.

### Pruebas realizadas

- Tests **unitarios** con Pytests (25): se ha probado que la lógica correspondiente a los servicios de las comunidades y las rutas funcionen correctamente, valorando casos positivos y negativos.
- Tests de **integración** (14): se ha probado (concretamente para el módulo `community_join_request`) que su integración y sus casos positivos y negativos se evalúan de forma satisfactoria.
- Tests de **carga** con Locust (5): se han diseñado pruebas que evalúen las peticiones concurrentes a las rutas realacionadas con las comunidades.
- Tests de **interfaz** con Selenium (8): se ha probado el recorrido por la vista de la plataforma que realizaría un usuario para unirse a una comunidad, crearla, subir y listar datasets.

### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. Workflow "Create issue if author is not found in .mailmap"

Consiste en crear una issue si se detecta que un autor o correo de autor que no está en el .mailmap realiza commits en el repositorio. De este modo se consigue que no se utilicen varios nombres de autor por persona. Se activa cada vez que se hace un push a la rama `develop`.

#### 2. Workflow "Merge Migrations"

Este workflow comprueba si hay conflictos en las migraciones de flask por la existencia de distintas HEADS y, por tanto, verifica si se generan errores al aplicar las migraciones con `flask db upgrade`. Si existen, se _mergean_ las HEADS, mediante el comando `flask db merge heads` y hace un commit con la migración. 
El problema se da cuando trabajamos con varias ramas y creamos migraciones en estas. Cuando se mergean las ramas a la rama principal, hay conflictos en las migraciones porque todas las migraciones nuevas son el HEAD. Se activa cuando se hace push a develop.

#### 3. Workflow de sincronización de ramas (*PR main <- develop*) (junto con Pablo Ferández Pérez)

(explicado más detalladamente en el apartado de ([Pablo Fernández Pérez](#pablo-fernández-pérez)))

## Daniel Vela Camacho

### Descripción técnica del *Work Item*: Staging Area

Esta tarea tuvo como resultado la creación de una zona específica para la preparación de datasets antes de su publicación en plataformas como Zenodo o Fakenodo. Esta implementación realizada en el módulo `dataset` permite a los usuarios gestionar el estado de los datasets, realizar ediciones previas y seleccionar cuáles publicar. Los datasets cuentan con un estado asociado (Unstaged, Staged o Published), facilitando su identificación y control. Para ello, se añadió el atributo _dataset_status_ en el modelo de datos y se implementaron funciones en los repositorios para filtrar datasets según su estado.
A nivel de servicio, se definieron operaciones para cambiar el estado de los datasets individualmente o en bloque, así como su publicación en plataformas externas. 

### Pruebas realizadas
Se desarrollaron pruebas para validar estos cambios, evitar acciones redundantes y garantizar la correcta gestión de los estados. Además, se realizaron pruebas de carga para evaluar el rendimiento del sistema bajo solicitudes concurrentes, asegurando una gestión eficiente y robusta de los procesos.

- Tests de **integración** (9):  los casos de prueba desarrollados abarcan diferentes escenarios para garantizar una cobertura integral de las funcionalidades relacionadas con la gestión del estado de los datasets. Estos incluyen pruebas para verificar que un usuario no pueda cambiar el estado de un dataset que no le pertenece validar que no se pueda cambiar el estado de un dataset a uno en el que ya se encuentra, además de pruebas para confirmar que un usuario pueda cambiar correctamente el estado de un dataset entre Unstaged, Staged y Published, tanto individualmente como en lotes. Finalmente, se probaron las integraciones con Fakenodo/Zenodo para asegurar que los procesos de publicación se realicen de manera adecuada.
- Tests de **interfaz** con Selenium (6): los escenarios considerados para los tests de interfaz incluyen las acciones de stagear un dataset, unstagear un dataset, stagear todos los datasets, unstagear todos los datasets y proceder con su publicación.
- Tests de **carga** con Locust (6): el código realiza pruebas de carga para evaluar el rendimiento de los endpoints relacionados con la gestión de datasets. Incluye pruebas para cargar la página de subida, cambiar el estado de un dataset (stagear/unstagear), gestionar todos los datasets en lote (stagear/ unstagear) y publicarlos. Estas tareas simulan solicitudes concurrentes para asegurar la capacidad del sistema bajo carga.


### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. Workflow para la revisión de código

El workflow _lint.yml_ automatiza la revisión y el formateo de código Python en las ramas `main` y `develop` al realizar push o pull requests. Utiliza flake8 para analizar errores de estilo según PEP8 y _black_ para formatear automáticamente el código en la carpeta `app`. Si se detectan cambios tras el formateo, estos se confirman y se envían automáticamente a la rama del pull request, asegurando que el código se mantenga limpio y conforme a los estándares.

## Visión global del proceso de desarrollo *(1500 palabras)* <!--{#visión-global-del-proceso-de-desarrollo-(1500-palabras)}-->

El proceso de desarrollo se basó en las siguientes etapas:

- **Planificación**: A la hora de planificar una tarea, debemos de crear una issue en el project para hacer seguimiento de esta. La issue deberá de pasar por sus estados naturales(Todo, in progress, in review, done). Para crearla, se debe de hacer según se explica en el acta fundacional que, entre otras cosas, indica que añadamos un tag, que le indiquemos una prioridad, etc.

- **Desarrollo**: Para el desarrollo, si se estima que se van a realizar varios cambios, se deberá de hacer una rama específica para la tarea. Si se está absolutamente seguro que no va a dar error y que no necesita revisión, como puede ser hacer tareas de documentación, se podrá hacer cambio directamente a develop. La issuse asociada  al cambio, se deberá de mantener actualizada. De este modo, cuando se complete el cambio, se deberá de actualizar la issue, cerrándose únicamente cuando llegue el cambio a main. Cuando se trate de una pull request, deberá de revisarse el cambio por al menos una persona.

- **Pruebas**: Dependiendo del cambio que sea, se harán pruebas para comprobar que el cambio es correcto. Por ejemplo, si un cambio no se muestra en la interfaz, en principio no tendría sentido hacer un test de selenium,  sino un test unitario o de interfaz.

- **Integración continua**: cuando se crea una pull request o se hace push a develop o a main, se activan workflows que hacen distintas tareas, como son ejecutar las pruebas unitarias o comprobar la calidad del código. Además, hay workflows que solucionan errores recurrentes, como son el problema con las migraciones de flask por haber varias HEADs.

- **Despliegue**: Una vez se integra un cambio, este se despliega automáticamente en render. Se tiene un render para la rama develop y otro para la rama main, para así poder comprobar el desarrollo y la producción.

## Entorno de desarrollo *(800 palabras)*  <!--{#entorno-de-desarrollo-(800-palabras)}-->
1. Introducción
2. Cómo se instala manual, Docker y Vagrant
3. Entorno de desarrollo y explicar las extensiones utilizadas
4. Herramientas en requirements.txt
5. Métodos de instalación (compatibilidad con linux, etc.)
6. Indicar la fuente de dónde se saca esto si se saca del manual de usuario
7. Indicar qué se ha incluido en el env
El equipo utilizó una combinación de herramientas, incluyendo:

- **IDE y Sistemas de Control de Versiones**: Visual Studio Code, Git y GitHub.

- **Entornos de Prueba y Producción**: Docker, Render y Raspberry Pi OS.

- **Gestores de Bases de Datos**: MariaDB.

- **Automatización**: GitHub Actions.

- **Colaboración y Documentación**: Google Drive, OneDrive, ChatGPT, Google Forms, Google Sheets, Google Docs, Markdown y Copilot.

- **SO**: ubuntu

La configuración inicial del entorno está detallada en el README.md de este mismo repositorio en la sección **Instalación**.

## Ejercicio de propuesta de cambio <!--{#ejercicio-de-propuesta-de-cambio}-->

El objetivo de esta ejercicio es añadir una nueva funcionalidad al proyecto tortilla-hub para fomentar la participación activa de la comunidad. El desarrollo se llevaría a cabo de la siguiente manera:

#### Work Item: Desarrollo de un foro para fomentar la participación de la comunidad (Dificultad: High)

#### **1. Definir los requerimientos del cambio**
- **Título del Issue**: _Foro comunidades: Desarrollo de la funcionalidad_
- **Descripción**: Se debe implementar una sección en la plataforma que permita a los usuarios colaborar mediante un foro de discusión.
- **Criterios de Aceptación**: N/A
- **Etiqueta**: WI.
- **Asignado**: X.
- **Prioridad**: M (medium).
- **Fecha Límite**: _la que corresponda_.

    Pasos para crear un Issue:
    1. Abrir el repositorio en GitHub:
    ```
    git clone https://github.com/EGC-G2-tortilla/tortilla-hub.git
    cd tortilla-hub
    ```
    2. Crear un nuevo issue:
    - Navegar a la sección "Issues" del repositorio y pulsar en "New Issue".
    - Completar el issue siguiendo el formato definido en el archivo de gestión de issues (5.1 del **Acta de constición**) y el contenido anteriormente mencionado.

    3. Configurar una rama de trabajo:
    - Crear una rama task/fomentar-comunidad a partir de la rama `develop`:
    ```
    git checkout -b task/fomentar-comunidad
    ````

    4. Implementación:
    - Desarrollar los cambios requeridos empleando como herramienta Visual Studio Code y las configuraciones indicadas.
    - _Nota: Se asume que se han instalado las dependencias necesarias y se ha configurado la base de datos correctamente tal y como se indica en el manual de instalación del proyecto_.

#### **2. Subir los cambios a GitHub**
- Se realizarán commits atómicos siguiendo las buenas prácticas definidas:
```
git add foro.py
git commit -m "feat: foro para las comunidades"
```

#### **3. Pruebas**
- Se realizarán una serie de pruebas para obtener una cobertura óptima de código de la funcionalidad implementada. Entre ellas deberían poder realizarse:
  - Test unitarios: que prueben los casos positivos y negativos de cada funcionalidad.
  - Test de selenium: para verificar cómo se muestran los elementos en la vista diseñada.
  - Tests de carga: para evaluar cómo se comporta el sistema ante peticiones concurrentes de múltiples usuarios.
- Los cambios se añadirán siguiendo la política de commits definida:
```
git add test_selenium.py
git commit -m "test: pruebas de interfaz con selenium para el foro"
```
  

#### **4. Realizar Pull Request**
- Subir la rama al repositorio remoto:
```
git push origin task/fomentar-comunidad
```
- Crear un Pull Request en GitHub y asignar revisores. La Pull Request deberá cumplir con la siguiente plantilla:
  - Descripción clara del cambio: Explicar qué se ha modificado y por qué.
  - Motivación del cambio: Contextualizar por qué el cambio es necesario (por ejemplo, corregir un bug o implementar una nueva característica).
  - Impacto del cambio: Describir cómo afectará el sistema o qué áreas del código se ven impactadas.
  - Evidencia de pruebas: Proporcionar información sobre las pruebas ejecutadas para validar el cambio.
  - Instrucciones adicionales: Indicar si es necesario realizar alguna acción posterior a la integración del PR (como migraciones de base de datos o despliegues especiales).

#### **5. Fusionar y documentar el cambio**
Una vez aprobada la Pull Request, fusionarla con la rama develop:
```
git checkout develop
git merge task/fomentar-comunidad
git push origin develop
```

## Conclusiones y trabajo futuro <!--{#conclusiones-y-trabajo-futuro}-->

El proyecto Tortilla-Hub-1 demuestra la importancia de una gestión estructurada y colaborativa en el desarrollo de software. Para el futuro, se proponen las siguientes mejoras:

Integración de Codacy para análisis de calidad código.

Reemplazo de Raspberry Pi por servidores con mayor capacidad.

Expansión de las funcionalidades de las comunidades.

Mayor cobertura de tests.

Automatización y estandarización de procesos clave (GitHub Actions, migraciones).

Si contásemos con más tiempo, hubiese sido una buena idea pararnos a analizar en detalle el estado de la Pipeline actual y refinarla para que sea óptima en cuanto al uso de recursos de GitHub Actions y poder también evitar la redundancia en el flujo. 

1. Detallar más la funcionalidad de los WI, para tener claro el alcance de cada uno y poder planificar mejor, además de ahorrar comunicación con el profesorado.