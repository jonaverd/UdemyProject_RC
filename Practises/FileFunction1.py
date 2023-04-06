# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).

def abrir_leer(nombre):
    archivo = open(nombre)
    return archivo.read()

print(abrir_leer('ejemplo.txt'))