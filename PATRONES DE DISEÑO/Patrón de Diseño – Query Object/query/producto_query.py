import json 
import os 
from entidad.producto import Producto 

class ProductoQuery: 
    def __init__(self, archivo_productos='productos.json'): 
        self.archivo_productos = os.path.join(os.path.dirname(__file__), '..', archivo_productos) 
        self.criterios = [] 
        
    def cargar_productos(self): 
        if not os.path.exists(self.archivo_productos): 
            return [] 
        
        with open(self.archivo_productos, 'r') as file: 
            productos_dict = json.load(file) 
            return [Producto.from_dict(p) for p in productos_dict] 
        
    def filtrar_por_nombre(self, nombre): 
        self.criterios.append(lambda p: nombre.lower() in p.nombre.lower()) 
        return self 
    
    def filtrar_por_precio_min(self, precio_min): 
        self.criterios.append(lambda p: p.precio >= precio_min) 
        return self 
    
    def filtrar_por_precio_max(self, precio_max): 
        self.criterios.append(lambda p: p.precio <= precio_max) 
        return self 
    
    def filtrar_por_cantidad_min(self, cantidad_min): 
        self.criterios.append(lambda p: p.cantidad >= cantidad_min) 
        return self 
    
    def ejecutar(self): 
        productos = self.cargar_productos() 
        for criterio in self.criterios: 
            productos = filter(criterio, productos) 
            return list(productos)