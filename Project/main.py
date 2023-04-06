import os
from pathlib import Path


def clean():
    """limpia el terminal de salida"""
    os.system('cls' if os.name == 'nt' else 'clear')


def use_readfile(filename):
    """abre un archivo, lo lee y lo cierra"""
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content


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


def register():
    """comprueba si la entrada es un nombre con formato valido"""
    print(">> Registro >>")
    username = input("[Entrada] dime tu nombre: ")

    while not username.isalpha():
        clean()
        print(">> Registro >>")
        username = input(f"[Error] el nombre '{username}' no es valido. Vuelve a intentarlo: ")

    return username


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


def read_recipe():
    """lee la receta de un archivo"""
    list_categories = categories()
    print(f"[Info] leyendo recetas en {base_path()}\n")
    show_categories(list_categories)
    option = input("[Entrada] elige una categoria: ")

    # categorias
    while not validate_option(option, 0, len(list_categories)-1):
        clean()
        print(f"[Info] leyendo recetas en {base_path()}\n")
        show_categories(list_categories)
        option = input("[Entrada] elige una categoria: ")
    else:
        category_selected = list_categories[int(option)]
        list_recipes = recipes(category_selected)
        clean()
        print(f"[Info] leyendo recetas en {category_selected}\n")
        show_recipes(list_recipes)
        option = input("[Entrada] elige una receta para ver: ")

        # recetas
        while not validate_option(option, 0, len(list_recipes)-1):
            clean()
            print(f"[Info] leyendo recetas en {category_selected}\n")
            show_recipes(list_recipes)
            option = input("[Entrada] elige una receta para ver: ")
        else:
            clean()
            print(f"[Salida] receta para '{Path(list_recipes[int(option)]).stem}'\n")
            print(use_readfile(list_recipes[int(option)]))


def options(user):
    """opciones disponibles del menu"""
    print(">> Opciones >>")
    print(f"[Info] usuario registrado {user.upper()}")
    print(f"[Info] localizadas en {base_path()}")
    print(f"[Info] total de {len(recipes(base_path()))} recetas\n")
    print(f"[1] leer receta\n"
          f"[2] crear receta\n"
          f"[3] crear categoria\n"
          f"[4] eliminar receta\n"
          f"[5] eliminar categoria\n"
          f"[6] finalizar programa\n")


def manager(user):
    """gestiona las operaciones del usuario"""
    options(user)
    option = input("[Entrada] elige una opcion: ")

    while option != '6':
        if option == '1':
            clean()
            read_recipe()
            input("\n<< pulsa para volver >> ")

        elif option == '2':
            clean()
            print("hey")
            input("<< pulsa para volver >> ")

        elif option == '3':
            clean()
            print("hey")
            input("<< pulsa para volver >> ")

        elif option == '4':
            clean()
            print("hey")
            input("<< pulsa para volver >> ")

        elif option == '5':
            clean()
            print("hey")
            input("<< pulsa para volver >> ")

        clean()
        options(user)
        option = input("[Entrada] elige una opcion: ")

    else:
        clean()
        print(">> Finalizar >>")
        print("[Salida] hasta luego")


def main():
    """Programa principal"""
    user = register()
    clean()
    manager(user)


main()
