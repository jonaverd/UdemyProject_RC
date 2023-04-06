# Abre el archivo texto.txt e imprime su contenido.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

mi_archivo = open("texto.txt")
print(mi_archivo.read())
mi_archivo.close()