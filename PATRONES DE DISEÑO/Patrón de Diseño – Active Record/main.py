from producto import Producto 
def ejemplo_uso(): 
    # Crear y guardar un nuevo producto 
    producto1 = Producto(id_producto=1, nombre="Laptop",precio=1200.00, cantidad=10) 
    producto1.guardar() 
    print("Producto agregado:", producto1) 
    # Crear y guardar otro producto 
    producto2 = Producto(id_producto=2, nombre="Mouse", precio=25.50, cantidad=50) 
    producto2.guardar() 
    print("Producto agregado:", producto2) 
    # Obtener todos los productos 
    productos = Producto.todos() 
    print("\nLista de todos los productos:") 
    for producto in productos: 
        print(producto) 
    # Actualizar un producto existente 
    producto1.precio = 1150.00 
    producto1.cantidad = 8 
    producto1.actualizar() 
    print("\nProducto actualizado:", producto1) 
    # Encontrar un producto por ID 
    producto_encontrado = Producto.encontrar_por_id(1) 
    if producto_encontrado: 
        print("\nProducto encontrado por ID:", producto_encontrado) 
    # Eliminar un producto 
    producto2.eliminar() 
    print("\nProducto con ID 2 eliminado.") 
    # Obtener todos los productos despus de la eliminacin 
    productos = Producto.todos() 
    print("\nLista de todos los productos despus de la eliminacin:") 
    for producto in productos: 
        print(producto) 
if __name__ == "__main__": 
    ejemplo_uso()