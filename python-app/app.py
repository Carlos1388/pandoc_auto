import subprocess
import os

def convert_with_pandoc(input_file, output_file):
    """
    Función para convertir un archivo usando Pandoc a través de Docker.
    """
    input_path = os.path.abspath(f"./data/inputs/{input_file}")
    output_path = os.path.abspath(f"./data/outputs/{output_file}")
    
    # No montar el archivo de salida, solo el directorio
    command = [
        'docker', 'run', '--rm',
        '--volume', f"{os.path.dirname(input_path)}:/data/inputs",  # Montar el directorio de entrada
        '--volume', f"{os.path.dirname(output_path)}:/data/outputs",  # Montar el directorio de salida
        'pandoc_mod',
        # '--pdf-engine=xelatex',
        # '-t','context',
        '--shift-heading-level-by=-2',
        # '--extract-media', '/data/outputs',
        f"/data/inputs/{input_file}",   # <-- Cambiar el directorio de entrada si se quiere buscar en subcarpetas
        '-o', f"/data/outputs/{output_file}"  # <-- Cambiar el directorio de entrada si se quiere buscar en subcarpetas
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Archivo {input_file} convertido a {output_file} correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Pandoc: {e}")

if __name__ == "__main__":

    # INPUT
    formato_salida = 'md'   # Formato de salida

    # Asegúrate de que los directorios de salida existen
    os.makedirs('./data/outputs/', exist_ok=True)  # <-- Cambiar el directorio de entrada si se quiere buscar en subcarpetas

    # Listar archivos en el directorio input

    input_dir = './data/inputs/'  # <-- Cambiar el directorio de entrada si se quiere buscar en subcarpetas

    files = os.listdir(input_dir)

    # Iterar sobre los archivos y convertirlos a .algo
    for file in files:
        if os.path.isfile(os.path.join(input_dir, file)):  # Verifica que sea un archivo
            input_file = file
            output_file = file.split('.')[0] + f'.{formato_salida}'
            if os.path.exists(os.path.join('./data/outputs/', output_file)):  # <-- Cambiar el directorio de entrada si se quiere buscar en subcarpetas
                print(f"El archivo {output_file} ya existe y será sobrescrito.")
                # borrar el archivo existente
                os.remove(os.path.join('./data/outputs/', output_file))  # <-- Cambiar el directorio de entrada si se quiere buscar en subcarpetas
            convert_with_pandoc(input_file, output_file)
    print("Proceso terminado.")