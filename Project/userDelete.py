from userTools import *


def use_deletefile(filename):
    """elimina un archivo"""
    os.remove(filename)


def use_deletefolder(foldername):
    """elimina una carpeta"""
    shutil.rmtree(foldername, ignore_errors=True)


def delete_recipe():
    """elimina la receta del archivo"""
    list_categories = categories()
    print(f">> Eliminar Receta >>")
    print(f"[Info] leyendo categorias en {base_path()}\n")
    show_categories(list_categories)
    print(f"[Info] introduce «cancelar» para salir")
    option = input("[Entrada] elige una categoria: ")

    # categorias
    while not validate_option(option, 0, len(list_categories) - 1):
        if cancel(option):
            break
        clean()
        print(f">> Eliminar Receta >>")
        print(f"[Info] leyendo categorias en {base_path()}\n")
        show_categories(list_categories)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una categoria: ")
    else:
        category_selected = list_categories[int(option)]
        list_recipes = recipes(category_selected)
        clean()
        print(f">> Eliminar Receta >>")
        print(f"[Info] leyendo recetas en {category_selected}\n")
        show_recipes(list_recipes)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una receta para eliminar: ")

        # recetas
        while not validate_option(option, 0, len(list_recipes) - 1):
            if cancel(option):
                break
            clean()
            print(f">> Eliminar Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}\n")
            show_recipes(list_recipes)
            print(f"[Info] introduce «cancelar» para salir")
            option = input("[Entrada] elige una receta para eliminar: ")
        else:
            clean()
            print(f">> Eliminar Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}")
            print(f"\n[Salida] receta eliminada")
            use_deletefile(list_recipes[int(option)])


def delete_category():
    """elimina la categoria del archivo"""
    list_categories = categories()
    print(f">> Eliminar Categoria >>")
    print(f"[Info] leyendo categorias en {base_path()}\n")
    show_categories(list_categories)
    print(f"[Info] introduce «cancelar» para salir")
    option = input("[Entrada] elige una categoria para eliminar: ")

    # categorias
    while not validate_option(option, 0, len(list_categories) - 1):
        if cancel(option):
            break
        clean()
        print(f">> Eliminar Categoria >>")
        print(f"[Info] leyendo categorias en {base_path()}\n")
        show_categories(list_categories)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una categoria para eliminar: ")
    else:
        category_selected = list_categories[int(option)]
        clean()
        print(f">> Eliminar Categoria >>")
        print(f"[Info] leyendo categorias en {base_path()}")
        print(f"\n[Salida] categoria eliminada")
        use_deletefolder(category_selected)

