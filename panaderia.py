class Panaderia:
    def __init__ (self, nombre, precio, tipo):
        self.__nombre = nombre
        self.__precio = precio
        self.__tipo = tipo
@property
def nombre(self):
    return nombre
@property
def precio(self):
    return precio
@property
def tipo(self):
    return tipo

@nombre.setter
def nombre(self, nuevo_nombre):
    if len(nuevo_nombre) < 0:
        raise ValueError ("Error")
    self.__nombre = nuevo_nombre
@precio.setter
def precio (self, nuevo_precio):
    if nuevo_precio < 0:
        raise ValueError ("Error")
    self.__precio = nuevo_precio
@tipo.setter
def tipo (self, valor):
    if valor not in ("unidad", "peso"):
        raise ValueError ("Error de precio")
    self.__tipo = valor

def __str__ (self):
    return f"{self.__nombre}, - ${self.__precio} ({self.__tipo})"

def calcular_subtotal(self, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")
    return self.__precio * cantidad
