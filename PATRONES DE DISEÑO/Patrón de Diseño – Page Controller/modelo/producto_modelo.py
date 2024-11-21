class Producto: 
    def __init__(self, id_producto: int, nombre: str, precio: float, cantidad: int): 
        self.id_producto = id_producto 
        self.nombre = nombre 
        self.precio = precio 
        self.cantidad = cantidad 
        
    def __str__(self): 
        return f"Producto {self.id_producto}: {self.nombre} - Precio: {self.precio}, Cantidad: {self.cantidad}" 
    
class ProductoModelo: 
    def __init__(self): 
        self.productos = [] 
    
    def agregar_producto(self, producto: Producto): 
        self.productos.append(producto) 
        
    def obtener_productos(self): 
        return self.productos 
    
    def obtener_producto_por_id(self, id_producto: int): 
        for producto in self.productos: 
            if producto.id_producto == id_producto: 
                return producto 
        return None