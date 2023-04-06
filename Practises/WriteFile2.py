# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

log = "Nuevo inicio de sesión"

archivo = open('mi_archivo2.txt','a')
archivo.write(log)
archivo.close()

archivo = open('mi_archivo2.txt','r')
print(archivo.read())
archivo.close()