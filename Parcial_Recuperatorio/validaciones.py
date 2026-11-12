def validar_menu(numero):

    numero = int(input("Ingrese la opción del menú que desee: "))

    while numero < 0 or numero > 6:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 6. Vuelva a intentarlo.")
        numero = int(input("Ingrese la opción del menú que desee: "))

    return numero



def ingresar_numero_candidatos():
    """
    Solicita al usuario la cantidad de candidatos que desea ingresar
    y devuelve el valor introducido convertido a un número entero.

    Returns:
        int: La cantidad de candidatos ingresada por el usuario.
    """
    numero = int(input("Ingrese el número de candidatos deseado: "))

    return numero


def validar_listas_numero_candidatos(numero):
    """
    Valida que la cantidad de candidatos ingresada esté entre 1 y 30.
    Si el valor está fuera de ese rango, vuelve a solicitarlo
    hasta que sea válido.

    Args:
        numero (int): Cantidad de candidatos ingresada inicialmente.

    Returns:
        int: Cantidad de candidatos validada, entre 1 y 30.
    """
    while numero < 1 or numero > 15:
        print("La cantidad de candidatos ingresada es inválida. Debe utilizar un número entre 1 y 15. Vuelva a intentarlo.")
        numero = int(input("Ingrese la cantidad de candidatos deseada: "))

    return numero



def validar_nombres_candidatos(nombre):
    """
    Valida que el nombre de un candidato tenga al menos 5 caracteres
    y contenga únicamente letras mayúsculas, minúsculas o espacios.

    Args:
        nombre (str): Nombre del candidato que se desea validar.

    Returns:
        bool: True si el nombre es válido, False en caso contrario.
    """
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


def validar_nota_primer_parcial(lista_notas_primer_parcial, i):
    """
    Solicita y valida la nota del primer parcial de un candidato.
    La nota debe ser un número entero entre 0 y 10.
    Si está fuera del rango, vuelve a solicitarla.

    Args:
        lista_notas_primer_parcial (list): Lista con las notas del primer parcial.
        i (int): Índice del candidato cuya nota se desea cargar.

    Returns:
        None: La nota se guarda directamente en la lista recibida.
    """
    lista_notas_primer_parcial[i] = int(input("Ingrese la nota del primer parcial: "))

    while lista_notas_primer_parcial[i] < 0 or lista_notas_primer_parcial[i] > 10:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 10. Vuelva a intentarlo.")
        lista_notas_primer_parcial[i] = int(input("Ingrese la nota del primer parcial: "))



def validar_nota_segundo_parcial(lista_notas_segundo_parcial, i):
    """
    Solicita y valida la nota del segundo parcial de un candidato.
    La nota debe ser un número entero entre 0 y 10.
    Si está fuera del rango, vuelve a solicitarla.

    Args:
        lista_notas_segundo_parcial (list): Lista con las notas del segundo parcial.
        i (int): Índice del candidato cuya nota se desea cargar.

    Returns:
        None: La nota se guarda directamente en la lista recibida.
    """
    lista_notas_segundo_parcial[i] = int(input("Ingrese la nota del segundo parcial: "))

    while lista_notas_segundo_parcial[i] < 0 or lista_notas_segundo_parcial[i] > 10:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 10. Vuelva a intentarlo.")
        lista_notas_segundo_parcial[i] = int(input("Ingrese la nota del segundo parcial: "))

