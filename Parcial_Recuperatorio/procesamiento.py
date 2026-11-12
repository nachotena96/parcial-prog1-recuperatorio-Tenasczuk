from validaciones import validar_nombres_candidatos, validar_nota_primer_parcial, validar_nota_segundo_parcial  

def crear_listas(numero):
#pedir numero de candidatos

    for i in range(numero):
            nombre = input("Ingrese el nombre del candidato: ")

            while not validar_nombres_candidatos(nombre):
                print("Nombre del candidato inválido.")

                nombre = input(f"Ingrese el nombre del candidato {i + 1}: ")

            nombre[i] = nombre





























def crear_lista_nombres(numero):
    lista_nombres = [""] * numero
    return lista_nombres


def crear_lista_notas_primer_parcial(numero):
    lista_notas_primer_parcial = [0] * numero
    return lista_notas_primer_parcial


def crear_lista_notas_segundo_parcial(numero):
    lista_notas_segundo_parcial = [0] * numero
    return lista_notas_segundo_parcial



def ingresar_nombre_candidato(nombres, numero):
    """
    Solicita al usuario el nombre de cada candidato y lo almacena
    en la lista de nombres recibida.

    Args:
        nombres (list): Lista donde se guardarán los nombres.
        numero (int): Cantidad de candidatos cuyos nombres se ingresarán.

    Returns:
        list: La lista con los nombres ingresados.
    """
    for i in range(numero):
        nombres[i] = input("Ingrese el nombre del candidato: ")

    return nombres



def calcular_promedio(lista_notas_primer_parcial, lista_notas_segundo_parcial, numero):
    """
    Calcula el promedio de los dos parciales de cada candidato
    y almacena los resultados en una nueva lista.

    Args:
        lista_notas_primer_parcial (list): Notas del primer parcial.
        lista_notas_segundo_parcial (list): Notas del segundo parcial.
        numero (int): Cantidad de candidatos.

    Returns:
        list: Lista con los promedios de todos los candidatos.
    """
    lista_promedio = [0] * numero

    for i in range(numero):
        lista_promedio[i] = (lista_notas_primer_parcial[i] + lista_notas_segundo_parcial[i]) / 2

    return lista_promedio



def clasificar_promedios(lista_promedio):
    """
    Clasifica a los candidatos según sus promedios en tres categorías:
    promocionan, aprueban o desaprueban.

    Args:
        lista_promedio (list): Lista con los promedios de los candidatos.

    Returns:
        tuple: Cantidad de candidatos que promocionan, aprueban
        y desaprueban, en ese orden.
    """
    contador_promociona = 0
    contador_aprueba = 0
    contador_desaprueba = 0

    for promedio in lista_promedio:
        if promedio >= 6:
            contador_promociona = contador_promociona + 1

        elif promedio >= 4:
            contador_aprueba = contador_aprueba + 1

        else:
            contador_desaprueba = contador_desaprueba + 1

    print(f"candidatos que promocionan: {contador_promociona}")
    print(f"candidatos que aprueban: {contador_aprueba}")
    print(f"candidatos que desaprueban: {contador_desaprueba}")

    return contador_promociona, contador_aprueba, contador_desaprueba



def calcular_prom_gral(lista_promedio, numero):
    """
    Calcula el promedio general de todos los candidatos a partir
    de sus promedios individuales.

    Args:
        lista_promedio (list): Lista con los promedios de los candidatos.
        numero (int): Cantidad de candidatos.

    Returns:
        float: El promedio general de todos los candidatos.
    """
    acumulador_promedio = 0

    for promedio in lista_promedio:
        acumulador_promedio = acumulador_promedio + promedio

    promedio_general = acumulador_promedio / numero

    return promedio_general



def calcular_max_min(lista_promedio, lista_nombres):
    """
    Busca el promedio máximo y mínimo de los candidatos y los nombres
    de quienes obtuvieron esos promedios.

    Args:
        lista_promedio (list): Lista con los promedios de los candidatos.
        lista_nombres (list): Lista con los nombres de los candidatos.

    Returns:
        list: Promedio máximo, nombre del candidato con el máximo,
        promedio mínimo y nombre del candidato con el mínimo.
    """
    maximo = 0
    minimo = 10
    nombre_maximo = ""
    nombre_minimo = ""

    for i in range(len(lista_promedio)):

        if lista_promedio[i] > maximo:
            maximo = lista_promedio[i]
            nombre_maximo = lista_nombres[i]

        if lista_promedio[i] < minimo:
            minimo = lista_promedio[i]
            nombre_minimo = lista_nombres[i]

    return [maximo, nombre_maximo, minimo, nombre_minimo]



def ordenar_listas(lista_promedios, lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial):
    """
    Ordena los promedios de mayor a menor y reorganiza las listas
    de nombres y notas para mantener los datos de cada candidato asociados.

    Args:
        lista_promedios (list): Lista con los promedios de los candidatos.
        lista_nombres (list): Lista con los nombres de los candidatos.
        lista_notas_primer_parcial (list): Notas del primer parcial.
        lista_notas_segundo_parcial (list): Notas del segundo parcial.

    Returns:
        list: Lista con los promedios ordenados de mayor a menor.
        list: Lista de nombres reorganizada.
        list: Lista de notas del primer parcial reorganizada.
        list: Lista de notas del segundo parcial reorganizada.
    """
    n = len(lista_promedios)

    for i in range(n):
        for j in range(n - 1):
            if lista_promedios[j] < lista_promedios[j + 1]:

                promedio_auxiliar = lista_promedios[j + 1]
                lista_promedios[j + 1] = lista_promedios[j]
                lista_promedios[j] = promedio_auxiliar

                nombre_auxiliar = lista_nombres[j + 1]
                lista_nombres[j + 1] = lista_nombres[j]
                lista_nombres[j] = nombre_auxiliar

                nota_primer_parcial_auxiliar = lista_notas_primer_parcial[j + 1]
                lista_notas_primer_parcial[j + 1] = lista_notas_primer_parcial[j]
                lista_notas_primer_parcial[j] = nota_primer_parcial_auxiliar

                nota_segundo_parcial_auxiliar = lista_notas_segundo_parcial[j + 1]
                lista_notas_segundo_parcial[j + 1] = lista_notas_segundo_parcial[j]
                lista_notas_segundo_parcial[j] = nota_segundo_parcial_auxiliar

    return lista_promedios, lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial



def mostrar_ranking_candidatos(lista_promedios, lista_nombres):
    """
    Muestra por pantalla la lista de nombres de los candidatos
    y la lista de sus promedios.

    Args:
        lista_promedios (list): Lista con los promedios de los candidatos.
        lista_nombres (list): Lista con los nombres de los candidatos.

    Returns:
        None: Muestra ambas listas por pantalla.
    """
    print(lista_nombres)
    print(lista_promedios)



def buscar_nombre(nombre_objetivo, lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial, lista_promedio):
    """
    Busca un candidato por su nombre y obtiene sus notas y promedio.

    Args:
        nombre_objetivo (str): Nombre del candidato que se desea buscar.
        lista_nombres (list): Lista con los nombres de los candidatos.
        lista_notas_primer_parcial (list): Notas del primer parcial.
        lista_notas_segundo_parcial (list): Notas del segundo parcial.
        lista_promedio (list): Promedios de los candidatos.

    Returns:
        list: Lista con la nota del primer parcial, la nota del segundo
        parcial y el promedio, si encuentra al candidato.
        int: -1 si el candidato no existe.
    """
    for i in range(len(lista_nombres)):
        if nombre_objetivo == lista_nombres[i]:
            nota1 = lista_notas_primer_parcial[i]
            nota2 = lista_notas_segundo_parcial[i]
            promedio = lista_promedio[i]

            return [nota1, nota2, promedio]

    return -1



def mostrar_notas_y_promedio_candidato(nombre_objetivo, nota1, nota2, promedio):
    """
    Muestra por pantalla el nombre del candidato, las notas de ambos
    parciales y su promedio.

    Args:
        nombre_objetivo (str): Nombre del candidato.
        nota1 (int): Nota del primer parcial.
        nota2 (int): Nota del segundo parcial.
        promedio (float): Promedio del candidato.

    Returns:
        None: Muestra los datos por pantalla.
    """
    print(f"Nombre del candidato: {nombre_objetivo}")
    print(f"Nota del primer parcial: {nota1}")
    print(f"Nota del segundo parcial: {nota2}")
    print(f"Promedio: {promedio}")



def contar_vocales(nombre):
    """
    Cuenta la cantidad de vocales que contiene un nombre,
    considerando vocales minúsculas y mayúsculas.

    Args:
        nombre (str): Nombre en el que se contarán las vocales.

    Returns:
        int: Cantidad de vocales encontradas.
    """
    vocales = "aeiouAEIOU"
    contador = 0

    for i in range(len(nombre)):  # Recorre las letras del nombre

        for j in range(len(vocales)):  # Compara cada letra con las vocales
            if nombre[i] == vocales[j]:
                contador = contador + 1
                break

    return contador



def ingresar_nombre_candidato_juego():
    """
    Solicita al usuario el nombre del candidato que desea buscar
    y devuelve el nombre ingresado.

    Returns:
        str: El nombre del candidato que se desea buscar.
    """
    nombre_objetivo = input("Ingrese el nombre deseado del candidato: ")
    return nombre_objetivo



def invertir_nombre(nombre):
    """
    Invierte el orden de los caracteres de un nombre.

    Args:
        nombre (str): Nombre que se desea invertir.

    Returns:
        str: Nombre con los caracteres en orden inverso.
    """
    return nombre[::-1]