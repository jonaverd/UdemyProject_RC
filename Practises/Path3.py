# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a
# partir de la siguiente estructura de carpetas:
# home (directorio base)
#      --> Curso Python
#             --> Día 6
#                   --> practicas_path.py
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path
# que refiere a la carpeta base del usuario.

from pathlib import Path

ruta = Path.home() / Path("Curso Python", "Día 6", "practicas_path.py")

