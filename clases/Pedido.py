class Pedido:
    def __init__(self, dni_cliente: int, lista_productos):
        self.__dni_cliente = dni_cliente
        self.__lista_productos = lista_productos