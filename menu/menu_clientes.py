from clases import Cliente
from validaciones import validacion_input
import os 
clientes = []
def menu_clientes():
    print("### MENU DE GESTION DE CLIENTES ###\n")
    while True:
        op = input("Ingrese una opcion\n1)Añadir Cliente\n2)Mostrar lista de clientes\n3)Modificar datos de cliente\n4)Borrar Cliente\n5)SALIR")
        if validacion_input.validar_a_numero(op):
            os.system('clear')
            print("Numero añadido correctamente")
        else:
            os.system('clear')
            print("Ingresaste un dato no valido. Intente nuevamente")



