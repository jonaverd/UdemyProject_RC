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
    if word.isalpha():
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
        print("[Info] no hay recetas disponibles")
    else:
        for index, element in enumerate(list_recipes):
            print(f"{index} - {Path(element).stem}")
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
        print("[Info] no hay categorias disponibles")
    else:
        for index, element in enumerate(list_categories):
            print(f"{index} - {Path(element).name}")
        print("")
