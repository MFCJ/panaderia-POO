#==========nivel 1===========
class Producto:
    def __init__(self, nombre, precio, tipo):
        self.__nombre = nombre
        self.__precio = precio
        self.__tipo = tipo
        
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def tipo(self):
        return self.__tipo

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) == 0:
            raise ValueError ("Error")
        self.__nombre = nuevo_nombre
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("Error")
        self.__precio = nuevo_precio
    @tipo.setter
    def tipo(self, valor):
        if valor not in ("unidad", "peso"):
            raise ValueError("Error de precio")
        self.__tipo = valor

    def calcular_subtotal(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        return self.__precio * cantidad
    def __str__(self):
        return f"{self.__nombre}, - ${self.__precio} ({self.__tipo})"

#==========nivel 2===========

class ItemVenta:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad

    @property
    def producto(self):
        return self.__producto

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self.__cantidad = nueva_cantidad

    def calcular_subtotal(self):
        return self.__producto.calcular_subtotal(self.__cantidad)
    def __str__(self):
        subtotal = self.calcular_subtotal()
        return f"{self.__producto.nombre}: {self.__cantidad} x {self.__producto.precio} = ${subtotal}"

#==========nivel 3===========
class Venta:
    def __init__(self):
        self.__items = []
        self.__total = 0
    def agregar_item(self, producto, cantidad):
        self.__items.append(ItemVenta(producto, cantidad))
    def calcular_total(self):
        total_acumulado = 0
        for item in self.__items:
            total_acumulado += item.calcular_subtotal()
        self.__total = total_acumulado
        return self.__total
    def obtener_items(self):
        return self.__items.copy()
    @property
    def total (self):
        return self.__total
    def mostrar_resumen(self):
        print ("_________________________Resumen del dia_________________________")
        for item in self.__items:
            print (item)
        print (f"total del dia: ${self.__total}")