class ProductoVista: 
    def mostrar_productos(self, productos): 
        if productos: 
            print("\nLista de productos:") 
            for producto in productos: 
                print(producto) 
                
        else: 
            print("\nNo hay productos disponibles.") 
        
    def mostrar_detalle_producto(self, producto): 
        if producto: 
            print(f"\nDetalles del Producto:") 
            print(producto) 
            
        else: 
            print("\nProducto no encontrado.") 
            
    
    def mostrar_mensaje(self, mensaje): 
        print(mensaje)