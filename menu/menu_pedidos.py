import json
from validaciones import validacion_input
from clases import Pedido
from historico_pedidos import historico_pedidos
import os

def guardar_pedidos_json(pedidos, filename='historico_pedidos.json'):
    data = []
    for pedido in pedidos:
        data.append({
            'id': pedido.get_id(),
            'dni_cliente': pedido.get_dni_cliente(),
            'productos': list(pedido.get_lista_productos())
        })
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def cargar_pedidos_json(filename='historico_pedidos.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        pedidos = []
        for p in data:
            pedido = Pedido.Pedido(p['dni_cliente'], p['productos'])
            pedidos.append(pedido)
        return pedidos
    except FileNotFoundError:
        return []

def modificar_pedido():
    pedidos = cargar_pedidos_json()
    if not pedidos:
        print("No hay pedidos para modificar.")
        return
    for pedido in pedidos:
        print(pedido)
    id_mod = input("Ingrese el ID del pedido a modificar: ")
    if not id_mod.isdigit():
        print("ID no válido.")
        return
    id_mod = int(id_mod)
    for pedido in pedidos:
        if pedido.get_id() == id_mod:
            print("Pedido seleccionado:")
            print(pedido)
            while True:
                codigo = input("Ingrese el código del producto a modificar (o S para salir): ")
                if codigo.lower() == 's':
                    break
                for i, (cod, cantidad) in enumerate(pedido.get_lista_productos()):
                    if int(codigo) == int(cod):
                        nueva_cantidad = input(f"Cantidad actual: {cantidad}. Ingrese la nueva cantidad: ")
                        if nueva_cantidad.isdigit():
                            pedido.get_lista_productos()[i] = (cod, int(nueva_cantidad))
                            print("Cantidad modificada.")
                        else:
                            print("Cantidad no válida.")
                        break
                else:
                    print("Producto no encontrado en el pedido.")
            break
    guardar_pedidos_json(pedidos)
    print("Pedido modificado y guardado.")

def borrar_pedido():
    pedidos = cargar_pedidos_json()
    if not pedidos:
        print("No hay pedidos para borrar.")
        return
    for pedido in pedidos:
        print(pedido)
    id_borrar = input("Ingrese el ID del pedido a borrar: ")
    if not id_borrar.isdigit():
        print("ID no válido.")
        return
    id_borrar = int(id_borrar)
    pedidos_filtrados = [p for p in pedidos if p.get_id() != id_borrar]
    if len(pedidos_filtrados) == len(pedidos):
        print("No se encontró el pedido con ese ID.")
    else:
        guardar_pedidos_json(pedidos_filtrados)
        print("Pedido eliminado correctamente.")

def menu_pedidos():
    print("### MENÚ DE PEDIDOS ###")
    option = input("INGRESE UNA OPCIÓN\n1-CREAR PEDIDO\n2-HISTORIAL DE PEDIDOS\n3-MODIFICAR PEDIDO\n4-BORRAR PEDIDO")
    if validacion_input.validar_a_numero(option):
        option = int(option)
        if option == 1:
            nuevo_pedido = Pedido.Pedido(0,[])
            print(f"Codigo de pedido generado automaticamente. {nuevo_pedido.get_id()}")

            while True:
                dni = input("Ingrese el DNI del cliente ")
                if validacion_input.validar_a_numero(dni):
                    nuevo_pedido.set_dni_cliente(dni)
                    break
    
            while True:
                codigo = input("Agregue el codigo del producto. Para finalizar presione S")
                if codigo.lower() == 's':
                    os.system('clear')
                    nuevo_pedido.generar_pedido()
                    historico_pedidos.append(nuevo_pedido)
                    guardar_pedidos_json(historico_pedidos)
                    break
                else:
                    cantidad = input('Ingrese la cantidad ')
                    nuevo_pedido.agregar_producto(codigo, cantidad)
            print(nuevo_pedido)
        elif option == 2:
            pedidos = cargar_pedidos_json()
            for pedido in pedidos:
                print(pedido)
        elif option == 3:
            modificar_pedido()
        elif option == 4:
            borrar_pedido()
        else: 
            print('Numero no valido')
    else:
        print('Numero no valido')