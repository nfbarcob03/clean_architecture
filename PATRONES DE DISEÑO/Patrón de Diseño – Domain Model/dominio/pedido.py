from datetime import datetime 
from dominio.cliente import Cliente 
from dominio.producto import Producto 

class Pedido: 
    def __init__(self, id_pedido: int, cliente: Cliente): 
        self.id_pedido = id_pedido 
        self.cliente = cliente 
        self.productos = [] 
        self.fecha_pedido = datetime.now() 
        self.estado = "Pendiente" 
        
    def __repr__(self): 
        return f"Pedido({self.id_pedido}, Cliente: {self.cliente.nombre}, Estado: {self.estado})" 
    
    def agregar_producto(self, producto: Producto, cantidad: int): 
        if producto.stock < cantidad: 
            raise ValueError("Stock insuficiente para el producto solicitado.") 
        producto.ajustar_stock(-cantidad) 
        self.productos.append((producto, cantidad)) 
    
    def calcular_total(self): 
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos) 
        return total 
    
    def confirmar_pedido(self): 
        if not self.productos: 
            raise ValueError("No se puede confirmar un pedido sin productos.") 
        self.estado = "Confirmado"