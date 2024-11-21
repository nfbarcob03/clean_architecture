import json 
import os 
class Producto: 
    archivo_productos = 'productos.json' 

    def __init__(self, id_producto: int, nombre: str, precio: float, cantidad: int): 
        self.id_producto = id_producto 
        self.nombre = nombre
        self.precio = precio 
        self.cantidad = cantidad 

    def guardar(self): 
        productos = self._cargar_productos() 
        productos.append(self.to_dict()) 
        self._guardar_productos(productos) 

    def actualizar(self): 
        productos = self._cargar_productos() 
        for i, producto in enumerate(productos): 
            if producto['id_producto'] == self.id_producto: 
                productos[i] = self.to_dict() 
                self._guardar_productos(productos) 
                return True 
            return False 

    def eliminar(self): 
        productos = self._cargar_productos() 
        productos = [producto for producto in productos if producto['id_producto'] != self.id_producto] 
        self._guardar_productos(productos) 

    @classmethod 
    def encontrar_por_id(cls, id_producto: int): 
        productos = cls._cargar_productos() 
        for producto in productos: 
            if producto['id_producto'] == id_producto: 
                return cls.from_dict(producto) 
            return None 
            
    @classmethod 
    def todos(cls):
        productos = cls._cargar_productos() 
        return [cls.from_dict(producto) for producto in productos] 

    @staticmethod 
    def _cargar_productos(): 
        if not os.path.exists(Producto.archivo_productos): 
            return [] 
        with open(Producto.archivo_productos, 'r') as file: 
            return json.load(file) 
        
    @staticmethod 
    def _guardar_productos(productos): 
        with open(Producto.archivo_productos, 'w') as file: 
            json.dump(productos, file, indent=4) 
            
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

    def __str__(self): 
        return f"Producto {self.id_producto}: {self.nombre} - Precio: {self.precio}, Cantidad: {self.cantidad}"