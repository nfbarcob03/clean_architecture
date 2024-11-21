from dominio.cliente import Cliente 
from dominio.producto import Producto 
from dominio.pedido import Pedido 

def main(): 
    # Crear cliente 
    cliente = Cliente(1, "Rodrigo Silva", "rodrigo@example.com") 
    #Crear productos 
    producto_1 = Producto(1, "Laptop", 1500.00, 10) 
    producto_2 = Producto(2, "Mouse", 25.00, 100) 
    # Crear pedido 
    pedido = Pedido(1, cliente) 
    # Agregar productos al pedido 
    pedido.agregar_producto(producto_1, 1) 
    pedido.agregar_producto(producto_2, 2) 
    # Calcular total del pedido 
    total = pedido.calcular_total() 
    print(f"Total del pedido: {total}") 
    # Confirmar el pedido 
    pedido.confirmar_pedido()
    print(f"Pedido confirmado: {pedido}") 
    
if __name__ == "__main__": 
    main()