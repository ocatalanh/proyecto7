import os

def listar_archivos(directorio):
    for root, dirs, files in os.walk(directorio):
        # Filtrar archivos y directorios ocultos
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.')]
        
        # Imprimir la ruta relativa del directorio actual
        print(f"Directorio: {os.path.relpath(root, directorio)}")
        
        for file in files:
            print(f"  Archivo: {file}")
        
        print()  # Línea en blanco para separar las carpetas

if __name__ == "__main__":
    directorio = input("Introduce el directorio a listar: ")
    listar_archivos(directorio)
