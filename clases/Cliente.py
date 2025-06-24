class Cliente:
    def __init__(self, dni: int, nombre: str, apellido:str, email: str, direccion: str):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__direccion = direccion

    def __str__(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.dni}\nEmail: {self.email}\nDireccion: {self.direccion}'

    '''GETTERS usando @property para simplificar el acceso'''
    @property
    def dni(self) -> int:
        return self.__dni
    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def apellido(self) -> str:
        return self.__apellido
    @property
    def email(self) -> str:
        return self.__email
    @property
    def direccion(self) -> str:
        return self.__direccion

    '''SETTERS usando @property.setter para simplificar la asignación'''
    '''Retorno None en los setters porque solo asigno, no me importa su valor'''
    @dni.setter
    def dni(self, dni: int) -> None:
        self.__dni = dni
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre
    @apellido.setter
    def apellido(self, apellido: str) -> None:
        self.apellido = apellido
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
    @direccion.setter 
    def direccion(self, direccion: str) -> None:
        self.__direccion = direccion
    

cliente1 = Cliente(45412623,'Lucas', 'Oelschlager', 'lucas@gmail.com', 'cullen 669')
print(cliente1.nombre)
cliente1.nombre = 'daniel'



