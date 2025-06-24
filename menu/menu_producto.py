from clases import Producto
productos = []
def menu_producto():
    option = input('1) Crear Producto\n2) Mostrar Productos\n3) Modificar Producto\n4) Eliminar Producto')
    if option == 1 or option == '1':
        nuevo_producto = Producto.Producto(0, '','', 0, 0)
        while True:
            codigo = input('Ingrese el codigo del producto ')
            if not codigo.isdigit():
                print('El codigo debe ser solo numeros ')
            else:
                codigo = int(codigo)
                nuevo_producto.set_codigo(codigo)
                break
        while True:
            nombre = input('Ingrese el nombre ')
            if len(nombre) < 3 or not nombre.isalpha():
                print('El nombre debe tener al menos 3 caracteres y no contener numeros')
            else:
                nuevo_producto.set_nombre(nombre)
                break
        while True:
            desc = input('ingrese la descripcion del producto ')
            if len(desc.split()) < 1 or not desc.isalpha():
                print('La descripcion debe tener al menos una palabra y no contener numeros')
            else:
                nuevo_producto.set_descripcion(desc)
                break
        while True:
            precio = input('Ingrese el precio del producto ')
            if precio.isdigit():
                precio = float(precio)
            if float(precio < 0):
                print('El precio debe ser mayor a 0 ')
            elif precio < 0:
                print('Ingrese un precio valido. Mayor a 0')
            else:
                precio = float(precio)
                nuevo_producto.set_precio(precio)
                break
        while True:
            stock = input('Ingrese el stock del producto ')
            if not stock.isdigit():
                stock = int(stock)
                print('El stock debe ser representado en numeros enteros ')
            else:
                nuevo_producto.set_stock(stock)
                print('Producto Creado exitosamente')
                print(f'{nuevo_producto.__str__()}\n')
                op = input('Confirmar producto? S/N')
                if op.lower() == 's':
                    productos.append(nuevo_producto)
                    break
                else:
                    break
    if option == 2 or option == '2':
        for producto in productos:
            print(producto)
            input('\nPresione una tecla para salir')
    elif option == 3 or option == '3':
        codigo = input("Ingrese el codigo del producto a modificar ")
        codigo = int(codigo)
        for producto in productos:
            if codigo == producto.get_codigo():
                op = input("Ingrese el dato a modificar. \n1)CODIGO:\n2)NOMBRE:\n 3)DESCRIPCION:\n 4)PRECIO:\nSTOCK:\n")
                if op.isdigit():
                    op = int(op)
                if op == 1:
                    nuevo_codigo = input('Ingrese el nuevo codigo ')
                    producto.set_codigo(nuevo_codigo)
                elif op == 2:
                    nuevo_nombre = input('Ingrese el nuevo nombre')
                    producto.set_nombre(nuevo_nombre)
                elif op == 3:
                    nueva_desc = input("Ingrese la nueva descripcion ")
                    producto.set_descripcion(nueva_desc)
                elif op == 4:
                    nuevo_precio = input("Ingrese el nuevo precio del producto ")
                    producto.set_precio = (float(nuevo_precio))
                elif op == 5:
                    nuevo_stock = input("Ingrese el nuevo stock del producto ")
                    producto.set_stock(nuevo_stock)
            print(f"Producto modificado con exito \n{producto.__str__()}")
            



        
            
