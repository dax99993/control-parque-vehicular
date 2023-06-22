# Contenedor para servicio de control parque vehicular.
Repositorio para mantener en orden las partes para crear el proyecto,
cada parte es un submodulo en git.
El submodulo Backend y Frontend contienen instrucciones de como ser ejecutados
para desarrollo.
El sub

## Common
Contienen todos los modelos que son utilizados en la backend y frontend
para minimizar reduccion de codigo.


## Backend
Contiene todas las dependencias y archivos para hacer tener un servidor backend,
con una dependencia a Common para obtener los modelos.

## Frontend
Contiene todas las dependencias y archivos para hacer tener un servicio frontend,
con una dependencia a Common para obtener los modelos al realizar las peticiones
a la API.


## Instalacion

### Clonar el repositorio
```sh
git clone https://github.com/dax99993/control-parque-vehicular
git submodule update --init --recursive
git submodule update --recursive --remote
```

