from clases import Producto
from validaciones import validacion_input
productos = []
def menu_producto():
    option = input('1) Crear Producto\n2) Mostrar Productos\n3) Modificar Producto\n4) Eliminar Producto')
    if option == 1 or option == '1':
        nuevo_producto = Producto.Producto(0, '','', 0, 0)
        print(f"Codigo generado automaticamente, el codigo es: {nuevo_producto.get_codigo()}") 

        while True:
            nombre = input('Ingrese el nombre ')
            if validacion_input.validar_texto(nombre):
                nuevo_producto.set_nombre(nombre)
                break
            else:
                print('El nombre debe tener al menos 3 caracteres y no contener numeros')
        while True:
            desc = input('ingrese la descripcion del producto ')
            if validacion_input.validar_texto(desc):
                nuevo_producto.set_descripcion(desc)
                break
            else:
                 print('La descripcion debe tener al menos una palabra y no contener numeros')
        while True:
            precio = input('Ingrese el precio del producto ')
            if validacion_input.validar_a_numero(precio):
                precio = float(precio)
                nuevo_producto.set_precio(precio)
                break
            else:
                print('El precio debe ser mayor a 0 y no contener LETRAS')  
        while True:
            stock = input('Ingrese el stock del producto ')
            if validacion_input.validar_a_numero(stock):
                stock = int(stock)
                nuevo_producto.set_stock(stock)
                print('Producto Creado exitosamente')
                print(f'{nuevo_producto.__str__()}\n')
                op = input('Confirmar producto? S/N')
                if op.lower() == 's':
                    productos.append(nuevo_producto)
                    print("PRODUCTO CREADO CON EXITO")
                    break
                else:
                    break
            else:
                print('El stock debe ser representado en numeros enteros ')      


    ##MOSTRAR LOS PRODUCTOS
    elif option == 2 or option == '2':
        for producto in productos:
            print(producto)
            input('\nPresione una tecla para salir')


    ##MODIFICAR UN PRODUCTO
    elif option == 3 or option == '3':
        codigo = input("Ingrese el codigo del producto a modificar ")
        if validacion_input.validar_a_numero(codigo):
            codigo = int(codigo)
            for producto in productos:
                if codigo == producto.get_codigo():
                    op = input("Ingrese el dato a modificar.\n1)NOMBRE:\n2)DESCRIPCION:\n3)PRECIO:\n4)STOCK:\n")
                    if validacion_input.validar_a_numero(op):
                        op = int(op)
                        if op == 1:
                            nuevo_nombre = input('Ingrese el nuevo nombre')
                            producto.set_nombre(nuevo_nombre)
                        elif op == 2:
                            nueva_desc = input("Ingrese la nueva descripcion ")
                            producto.set_descripcion(nueva_desc)
                        elif op == 3:
                            nuevo_precio = input("Ingrese el nuevo precio del producto ")
                            producto.set_precio(float(nuevo_precio))
                        elif op == 4:
                            nuevo_stock = input("Ingrese el nuevo stock del producto ")
                            producto.set_stock(nuevo_stock)
                    else:
                        print("INGRESE UN NUMERO VALIDO ")
        else:
            print("NUMERO NO VALIDO")
        print(f"Producto modificado con exito \n{producto.__str__()}")
        
    ##ELIMINAR UN PRODUCTO
    elif option == 4 or option == '4':
        codigo = input("Ingrese el codigo del producto a modificar ")
        if validacion_input.validar_a_numero(codigo):
            codigo = int(codigo)
            for producto in productos:
                if codigo == producto.get_codigo():
                    print(producto.__str__())
                    op = input("\nConfirmar? S/N")
                    if op.lower() == 's':
                        productos.remove(producto)
                        print("Producto eliminado")
        else:
            print("INGRESE UN NUMERO VALIDO")







