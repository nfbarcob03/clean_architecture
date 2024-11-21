from gateway.producto_gateway import ProductoGateway 
from entidad.producto import Producto 

def mostrar_menu(): 
    print("\nGestin de Productos") 
    print("1. Agregar Producto") 
    print("2. Listar Productos") 
    print("3. Actualizar Stock de Producto") 
    print("4. Eliminar Producto") 
    print("5. Salir") 
    return input("Selecciona una opcin: ") 

def main(): 
    gateway = ProductoGateway() 
    while True: 
        opcion = mostrar_menu()
        if opcion == "1": 
            nombre = input("Nombre del producto: ") 
            precio = float(input("Precio del producto: ")) 
            cantidad = int(input("Cantidad en stock: ")) 
            id_producto = gateway.obtener_todos_los_productos()[-1].id_producto + 1 if gateway.obtener_todos_los_productos() else 1 
            producto = Producto(id_producto, nombre, precio, cantidad) 
            gateway.agregar_producto(producto) 
            print(f"Producto agregado: {producto}") 
        elif opcion == "2": 
            productos = gateway.obtener_todos_los_productos() 
            if productos: 
                for producto in productos: 
                    print(producto) 
            else: 
                print("No hay productos registrados.") 
        elif opcion == "3": 
            id_producto = input("ID del producto a actualizar: ") 
            if id_producto.isdigit(): 
                producto = gateway.obtener_producto_por_id(int(id_producto)) 
                if producto: 
                    nueva_cantidad = int(input("Nueva cantidad en stock: ")) 
                    producto.actualizar_stock(nueva_cantidad) 
                    gateway.actualizar_producto(producto)
                    print(f"Producto actualizado: {producto}") 
                else: print("Producto no encontrado.") 
            else: print("Por favor, ingresa un nmero vlido para el ID del producto.") 
        elif opcion == "4": 
            id_producto = input("ID del producto a eliminar: ") 
            if id_producto.isdigit(): 
                if gateway.eliminar_producto(int(id_producto)): 
                    print(f"Producto con ID {id_producto} eliminado.") 
                else: print("Producto no encontrado.") 
            else: print("Por favor, ingresa un nmero vlido para el ID del producto.") 
        elif opcion == "5": 
            print("Saliendo...") 
            break
        else: 
            print("Opcin no vlida. Intntalo de nuevo.") 
            
if __name__ == "__main__": 
    main()