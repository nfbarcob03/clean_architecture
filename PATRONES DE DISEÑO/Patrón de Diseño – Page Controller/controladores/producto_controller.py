from flask import render_template, request 
from modelo.producto_modelo import ProductoModelo, Producto 

class ProductoController: 
    def __init__(self): 
        self.modelo = ProductoModelo() 
        self._cargar_datos_iniciales() 
        
    def _cargar_datos_iniciales(self): 
        # Agregar algunos productos iniciales 
        self.modelo.agregar_producto(Producto(1, "Laptop", 1200.00, 10)) 
        self.modelo.agregar_producto(Producto(2, "Mouse", 25.50, 50)) 
        self.modelo.agregar_producto(Producto(3, "Teclado", 45.00, 30)) 
        
    def lista_productos(self): 
        productos = self.modelo.obtener_productos() 
        return render_template('lista_productos.html', productos=productos) 
    
    def detalle_producto(self, id_producto): 
        producto = self.modelo.obtener_producto_por_id(id_producto) 
        
        if producto: 
            return render_template('detalle_producto.html', producto=producto) 
        else: 
            return "Producto no encontrado", 404