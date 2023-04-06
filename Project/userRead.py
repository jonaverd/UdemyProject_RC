from userTools import *


def use_readfile(filename):
    """abre un archivo, lo lee y lo cierra"""
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content


def read_recipe():
    """lee la receta de un archivo"""
    list_categories = categories()
    print(f">> Leer Receta >>")
    print(f"[Info] leyendo recetas en {base_path()}\n")
    show_categories(list_categories)
    print(f"[Info] introduce «cancelar» para salir")
    option = input("[Entrada] elige una categoria: ")

    # categorias
    while not validate_option(option, 0, len(list_categories) - 1):
        if option == "cancelar":
            break
        clean()
        print(f">> Leer Receta >>")
        print(f"[Info] leyendo recetas en {base_path()}\n")
        show_categories(list_categories)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una categoria: ")
    else:
        category_selected = list_categories[int(option)]
        list_recipes = recipes(category_selected)
        clean()
        print(f">> Leer Receta >>")
        print(f"[Info] leyendo recetas en {category_selected}\n")
        show_recipes(list_recipes)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una receta para ver: ")

        # recetas
        while not validate_option(option, 0, len(list_recipes) - 1):
            if option == "cancelar":
                break
            clean()
            print(f">> Leer Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}\n")
            show_recipes(list_recipes)
            print(f"[Info] introduce «cancelar» para salir")
            option = input("[Entrada] elige una receta para ver: ")
        else:
            clean()
            print(f">> Leer Receta >>")
            print(f"[Salida] receta para '{Path(list_recipes[int(option)]).stem}'\n")
            print(use_readfile(list_recipes[int(option)]))
