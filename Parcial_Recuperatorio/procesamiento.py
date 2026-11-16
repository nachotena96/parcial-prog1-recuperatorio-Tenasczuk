from validaciones import validar_nombres_postulantes, ingresar_y_validar_numero_postulantes, validar_nombres_postulantes, validar_nota



def inicializar_listas_postulantes() -> tuple[int, list[str], list[int], list[int], list[float]]:
    """
    Solicita la cantidad de postulantes y crea las listas necesarias
    para almacenar sus nombres, notas de las pruebas y promedios.

    Returns:
        tuple: Contiene los siguientes elementos:
            - int: Cantidad de postulantes.
            - list[str]: Lista de nombres de los postulantes.
            - list[int]: Lista de notas de las pruebas técnicas.
            - list[int]: Lista de notas de las pruebas psicotécnicas.
            - list[float]: Lista de promedios de los postulantes.
    """

    cantidad_postulantes = ingresar_y_validar_numero_postulantes()

    lista_nombres = [""] * cantidad_postulantes
    lista_notas_prueba_tecnica = [0] * cantidad_postulantes
    lista_notas_prueba_psicotecnica = [0] * cantidad_postulantes
    lista_promedios = [0.0] * cantidad_postulantes

    return cantidad_postulantes, lista_nombres, lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica, lista_promedios






def cargar_nombres_postulantes(nombres: list[str], numero: int) -> list[str]:
    """
    Solicita los nombres de los postulantes, valida que cumplan con
    las condiciones establecidas y los almacena en la lista recibida.

    Args:
        nombres (list[str]): Lista donde se almacenarán los nombres.
        numero (int): Cantidad de postulantes cuyos nombres se ingresarán.

    Returns:
        list[str]: Lista con los nombres de los postulantes ingresados.
    """

    for i in range(numero):
            
            nombre = input("Ingrese el nombre del postulante: ")

            while not validar_nombres_postulantes(nombre):
                print("Nombre del postulante inválido.")

                nombre = input(f"Ingrese el nombre del postulante {i + 1}: ")

            nombres[i] = nombre

    return nombres






def cargar_notas_postulantes(lista_notas_prueba_tecnica: list[int], lista_notas_prueba_psicotecnica: list[int], numero: int) -> tuple[list[int], list[int]]:
    """
    Solicita las notas de las pruebas técnicas y psicotécnicas de cada
    postulante, valida que se encuentren entre 0 y 10 y las almacena
    en sus respectivas listas.

    Args:
        lista_notas_prueba_tecnica (list[int]): Lista donde se almacenan
            las notas de las pruebas técnicas.
        lista_notas_prueba_psicotecnica (list[int]): Lista donde se
            almacenan las notas de las pruebas psicotécnicas.
        numero (int): Cantidad de postulantes cuyas notas se ingresarán.

    Returns:
        tuple[list[int], list[int]]: Tupla que contiene las listas
        de notas técnicas y psicotécnicas actualizadas.
    """

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

    return lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica






def calcular_promedios_postulantes(lista_notas_prueba_tecnica: list[int], lista_notas_prueba_psicotecnica: list[int], numero: int) -> list[float]:
    """
    Calcula el promedio de las notas técnicas y psicotécnicas de cada
    postulante y almacena los resultados en una nueva lista.

    Args:
        lista_notas_prueba_tecnica (list[int]): Lista de notas de las
            pruebas técnicas.
        lista_notas_prueba_psicotecnica (list[int]): Lista de notas de
            las pruebas psicotécnicas.
        numero (int): Cantidad de postulantes.

    Returns:
        list[float]: Lista con los promedios calculados de cada postulante.
    """

    lista_promedio = [0] * numero

    for i in range(numero):
        lista_promedio[i] = (lista_notas_prueba_tecnica[i] + lista_notas_prueba_psicotecnica[i]) / 2

    return lista_promedio





def clasificar_promedios(lista_promedio: list[float]) -> tuple[int, int, int]:
    """
    Clasifica a los postulantes según sus promedios y contabiliza
    cuántos pertenecen a cada categoría:
    - Contratables: promedio igual o superior a 6.
    - En revisión: promedio igual o superior a 4 e inferior a 6.
    - Descartados: promedio inferior a 4.

    Args:
        lista_promedio (list[float]): Lista con los promedios
            de los postulantes.

    Returns:
        tuple[int, int, int]: Cantidad de postulantes contratables,
        en revisión y descartados, respectivamente.
    """

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

    print(f"postulantes Contratables: {contador_contratable}")
    print(f"postulantes en revisión: {contador_revision}")
    print(f"postulantes Descartados: {contador_descartado}")

    return contador_contratable, contador_revision, contador_descartado





def calcular_prom_gral(lista_promedio: list[float], numero: int) -> float:
    """
    Calcula el promedio general de todos los postulantes a partir
    de sus promedios individuales.

    Args:
        lista_promedio (list[float]): Lista con los promedios
            individuales de los postulantes.
        numero (int): Cantidad de postulantes registrados.

    Returns:
        float: Promedio general de todos los postulantes.
    """

    acumulador_promedio = 0

    for promedio in lista_promedio:
        acumulador_promedio = acumulador_promedio + promedio

    promedio_general = acumulador_promedio / numero

    return promedio_general





def calcular_max_min(lista_promedio: list[float], lista_nombres: list[str]) -> list[float | str]:
    """
    Busca los promedios máximo y mínimo de los postulantes e identifica
    los nombres correspondientes a cada uno.

    Args:
        lista_promedio (list[float]): Lista con los promedios
            individuales de los postulantes.
        lista_nombres (list[str]): Lista con los nombres de los postulantes.

    Returns:
        list[float | str]: Lista que contiene, en este orden:
            - float: Promedio máximo.
            - str: Nombre del postulante con el promedio máximo.
            - float: Promedio mínimo.
            - str: Nombre del postulante con el promedio mínimo.
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





def ordenar_listas(lista_promedios: list[float], lista_nombres: list[str], lista_notas_primer_parcial: list[int], lista_notas_segundo_parcial: list[int]) -> tuple[list[float], list[str], list[int], list[int]]:
    """
    Ordena los promedios de los postulantes de mayor a menor mediante
    el algoritmo de ordenamiento burbuja. También intercambia los
    elementos correspondientes de las listas paralelas para mantener
    asociados los datos de cada postulante.

    Args:
        lista_promedios (list[float]): Lista de promedios individuales.
        lista_nombres (list[str]): Lista de nombres de los postulantes.
        lista_notas_primer_parcial (list[int]): Lista de notas del
            primer parcial.
        lista_notas_segundo_parcial (list[int]): Lista de notas del
            segundo parcial.

    Returns:
        tuple[list[float], list[str], list[int], list[int]]: Tupla que
        contiene las cuatro listas ordenadas, conservando la relación
        entre los datos de cada postulante.
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





def mostrar_ranking_postulantes(lista_promedios, lista_nombres):
    """
    Muestra por pantalla la lista de nombres de los postulantes
    y la lista de sus promedios.

    Args:
        lista_promedios (list): Lista con los promedios de los postulantes.
        lista_nombres (list): Lista con los nombres de los postulantes.

    Returns:
        None: Muestra ambas listas por pantalla.
    """
    print(lista_nombres)
    print(lista_promedios)





def buscar_nombre(nombre_objetivo: str, lista_nombres: list[str], lista_notas_primer_parcial: list[int], lista_notas_segundo_parcial: list[int], lista_promedio: list[float]) -> list[int | float] | int:
    """
    Realiza una búsqueda secuencial del nombre de un postulante.
    Si encuentra una coincidencia, devuelve sus notas y promedio.
    Si no encuentra el nombre, devuelve -1.

    Args:
        nombre_objetivo (str): Nombre del postulante que se desea buscar.
        lista_nombres (list[str]): Lista de nombres registrados.
        lista_notas_primer_parcial (list[int]): Lista de notas del
            primer parcial.
        lista_notas_segundo_parcial (list[int]): Lista de notas del
            segundo parcial.
        lista_promedio (list[float]): Lista de promedios individuales.

    Returns:
        list[int | float] | int: Lista con las dos notas y el promedio
        del postulante encontrado, o -1 si no existe una coincidencia.
    """

    for i in range(len(lista_nombres)):
        if nombre_objetivo == lista_nombres[i]:
            nota1 = lista_notas_primer_parcial[i]
            nota2 = lista_notas_segundo_parcial[i]
            promedio = lista_promedio[i]

            return [nota1, nota2, promedio]

    return -1





def mostrar_notas_y_promedio_postulante(nombre_objetivo: str, nota1: int, nota2: int, promedio: float) -> None:
    """
    Muestra por pantalla el nombre, las notas de ambos parciales
    y el promedio del postulante.

    Args:
        nombre_objetivo (str): Nombre del postulante.
        nota1 (int): Nota obtenida en el primer parcial.
        nota2 (int): Nota obtenida en el segundo parcial.
        promedio (float): Promedio obtenido por el postulante.

    Returns:
        None: No devuelve ningún valor. Solamente muestra
        la información por pantalla.
    """

    print(f"Nombre del postulante: {nombre_objetivo}")
    print(f"Nota del primer parcial: {nota1}")
    print(f"Nota del segundo parcial: {nota2}")
    print(f"Promedio: {promedio}")





def contar_vocales(nombre: str) -> int:
    """
    Cuenta la cantidad de vocales presentes en el nombre recibido.
    Considera tanto las vocales minúsculas como las mayúsculas.

    Args:
        nombre (str): Nombre cuyos caracteres se desean analizar.

    Returns:
        int: Cantidad de vocales encontradas en el nombre.
    """

    vocales = "aeiouAEIOU"
    contador = 0

    for i in range(len(nombre)): # Recorre el nombre

        for j in range(len(vocales)): # Compara cada letra con las vocales
            if nombre[i] == vocales[j]:
                contador = contador + 1
                break

    return contador





def ingresar_nombre_postulante_juego() -> str:
    """
    Solicita al usuario el nombre del postulante que desea utilizar
    en el juego.

    Returns:
        str: Nombre ingresado por el usuario.
    """

    nombre_objetivo = input("Ingrese el nombre deseado del postulante: ")
    return nombre_objetivo





def invertir_nombre(nombre: str) -> str:
    """
    Invierte el orden de los caracteres del nombre recibido.

    Args:
        nombre (str): Cadena de texto que se desea invertir.

    Returns:
        str: Nombre con sus caracteres en orden inverso.
    """

    return nombre[::-1]
