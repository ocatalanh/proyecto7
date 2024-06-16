import os

def listar_archivos_y_subcarpetas(carpeta):
    for ruta_directorio, subcarpetas, archivos in os.walk(carpeta):
        print(f'Directorio: {ruta_directorio}')
        for subcarpeta in subcarpetas:
            print(f'  Subcarpeta: {subcarpeta}')
        for archivo in archivos:
            print(f'  Archivo: {archivo}')


# Especifica la ruta de la carpeta que quieres listar
carpeta = r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS'
listar_archivos_y_subcarpetas(carpeta)
