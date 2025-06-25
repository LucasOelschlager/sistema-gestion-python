class Producto:
    _id_counter = 1
    def __init__(self, codigo: int, nombre: str, descripcion: str, precio: float, stock: int = 0):
        self.__codigo = Producto._id_counter
        Producto._id_counter += 1
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock

    def __str__(self):
        return f'Codigo: {self.__codigo}\nNombre: {self.__nombre}\nDescripcion: {self.__descripcion}\nPrecio: {self.precio}\nStock: {self.stock}'

    '''GETTERS'''    
    def get_codigo(self) -> int:
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    def get_precio(self):
        return self.__precio
    def get_stock(self):
        return self.__stock
    
    '''SETTERS'''
    def set_codigo(self, int = 0) -> None:
        self.__codigo = int
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    def set_precio(self, precio = 0):
        self.precio = precio
    def set_stock(self, stock = 0):
        self.stock = stock




