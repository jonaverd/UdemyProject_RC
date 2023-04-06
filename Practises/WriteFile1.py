# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

# Modos de apertura 'r' solo lectura,
# 'w' escritura sobrescribiendo,
# 'a' escritura a partir del final

archivo = open('mi_archivo.txt','w')
archivo.write("Nuevo texto")
archivo.close()

archivo = open('mi_archivo.txt','r')
print(archivo.read())
archivo.close()