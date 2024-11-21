class Producto: 
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int): 
        self.id_producto = id_producto 
        self.nombre = nombre 
        self.precio = precio 
        self.stock = stock 
        
    def __repr__(self): 
        return f"Producto({self.id_producto}, '{self.nombre}', Precio: {self.precio}, Stock: {self.stock})" 
    
    def ajustar_stock(self, cantidad: int): 
        if self.stock + cantidad < 0: 
            raise ValueError("No hay suficiente stock para realizar la operacin.") 
        self.stock += cantidad

        