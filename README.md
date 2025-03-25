# Artify - Descarga automática de portadas de álbumes de Spotify
Artify es una extensión de Spotify desde la terminal que permite descargar las portadas en HD de tus álbumes favoritos guardados en la biblioteca, ordenándolos y guardándolos dentro de tu computadora para preservar el arte de las portadas musicales.

## Características
- Descarga automática de portadas de álbumes agregados recientemente.
- Eliminación automática de imágenes de álbumes eliminados de la biblioteca.
- Manejo de cambios en portadas de álbumes.

## Instalación

### 1. Clonar el repositorio
```sh
git clone https://github.com/tu_usuario/artify.git
cd artify
```

### 2. Crear y activar un entorno virtual
#### Windows
```sh
python -m venv venv
venv\Scripts\activate
```
#### MacOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```sh
pip install -r requirements.txt
```

## Configuración de Spotify API
1. Crea una aplicación en el [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Obtén tu `Client ID` y `Client Secret`.
3. Configura los scopes necesarios en tu aplicación.
4. Añade tu `CLIENT_ID` y `CLIENT_SECRET` en el archivo `.env`.

NOTA: El archivo `.env` deberá verse así:
```sh
CLIENT_ID = "tu_client_id_aquí"
CLIENT_SECRET = "tu_client_secret_aquí"
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-library-read"
```

## Uso
Simplemente, una vez creado el archivo `.env` y habiendo sincronizado los datos a la API de Spotify podemos empezar desde la terminal con:
```sh
python main.py
```
El programa monitoreará tu biblioteca y gestionará automáticamente las portadas de los álbumes.

## Contribuir
Si quieres contribuir, haz un fork del proyecto y envía un pull request con tus mejoras.

## Licencia
Este proyecto está bajo la licencia MIT.
