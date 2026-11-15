from validaciones import validar_nombres_postulantes, ingresar_y_validar_numero_postulantes, validar_nombres_postulantes, validar_nota


def inicializar_listas_postulantes(): #Crea las listas vacías

    cantidad_postulantes = ingresar_y_validar_numero_postulantes()

    lista_nombres = [""] * cantidad_postulantes
    lista_notas_prueba_tecnica = [0] * cantidad_postulantes
    lista_notas_prueba_psicotecnica = [0] * cantidad_postulantes
    lista_promedios = [0.0] * cantidad_postulantes

    return cantidad_postulantes, lista_nombres, lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica, lista_promedios




def cargar_nombres_postulantes(nombres, numero): #Solicita y almacena los nombres /// #esto ya esta, tenes que ver que cuando pones l no te indica "nombre invalido"
#pedir numero de postulantes

    for i in range(numero):
            
            nombre = input("Ingrese el nombre del postulante: ")

            while not validar_nombres_postulantes(nombre):
                print("Nombre del postulante inválido.")

                nombre = input(f"Ingrese el nombre del postulante {i + 1}: ")

            nombres[i] = nombre  #///La primera variable es un texto y la segunda es la lista que queremos completar.///

    return nombres



def cargar_notas_postulantes(lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica, numero): #esto esta

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




def calcular_promedios_postulantes(lista_notas_prueba_tecnica, lista_notas_prueba_psicotecnica, numero): #esto esta
    lista_promedio = [0] * numero

    for i in range(numero):
        lista_promedio[i] = (lista_notas_prueba_tecnica[i] + lista_notas_prueba_psicotecnica[i]) / 2

    return lista_promedio




def clasificar_promedios(lista_promedio): #esto esta

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



def ordenar_listas(lista_promedios, lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial): # esto esta

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




def buscar_nombre(nombre_objetivo, lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial, lista_promedio): #esto ya esta

    for i in range(len(lista_nombres)):
        if nombre_objetivo == lista_nombres[i]:
            nota1 = lista_notas_primer_parcial[i]
            nota2 = lista_notas_segundo_parcial[i]
            promedio = lista_promedio[i]

            return [nota1, nota2, promedio]

    return -1



def mostrar_notas_y_promedio_postulante(nombre_objetivo, nota1, nota2, promedio):

    print(f"Nombre del postulante: {nombre_objetivo}")
    print(f"Nota del primer parcial: {nota1}")
    print(f"Nota del segundo parcial: {nota2}")
    print(f"Promedio: {promedio}")



def contar_vocales(nombre):

    vocales = "aeiouAEIOU"
    contador = 0

    for i in range(len(nombre)):  # Recorre el nombre

        for j in range(len(vocales)):  # Compara cada letra con las vocales
            if nombre[i] == vocales[j]:
                contador = contador + 1
                break

    return contador



def ingresar_nombre_postulante_juego():

    nombre_objetivo = input("Ingrese el nombre deseado del postulante: ")
    return nombre_objetivo



def invertir_nombre(nombre):

    return nombre[::-1]