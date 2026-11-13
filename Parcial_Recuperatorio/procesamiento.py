from validaciones import validar_nombres_candidatos, ingresar_y_validar_numero_candidatos, validar_nombres_candidatos, validar_nota


def crear_listas_nombres(numero):
#pedir numero de candidatos

    for i in range(numero):
            nombre = input("Ingrese el nombre del candidato: ")

            while not validar_nombres_candidatos(nombre):
                print("Nombre del candidato inválido.")

                nombre = input(f"Ingrese el nombre del candidato {i + 1}: ")

            nombre[i] = nombre








def crear_lista(): #esto ya esta

    numero = ingresar_y_validar_numero_candidatos()


    lista_nombres = [""] * numero
    lista_notas_primer_parcial = [0] * numero
    lista_notas_segundo_parcial = [0] * numero

    print(lista_nombres)
    print(lista_notas_primer_parcial)
    print(lista_notas_segundo_parcial)

    return lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial



def ingresar_nombre_candidato(nombres, numero): #esto ya esta, tenes que ver que cuando pones l no te indica "nombre invalido"

    for i in range(numero):

        nombre = input("Ingrese el nombre del candidato: ")

        while not validar_nombres_candidatos(nombre):
            print("Nombre inválido. Intente nuevamente.")
            nombre = input("Ingrese el nombre del candidato: ")

    nombres[i] = nombre

    return nombres



def ingresar_notas(lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica, numero): #esto esta

    for i in range(numero):

        nota_prueba_tecnica = int(input("Ingrese la nota de la prueba tecnica: "))

        while not validar_nota(nota_prueba_tecnica):
            print("Nota inválida. Debe ingresar un valor entre 0 y 10.")
            nota_prueba_tecnica = int(input("Ingrese la nota de la prueba tecnica: "))

        lista_notas_prueba_tecnica[i] = nota_prueba_tecnica

        nota_prueba_psicotecnica = int(input("Ingrese la nota de la prueba psicotecnica: "))

        while not validar_nota(nota_prueba_psicotecnica):
            print("Nota inválida. Debe ingresar un valor entre 0 y 10.")
            nota_prueba_psicotecnica = int(input("Ingrese la nota de la prueba psicotecnica: "))

        lista_notas_prueba_psicotecnica[i] = nota_prueba_psicotecnica

    return lista_notas_prueba_tecnica, lista_notas_prueba_tecnica



def calcular_promedio(lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica, numero): #esto esta
    lista_promedio = [0] * numero

    for i in range(numero):
        lista_promedio[i] = (lista_notas_prueba_tecnica[i] + lista_notas_prueba_psicotecnica[i]) / 2

    return lista_promedio



def clasificar_promedios(lista_promedio):

    contador_contratable = 0
    contador_revision = 0
    contador_descartado = 0

    for promedio in lista_promedio:
        if promedio >= 6:
            contador_contratable = contador_contratable + 1

        elif promedio >= 4:
            contador_revision = contador_revision + 1

        else:
            contador_descartado = contador_descartado + 1

    print(f"Candidatos Contratables: {contador_contratable}")
    print(f"Candidatos en revisión: {contador_revision}")
    print(f"Candidatos Descartados: {contador_descartado}")

    return contador_contratable, contador_revision, contador_descartado



def calcular_prom_gral(lista_promedio, numero): # esto esta

    acumulador_promedio = 0

    for promedio in lista_promedio:
        acumulador_promedio = acumulador_promedio + promedio

    promedio_general = acumulador_promedio / numero

    return promedio_general



def calcular_max_min(lista_promedio, lista_nombres): #esto esta

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