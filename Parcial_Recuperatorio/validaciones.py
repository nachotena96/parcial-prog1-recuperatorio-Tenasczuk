
def validar_menu() -> int:
    """
    Solicita al usuario una opción del menú y valida que se encuentre
    dentro del rango permitido (0 a 6).

    Returns:
        int: Número de opción ingresado y validado.
    """

    numero = int(input("Ingrese la opción del menú que desee: "))

    while numero < 0 or numero > 6:
        print("El valor ingresado es inválido. Debe utilizar un número entre 0 y 6. Vuelva a intentarlo.")
        numero = int(input("Ingrese la opción del menú que desee: "))

    return numero





def ingresar_y_validar_numero_postulantes() -> int:
    """
    Solicita al usuario la cantidad de postulantes que desea ingresar
    y valida que se encuentre dentro del rango permitido (1 a 15).

    Returns:
        int: Cantidad de postulantes ingresada y validada.
    """

    numero = int(input("Ingrese la cantidad de postulantes deseada (1 - 15): "))

    while numero < 1 or numero > 15:
        print("La cantidad de postulantes ingresada es inválida. Debe utilizar un número entre 1 y 15. Vuelva a intentarlo.")
        numero = int(input("Ingrese la cantidad de postulantes deseada (1 - 15): "))

    return numero





def validar_nombres_postulantes(nombre: str) -> bool:
    """
    Valida que el nombre del postulante tenga al menos 5 caracteres
    y que esté compuesto únicamente por letras mayúsculas, minúsculas
    y espacios.

    Args:
        nombre (str): Nombre ingresado por el usuario.

    Returns:
        bool: True si el nombre cumple con las condiciones establecidas,
        False en caso contrario.
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




def validar_nota(nota: float) -> bool:
    """
    Valida que la nota ingresada se encuentre dentro del rango
    permitido (0 a 10).

    Args:
        nota (float): Nota que se desea validar.

    Returns:
        bool: True si la nota está dentro del rango permitido,
        False en caso contrario.
    """

    if nota < 0 or nota > 10:
        return False

    return True





def cantidad_listas(cantidad: int) -> bool:
    """
    Comprueba si existen postulantes registrados en las listas.

    Args:
        cantidad (int): Cantidad de postulantes registrados.

    Returns:
        bool: False si no hay postulantes registrados,
        True si existe al menos uno.
    """

    if cantidad == 0:
        print("Usted no tiene listas cargadas, primero debe registrar los alumnos. Ingrese 1 para el registro, o presione 0 para salir del menu ")
        return False
        
    return True


