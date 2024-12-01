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
