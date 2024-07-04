import csv
###FUNCIONES
def menu():
    print("### MENU PRINCIPAL ### ")
    print("1. Filtro Jugador.")
    print("2. Filtro consola y año.")
    print("3. Escribir archivos.")
    print("4. Salir.")


def menu_escritura():
    print("1) Escribir filtro jugador")
    print("2) Escribir filtro consola y año")

def verificar_juego(singleplayer,multiplayer):
    if singleplayer == "1":
        juego1 = singleplayer.split("1")
        if len(juego1) > 10:
            return False
        else:
            print(juego1)



def verificar_consola_y_año(consola,año):
   L2 = []
   with open("juegos.csv", "r", newline="") as arch:
       consola = csv.reader(arch)
       print(consola)
       for linea in consola:
           print(linea)
           L2.append(linea)

           

def escribir_archivo(a,b):
    a = ""
    with open("filtro_juegos.txt") as archivo:
        archivo.write(a)
### MENU
d = {}
while True:
    menu()
    op = input("Ingrese opcion: ")
    if op == "1":
        tipo_juego = input("Singleplayer o Multiplayer (s/m)?: ")
        resultado_juego = verificar_juego()
        print("El resultado de la busqueda es (los 10 primeros): ", resultado_juego)
    elif op == "2":
        buscar = input("Ingrese Tipo de consola: ")
        buscar_año = input("Ingrese año: ")
    elif op == "3":
        print()

    else:
        op == "4"
        print("Saliendo del sistema...")
        break
    
