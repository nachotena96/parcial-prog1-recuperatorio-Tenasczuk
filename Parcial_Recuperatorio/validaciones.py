def validar_menu(numero):

    numero = int(input("Ingrese la opción del menú que desee: "))

    while numero < 0 or numero > 6:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 6. Vuelva a intentarlo.")
        numero = int(input("Ingrese la opción del menú que desee: "))

    return numero



def ingresar_y_validar_numero_candidatos(): #esto esta

    numero = int(input("Ingrese la cantidad de candidatos deseada (1 - 15): "))

    while numero < 1 or numero > 15:
        print("La cantidad de candidatos ingresada es inválida. Debe utilizar un número entre 1 y 15. Vuelva a intentarlo.")
        numero = int(input("Ingrese la cantidad de candidatos deseada: "))

    return numero



def validar_nombres_candidatos(nombre):

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



#def validar_nota_segundo_parcial(lista_notas_segundo_parcial, i):
    #"""
    #Solicita y valida la nota del segundo parcial de un candidato.
    #La nota debe ser un número entero entre 0 y 10.
    #Si está fuera del rango, vuelve a solicitarla.
#
    #Args:
        #lista_notas_segundo_parcial (list): Lista con las notas del segundo parcial.
        #i (int): Índice del candidato cuya nota se desea cargar.
#
    #Returns:
        #None: La nota se guarda directamente en la lista recibida.
    #"""
    #lista_notas_segundo_parcial[i] = int(input("Ingrese la nota del segundo parcial: "))
#
    #while lista_notas_segundo_parcial[i] < 0 or lista_notas_segundo_parcial[i] > 10:
        #print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 10. Vuelva a intentarlo.")
        #lista_notas_segundo_parcial[i] = int(input("Ingrese la nota del segundo parcial: "))

