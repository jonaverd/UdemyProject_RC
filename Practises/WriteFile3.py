# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" .
# Inserta un tabulador entre cada elemento de la lista para separarlos.
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# Imprime el contenido completo de "registro.txt" al finalizar.
# Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t.
# También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt','a')
for line in registro_ultima_sesion:
    archivo.writelines(line + "\t")
archivo.close()

archivo = open('registro.txt','r')
print(archivo.read())
archivo.close()