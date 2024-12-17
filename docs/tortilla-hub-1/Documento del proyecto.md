# TORTILLA-HUB-1

* Grupo 2  
* Curso escolar: 2024/2025  
* Asignatura: Evolución y Gestión de la Configuración

## Miembros

| Miembro | Implicación |
| :---- | :---- |
| Fernández Pérez, Pablo | 10 |
| Iborra Conejo, José Miguel | 10 |
| Macías Ferrera, Antonio | 10 |
| Maureira Flores, Benjamín Ignacio | 10 |
| Ridruejo Pineda, Guadalupe | 10|
| Santana Rubio, Delfín | 10 |
| Vela Camacho, Daniel | 10 |

## Índice

[Indicadores del Proyecto](#indicadores-del-proyecto)

[Descripción de los Work Items implementados](#descripción-de-los-work-items-implementados)

[Integración con otros equipos](#integración-con-otros-equipos)

[Resumen Ejecutivo](#resumen-ejecutivo)

[Descripción del sistema](#descripción-del-sistema)

[Visión global del proceso de desarrollo](#visión-global-del-proceso-de-desarrollo)

[Entorno de desarrollo](#entorno-de-desarrollo)

[Ejercicio de propuesta de cambio](#ejercicio-de-propuesta-de-cambio)

[Conclusiones y trabajo futuro](#conclusiones-y-trabajo-futuro)

# Indicadores del Proyecto

| Miembro del equipo | Horas | Commits | LoC | Test | Issues | Work Item |
| :----- | :----- | :----- | :----- | :----- | :----- | :----- |
| Fernández Pérez, Pablo | 18h | 42  | +1144 -322 | 10 | 16 | Upload, analyse and repair UVL |
| Iborra Conejo, José Miguel | 14h 15min |24  | +4074 -823  | 10 | 5 | Rate datasets / models |
| Macías Ferrera, Antonio |34h 30min  |67  | +14659 -6186  | 16 | 18 | Dashboard |
| Maureira Flores, Benjamín Ignacio |21h |28  | +13418 -74  | 10 | 9 | Sync with github/gitlab |
| Ridruejo Pineda, Guadalupe | 38h 30min | 54 | +1745 -668  | 9 | 9 | Improve UI |
| Santana Rubio, Delfín |19h  | 94 | +5922 -2715 | 52 | 28 | Create communities |
| Vela Camacho, Daniel |21h  | 64 | +2951 -1569 | 21 | 26 | Staging area |
| **TOTAL** | 166h 15min| 373 | +43913 - 12357 | 128 | 111 |  |


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
- **Definición de pautas de trabajo:** Todas las normas y directrices relacionadas con la gestión del repositorio y del código fuente quedaron documentadas en el ([Acta Fundacional](https://github.com/EGC-G2-tortilla/tortilla-hub/blob/main/docs/Acta%20fundacional.md)), garantizando un desarrollo ordenado y coordinado. Estas pautas han sido cumplidas satisfactoriamente por ambos equipos.

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
  - Test de **carga** con Locust (3): se comprueba el rendimiento del servidor de cara a un escenario de múltiples peticiones de subir archivo UVL.

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

**NOTA**: Al usar secrets para conectar la aplicación con los servicios de Github y Gitlab, dichos secrets no se pueden dejar en el código ni en el repositorio, sólo están en Render. Entonces, debido a las limitaciones de las variables de entorno y las limitaciones de los propios servicios (Github solo deja añadir una *redirect_uri*), se ha decidido que Github solo funciona en producción y Gitlab funciona tanto en producción como en desarrollo

### Pruebas realizadas

- Tests **de integración** con Pytest y Unittest (10): se han probado el _signup_ y el _login_ de Github y Gitlab y la obtención de los repositorios destino, mockeando respuestas de la API y probando casos positivos y negativos. 

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

(explicado más detalladamente en el apartado de [Pablo Fernández Pérez](#pablo-fernández-pérez))

## Daniel Vela Camacho

### Descripción técnica del *Work Item*: Staging Area

Esta tarea tuvo como resultado la creación de una zona específica para la preparación de datasets antes de su publicación en plataformas como Zenodo o Fakenodo. Esta implementación realizada en el módulo `dataset` permite a los usuarios gestionar el estado de los datasets, realizar ediciones previas y seleccionar cuáles publicar. Los datasets cuentan con un estado asociado (Unstaged, Staged o Published), facilitando su identificación y control. Para ello, se añadió el atributo _dataset_status_ en el modelo de datos y se implementaron funciones en los repositorios para filtrar datasets según su estado.
A nivel de servicio, se definieron operaciones para cambiar el estado de los datasets individualmente o en bloque, así como su publicación en plataformas externas. 

### Pruebas realizadas

- Tests de **integración** (9):  los casos de prueba desarrollados abarcan diferentes escenarios para garantizar una cobertura integral de las funcionalidades relacionadas con la gestión del estado de los datasets. Estos incluyen pruebas para verificar que un usuario no pueda cambiar el estado de un dataset que no le pertenece validar que no se pueda cambiar el estado de un dataset a uno en el que ya se encuentra, además de pruebas para confirmar que un usuario pueda cambiar correctamente el estado de un dataset entre Unstaged, Staged y Published, tanto individualmente como en lotes. Finalmente, se probaron las integraciones con Fakenodo/Zenodo para asegurar que los procesos de publicación se realicen de manera adecuada.
- Tests de **interfaz** con Selenium (6): los escenarios considerados para los tests de interfaz incluyen las acciones de stagear un dataset, unstagear un dataset, stagear todos los datasets, unstagear todos los datasets y proceder con su publicación.
- Tests de **carga** con Locust (6): el código realiza pruebas de carga para evaluar el rendimiento de los endpoints relacionados con la gestión de datasets. Incluye pruebas para cargar la página de subida, cambiar el estado de un dataset (stagear/unstagear), gestionar todos los datasets en lote (stagear/ unstagear) y publicarlos. Estas tareas simulan solicitudes concurrentes para asegurar la capacidad del sistema bajo carga.


### CI/CD: Integración Continua, Despliegue Continuo y contribuciones al proyecto

#### 1. Workflow para la revisión de código

El workflow _lint.yml_ automatiza la revisión y el formateo de código Python en las ramas `main` y `develop` al realizar push o pull requests. Utiliza flake8 para analizar errores de estilo según PEP8 y _black_ para formatear automáticamente el código en la carpeta `app`. Si se detectan cambios tras el formateo, estos se confirman y se envían automáticamente a la rama del pull request, asegurando que el código se mantenga limpio y conforme a los estándares.

## Visión global del proceso de desarrollo <!--{#visión-global-del-proceso-de-desarrollo-(1500-palabras)}-->

El proceso de desarrollo se basó en las siguientes etapas:

- **Planificación**: A la hora de afrontar una nueva tarea (en nuestro equipo se ha seguido una planificación individual), se debe crear una issue en el tablero de proyecto de GitHub siguiendo la plantilla establcecida en el [Acta Fundacional](https://github.com/EGC-G2-tortilla/tortilla-hub/blob/main/docs/Acta%20fundacional.md) para hacer seguimiento de esta. La issue deberá de pasar por los estados definidos (TODO, IN PROGRESS, IN REVIEW, DONE). Además, será necesario añadirle una etiqueta (WI, documentation, bug, workflow, fakenodo) e indicar la prioridad, así como la fecha límite de entrega.

- **Desarrollo**: Para el desarrollo, si se estima que se van a realizar varios cambios, se deberá crear una rama específica para la tarea. Si se está absolutamente seguro que no va a haber errores y que no necesita revisión, como pueden ser las tareas de documentación, se podrá hacer el cambio directamente en `develop`. La issuse asociada al cambio, se deberá mantener actualizada. De este modo, cuando se complete el cambio, se deberá actualizar la issue, cerrándose únicamente cuando llegue el cambio a main. Cuando se trate de una pull request, deberá revisarse el cambio por, al menos, una persona.

- **Pruebas**: Dependiendo de la naturaleza de la tarea, se harán pruebas para comprobar el funcionamiento esperado de la misma, ya sean de interfaz con Selenium, unitarias con Pytest, de integración o de carga con Locust. 

- **Integración continua**: cuando se crea una pull request o se hace push a `develop` o a `main`, se activan workflows que hacen distintas tareas, como son ejecutar las pruebas unitarias o comprobar la calidad del código. Además, hay workflows que solucionan errores recurrentes, como son el problema con las migraciones de flask por haber varias HEADs.

- **Despliegue**: Una vez se integra un cambio, este se despliega automáticamente en Render, tanto para el desarrollo (rama `develop`) como para producción (rama `main`).

## Entorno de desarrollo  <!--{#entorno-de-desarrollo}-->
El entorno de desarrollo es el conjunto de herramientas, configuraciones y recursos utilizados para desarrollar, probar y desplegar el proyecto. El equipo ha trabajado con distintas configuraciones, tanto manuales como automatizadas, para asegurar la compatibilidad y facilidad en el despliegue.

### Instalación del entorno

Contamos con tres métodos distintos de instalación: manual, Docker y Vagrant. Cada método sigue unas pautas y variables de entorno distintas. Para conocer en detalle cómo llevar a cabo cada una de las instalaciones mencionadas, visite el siguiente enlace: https://docs.uvlhub.io/installation

### Resumen de las extensiones y dependencias

- **Frameworks y Herramientas Principales**:
  - **Flask (3.0.3)**: Framework ligero para el desarrollo web con Python.
  - **Flask-Cors (4.0.1)**: Soporte para CORS en aplicaciones Flask.
  - **Flask-SQLAlchemy (3.1.1)**: Extensión que facilita el uso de bases de datos relacionales con SQLAlchemy.
  - **Flask-RESTful (0.3.10)**: Herramienta para crear APIs RESTful en Flask.
  - **Flask-Migrate (4.0.7)**: Gestión de migraciones de base de datos con Flask.
  - **SQLAlchemy (2.0.31)**: ORM que facilita la interacción con bases de datos SQL.
  - WTForms (3.1.2) y Flask-WTF (1.2.1): Manejo avanzado de formularios en aplicaciones web.

- **Bases de Datos:**
  
  - **PyMySQL (1.1.1)**: Cliente de MySQL para Python.
  - **SQLAlchemy-Utils (0.41.2)**: Extensiones adicionales para SQLAlchemy.
  - **alembic (1.13.2)**: Herramienta para migraciones de bases de datos.

- **Pruebas y Cobertura:**
  - **pytest (8.2.2)**: Framework para pruebas unitarias.
  - **pytest-cov (5.0.0)**: Genera informes de cobertura de código en pruebas.
  - **pytest-asyncio (0.25.0)**: Extiende pytest con soporte para coroutines y pruebas asíncronas.
  - **selenium (4.22.0)**: Automatización de pruebas en navegadores.
  - **responses (0.25.3)**: Herramienta para mockear peticiones HTTP en pruebas.

- **Automatización y CI/CD:**
  - **GitPython (3.1.43)**: Interacción con repositorios Git desde Python.
  - **PyGithub (2.5.0)**: Interfaz para interactuar con la API de GitHub.
  - **webdriver-manager (4.0.1)**: Descarga y gestiona drivers para Selenium.

### Métodos de instalación
Para la instalación del sistema, es recomendable usar un sistema operativo Linux, en concreto usamos **Ubuntu 22.04 LTS**. Cabe mencionar que es buena idea tener este sistema operativo instalado y no hacer uso de una máquina virtual, ya que pueden surgir errores si el sistema no maneja correctamente la virtualización anidada en caso de hacer un despliegue con Vagrant.
También se ha comprobado por parte de un miembro del equipo que el proyecto se puede desplegar correctamente con Mac OS Sequoia.

### Archivos .env
En los archivos .env podemos encontrar las variables de entorno necesarias para que el despliegue del proyecto sea exitoso. Se han añadido ciertas variables extra debido al desarrollo de WIs que así lo requerían.

### Herramientas de desarrollo
En cuanto a las herramientas usadas durante el desarrollo, el equipo utilizó el IDE **Visual Studio Code**, **Git** para el control de versiones desde consola y **GitHub** para el alojamiento del repositorio.

### Entornos de Prueba y Producción: Render
El proyecto cuenta con dos despliegues, uno en producción y otro en desarrollo. Puede visitar ambos en las siguientes URLs:

https://tortilla-hub-development.onrender.com/

https://tortilla-hub-production.onrender.com/

### Gestores de Bases de Datos
El sistema utiliza **MariaDB** como gestor de bases de datos principal. MariaDB es una bifurcación de MySQL, ampliamente reconocida por su alto rendimiento, estabilidad y compatibilidad con aplicaciones que previamente utilizaban MySQL. Se trata de un sistema de gestión de bases de datos relacional (RDBMS) de código abierto, diseñado para ofrecer velocidad y robustez, siendo ideal para aplicaciones que requieren un manejo eficiente de grandes volúmenes de datos.

### Automatización: GitHub Actions.
Todas las configuraciones de CI/CD  se han  realizado a través de  la herramienta **GitHub Actions**, dado que el control de versiones se llevó a cabo en GitHub y el equipo pudo familiarizarse rápidamente con su uso.


### Colaboración y Documentación en el Equipo
Para garantizar una comunicación efectiva, la gestión de tareas y una documentación clara, el equipo utilizó diversas herramientas que facilitaron el flujo de trabajo colaborativo:
**Google Drive** y **OneDrive**.
Estas plataformas de almacenamiento en la nube permitieron al equipo organizar el contenido, asegurando que todos los miembros del equipo tuvieran acceso a la última versión de los archivos y la colaboración en tiempo real.

#### Google Forms, Sheets y Docs
- **Google Forms**: Utilizado para recopilar las aportaciones del grupo y poder unificarlas con facilidad.
- **Google Sheets**: Permitió tener una matriz de asignación de tareas inicial, cuando discutimos sobre qué miembro haría cada WI.
- **Google Docs**: Principal herramienta para redacción de documentación, actas de reuniones y acuerdos dentro del equipo.

### ChatGPT
Utilizado como herramienta de apoyo técnico y resolución rápida de dudas durante el desarrollo.
Ayudó a generar fragmentos de código, depurar problemas, optimizar configuraciones y aclarar conceptos complejos.


### GitHub Copilot
GitHub Copilot funcionó como un asistente de código, ayudando al equipo a acelerar el desarrollo al generar automáticamente fragmentos de código y reducir errores mediante sugerencias precisas basadas en el contexto del código, al mismo tiempo que facilitaba el aprendizaje de librerías y sintaxis menos conocidas.

**NOTA**: La configuración inicial del entorno está detallada en el [README.md](https://github.com/EGC-G2-tortilla/tortilla-hub) de este mismo repositorio en la sección Instalación.

# Ejercicio de propuesta de cambio

El objetivo de esta ejercicio es añadir una nueva funcionalidad al proyecto tortilla-hub para ajustarnos a los requerimientos establecidos en el Milestone 3 del proyecto de acuerdo con las directrices de la asignatura. El desarrollo se llevará a cabo de la siguiente manera:

## Work Item: Nueva tarjeta de Bienvenida (Dificultad: Low)

### **1. Definir la tarea (Issue) en GitHub Project: José Miguel Iborra Conejo**

Se deberá crear una tarea en forma de *Issue* en el [*GitHub Project*](https://github.com/orgs/EGC-G2-tortilla/projects/1) del respositorio del tortilla-hub con la siguiente información y completando los campos adecuado:

- **Título del Issue**: Nueva tarjeta de Bienvenida
- **Descripción**: Se deberá modificar la tarjeta de bienvenida que aparece en la página de inicio del proyecto (Home) para que, además de la información que ya tiene, se incluya al principio este mensaje: 
"
¡Felices fiestas! 🎉 Desde el equipo de **tortilla-hub** queremos desearles unas fiestas llenas de alegría, comida rica y momentos inolvidables con sus familias y amigos. Que el espíritu navideño les traiga no solo turrones y polvorones, sino también mucha suerte y energía para el próximo año. Y, por supuesto, esperamos que los Reyes Magos (o Papá Noel, no discriminamos a nadie 😉) vengan cargados de **buenas notas**, porque al carbón ya le tenemos suficiente respeto en la barbacoa. ¡A disfrutar y a recargar pilas para lo que viene! 🎄✨
"
- **Criterios de Aceptación**: El texto deberá mostrarse en la tarjeta de bienvenida de la página de inicio se haya iniciado sesión o no. El texto debe ser tal y como el que se describe en la tarea. La tarjeta deberá tener un nuevo color de estética más "navideña".
- **Etiqueta**: WI
- **Asignado**: Leetee2
- **Prioridad**: H (high)
- **Fecha Límite**: 18/12/2024
  

### **2. Elaboración de las modificaciones: Pablo Fernández Pérez**

En primer lugar, el encargado de este paso deberá crear una rama con el nombre ```task/nueva-tarjeta-bienvenida``` y traerla a su repositorio local. Desde ahí deberá realizar los cambios pertinentes modificando los siguientes archivos: 

1. En el archivo ```app/modules/public/templates/public/index.html```, el el *div* llamado ``` <div class="card card-dark">``` se deberá añadir lo siguiente:

```
<div class="card-body card-body-slim">
    ¡Felices fiestas! 🎉 Desde el equipo de *tortilla-hub* queremos desearles unas fiestas llenas de alegría, comida rica y momentos inolvidables con sus familias y amigos. Que el espíritu navideño les traiga no solo turrones y polvorones, sino también mucha suerte y energía para el próximo año. Y, por supuesto, esperamos que los Reyes Magos (o Papá Noel, no discriminamos a nadie 😉) vengan cargados de *buenas notas*, porque al carbón ya le tenemos suficiente respeto en la barbacoa. ¡A disfrutar y a recargar pilas para lo que viene! 🎄✨
</div>
```

2. En el archivo ```app/static/css/own.css``` se deberá modificar el estilo ```card-dark``` sustituyedo el fondo actual por el siguiente:

```
  background: #2B3947 radial-gradient(circle at center left, red, green);
```

Tras realizar las modificaciones ya comentadas, se deberá hacer `git add` de los archivos modificados, `git commit -m Feat: modificación de la tarjeta de bienvenida`y por último `git push` para incorporar los cambios al repositorio remoto.

### **3. Elaboración de la Pull Request: Daniel Vela Camacho**

Se deberá crear una pull request en la que se incorporen los cambios realizados en la rama ```task/nueva-tarjeta-bienvenida``` a la rama develop del proyecto tortilla-hub. Debe contener lo siguiente: 

- **Descripción del cambio:** Se ha actualizado la tarjeta de bienvenida que aparece en la página de inicio para que muestre una felicitación de navidad con un color divertido.

- **Motivación / Impacto:** Este cambio proporcionará una estética fresca y alegre a la página, dado así también sensación de actualidad acorde a las fiestas que vivimos a fecha de la finalización del proyecto.

- **Instrucciones:** Se debe comprobar visualmente que el cambio se ha realizado correctamente.

- **Asignado:** Leetee2

- **Revisor:** guardipin


### **4.Revisión de la Pull Request: Guadalupe Ridruejo Pineda**

Se deberá comprobar que los cambios se ha realizado de manera correctamente en el proyecto local antes de aprobar la *Pull Request*. 

1. Se deberá traer los últimos cambios al repositorio local: `git fetch``
2. Se deberá cambiar a la rama ```task/nueva-tarjeta-bienvenida``` haciendo: `git checkout <nombre_rama>`
3. Se tendrá que correr el proyecto en local desde esa rama y ver que en la página de inicio de uvlhub aparece la nueva tarjeta navideña.

Si todo esto es así se aprobará la Pull Request con un comentario: 
"
Las modificaciones se muestras correctamente. ¡Feliz Navidad! 👍✨👉🎁🙀
"


### **5.Creación de un test de interfaz para probar el cambio: Delfín Santana Rubio**

En primer lugar, el encargado de este paso deberá crear una rama con el nombre ```task/test-nueva-tarjeta-bienvenida``` y traerla a su repositorio local. Desde ahí deberá realizar los test pertinentes (en este caso se pide un test de interfaz que pruebe que el cambio se ha realizado correctamente): 

1. Crear una nueva carpeta en la ubicación: ```app/public``` llamada `tests` e incluir ahí el nuevo archivo `test_selenium.py`. 

2. En ese nuevo archivo ```app/public/tests/test_selenium.py``` se deberá implementar el siguiente test:

```
  class TestHomePage(unittest.TestCase):
    def test_home_page_text(self):
        driver = initialize_driver()

        try:
            host = get_host_for_selenium_testing()

            # Open the main page
            driver.get(f"{host}/")
            wait_for_page_to_load(driver)

            expected_text = """¡Felices fiestas! 🎉 Desde el equipo de *tortilla-hub* queremos desearles unas fiestas llenas de alegría, comida rica y momentos inolvidables con sus familias y amigos. Que el espíritu navideño les traiga no solo turrones y polvorones, sino también mucha suerte y energía para el próximo año. Y, por supuesto, esperamos que los Reyes Magos (o Papá Noel, no discriminamos a nadie 😉) vengan cargados de *buenas notas*, porque al carbón ya le tenemos suficiente respeto en la barbacoa. ¡A disfrutar y a recargar pilas para lo que viene! 🎄✨"""

            # Locate the element
            element = driver.find_element(By.XPATH, "//div[@class='card-body card-body-slim']")

            # Assertions
            self.assertEqual(element.text, expected_text)
            self.assertTrue(element.is_displayed(), "Popular datasets chart not displayed!")

            print("Data display test passed! Merry Christmas!")

        finally:
            # Close the browser
            close_driver(driver)


# Run tests
if _name_ == "_main_":
    unittest.main()
```

Tras realizar las modificaciones ya comentadas, se deberá hacer `git add` de los archivos modificados, `git commit -m Feat: modificación de la tarjeta de bienvenida`y por último `git push` para incorporar los cambios al repositorio remoto.



### **6.Creación de la Pull Request de pruebas: Benjamin Ignacio Maureira Flores**

Se deberá crear una pull request en la que se incorporen los cambios realizados en la rama ```task/test-nueva-tarjeta-bienvenida``` a la rama develop del proyecto tortilla-hub. Debe contener lo siguiente: 

- **Descripción del cambio:** Se creado un test de interfaz de selenium usando unitest (ya que public no es un modulo del proyecto) y se ha comprobado que funciona correctamente.

- **Motivación / Impacto:** Este cambio va acorde con las tareas de mantenimiento, calidad e integración continua del código que pretenden mantener un proyecto bien testeado en todos sus aspectos.

- **Instrucciones:** Se debe ejecutar el test con `rosemary selenium public` y comprobar que de positivo, además se debe comprobar visualmente que el cambio se ha realizado correctamente.

- **Asignado:** DelfinSR

- **Revisor:** antoniommff



### **7.Revisión de la Pull Request de pruebas: Antonio Macías Ferrera**
Se deberá comprobar que los cambios se ha realizado de manera correctamente en el proyecto local y que las pruebas de interfaz funcionan adecuadamente antes de aprobar la *Pull Request*. 

1. Se deberá traer los últimos cambios al repositorio local: `git fetch``
2. Se deberá cambiar a la rama ```task/test-nueva-tarjeta-bienvenida``` haciendo: `git checkout <nombre_rama>`
3. Se tendrá que correr el proyecto en local desde esa rama y ver que en la página de inicio de uvlhub aparece la nueva tarjeta navideña y que el test de selenium da positivo: `rosemary selenium public`.

Si todo esto es así se aprobará la Pull Request con un comentario: 
"
Los test funcionan correctamente. ¡Feliz Navidad! 👍✨👉🎁🙀
"



# Conclusiones y trabajo futuro

Creemos que nuestro proyecto ha sido un ejemplo claro de cómo una gestión estructurada, el trabajo colaborativo y la adopción de buenas prácticas en el desarrollo de software pueden llevar a resultados satisfactorios. La implementación de funcionalidades clave, como la creación de comunidades, el área de preparación (Staging Area), la sincronización con GitHub/GitLab y mejoras en la interfaz de usuario, ha permitido ofrecer una solución robusta y funcional a los problemas que se nos planteaban. Además, nos gustaría destacar que la integración de flujos de CI/CD mediante GitHub Actions, ha aumentado nuestro conocimiento sobre la metodología de una manera exponencial, de tal forma, que a día de hoy encontramos imposible desarrollar un nuevo proyecto de software sin CI/CD.

Durante el desarrollo, se identificaron diversas oportunidades de mejora y propuestas para el futuro:

- **Integración de Codacy**, para garantizar un análisis continuo de la calidad del código y reforzar las buenas prácticas de programación.

- **Reemplazo de Raspberry Pi** por servidores de mayor capacidad, lo que permitiría un despliegue más eficiente y estable, evitando limitaciones de rendimiento. La idea de desplegar nuestra aplicación en la Raspberry era ambiciosa y novedosa, pero pese a ser una tarea de difícil ejecución conseguimos desarrollarla casi al completo, nos frustramos al ver que la tecnología nos limitaba, a parte de perder muchas horas durante el intento de la implementación.

- **Ampliación de las funcionalidades de las comunidades**, ofreciendo mayor interacción y opciones personalizadas a los usuarios, incluso planteabamos la idea de incluir un foro para que los usuarios puedan interactuar directamente sobre los datasets.

- **Mayor cobertura de pruebas**, abarcando un espectro más amplio de escenarios y garantizando la fiabilidad del sistema ante cambios futuros.

- **Automatización y estandarización de procesos clave**, como las migraciones de bases de datos, que hemos tenido que hacerla nosotros para que no fuera una tarea tan tediosa y nos hubiera gustado que el proyecto original lo tuviera, sobre todo para contemplar la idea de que varias personas trabajen en el proyecto. También creemos que es esencial el uso de Github Projects, sobre todo para tener un vistazo muy rápido de las tareas y su estado, al ser 13 personas en el desarrollo, esto nos ha sido muy útil.

Por otro lado, nos hubiera gustado haber dedicado más tiempo al análisis detallado del **pipeline** actual. Esto habría permitido optimizar el uso de recursos en GitHub Actions, evitando **redundancias** y **reduciendo tiempos** en el flujo de trabajo.

Además, creemos que es imprescindible que se documente y se detalle mejor las **funcionalidades** y el **alcance** de los *Work Items*, lo que facilitaría la planificación y reduciría la dependencia de aclaraciones con el profesorado.

En resumen, el proyecto deja una base sólida para seguir evolucionando, con posibilidades claras de mejora que, si se implementan, consolidarán aún más su calidad, eficiencia y escalabilidad. Por nuestra parte, agradecer a todo el profesorado por darnos la oportunidad de aportar a este proyecto, en general ha sido una experiencia muy satisfactoria y ha sido un aprendizaje inmenso, sobre todo, sabiendo que nos vamos a ver en situaciones así al entrar al mundo laboral.