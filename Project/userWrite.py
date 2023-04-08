from userTools import *


def use_writefile(filename, content):
    """crea un archivo, lo escribe y lo cierra"""
    file = open(filename, 'w')
    file.write(str(content))
    file.close()


def use_writefolder(foldername):
    """crea una carpeta"""
    os.makedirs(foldername)


def create_recipe():
    """crea la receta en un archivo"""
    list_categories = categories()
    print(f">> Crear Receta >>")
    print(f"[Info] leyendo categorias en {base_path()}\n")
    show_categories(list_categories)
    print(f"[Info] introduce «cancelar» para salir")
    option = input("[Entrada] elige una categoria: ")

    # categorias
    while not validate_option(option, 0, len(list_categories) - 1):
        if cancel(option):
            break
        clean()
        print(f">> Crear Receta >>")
        print(f"[Info] leyendo categorias en {base_path()}\n")
        show_categories(list_categories)
        print(f"[Info] introduce «cancelar» para salir")
        option = input("[Entrada] elige una categoria: ")
    else:
        category_selected = list_categories[int(option)]
        list_recipes = recipes(category_selected)
        clean()
        print(f">> Crear Receta >>")
        print(f"[Info] leyendo recetas en {category_selected}\n")
        show_recipes_short(list_recipes, f"» Nueva Receta »")
        print(f"[Info] introduce «cancelar» para salir")
        filename = input(f"[Entrada] introduce un nombre para crear ({len(list_recipes)}): ")

        # Comprobamos si ya existe
        new_path = Path(category_selected, filename + ".txt")

        # recetas
        while not validate_name(filename) or cancel(filename) or exists_path(new_path, list_recipes):
            if cancel(filename):
                break
            clean()
            print(f">> Crear Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}\n")
            show_recipes_short(list_recipes, f"» Nueva Receta »")
            print(f"[Info] introduce «cancelar» para salir")
            if not validate_name(filename):
                filename = input(f"[Error] el nombre '{filename}' no es valido. Vuelve a intentarlo: ")
            elif exists_path(new_path, list_recipes):
                filename = input(f"[Error] la receta '{filename.upper()}' ya existe. Vuelve a intentarlo: ")
            # Comprobamos si ya existe
            new_path = Path(category_selected, filename + ".txt")
        else:
            clean()
            print(f">> Crear Receta >>")
            print(f"[Info] leyendo recetas en {category_selected}")
            print(f"\n[Salida] se va a registrar como '{filename}'.txt\n")
            path = Path(category_selected, filename + ".txt")
            print(f"[Info] introduce «cancelar» para salir")
            content = input("[Entrada] introduce el contenido de la receta: ")

            if not cancel(content):
                clean()
                print(f">> Crear Receta >>")
                print(f"[Info] leyendo recetas en {category_selected}")
                print(f"\n[Salida] receta creada")
                use_writefile(path, content)


def create_category():
    """crea la categoria en una carpeta"""
    list_categories = categories()
    print(f">> Crear Categoria >>")
    print(f"[Info] leyendo categorias en {base_path()}\n")
    show_categories_short(list_categories, f"» Nueva Categoria »")
    print(f"[Info] introduce «cancelar» para salir")
    foldername = input(f"[Entrada] introduce un nombre para crear ({len(list_categories)}): ")

    # Comprobamos si ya existe
    new_path = Path(base_path(), foldername)

    # categorias
    while not validate_name(foldername) or cancel(foldername) or exists_path(new_path, list_categories):
        if cancel(foldername):
            break
        clean()
        print(f">> Crear Categoria >>")
        print(f"[Info] leyendo categorias en {base_path()}\n")
        show_categories_short(list_categories, f"» Nueva Categoria »")
        print(f"[Info] introduce «cancelar» para salir")
        if not validate_name(foldername):
            foldername = input(f"[Error] el nombre '{foldername}' no es valido. Vuelve a intentarlo: ")
        elif exists_path(new_path, list_categories):
            foldername = input(f"[Error] la categoria '{foldername.upper()}' ya existe. Vuelve a intentarlo: ")
        # Comprobamos si ya existe
        new_path = Path(base_path(), foldername)
    else:
        if not cancel(foldername):
            clean()
            print(f">> Crear Categoria >>")
            print(f"[Info] leyendo categorias en {base_path()}")
            print(f"\n[Salida] categoria creada")
            path = Path(base_path(), foldername)
            use_writefolder(path)
