from validaciones import validar_menu
from procesamiento import crear_lista, ingresar_nombre_candidato, ingresar_notas

def main() -> None:
    """Función principal que gestiona el menú interactivo del sistema escolar."""
    cantidad = 0
    nombres = [""]
    parcial1 = [0]
    parcial2 = [0]
    promedios = [0.0]
    salir = False

    # Bucle principal del sistema
    while not salir:
        print("TITULO")
        print("1. Cargar Candidatos.")
        print("2. Mostrar listado")
        print("3. Mostrar estadísticas")
        print("4. Ver ranking (ordenado)")
        print("5. Buscar candidato")
        print("6. Juegos con un nombre")
        print("0. Salir")

        opcion = validar_menu("Seleccione una opción del menu: ")


        match opcion:
            case 1:
                nombres, nota_prueba_tecnica, nota_prueba_psicotecnica = crear_lista()

                nombres = ingresar_nombre_candidato(nombres, len(nombres))

                nota_prueba_tecnica, nota_prueba_psicotecnica = ingresar_notas(nota_prueba_tecnica, nota_prueba_psicotecnica, len(nombres))


if __name__ == "__main__":
    main()




#def pedir_numero():
    #"""
    #Solicita al usuario que ingrese un número entero y lo devuelve.
#
    #Returns:
        #int: El número ingresado por el usuario.
    #"""
    #numero = int(input("Ingrese un número: "))
#
    #return numero
#
#
#
#
#
#def ejecutar_menu(numero):
    #"""
    #Ejecuta la opción seleccionada por el usuario mediante una estructura
    #match-case y muestra un mensaje correspondiente a cada opción.
#
    #Args:
        #numero (int): Opción del menú seleccionada por el usuario.
#
    #Returns:
        #None: La función muestra mensajes por pantalla, pero no devuelve
        #ningún valor.
    #"""
    #match numero:
        #case 1:
            #print('Usted ha ingresado a "Cargar candidatos".')
#
        #case 2:
            #print('Usted ha ingresado a "Mostrar Listado".')
#
        #case 3:
            #print('Usted ha ingresado a "Mostrar Estadística".')
#
        #case 4:
            #print('Usted ha ingresado a "Ver Ranking (ORDENADO)".')
#
        #case 5:
            #print('Usted ha ingresado a "Buscar candidato".')
#
        #case 6:
            #print('Usted ha ingresado a "Juegos con un Nombre".')
#
        #case 0:
            #print("Saliendo del programa. Gracias por elegirnos.")
#
    #return numero
#
#
#
#
#
#def ejecutar_menu(numero):
    #print(f"DEBUG ejecutar_menu: {numero}")
#
    #match numero:
                #case 1:
                    #print('Usted ha ingresado a "Cargar candidatos".')
#
                #case 2:
                    #print('Usted ha ingresado a "Mostrar Listado".')
#
                #case 3:
                    #print('Usted ha ingresado a "Mostrar Estadística".')
#
                #case 4:
                    #print('Usted ha ingresado a "Ver Ranking (ORDENADO)".')
#
                #case 5:
                    #print('Usted ha ingresado a "Buscar candidato".')
#
                #case 6:
                    #print('Usted ha ingresado a "Juegos con un Nombre".')
#
                #case 0:
                    #print("Saliendo del programa. Gracias por elegirnos.")
#
#
#
#def main():
    #while True:
        #mostrar_menu()
#
        #opcion = int(input("Ingrese la opción del menú que desee: "))
        #opcion = validar_menu(opcion)
#
        #ejecutar_menu(opcion)
#
        #if opcion == 0:
            #break
#
#
#    
#
#def cargar_candidatos():
#
    #numero_candidatos = ingresar_numero_candidatos()
    #numero_candidatos = validar_listas_numero_candidatos(numero_candidatos)
#
    #nombres = crear_lista_nombres(numero_candidatos)
    #notas1 = crear_lista_notas_primer_parcial(numero_candidatos)
    #notas2 = crear_lista_notas_segundo_parcial(numero_candidatos)
#
    #for i in range(numero_candidatos):
#
        #nombre_candidato = input("Ingrese el nombre del candidato: ")
#
        #while not validar_nombres_candidatos(nombre_candidato):
            #print("Nombre inválido. Debe tener al menos 5 caracteres y contener solamente letras y espacios.")
            #nombre_candidato = input("Ingrese el nombre del candidato: ")
#
        #nombres[i] = nombre_candidato
#
        #cargar_nota_primer_parcial(notas1, i)
        #cargar_nota_segundo_parcial(notas2, i)
#
#
#
#cargar_candidatos()