from validaciones import validar_menu, cantidad_listas

from procesamiento import (inicializar_listas_postulantes, cargar_nombres_postulantes, cargar_notas_postulantes, calcular_promedios_postulantes,
                           
                            calcular_prom_gral, calcular_max_min, clasificar_promedios,

                            ordenar_listas, 
                            
                            buscar_nombre, 
                            
                            ingresar_nombre_postulante_juego, contar_vocales, invertir_nombre)


def main() -> None:
    """Función principal que gestiona el menú interactivo del sistema escolar."""
    cantidad_postulantes = 0
    nombres = [""]
    nota_prueba_tecnica = [0]
    nota_prueba_psicotecnica = [0]
    promedios = [0.0]
    salir = False

    # Bucle principal del sistema
    while not salir:
        print("GESTIÓN DE ENTREVISTAS")
        print("1. Cargar Postulantes. ")
        print("2. Mostrar Listado General. ")
        print("3. Mostrar Estadísticas del Proceso. ")
        print("4. Ver Ranking Postulantes (ordenado)")
        print("5. Buscar Postulante")
        print("6. Analizar Nombre de postulante")
        print("0. Salir")

        opcion = validar_menu("Seleccione una opción del menu: ")


        match opcion:
            case 1:
                cantidad_postulantes, nombres, nota_prueba_tecnica, nota_prueba_psicotecnica, promedios = inicializar_listas_postulantes()

                nombres = cargar_nombres_postulantes(nombres, cantidad_postulantes)

                nota_prueba_tecnica, nota_prueba_psicotecnica = cargar_notas_postulantes(nota_prueba_tecnica, nota_prueba_psicotecnica, cantidad_postulantes)

                promedios = calcular_promedios_postulantes(nota_prueba_tecnica, nota_prueba_psicotecnica, cantidad_postulantes)


            case 2:
                if cantidad_listas(cantidad_postulantes):
                    print(nombres)
                    print(nota_prueba_tecnica)
                    print(nota_prueba_psicotecnica)
                    print(promedios)

            # Y SI NO HAY NINGUNA LISTA CARGADA? TENES QUE MOSTRAR UN MENSAJE.


            case 3:
                if cantidad_listas(cantidad_postulantes):
                    promedio_general = calcular_prom_gral(promedios, cantidad_postulantes)
                    print("El promedio general de la camada es:", promedio_general)


                    maximo, nombre_maximo, minimo, nombre_minimo = calcular_max_min(promedios, nombres)
                    print("Mejor promedio:", maximo)
                    print("postulante:", nombre_maximo)

                    print("Peor promedio:", minimo)
                    print("postulante:", nombre_minimo)


                    clasificar_promedios(promedios)


            case 4:
                if cantidad_listas(cantidad_postulantes):
                    promedios, nombres, nota_prueba_tecnica, nota_prueba_psicotecnica = ordenar_listas(promedios, nombres, nota_prueba_tecnica, nota_prueba_psicotecnica)
                    for i in range(cantidad_postulantes):
                        print(i + 1, nombres[i], promedios[i])


            case 5:
                if cantidad_listas(cantidad_postulantes):
                    nombre_objetivo = input("Ingrese el nombre del postulante: ")
                
                
                    resultado = buscar_nombre(nombre_objetivo, nombres, nota_prueba_tecnica, nota_prueba_psicotecnica, promedios)


                    if resultado == -1:
                        print("El postulante no se encuentra registrado. ")

                    else:
                        nota_tecnica = resultado[0]  #Son las posiciones de la lista que devuelve tu función
                        nota_psicotecnica = resultado[1]
                        promedios = resultado[2]

                        print(f"Nota técnica: {nota_tecnica}")
                        print(f"Nota psicotécnica: {nota_psicotecnica}")
                        print(f"Promedio: {promedios}")


            case 6:
                if cantidad_listas(cantidad_postulantes):
                    nombre_objetivo = ingresar_nombre_postulante_juego()

                    cantidad_vocales = contar_vocales(nombre_objetivo)
                    nombre_invertido = invertir_nombre(nombre_objetivo)

                    print(f"Cantidad de vocales: {cantidad_vocales}")
                    print(f"Nombre invertido: {nombre_invertido}")


            case 0:
                print("Saliendo del Programa...")
                salir = True


            case _:
                print("Opción inválida. Por favor, seleccione una opción correcta. (0 - 6)")
                  



if __name__ == "__main__":
        main()
