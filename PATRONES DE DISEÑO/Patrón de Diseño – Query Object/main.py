from query.producto_query import ProductoQuery 
from entidad.producto import Producto 
import json 
def ejemplo_uso_query(): 
    # Crear algunos productos para trabajar con ellos 
    productos = [ Producto(id_producto=1, nombre="Laptop", precio=1200.00, cantidad=10), 
                 Producto(id_producto=2, nombre="Mouse", precio=25.50, cantidad=50), 
                 Producto(id_producto=3, nombre="Teclado", precio=45.00, cantidad=30), 
                 Producto(id_producto=4, nombre="Monitor", precio=300.00, cantidad=20), 
                 Producto(id_producto=5, nombre="Cargador", precio=15.00, cantidad=100) ] 
    
    # Guardar los productos en el archivo JSON 
    with open('productos.json', 'w') as file:
        productos_dict = [producto.to_dict() for producto in productos] 
        json.dump(productos_dict, file, indent=4) 
        # Crear una instancia de ProductoQuery 
        query = ProductoQuery() 
        # Realizar consultas dinmicas 
        print("Productos con nombre que contiene 'Lap':") 
        productos_filtrados = query.filtrar_por_nombre('Lap').ejecutar() 
        for producto in productos_filtrados: 
            print(producto) 

        print("\nProductos con precio mnimo de 50:") 
        productos_filtrados = query.filtrar_por_precio_min(50).ejecutar() 
        for producto in productos_filtrados: 
            print(producto) 

        print("\nProductos con precio mximo de 50:") 
        productos_filtrados = query.filtrar_por_precio_max(50).ejecutar() 
        for producto in productos_filtrados: 
            print(producto) 
        
        print("\nProductos con cantidad mnima de 20:") 
        productos_filtrados = query.filtrar_por_cantidad_min(20).ejecutar() 
        for producto in productos_filtrados: 
            print(producto) 
        
        print("\nProductos que contienen 'Cargador' en el nombre y precio menor o igual a 50:") 
        productos_filtrados = query.filtrar_por_nombre('Cargador').filtrar_por_precio_max(50).ejecutar() 
        for producto in productos_filtrados: 
            print(producto) 
            
if __name__ == "__main__":
    ejemplo_uso_query()