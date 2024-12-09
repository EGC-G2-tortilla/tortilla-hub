# [1.16.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.15.0...v1.16.0) (2024-12-10)


### Bug Fixes

* se ha solucionado un error en las solicitudes de entrar a una comunidad en el que se alteraba el id de user_profile sin querer ([63ad0a2](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/63ad0a225a55c5d0460ec3035884461d78f9e34d))
* Sustituido distutils por setuptools por quedar obsoleto ([c1a2f6a](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c1a2f6a07268ce48175e0b144e4f86f642c8493b))


### Features

* Añadido setup para monitorización con Grafana y Prometheus ([48abd8b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/48abd8b508c28174e8511e076c92e8b2addd8081))

# [1.15.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.14.2...v1.15.0) (2024-12-09)


### Features

* despliegue con vagrant arreglado ([ba7dfdb](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ba7dfdb18260f5355dd8f25a2cbcc988473a04ff))

## [1.14.2](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.14.1...v1.14.2) (2024-12-08)


### Bug Fixes

* Cambio en los Secrets y añadir un argumento al navegador ([8d8241d](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/8d8241d8f48918d0242ecdc8f97f1597bc5d8ac7))

## [1.14.1](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.14.0...v1.14.1) (2024-12-08)


### Bug Fixes

* Añadir argumentos para la compatibilidad del navegador ([b8e5a33](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/b8e5a33009f2c6e5c8b5364faf07756edc919967))

# [1.14.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.13.1...v1.14.0) (2024-12-08)


### Features

* Añadir workflow para medir la accesibilidad. ([a35ae36](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/a35ae3696a7924723a0a8e77e2a782cfe2f756fe))

## [1.13.1](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.13.0...v1.13.1) (2024-12-07)


### Bug Fixes

* se introducido una solucion para que el workflow de crear issues si el autor no esta en el .mailmap no de falsos positivos Close [#176](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/176) ([7890dd7](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/7890dd7b1bb3d619c99d124d70de7d5f34723ab6))

# [1.13.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.12.0...v1.13.0) (2024-12-05)


### Bug Fixes

* Corrección de test_client en las pruebas de descarga de todos los datasets ([aa72d9f](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/aa72d9ff7d50237127c28150129228766ee57973))
* Corregir del borrado de datos de las pruebas ([2258b28](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/2258b28deff36041f8ea655264cad3035f75b6f8))
* Mejorar la gestión de directorios temporales ([22f49fa](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/22f49fabf18515ac97fee52d5b7acb087301d4f3))


### Features

* Establecer el directorio de trabajo en las pruebas de transformación de archivos ([391959a](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/391959ab034cab1b76afc5c4b7f987611c42351d))
* nuevo workflow que crea una issue si detecta que se ha hecho push a main con un autor que no esta registrado en el archivo .mailmap ([4786e1d](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/4786e1defac54ae15c8d31914c9b6008707ed15d))

# [1.12.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.11.0...v1.12.0) (2024-12-04)


### Bug Fixes

* Arreglos codacy ([8f40afb](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/8f40afbbc0d3cd2b6cc62b6a87cca989846d03c6))
* Arreglos en tests para ejecución en rosemary ([e3986d8](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e3986d8b4665b15cf380a4ab00e7f670e839bce4))
* Errores de codacy y localización del entrypoint ([318eb85](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/318eb85fd58f8113984b501693c4aa962466bce4))


### Features

* Añadir entrypoint e imagen nueva para datos de prueba en develop. ([ae81140](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ae811401c608cbeac46ec75c01a61fadd29b9ddb)), closes [#167](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/167)

# [1.11.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.10.0...v1.11.0) (2024-12-03)


### Bug Fixes

* errores de estilo de linter solucionados ([eeb05a3](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/eeb05a3ba4faebaedd4d8abe07ad9904b8b0b918))
* **rating:** prevent users from updating existing ratings ([4fee2ca](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/4fee2ca70e268ba563d7121ffc94a589f240cc97))


### Features

* añadida funcionalidad y vista para poder ver las comunidades a las que pertenezco ([087e6ee](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/087e6ee848c4b9b2d18fa84e71fc0a4d8fcb5b11))
* añadido boton para poder acceder a mis comunidades desde el menu de la izquierda ([153eb82](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/153eb826370deb6fba19e7834de9d4e2eedb301c))
* añadido el test de selenium  para stagear un dataset ([48cd79b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/48cd79b5c7fb54de9a5c77548abb9d276b2194a5))
* añadido el test de selenium para unstagear un dataset ([728cc6a](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/728cc6a4e984cfa40924ccf363aafc5de52f894e))
* añadido poder unstagear todos los datasets simultánea ([e972103](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e972103e7b893814909914e9401c8f6363908179))
* Añadido test de interfaz para subir archivos UVL ([66946a6](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/66946a65790b5def9db08a3427ca231c66928cf7))
* añadidos los test para stagear todos los datasets y publicarlos ([e1999dd](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e1999dd79bf95ce0c16551b740afde6d5ea721d8))
* añadidos los tests de carga para las operaciones de staging area closes [#104](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/104) ([6fe9889](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/6fe98897d9bffd6431a0fbea1a6aa47ed3ad0479))
* añadidos tests de interfaz para stage all y unstage all datasets ([dad632d](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/dad632d2cd38da5d66658714f0529ef8b7a1d9e6))
* añadidos tests unitarios de stage all y unstage all datasets ([496f230](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/496f230ef12eff9d32848f377291fb4ff11c283a))
* **dataset:** add dataset rating functionality ([3aa8d47](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/3aa8d47f08c76a0683efb9ab0f82cb600c85d439))
* **dataset:** add DatasetRating model, migration, and seeders ([50c207d](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/50c207d5df2b5626568a11a38dc5686eafd59427))
* Mejoras en la UI al mostrar los mensajes de error de sintaxis ([d7ff6d4](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/d7ff6d41874b62d221032b068c2f776c16940bee))
* **rating:** integrate dataset rating functionality in frontend and update logic for rating modifications closes [#58](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/58) ([f2f22a5](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/f2f22a569973f67cfb010c48168a4ba4229855a4))

# [1.10.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.9.0...v1.10.0) (2024-12-02)


### Bug Fixes

* errores de estilos solucionados para que pase el test de codacy ([b40e240](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/b40e2403b701e400b47557fbc82ee0c5b175a743))


### Features

*  vista para funcionalidad para poder ver si tu solicitud de acceso a una comunidad se ha enviado y está siendo revisada o no y así que el usuario tenga feedback añadida ([6d43179](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/6d431795a7c847293886cce2d11efa9debd0ef5c))
* actualizadas rutas de CommunityJoinRequestService para que se pueda crear, aceptar y eliminar una solicitud para unirse a una comunidad ([e923ad4](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e923ad4cd0c5e2580f866ecd63a75794bbffb52d))
* añadida funcionalidad al servicio de comunidades para poder buscar por id ([5ff5db2](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/5ff5db2925d08d3288307521e18b8a2b38b627e7))
* añadido cambio para poder recibir solicitudes de unirse a comunidad desde el frontend ([b747088](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/b747088f0745450bbbfe8087077af4ee8eae358d))
* conseguida funcionalidad de aceptar y denegar solicitud para unirse a comunidad. ([d15d895](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/d15d8952f97dd665df0e49d2316a1606ac72bb68))
* creado modelo para la solicitud de unirse a una comunidad ([103df8b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/103df8b852e3c5040f1324ec7be94b285f202f4f))
* funcionalidad para poder ver si tu solicitud de acceso a una comunidad se ha enviado y está siendo revisada o no y así que el usuario tenga feedback añadida ([77b380c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/77b380c3bddae8a00ddf9043c2d48a168917cbf2))
* inicializado modulo con rosemary para enviar solicitud de unirse a una comunidad ([1225972](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/1225972eac600b091d96b2d09c95a2e6a621485c))
* migración de CommunityJoinRequestService creado ([0713888](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/071388843f04ab443457aae25fb2a1fe297d9d9b))
* repositorio de CommunityJoinRequest actualizado ([914abb8](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/914abb85d1611e34dafe11647f4724461003949c))

# [1.9.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.8.0...v1.9.0) (2024-12-01)


### Bug Fixes

* Agregar archivos faltantes en la carptea upload ([c6d057b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c6d057b153427a822bf187efa95dcf4ece088208))
* workflow es lanzado correctamente en PRs closes [#50](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/50) ([d23ae14](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/d23ae143fc93d16e793f8701ccbb83d412043d34))


### Features

* Añadidos los tests unitarios closes [#104](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/104) ([080e992](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/080e9923966c9b4a1d1d78cb14e3c0a56332a657))

# [1.8.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.7.0...v1.8.0) (2024-11-28)


### Bug Fixes

* ahora la url cuando subes un dataset a una comunidad está bien puesta. ([f262eaa](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/f262eaa117ac340e3265904d257104feeba1c563))
* Añadida validación para UVLs vacíos. Closes [#94](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/94) ([77dcd95](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/77dcd953178be7d7b8b34bb9be1b0c933a77750b))
* Arreglar errores codacy ([df8cad0](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/df8cad02c5ea6ba415d4af19d1165aac5b6c49b5))
* solucionado el error de que no se vea el link para acceder a las comunidades si no estas logueado. Close [#86](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/86) ([3e3594f](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/3e3594ff20777b7fb1fa96d6ab3335e1f7d1af47))
* solucionados errores de linter. Close [#69](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/69) ([afd5d20](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/afd5d20f47d7ce4bc91bd473d89a2651477f8a24))


### Features

* añadido boton para subir datasets a una comunidad ([db032f9](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/db032f92d433d90a0254cced97174b5b3e26c0e5))
* Añadido test de rendimiento con locust ([5243e13](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/5243e13cbaeefc68f5d8921a0fe32e0a097a0c0d))
* Añadido test de rendimiento con locust ([28f0813](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/28f0813440311a028dada1c8d5d494a83ceff8be))
* Añadidos más tests unitarios para la validación de UVLs ([4c60615](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/4c6061561376e7c1d7111e2881f81f44bb1bef41))
* Añadir funcionalidad para subir archivos desde GitHub ([475be15](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/475be158ca00e1aea08f9823242b0e25f9b20d64))
* funcionalidad añadida para subir datasets a una comunidad ([ecc9519](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ecc9519f2eb4c29221f298baa2a969cbbb24459a))
* Implementar vista de subida de archivo de github ([85fbb2c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/85fbb2c16fbde2d0ab0b3cfc46cd319837a484a9))

# [1.5.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.4.0...v1.5.0) (2024-11-19)


### Bug Fixes

* Añadida validación de uvl en la creación de un dataset ([992710e](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/992710e9d90473e40419e521f4891e1921d50aba))
* Añadida verificación condicional del estado del dataset antes de publicarlo ([007ca72](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/007ca72900905c124810a0d768a63e9094358e51))
* Añadido a tabla dataset que el id de comunidad pueda ser nulo ([5a621f2](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/5a621f2b16db9601df24c9cb294331c118aa2bed))
* añadido boton para volver a la vista de los datasets porque antes no se podia volver ([37bcd32](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/37bcd321d2b304a173ba6ef44803abc33c351bd6))
* Añadidos permisos de escritura al workflow ([687a8d5](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/687a8d56927734c44e5c9f3061d7e4258ecf6cdc))
* Añadir ORCID id al vincular a una cuenta existente ([b2316db](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/b2316dbd02c6f2745876926ca9ac83bd4f35ec79))
* Arreglado espacios en blanco ([dec50c5](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/dec50c5272db3017f062d6166e1569f83e276a4c))
* Arreglar las migraciones ([26a39f3](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/26a39f347b41761f6a049b2c0f9d6bc78395ffd4))
* cambiar la version de actions/checkout a una más nueva. Close [#39](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/39) ([49bcc7c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/49bcc7cf07402266bc6d47cd2fad473e6d1001da))
* Comprobación multiples o_auth_providers ([2e9c098](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/2e9c098add6fda9c8c799ddde613b243db19ce8f))
* Correción del archivo CHANGELOG.md ([a5fdde6](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/a5fdde6f235985cde178aafd5d1389e47e4fc4d7))
* Corregido error detectado en PR en el modulo dataset ([7f317cd](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/7f317cd7e81dff3d129476e18de29ecc306e42a0))
* Corregidos errores detectados en PR en el modulo flamapy ([94d7156](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/94d7156551d4f5d7da764fdacc38729d60393c6b))
* Error al pasar el id para sumular la creacion de un depósito ([98f7cd9](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/98f7cd97718c24e9ba6c4a68f3c1924346fe9bbe))
* error con flake8 por espacios ([cb891b8](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/cb891b8713669bc9c50a156666310ba8a248953a))
* error en la creación del atributo de dataset_status en las migraciones ([e8a5a55](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e8a5a55d11ff16fc23ec9417c73a7b7799b59f85))
* error por relacion entre community y datased solucionado en el archivo de migracion ([cfd7406](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/cfd7406175d96489c9cd96b33fd27f616faeb24c))
* Modulo completo ([2302849](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/2302849d6320431eaca845aae6b75a9b2b83ffea))
* organización de las migraciones por milestone closes[#45](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/45) ([c604e24](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c604e248888a5146cb0a3ca8b710f5f91a2fcf7c))
* Secretos actualizados ([6556537](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/6556537967e95c5ede51992752294a11beaf584e))
* seeders ahora no contienen datos repetidos closes [#47](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/47) ([2568047](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/2568047c60ab5629a6b113afe90bbad05547fb2c))
* solucionado error en vista de create_community cambiado zenodo.scripts por fakenodo.scripts ([6694dc1](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/6694dc1ed2a9c0b09e53cfee4c37e255ec165c82))
* Solucionado varias heads en migraciones ([04d2f91](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/04d2f91c440ea85036158364c880fbd15dd1ee93))
* workflow se lanza adecuadamente para pushes en main/ develop closes [#50](https://github.com/EGC-G2-tortilla/tortilla-hub/issues/50) ([4e76e4f](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/4e76e4f1b4d386c6bc475a623060e118bca38ef8))


### Features

* added name, url, description to community model ([45c5489](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/45c54895373ffe8ec1acb460ef2e0a4de52c27f5))
* Añadida corrección de errores de linting detectados mediante workflow ([5e2555c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/5e2555ca641c56f38ee4c8607b0254777ce2e404))
* añadida funcionalidad de admin a las comunidades ([ff3e4d3](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ff3e4d3fdf422bc6380ace649b4b7cd8fee786ac))
* añadida funcionalidad de listar los datatasets que pertenecen a una comunidad ([644b4ed](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/644b4ed47511c40713737ba7d62b2d3267ab78ed))
* añadida funcionalidad de unirse a comunidad ([9246fde](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/9246fde15ed2bcfded7d6699f72dd09cff2889bb))
* Añadida funcionalidad y vista para crear comunidades ([c632d41](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c632d4191b14d4bc0505e6b247ef2f9ee8e6f3e5))
* Añadida lógica de inicio de sesión y registro con Github ([c3bbc2a](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c3bbc2a34a4354cc48e9f652c50721777d925cc2))
* Añadida propiedad "estado"  al modelo de la entidad dataset ([9757cdd](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/9757cddf887f7e27c5f219974e88f159f783c0c8))
* añadida una vista para hacer pruebas ([291640f](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/291640f94c731b0d3430a4caa6186e39916c3b32))
* añadida vista de descripción de comunidad y botones para acceder a ella ([ce20af6](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ce20af6b77eb3d22feca88461d9d3d60db16fad0))
* añadida vista y funcionalidad para ver miembros de una comunidad ([684ff2b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/684ff2b38876c5e7b732399ed1d09a9b0f3d314e))
* Añadidas funcionalidades de staging, unstaging y publicación de datasets sin integración con Fakenodo ([f00824b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/f00824bbc30bd1651dff07be946220c9eef4cb58))
* añadido actions que mergea las migraciones las HEAD de las migraciones si detecta que hay varias. ([65f82b8](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/65f82b8d1587c83e9f0c852efaff4dfec53345ca))
* Añadido el archivo releaserc ([8b382a7](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/8b382a78998efb71f26d8e95ad834136e992c562))
* Añadido mensaje de error en dropzone y eliminación de UVL inválido ([7fde306](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/7fde3062e0a362bf1dd2f2531c5520436987979c))
* Añadido workflow de versionamiento automático ([71e7c7b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/71e7c7ba244a7910fad45caa50d94c6b510851cc))
* añadidos datos por defecto para community ([c8eb237](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c8eb237a031a8c91654f6e1f35dc3bec6feb990d))
* Añadir carga de archivos y publicar métodos de simulación en FakenodoService ([ffb4c92](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ffb4c9258b1a40848f961eb2361b0f7cf2d54b8f))
* Añadir carga de archivos y publicar métodos de simulación en FakenodoService ([83b2b20](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/83b2b2096d7e4607e8d890f610cf5f592d1078ba))
* Añadir configuración basica de OAuth e implementar sistema de sign-up con Google. ([ee13d7e](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/ee13d7e1dccf16b67900c4e127974b366be2ca14))
* Añadir el modelo de Fakenodo y el formulario ([4f39c5c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/4f39c5cdd0d1366e73c48e145c98c9420cdb9ded))
* Añadir el repositorio de Fakenodo para la interacción con la database ([11c12b5](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/11c12b5badce4f4ce929ea9579d04e31814f0647))
* Añadir funcionalidad para descargar todos los datasets como un archivo ZIP ([8d0d52a](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/8d0d52abfc3c39acf4ec32b483c98d8f39f74bf4))
* Añadir lógica de inicio de sesión y registro con OAuth ([37315e4](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/37315e4f4c53ab6895e3e24b21b6becb49f7917e))
* Añadir nueva validación de archivos antes de la carga ([2e9e809](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/2e9e80982c1c1abcb888112584460c35fea992e6))
* añadir opción para stagear todos los datasets a la vez ([a3b96cd](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/a3b96cd2112e89fb94531783f0c2a7bd1c858144))
* Añadir redirección para usuarios en el flujo de inicio de sesión y registro con Google. ([85eaf07](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/85eaf0752e44eae04979f1867c916d87020d1b3b))
* Añadir rutas para Fakenodo ([b115739](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/b1157397d73878872d71d70c3793ae8db5f074dc))
* Añadir soporte login y autenticación con ORCID ([99ba099](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/99ba099fc8918faef50abc1da437a4be898652db))
* Botón de descarga de todos los datasets ([a0506ad](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/a0506ad9036d60b12b7fb8b06228712d908e802a))
* Botones para subir modelos ([e5bc83c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e5bc83c277b44b67903156d79e9936d0f9730c0c))
* community form created(not finished) ([b714455](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/b7144558d40321daa46e1467ba4fa86eb2374ab6))
* creadas relaciones entre comunidades, usuarios y datasets ([9f962f0](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/9f962f055800081f12143cb9cb40cd88a25e1387))
* Creado el archivo changelog ([7930faa](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/7930faa77dff15876a6776ef65d1765bfd836886))
* created community model with rosemary ([02ddfc6](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/02ddfc64da817fe725bd15b08a910467406f591c))
* Implementar FakenodoService con funcionalidad de muck  básica ([f35c108](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/f35c108c01aa68e817383574bedfae4596d10b9a))
* implementar funcionalidad de validación de UVL sin necesidad de registrar el archivo en BD ([cc57c6b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/cc57c6b4c67cd26b85e5f5407c92fba09c77d847))
* Implementar subir desde Zip ([c0f71c3](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/c0f71c36c607cff0bd2ab37b74bffe31bb1746ec))
* Lógica creación de multicuentas con OAuth ([4a0ee57](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/4a0ee5762aecee8def0f3566f12a4d993afcb1ed))
* Mejorar la gestión de permisos y optimizar la carga de archivos ZIP ([cddcac1](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/cddcac1e4efe1bd4be70a9b1e042d40a20702d27))
* migraciones y seeders actualizados para corresponder actualización del modelo ([f72ef55](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/f72ef553094cf1d544c3ba15ed12ce05ce96a3eb))
* Primera vista de comunidades funcionando. Se pueden listar las comunidades. ([bdd0713](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/bdd071382d73c4858a95884ba0602b0222322ff1))
* Sustituir todas las llamadas a ZenodoService por FakenodoService y eliminar el modulo de zenodo ([dcb9184](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/dcb91849714c955c25c961a0611499c4de501573))


### Reverts

* Revert "Fix: estilo css modificado por Codacy" ([8685223](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/8685223b9281685aad2c2b402d3c1c7ce7b417da))

# Changelog

Todos los cambios notables en este proyecto se documentarán en este archivo.

# [1.4.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.3.1...v1.4.0) (2024-11-16)


### Features

* Añadido workflow para creación automática de PRs ([3ef6558](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/3ef6558fb7718d7482bf4c6bc40b65651eddb438))

## [1.3.1](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.3.0...v1.3.1) (2024-11-16)


### Bug Fixes

* Eliminados campos redundantes en la plantilla de issue ([e141c29](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e141c2996ba14d1912e278f16cfdc823ea76bd28))

# [1.3.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.2.0...v1.3.0) (2024-11-14)


### Bug Fixes

* cambiada la descripción a textarea ([33a6b50](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/33a6b50eb3342e8b70e50840f001376ca00637ed))


### Features

* Añadida corrección de errores de linting detectados mediante workflow ([7c18b85](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/7c18b85ac3de6accff21669ee6c66943fa217b49))

# [1.2.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.1.1...v1.2.0) (2024-10-31)

### Features

* Workflow para despliegue en render y eliminación de despliegue en pre-producción. ([e705aa6](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e705aa6e1ef4ba4c07db1b615218142be50e7b36))

## [1.1.1](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.1.0...v1.1.1) (2024-10-31)

### Bug Fixes

* Añadir .venv a gitignore ([02ddcb1](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/02ddcb1e975445e2aeea1b55d0d5a178f395467b))

# [1.1.0](https://github.com/EGC-G2-tortilla/tortilla-hub/compare/v1.0.0...v1.1.0) (2024-10-31)

### Features

* Workflow implementado para la Integración Continua con Codacy ([9cbc477](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/9cbc4774a80a63683ad48e792641f0d68db73bdf))

# 1.0.0 (2024-10-25)

### Features

* Añadido el archivo releaserc ([8d4c6ee](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/8d4c6eebab32bd100568df8ace3e0773d2f69ed1))
* Añadido workflow de versionamiento automático ([2af1c1c](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/2af1c1cc01efc30dac3f01f8a5bae633ce7e2237))
* Creación de la rama develop ([e80c647](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/e80c647a3d81d3996d2cae328bf9a252cd700b85))
* Creado el archivo changelog ([201b61b](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/201b61b5dde44d1af3a0a5fb927caf764753251e))

### Bug Fixes

* Añadidos permisos de escritura al workflow ([5760bda](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/5760bda89605a60e6098049bead6bb973133a441))
* First commit ([f27af8e](https://github.com/EGC-G2-tortilla/tortilla-hub/commit/f27af8ed4a4f1fda31cc926eccfd01449770faa0))

## [0.1.0] - 2024-10-22

### Added

* Primera versión estable del proyecto.
