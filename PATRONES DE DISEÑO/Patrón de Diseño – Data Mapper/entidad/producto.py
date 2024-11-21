class Producto: 
    def __init__(self, id_producto: int, nombre: str, precio: float, cantidad: int): 
        self.id_producto = id_producto 
        self.nombre = nombre 
        self.precio = precio 
        self.cantidad = cantidad 
    def __str__(self): 
        return f"Producto {self.id_producto}: {self.nombre} - Precio: {self.precio}, Cantidad: {self.cantidad}"