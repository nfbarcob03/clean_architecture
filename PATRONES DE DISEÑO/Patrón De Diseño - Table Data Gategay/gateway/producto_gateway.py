import json 
import os 
from entidad.producto import Producto 

class ProductoGateway: 
    def __init__(self, archivo_productos='productos.json'): 
        self.archivo_productos = archivo_productos 
        self.productos = self.cargar_productos() 
        
    def cargar_productos(self): 
        if not os.path.exists(self.archivo_productos): 
            return [] 
        with open(self.archivo_productos, 'r') as file: 
            productos_dict = json.load(file) 
            return [Producto.from_dict(p) for p in productos_dict]
    
    def guardar_productos(self): 
        with open(self.archivo_productos, 'w') as file: 
            productos_dict = [producto.to_dict() for producto in self.productos] 
            json.dump(productos_dict, file, indent=4) 
    
    def agregar_producto(self, producto: Producto): 
        self.productos.append(producto) 
        self.guardar_productos() 
    
    def obtener_todos_los_productos(self): 
        return self.productos 
    
    def obtener_producto_por_id(self, id_producto: int): 
        for producto in self.productos: 
            if producto.id_producto == id_producto: 
                return producto 
            return None 
        
    def actualizar_producto(self, producto_actualizado: Producto): 
        for i, producto in enumerate(self.productos): 
            if producto.id_producto == producto_actualizado.id_producto: 
                self.productos[i] = producto_actualizado 
                self.guardar_productos() 
                return True 
        return False 
    
    def eliminar_producto(self, id_producto: int): 
        self.productos = [producto for producto in self.productos if producto.id_producto != id_producto] 
        self.guardar_productos()