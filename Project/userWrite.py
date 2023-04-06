from userTools import *


def use_writefile(filename, content):
    """crea un archivo, lo lee y lo cierra"""
    file = open(filename, 'w')
    file.write(content)
    file.close()


def create_recipe():
    """crea la receta en un archivo"""
    list_categories = categories()
    print(f">> Crear Receta >>")
    print(f"[Info] leyendo recetas en {base_path()}\n")
    show_categories(list_categories)
    print(f"[Info] introduce «cancelar» para salir")
    option = input("[Entrada] elige una categoria: ")

    # categorias
    while not validate_option(option, 0, len(list_categories) - 1):
        if option == "cancelar":
            break
        clean()
        print(f">> Crear Receta >>")
        print(f"[Info] leyendo recetas en {base_path()}\n")
        show_categories(list_categories)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una categoria: ")
    else:
        category_selected = list_categories[int(option)]
        list_recipes = recipes(category_selected)
        clean()
        print(f">> Crear Receta >>")
        print(f"[Info] leyendo recetas en {category_selected}\n")
        show_recipes(list_recipes)
        print(f"[Info] introduce «cancelar» para salir")
        filename = input("[Entrada] introduce un nombre para crear: ")

        # Comprobamos si ya existe
        possible_path = str(Path(category_selected, filename + ".txt")).lower()
        possible_list = list(map(lambda x: str(x).lower(), list_recipes))

        # recetas
        while not validate_name(filename) or filename == "cancelar" or possible_path in possible_list:

            # Comprobamos si ya existe
            possible_path = str(Path(category_selected, filename + ".txt")).lower()
            possible_list = list(map(lambda x: str(x).lower(), list_recipes))

            if filename == "cancelar":
                break

            clean()
            print(f">> Crear Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}\n")
            show_recipes(list_recipes)
            print(f"[Info] introduce «cancelar» para salir")
            if not validate_name(filename):
                filename = input(f"[Error] el nombre '{filename}' no es valido. Vuelve a intentarlo: ")
            elif possible_path in possible_list:
                filename = input(f"[Error] la receta '{filename.upper()}' ya existe. Vuelve a intentarlo: ")
        else:
            clean()
            print(f">> Crear Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}")
            print(f"\n[Salida] se va a registrar como '{filename}'.txt\n")
            path = Path(category_selected, filename + ".txt")
            print(f"[Info] introduce «cancelar» para salir")
            content = input("[Entrada] introduce el contenido de la receta: ")

            if content != "cancelar":
                clean()
                print(f">> Crear Receta >>")
                print(f"[Info] leyendo recetas en {category_selected}")
                print(f"\n[Salida] receta creada")
                use_writefile(path, content)
