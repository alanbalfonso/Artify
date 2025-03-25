# image_handler.py

import os
import requests
import io
import json

# Diccionario para almacenar el mapeo entre el nombre seguro y el original
metadata_file = 'image_metadata.json'

# Función para limpiar los nombres de archivo y eliminar caracteres no válidos
def clean_filename(filename):
    # Lista de caracteres no válidos en los nombres de archivo
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    
    for char in invalid_chars:
        filename = filename.replace(char, '-')  # Reemplazamos los caracteres no válidos por '-'
    
    return filename

# Función para cargar el archivo de metadatos (si existe)
def load_metadata():
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as file:
            return json.load(file)
    return {}

# Función para guardar los metadatos
def save_metadata(metadata):
    with open(metadata_file, 'w') as file:
        json.dump(metadata, file, indent=4)

# Función para descargar la imagen del álbum y guardarla con el nombre "nombre del álbum - artista"
def download_album_image(album_url, album_name, artist_name, save_dir="downloads"):
    response = requests.get(album_url)
    
    if response.status_code == 200:
        # Crear la carpeta de destino si no existe
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # Crear el nombre del archivo con el formato "album_name - artist_name"
        filename = f"{album_name} - {artist_name}.jpg"
        safe_filename = clean_filename(filename)  # Limpiar el nombre del archivo
        
        file_path = os.path.join(save_dir, safe_filename)
        
        # Guardar la imagen con el nombre limpio
        image_data = io.BytesIO(response.content)
        
        with open(file_path, 'wb') as f:
            f.write(image_data.read())
        
        print(f"Imagen guardada: {file_path}")
        
        # Cargar los metadatos existentes
        metadata = load_metadata()
        
        # Registrar el nombre original y el nombre limpio
        metadata[safe_filename] = {'original_name': filename}
        
        # Guardar los metadatos
        save_metadata(metadata)

    else:
        print(f"Error al descargar la imagen: {response.status_code}")

# Función para eliminar una imagen de la carpeta si el álbum es eliminado
def delete_album_image(album_name, artist_name, save_dir="downloads"):
    filename = f"{album_name} - {artist_name}.jpg"
    safe_filename = clean_filename(filename)  # Limpiar el nombre del archivo
    
    file_path = os.path.join(save_dir, safe_filename)
    
    # Cargar los metadatos
    metadata = load_metadata()

    # Verificar si existe el archivo
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Imagen eliminada: {file_path}")
        
        # Eliminar el registro de los metadatos
        if safe_filename in metadata:
            del metadata[safe_filename]
            save_metadata(metadata)
    else:
        print(f"Imagen no encontrada para eliminar: {file_path}")

# Función para obtener el nombre original a partir del nombre seguro
def get_original_name(safe_filename):
    # Cargar los metadatos
    metadata = load_metadata()
    
    if safe_filename in metadata:
        return metadata[safe_filename]['original_name']
    return safe_filename  # Si no existe, devolver el nombre seguro por defecto
