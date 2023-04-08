import os
from pathlib import Path


def clean():
    """limpia el terminal de salida"""
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_option(input, min, max):
    """valida que la entrada sea una opcion valida"""
    if not input.isdigit():
        return False
    else:
        if int(input) < min:
            return False
        elif int(input) > max:
            return False
        else:
            return True


def validate_name(word):
    """valida que la entrada contenga solo letras"""
    word = word.replace(" ", "")
    if word.isalpha():
        return True
    else:
        return False


def cancel(input):
    """comprueba si la entrada es una orden de cancelar la operacion"""
    commands = ["cancelar", "salir", "pause", "stop", "cancel", "quit", "exit", "c", "q"]
    input = input.replace(" ", "")
    input = input.lower()
    if input in commands:
        return True
    else:
        return False


def exists_path(path, pathlist):
    """Comprueba si existe el path (archivo o carpeta) dentro de la lista"""
    new = str(path).lower()
    # evitamos sensibilidad de mayusculas y minusculas
    current = list(map(lambda x: str(x).lower(), pathlist))
    if new in current:
        return True
    else:
        return False


def base_path():
    """extrae la ruta base de las recetas"""
    route = Path("Recetas").resolve()
    return route


def recipes(path):
    """extrae todas las recetas que hay"""
    files = []
    for f in path.glob("**/*.txt"):
        files.append(f)
    return files


def show_recipes(list_recipes):
    """muestra todas las recetas disponibles"""
    if len(list_recipes) == 0:
        print("[Salida] no hay recetas disponibles\n")
    else:
        for index, element in enumerate(list_recipes):
            print(f"{index} - {Path(element).stem}")
        print("")


def show_recipes_short(list_recipes, *extra_info):
    """muestra las ultimas recetas disponibles, añadiendo una info adicional"""
    if len(list_recipes) == 0:
        print("[Salida] no hay recetas disponibles\n")
    else:
        print("(...)")
        for element in list_recipes[-3:]:
            print(f"{list_recipes.index(element)} - {Path(element).stem}")
        if len(extra_info) != 0:
            for inf in extra_info:
                print(inf)
        print("")


def categories():
    """extrae todas las categorias que hay"""
    folders = []
    for fd in base_path().glob('*'):
        folders.append(fd)
    return folders


def show_categories(list_categories):
    """muestra todas las categorias disponibles"""
    if len(list_categories) == 0:
        print("[Salida] no hay categorias disponibles\n")
    else:
        for index, element in enumerate(list_categories):
            print(f"{index} - {Path(element).name}")
        print("")


def show_categories_short(list_categories, *extra_info):
    """muestra las ultimas categorias disponibles, añadiendo una info adicional"""
    if len(list_categories) == 0:
        print("[Salida] no hay categorias disponibles\n")
    else:
        print("(...)")
        for element in list_categories[-3:]:
            print(f"{list_categories.index(element)} - {Path(element).stem}")
        if len(extra_info) != 0:
            for inf in extra_info:
                print(inf)
        print("")
