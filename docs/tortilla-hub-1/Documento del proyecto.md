# TORTILLA-HUB-1

* Grupo 2  
* Curso escolar: 2024/2025  
* Asignatura: Evolución y Gestión de la Configuración

# Miembros <!--{#miembros}-->

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

[Miembros](#miembros)

[Indicadores del Proyecto](#indicadores-del-proyecto)

[Descripción de los Work Items implementados](#descripción-de-los-work-items-implementados)

[Integración con otros equipos](#integración-con-otros-equipos)

[Resumen Ejecutivo (800 palabras)](#resumen-ejecutivo-\(800-palabras\))

[Descripción del sistema (1500 palabras)](#descripción-del-sistema-\(1500-palabras\))

[Visión global del proceso de desarrollo (1500 palabras)](#visión-global-del-proceso-de-desarrollo-\(1500-palabras\))

[Entorno de desarrollo (800 palabras)](#entorno-de-desarrollo-\(800-palabras\))

[Ejercicio de propuesta de cambio](#ejercicio-de-propuesta-de-cambio)

[Conclusiones y trabajo futuro](#conclusiones-y-trabajo-futuro)

# Indicadores del Proyecto <!--{#indicadores-del-proyecto}-->

| Miembro del equipo | Horas | Commits | LoC | Test | Issues | Work Item |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Fernández Pérez, Pablo | 13h | 40  |+1090 -322   |  | 16 | Upload, analyse and repair UVL |
| Iborra Conejo, José Miguel | 14h 13min |24  |+4074 -823  |  |5  | Rate datasets / models |
| Macías Ferrera, Antonio |28h 13min  |57  |+12940 -4462  |  |17  | Dashboard |
| Maureira Flores, Benjamín Ignacio |20h 11min  |27  |+13418 -74  |  |8  | Sync with github/gitlab |
| Ridruejo Pineda, Guadalupe | 36h 8min |  |  |  |  | Improve UI |
| Santana Rubio, Delfín |16h 27min  |90  |+5833 -2684  | 53 |26  | Create communities |
| Vela Camacho, Daniel |21h 3min  |58  |+2863 -1530  |  |25  | Staging area |
| **TOTAL** |  |  |  |  |  |  |

# Descripción de los Work Items implementados <!--{#descripción-wis}-->

#### **1. Upload, Analyse, and Repair UVL:**
Esta funcionalidad permite a los usuarios cargar archivos UVL (Universal Variability Language) y verificar su validez sintáctica. Si se detectan errores, el sistema indica la línea exacta donde ocurren, ayudando al usuario a corregirlos. Esto resuelve una necesidad clave: evitar que los usuarios suban archivos UVL con errores cuando cargan un nuevo dataset a UVLHub. Anteriormente, no existía un sistema de comprobación, lo que dificultaba la detección de errores. 

#### **2. Rate Datasets:**
Se ha desarrollado un sistema de calificación para que los usuarios puedan evaluar datasets. Esta funcionalidad incluye:

- Sistema de valoración mediante estrellas: Los usuarios pueden asignar una puntuación a un dataset y actualizarla si lo desean.

- Cálculo y visualización de estadísticas: Se muestra la puntuación media y el número total de calificaciones para cada dataset, ofreciendo a otros usuarios información relevante sobre la calidad del contenido.

#### **3. Dashboard:**
Se ha modificado la pantalla principal ("Home") para mostrar datos y estadísticas relevantes sobre los datasets. Esta vista inicial permite a los usuarios logueados tener una visión general del contenido más destacado y del estado de los datasets disponibles en el sistema.

#### **4. Sync with GitHub/GitLab:**
Se ha implementado la sincronización con plataformas como GitHub y GitLab para facilitar la gestión de modelos UVL. Los usuarios pueden iniciar sesión en estas plataformas desde la vista de "Upload Dataset" y, al cargar un dataset a Zenodo, también pueden subirlo automáticamente a un repositorio personal en GitHub o GitLab, integrando ambas plataformas en el flujo de trabajo.

#### **5. Improve UI:**
Se ha mejorado la interfaz de usuario para que la enumeración del contenido de los datasets sea lo más similar posible a la experiencia ofrecida por GitHub. Este cambio busca mejorar la usabilidad, basándose en el principio de previsibilidad, facilitando la navegación y el uso intuitivo del sistema.

#### **6. Create Communities:**
Se ha introducido la funcionalidad de comunidades en UVLHub.io, permitiendo a los usuarios:

- Crear y listar comunidades.
- Solicitar unirse a una comunidad y, tras la aprobación del administrador, integrarse a ella.
Subir datasets específicos a comunidades.
- Cada comunidad cuenta con un administrador que gestiona las solicitudes de membresía, asegurando un control adecuado sobre los miembros y el contenido compartido.

#### **7. Staging Area:**
Se ha diseñado una "zona de preparación" que permite a los usuarios gestionar sus datasets antes de publicarlos en plataformas como Zenodo o Fakenodo. Esta área ofrece:

- Selección de datasets: Los usuarios pueden decidir qué datasets quieren publicar y cuáles mantener en estado privado.
- Edición previa a la publicación: Se permite realizar modificaciones en los metadatos, corregir errores o ajustar cualquier aspecto del dataset antes de su publicación final.
- Indicador de estado: Cada dataset tiene un indicador que muestra si está listo para ser publicado, en proceso de revisión o pendiente de ajustes.

Esta funcionalidad proporciona flexibilidad, control y asegura que el contenido cumpla con los estándares de calidad antes de hacerse público.

# Integración con otros equipos <!--{#integración-con-otros-equipos}-->

Este proyecto es el resultado de la colaboración entre los equipos **Tortilla-Hub-1** (nuestro equipo) y **Tortilla-Hub-2**. 

Desde el inicio, se celebró una reunión conjunta en la que se definieron los acuerdos fundamentales que guiarían todo el desarrollo del proyecto. En esta reunión, se tomaron las siguientes decisiones clave:

- **Asignación de Work Items:** Se estableció claramente qué _Work Items_ serían responsabilidad de cada equipo.
- **Uso de un repositorio común:** Se decidió trabajar desde el principio en un repositorio compartido ([tortilla-hub](https://github.com/EGC-G2-tortilla/tortilla-hub)) para minimizar posibles errores y conflictos durante la integración de los subproyectos.
- **Definición de pautas de trabajo:** Todas las normas y directrices relacionadas con la gestión del repositorio y del código fuente quedaron documentadas en el **Acta de Constitución**, garantizando un desarrollo ordenado y coordinado. Estas pautas han sido cumplidas satisfactoriamente por ambos equipos.

Guadalupe Ridruejo Pineda asumió el rol de coordinadora, asegurando una correcta sincronización entre los equipos. Además, se mantuvo una comunicación diaria a través de un grupo común de **WhatsApp**, lo que facilitó una colaboración fluida y eficiente a lo largo de todo el proyecto. 

# Resumen Ejecutivo <!--{#resumen-ejecutivo}-->

Tortilla-hub es un fork del proyecto UVLHub de DiversoLab, creado para la asignatura Evolución y Gestión de la configuración (EGC) del grado en Ingeniería del Software de la Universidad de Sevilla desarrollado gracias a la colaboración de dos equipos: **tortilla-hub-1** y **tortilla-hub-2**.

Este proyecto sirve como repositorio de modelos de características en formato UVL, integrado con Zenodo y Flamapy. Incluye varias modificaciones realizadas por los estudiantes del curso, lo que proporciona experiencia práctica en un entorno de implementación e integración continua. Los estudiantes han practicado la automatización de pruebas y verificaciones mediante GitHub Actions y han colaborado de manera eficaz dentro de varios equipos. 

Tortilla-hub-1 ha contribuido al proyecto proporcionando un entorno robusto y funcional para la gestión, calificación y publicación de datasets, permitendo a los usuarios realizar operaciones clave como la carga y verificación de datasets, integración con plataformas externas como GitHub y GitLab, y la creación y gestión de comunidades. Además, se han añadido modificaciones de diseño para facilitar la evolución continua y mantener altos estándares de usabilidad y eficiencia.

El proyecto incluye, además, funcionalidades clave como la "zona de preparación" (staging area) para gestionar datasets antes de su publicación definitiva, un dashboard interactivo para visualizar estadísticas y datos relevantes, y mecanismos de validación automática de UVLs para garantizar la calidad y consistencia de los datos. Asimismo, se han integrado flujos de trabajo automatizados para la integración continua y el despliegue continuo, tal y como se detallará en el punto siguiente.

## Descripción del sistema *(1500 palabras)* <!--{#descripción-del-sistema-(1500-palabras)}-->

- _Incluir módulos y aportaciones_
- _Pruebas realizadas_
- _CI_
- _CD_

## Visión global del proceso de desarrollo *(1500 palabras)* <!--{#visión-global-del-proceso-de-desarrollo-(1500-palabras)}-->

El proceso de desarrollo se basó en las siguientes etapas:

- **Planificación**: Selección de Work Items, subdivisión de tareas (se debía estimar tamaño, prioridad y etiquetas, en función de si afectaba a un WI, a la implementación de Fakenodo, si se trataba de un Workflow o si era documentación) y creación de issues en el tablero del proyecto.

- **Desarrollo**: Implementación de funcionalidades en ramas específicas siguiendo un modelo de trabajo colaborativo.

- **Pruebas**: Realización de pruebas unitarias, de integración, de carga y de interfaz (según correspondiese a la tarea en concreto) para garantizar la calidad.

- **Integración continua**: Uso de workflows de GitHub Actions para automatizar tareas como verificación de migraciones y control de calidad.

- **Despliegue**: Implementación en entornos de producción utilizando Docker y Render.

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