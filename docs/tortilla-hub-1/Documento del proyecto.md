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

Tortilla-Hub-1 es un sistema desarrollado por el Grupo 2 en el curso 2024/2025 como parte de la asignatura Evolución y Gestión de la Configuración. El proyecto tiene como objetivo principal proporcionar un entorno robusto y funcional para la gestión, calificación y publicación de datasets. Este sistema permite a los usuarios realizar operaciones clave como la carga y verificación de datasets, integración con plataformas externas como GitHub y GitLab, y la creación y gestión de comunidades. Además, se ha diseñado para facilitar la evolución continua y mantener altos estándares de usabilidad y eficiencia.

El proyecto incluye funcionalidades clave como la "zona de preparación" (staging area) para gestionar datasets antes de su publicación definitiva, un dashboard interactivo para visualizar estadísticas y datos relevantes, y mecanismos de validación automática de UVLs para garantizar la calidad y consistencia de los datos. Asimismo, se han integrado flujos de trabajo automatizados para la gestión de migraciones y detección de inconsistencias en los nombres de autores, mejorando así la eficiencia y colaboración del equipo.

## Descripción del sistema *(1500 palabras)* <!--{#descripción-del-sistema-(1500-palabras)}-->

Tortilla-Hub-1 se compone de varios módulos funcionales interrelacionados:

Cargador y validador de UVLs: Permite a los usuarios subir archivos UVL, verificando su validez sintáctica e indicando errores específicos cuando los haya.

Dashboard: Proporciona una vista general de las estadísticas del sistema, incluyendo el número de datasets, calificaciones y usuarios activos.

Integración con GitHub/GitLab: Facilita la carga de datasets en repositorios externos y sincronización con plataformas populares de desarrollo.

Creación y gestión de comunidades: Los usuarios pueden crear y unirse a comunidades temáticas, cargar datasets y participar en actividades colaborativas.

Staging Area: Un espacio dedicado a la preparación y edición de datasets antes de su publicación.

Cada módulo está desarrollado utilizando principios de arquitectura modular y patrones de diseño que garantizan su extensibilidad y mantenibilidad. El sistema también incluye flujos de trabajo automatizados para la gestión de migraciones de bases de datos y verificación de consistencia en la configuración del proyecto.

## Visión global del proceso de desarrollo *(1500 palabras)* <!--{#visión-global-del-proceso-de-desarrollo-(1500-palabras)}-->

El proceso de desarrollo se basó en las siguientes etapas:

Planificación: Identificación de requisitos y creación de issues en el tablero del proyecto.

Desarrollo: Implementación de funcionalidades en ramas específicas siguiendo un modelo de trabajo colaborativo.

Pruebas: Realización de pruebas unitarias, integradas y de sistema para garantizar la calidad.

Integración continua: Uso de workflows de GitHub Actions para automatizar tareas como verificación de migraciones y control de calidad.

Despliegue: Implementación en entornos de producción utilizando Docker y Render.

## Entorno de desarrollo *(800 palabras)*  <!--{#entorno-de-desarrollo-(800-palabras)}-->

El equipo utilizó una combinación de herramientas modernas, incluyendo:

IDE y Sistemas de Control de Versiones: Visual Studio Code, Git y GitHub.

Entornos de Prueba y Producción: Docker, Render y Raspberry Pi OS.

Gestores de Bases de Datos: MariaDB.

Automatización: GitHub Actions y Selenium IDE.

Colaboración y Documentación: Google Drive, Markdown y Copilot.

La configuración inicial del entorno incluye la instalación de dependencias mediante Docker Compose y la configuración de bases de datos y servicios auxiliares.

## Ejercicio de propuesta de cambio <!--{#ejercicio-de-propuesta-de-cambio}-->

El objetivo de esta ejercicio es añadir una nueva funcionalidad al proyecto tortilla-hub para fomentar la participación activa de la comunidad. Implementaremos una sección en el repositorio que permita a los usuarios colaborar mediante un foro de discusión. El desarrollo se llevaría a cabo de la siguiente manera:

#### Work Item: Desarrollo de la funcionalidad de fomento de la comunidad

1. Definir los requerimientos del cambio
Título del Issue: feat: Fomentar la comunidad mediante un foro de discusión y lineamientos para contribución
Descripción del Cambio:
Añadir un archivo CONTRIBUTING.md con guías detalladas para colaboradores.
Crear una sección en la documentación para promover el uso del foro de discusión de GitHub.
Configurar GitHub Discussions en el repositorio para facilitar la interacción con la comunidad.
Criterios de Aceptación:
Archivo CONTRIBUTING.md visible en el repositorio raíz.
Foro de discusiones habilitado y promovido en la documentación.

1. Crear un Issue
Abrir el repositorio en GitHub:
bash
Copiar código
git clone https://github.com/EGC-G2-tortilla/tortilla-hub.git
cd tortilla-hub


Crear un nuevo issue:
Navegar a la sección "Issues" del repositorio y pulsar en "New Issue".
Completar el issue siguiendo el formato definido en el archivo de gestión de issues (5.1 del documento subido).

3. Configurar una rama de trabajo
Crear una rama task/fomentar-comunidad:
bash
Copiar código
git checkout -b task/fomentar-comunidad



4. Implementación
4.1. Crear el archivo CONTRIBUTING.md
Crear el archivo en el directorio raíz:
bash
Copiar código
touch CONTRIBUTING.md


Añadir lineamientos para colaboradores:
markdown
Copiar código
# Guía para Contribuidores

Gracias por tu interés en contribuir a *tortilla-hub*. Sigue estas pautas:

1. **Fork del repositorio.**
2. Crea una rama descriptiva (`task/nueva-funcionalidad`).
3. Realiza cambios pequeños y claros.
4. Haz un pull request detallando tus cambios.
5. Participa en las discusiones y revisiones.

Para más información, consulta la [documentación](docs/).


Añadir cambios al staging y confirmar:
bash
Copiar código
git add CONTRIBUTING.md
git commit -m "docs: agregar guía para contribuidores"


4.2. Habilitar GitHub Discussions
En el repositorio, ir a Settings > Discussions y habilitarlo.
Crear categorías relevantes (e.g., "Preguntas", "Propuestas", "Errores").
4.3. Actualizar documentación
Modificar el archivo de documentación principal (/docs/index.md):
Añadir una sección para promover GitHub Discussions:
markdown
Copiar código
## Fomenta la Comunidad
- Participa en el foro de [Discussions](https://github.com/EGC-G2-tortilla/tortilla-hub/discussions) para preguntas y propuestas.
- Sigue la [Guía para Contribuidores](CONTRIBUTING.md).


Confirmar cambios:
bash
Copiar código
git add docs/index.md
git commit -m "docs: agregar sección sobre fomento de la comunidad"



5. Pruebas
Revisar que el archivo CONTRIBUTING.md sea legible y visible en la página principal del repositorio.
Validar que el enlace a Discussions funcione correctamente.

6. Realizar Pull Request
Subir la rama al repositorio remoto:
bash
Copiar código
git push origin task/fomentar-comunidad


Crear un Pull Request en GitHub y asignar revisores.

7. Fusionar y documentar el cambio
Una vez aprobada la Pull Request, fusionarla con la rama develop:
bash
Copiar código
git checkout develop
git merge task/fomentar-comunidad
git push origin develop


Documentar el cambio en el registro de versiones (CHANGELOG.md):
markdown
Copiar código
## [1.1.0] - 2024-12-15
### Añadido
- Archivo `CONTRIBUTING.md` para nuevos colaboradores.
- Habilitado GitHub Discussions para promover interacción.



Este proceso asegura que el cambio cumple con los estándares de gestión de configuración, promoviendo una comunidad más participativa y alineada con los objetivos del proyecto.


## Conclusiones y trabajo futuro <!--{#conclusiones-y-trabajo-futuro}-->

El proyecto Tortilla-Hub-1 demuestra la importancia de una gestión estructurada y colaborativa en el desarrollo de software. Para el futuro, se proponen las siguientes mejoras:

Integración de Codacy para análisis de calidad código.

Reemplazo de Raspberry Pi por servidores con mayor capacidad.

Expansión de las funcionalidades de las comunidades.