import json
from clases import Cliente
from validaciones import validacion_input
import os 
clientes = []

def guardar_clientes_json(clientes, filename='clientes.json'):
    data = []
    for cli in clientes:
        data.append({
            'dni': cli.dni,
            'nombre': cli.nombre,
            'apellido': cli.apellido,
            'email': cli.email,
            'direccion': cli.direccion
        })
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def cargar_clientes_json(filename='clientes.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        clientes.clear()
        for c in data:
            cli = Cliente.Cliente(c['dni'], c['nombre'], c['apellido'], c['email'], c['direccion'])
            clientes.append(cli)
    except FileNotFoundError:
        pass

def menu_clientes():
    cargar_clientes_json()  # Cargar clientes al iniciar
    print("### MENU DE GESTION DE CLIENTES ###\n")
    while True:
        op = input("Ingrese una opcion\n1)Añadir Cliente\n2)Mostrar lista de clientes\n3)Modificar datos de cliente\n4)Borrar Cliente\n5)SALIR")
        if validacion_input.validar_a_numero(op):
            os.system('clear')
            op = int(op)
            if op == 1: 
                nuevo_cliente = Cliente.Cliente(0, "", "", "", "")
                while True:
                    dni = input("Ingrese el DNI del cliente ")
                    if validacion_input.validar_a_numero(dni):
                        confirm = input(f"El dni ingresado es {dni}. Desea confirmar? S/N")
                        if validacion_input.validar_texto(confirm):
                            if confirm.lower() == 's':
                                nuevo_cliente.dni = dni
                        nombre = input("Ingrese el nombre del cliente ")
                        while True:
                            if validacion_input.validar_texto(nombre):
                                nuevo_cliente.nombre = nombre
                                break
                            else:
                                print("El nombre no es valido")
                        while True:           
                            apellido = input("Ingrese el apellido del cliente ")                              
                            if validacion_input.validar_texto(apellido):
                                nuevo_cliente.apellido = apellido
                                break
                            else:
                                print("El apellido no es valido")
                        email = input("Ingrese el email del cliente ")
                        nuevo_cliente.email = email
                        direccion = input("Ingrese la direccion del cliente")
                        nuevo_cliente.direccion = direccion
                        clientes.append(nuevo_cliente)
                        guardar_clientes_json(clientes)
                        break
        else:
            os.system('clear')
            print("Ingresaste un dato no valido. Intente nuevamente")
            break



