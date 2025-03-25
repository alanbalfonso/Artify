import time
from spotify_api import get_recently_added_albums
from image_handler import download_album_image, delete_album_image

RUN_DURATION = 60 * 60  # 1 hora

def main():
    print("Iniciando monitoreo de la biblioteca de Spotify...")

    downloaded_albums = {}

    while True:
        albums = get_recently_added_albums()

        # Descargar imágenes de álbumes agregados recientemente
        for album_id, album_name, artist_name, album_url in albums:
            if album_id not in downloaded_albums:
                download_album_image(album_url, album_name, artist_name)
                downloaded_albums[album_id] = (album_name, artist_name)

        # Eliminar imágenes de álbumes eliminados de la biblioteca
        for album_id in list(downloaded_albums.keys()):
            if album_id not in [a[0] for a in albums]:
                album_name, artist_name = downloaded_albums.pop(album_id)
                delete_album_image(album_name, artist_name)

        time.sleep(60)  # Revisar cambios cada minuto

if __name__ == "__main__":
    main()
