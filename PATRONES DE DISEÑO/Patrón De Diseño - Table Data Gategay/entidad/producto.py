class Producto: 
    def __init__(self, id_producto: int, nombre: str, precio: float, cantidad: int): 
        self.id_producto = id_producto 
        self.nombre = nombre 
        self.precio = precio 
        self.cantidad = cantidad 

    def actualizar_stock(self, cantidad: int): 
        self.cantidad = cantidad 

    def __str__(self): 
        return f"Producto {self.id_producto}: {self.nombre} - Precio: {self.precio}, Cantidad: {self.cantidad}" 
    
    @staticmethod 
    def from_dict(producto_dict): 
        return Producto( 
            id_producto=producto_dict['id_producto'], 
            nombre=producto_dict['nombre'], 
            precio=producto_dict['precio'], 
            cantidad=producto_dict['cantidad'] 
            ) 
    
    def to_dict(self): 
        return { 
            'id_producto': self.id_producto, 
            'nombre': self.nombre, 
            'precio': self.precio, 
            'cantidad': self.cantidad 
            }