from userTools import *
from userRead import *
from userWrite import *


def register():
    """comprueba si la entrada es un nombre con formato valido"""
    print(">> Registro >>")
    username = input("[Entrada] introduce tu nombre: ")

    while not validate_name(username):
        clean()
        print(">> Registro >>")
        username = input(f"[Error] el nombre '{username}' no es valido. Vuelve a intentarlo: ")

    return username


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
            create_recipe()
            input("\n<< pulsa para volver >> ")

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
