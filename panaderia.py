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
        
#========== nivel 4.2 ===========
    def calcular_vuelto(self, dinero_recibido):
        vuelto = dinero_recibido - self.__total
        if vuelto < 0:
            falta = (-1) *  vuelto # ó falta = abs(vuelto)
            raise ValueError (f"Error, el dinero no es suficiente, faltan ${falta}")
        print (f"El vuelto es {vuelto}")
        return vuelto
#========== nivel 4.3 ===========
    @staticmethod
    def desglosa_vuelto(vuelto):
        if vuelto <= 0:
            print ("No hay vuelto")
            return
        billetes = [1000, 500, 200, 100, 50, 20, 10]
        resto = vuelto
        
        print (f"Desglose de ${vuelto}")
        
        for billete in billetes:
            if resto >= billete:
                cantidad = resto // billete
                print (f"${billete}: {cantidad} billetes")
                resto -= cantidad * billete
        if resto > 0:
            print (f"Sobran ${resto} monedas")

        
#========== nivel 4 ===========
class Caja:
    def __init__(self, dinero_inicial = 50000):
        self.__dinero_disponible = dinero_inicial
    @property
    def dinero_disponible(self):
        return self.__dinero_disponible
    
    def agregar_dinero(self, monto):
        if monto <= 0:
            raise ValueError ("Error, monto negativo o cero")
        self.__dinero_disponible += monto
        print (f"Se agregaron a la caja: ${monto}")
    
    def restar_dinero (self, monto):
        if monto <= 0:
            raise ValueError ("Error, monto negativo o cero")
        if self.__dinero_disponible < monto:
            raise ValueError ("Tu monto es superior al ${self.__dinero_disponible}")
        self.__dinero_disponible -= monto
        print (f"Se sacaron de la caja: ${monto}")
        
#========== nivel 5 ===========
def main():
    caja = Caja(50000)
    lista_producto = [
        Producto("Pan Francés", 500, "unidad"),
        Producto("Medialuna", 300, "unidad"),
        Producto("Factura", 400, "unidad"),
        Producto("Pan de campo", 800, "unidad"),
        Producto("Pan rallado", 2000, "peso")
        ]
#========== nivel 5.2 ===========
    while True:
        print("Opciones del menú:")
        print ("=== PANADERÍA ===")
        print ("1. Ver productos disponibles")
        print ("2. Realizar venta")
        print ("3. Ver saldo de caja")
        print ("4. Salir")
        opcion = input ("Selecciona una opcion: ")

#========== nivel 5.3 ===========
        if opcion == "1":
            print("===========Produtos disponible===========")
            for i, producto in enumerate (lista_producto, start = 1):
                print (f"{i}. {producto}")
#========== nivel 5.4 ===========
        elif opcion == "2":
            print("---Venta nueva---")
            mi_venta = Venta()
            while True:
                for i, prod in enumerate (lista_producto, start = 1):
                    print (f"{i}{prod.nombre}- ${prod.precio} ({prod.tipo})")
                seleccion = input("Selecciona una opcion o 0 para salir: ")
                if seleccion == "0":
                    break
                try:
                    numero = int (seleccion)
                    producto_elegido = lista_producto[numero - 1]
                except:
                    print ("Error, colocaste una opcion no valida")

if __name__ == "__main__":
    main()