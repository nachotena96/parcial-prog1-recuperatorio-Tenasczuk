def validar_menu(numero):
    """
    Valida que la opción ingresada para el menú esté dentro del rango permitido.
    Si el número es menor que 0 o mayor que 6, vuelve a solicitarlo
    hasta que sea válido.

    Args:
        numero (int): Opción ingresada por el usuario.

    Returns:
        int: La opción validada, entre 0 y 6.
    """
    while numero < 0 or numero > 6:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 6. Vuelva a intentarlo.")
        numero = int(input("Ingrese la opción del menú que desee: "))

    return numero



def ingresar_numero_alumnos():
    """
    Solicita al usuario la cantidad de alumnos que desea ingresar
    y devuelve el valor introducido convertido a un número entero.

    Returns:
        int: La cantidad de alumnos ingresada por el usuario.
    """
    numero = int(input("Ingrese el número de alumnos deseado: "))

    return numero


def validar_listas_numero_alumnos(numero):
    """
    Valida que la cantidad de alumnos ingresada esté entre 1 y 30.
    Si el valor está fuera de ese rango, vuelve a solicitarlo
    hasta que sea válido.

    Args:
        numero (int): Cantidad de alumnos ingresada inicialmente.

    Returns:
        int: Cantidad de alumnos validada, entre 1 y 30.
    """
    while numero < 1 or numero > 15:
        print("La cantidad de alumnos ingresada es inválida. Debe utilizar un número entre 1 y 15. Vuelva a intentarlo.")
        numero = int(input("Ingrese la cantidad de alumnos deseada: "))

    return numero



def validar_nombres_alumnos(nombre):
    """
    Valida que el nombre de un alumno tenga al menos 5 caracteres
    y contenga únicamente letras mayúsculas, minúsculas o espacios.

    Args:
        nombre (str): Nombre del alumno que se desea validar.

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


def cargar_nota_primer_parcial(lista_notas_primer_parcial, i):
    """
    Solicita y valida la nota del primer parcial de un alumno.
    La nota debe ser un número entero entre 0 y 10.
    Si está fuera del rango, vuelve a solicitarla.

    Args:
        lista_notas_primer_parcial (list): Lista con las notas del primer parcial.
        i (int): Índice del alumno cuya nota se desea cargar.

    Returns:
        None: La nota se guarda directamente en la lista recibida.
    """
    lista_notas_primer_parcial[i] = int(input("Ingrese la nota del primer parcial: "))

    while lista_notas_primer_parcial[i] < 0 or lista_notas_primer_parcial[i] > 10:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 10. Vuelva a intentarlo.")
        lista_notas_primer_parcial[i] = int(input("Ingrese la nota del primer parcial: "))



def cargar_nota_segundo_parcial(lista_notas_segundo_parcial, i):
    """
    Solicita y valida la nota del segundo parcial de un alumno.
    La nota debe ser un número entero entre 0 y 10.
    Si está fuera del rango, vuelve a solicitarla.

    Args:
        lista_notas_segundo_parcial (list): Lista con las notas del segundo parcial.
        i (int): Índice del alumno cuya nota se desea cargar.

    Returns:
        None: La nota se guarda directamente en la lista recibida.
    """
    lista_notas_segundo_parcial[i] = int(input("Ingrese la nota del segundo parcial: "))

    while lista_notas_segundo_parcial[i] < 0 or lista_notas_segundo_parcial[i] > 10:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 10. Vuelva a intentarlo.")
        lista_notas_segundo_parcial[i] = int(input("Ingrese la nota del segundo parcial: "))

