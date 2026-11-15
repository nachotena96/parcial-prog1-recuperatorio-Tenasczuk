def ordenar_listas(lista_promedios, lista_nombres, lista_notas_primer_parcial, lista_notas_segundo_parcial):
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


# DATOS DE PRUEBA

nombres = ["Ignacio", "Martina", "Lucas"]

prueba_tecnica = [6, 9, 7]

prueba_psicotecnica = [7, 10, 8]

promedio = [6.5, 9.5, 7.5]


# MOSTRAR LISTAS ORIGINALES

print("----- ANTES DE ORDENAR -----")

print("Nombres:", nombres)
print("Prueba técnica:", prueba_tecnica)
print("Prueba psicotécnica:", prueba_psicotecnica)
print("Promedios:", promedio)


# ORDENAR LISTAS

promedio, nombres, prueba_tecnica, prueba_psicotecnica = ordenar_listas(
    promedio,
    nombres,
    prueba_tecnica,
    prueba_psicotecnica
)


# MOSTRAR LISTAS ORDENADAS

print("\n----- DESPUÉS DE ORDENAR -----")

print("Nombres:", nombres)
print("Prueba técnica:", prueba_tecnica)
print("Prueba psicotécnica:", prueba_psicotecnica)
print("Promedios:", promedio)