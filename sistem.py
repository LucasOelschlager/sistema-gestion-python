
import os 
from menu import menu_producto, menu_clientes, menu_pedidos

def sistem():
    while True:
        print('#### BIENVENIDO ####\n')
        option = input('\n1)Gestionar Productos\n2)Gestionar Clientes\n3)Gestionar Pedidos\n4)Historial de operaciones\n5)Salir ')
        os.system('clear')
        if option == '1' or option == 1:
            menu_producto.menu_producto()
        elif option == 2 or option == '2':
            menu_clientes.menu_clientes()
        elif option == 3 or option == '3':
            menu_pedidos.menu_pedidos()
        elif option == 4 or option == '4':
            print('Historial')
        elif option == 5 or option == '5    ':
            exit()
        else:
            print('Opcion incorrecta')
sistem()