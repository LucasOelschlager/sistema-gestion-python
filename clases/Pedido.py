from menu.menu_producto import productos

class Pedido:
    _id_counter = 1
    def __init__(self, dni_cliente: int, lista_productos=None):
        self.__id = Pedido._id_counter
        Pedido._id_counter += 1
        self.__dni_cliente = dni_cliente
        self.__lista_productos = lista_productos if lista_productos is not None else []

    def __str__(self):
        return self.generar_pedido()

    def get_dni_cliente(self):
        return self.__dni_cliente
    def get_lista_productos(self):
        return self.__lista_productos
    def get_id(self):
        return self.__id

    def set_dni_cliente(self, value):
        self.__dni_cliente = value

    def calcular_total(self):
        total = 0
        for codigo, cantidad in self.__lista_productos:
            for item in productos:
                if item.get_codigo() == int(codigo):
                    total += item.get_precio() * int(cantidad)
        return total

    def agregar_producto(self, codigo, cantidad):
        self.__lista_productos.append((codigo, cantidad))

    def generar_pedido(self):
        productos_str = ""
        for codigo, cantidad in self.__lista_productos:
            for item in productos:
                if int(codigo) == item.get_codigo():
                    productos_str += f"\n- {item.get_nombre()} (Código: {codigo}) x {cantidad} - Precio unitario: {item.get_precio()}"
            
        return f"Pedido N°: {self.__id}\nCliente DNI: {self.__dni_cliente}\nPRODUCTOS:{productos_str}\nTOTAL: {self.calcular_total()}"