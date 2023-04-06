# Abre el archivo texto.txt e imprime únicamente la segunda línea.

mi_archivo = open("texto2.txt")
segunda_linea = mi_archivo.readlines()[1]
print(segunda_linea)
mi_archivo.close()