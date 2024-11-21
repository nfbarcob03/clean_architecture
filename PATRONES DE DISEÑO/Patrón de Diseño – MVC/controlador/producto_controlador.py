from modelo.producto_modelo import Producto, ProductoModelo 
from vista.producto_vista import ProductoVista 

class ProductoControlador: 
    def __init__(self, modelo: ProductoModelo, vista: ProductoVista): 
        self.modelo = modelo 
        self.vista = vista 
    
    def agregar_producto(self, id_producto: int, nombre: str, precio: float, cantidad: int): 
        producto = Producto(id_producto, nombre, precio, cantidad) 
        self.modelo.agregar_producto(producto) 
        self.vista.mostrar_mensaje(f"Producto '{nombre}' agregado exitosamente.") 
        
    def mostrar_productos(self): 
        productos = self.modelo.obtener_productos() 
        self.vista.mostrar_productos(productos) 
    
    def mostrar_detalle_producto(self, id_producto: int): 
        producto = self.modelo.obtener_producto_por_id(id_producto) 
        self.vista.mostrar_detalle_producto(producto) 
        
    def eliminar_producto(self, id_producto: int): 
        producto = self.modelo.obtener_producto_por_id(id_producto) 
        if producto: 
            self.modelo.eliminar_producto(id_producto) 
            self.vista.mostrar_mensaje(f"Producto '{producto.nombre}' eliminado exitosamente.") 
        else: 
            self.vista.mostrar_mensaje("Producto no encontrado.")
