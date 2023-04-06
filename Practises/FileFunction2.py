# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(nombre):
    archivo = open(nombre, 'w')
    archivo.write("contenido eliminado")

sobrescribir('ejemplo.txt')