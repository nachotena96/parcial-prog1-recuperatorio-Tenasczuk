def validar_menu(numero):

    numero = int(input("Ingrese la opción del menú que desee: "))

    while numero < 0 or numero > 6:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 6. Vuelva a intentarlo.")
        numero = int(input("Ingrese la opción del menú que desee: "))

    return numero



def ingresar_y_validar_numero_postulantes(): #esto esta

    numero = int(input("Ingrese la cantidad de postulantes deseada (1 - 15): "))

    while numero < 1 or numero > 15:
        print("La cantidad de postulantes ingresada es inválida. Debe utilizar un número entre 1 y 15. Vuelva a intentarlo.")
        numero = int(input("Ingrese la cantidad de postulantes deseada: "))

    return numero



def validar_nombres_postulantes(nombre):

    if len(nombre) < 5:
        return False

    for i in range(len(nombre)):
        caracter = nombre[i]

        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z"
        espacio = caracter == " "

        if not (minuscula or mayuscula or espacio):
            return False

    return True


def validar_nota(nota):
    if nota < 0 or nota > 10:
        return False

    return True



def cantidad_listas(cantidad: int) -> bool:
    if cantidad == 0:
        print("Usted no tiene listas cargadas, primero debe registrar los alumnos. Ingrese 1 para el registro, o presione 0 para salir del menu ")
        return False
        
    return True

