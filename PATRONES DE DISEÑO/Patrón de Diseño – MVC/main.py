from modelo.producto_modelo import ProductoModelo 
from vista.producto_vista import ProductoVista 
from controlador.producto_controlador import ProductoControlador 

def ejemplo_uso_mvc(): 
    modelo = ProductoModelo() 
    vista = ProductoVista() 
    controlador = ProductoControlador(modelo, vista) 
    # Agregar productos 
    controlador.agregar_producto(1, "Laptop", 1200.00, 10) 
    controlador.agregar_producto(2, "Mouse", 25.50, 50) 
    controlador.agregar_producto(3, "Teclado", 45.00, 30) 
    # Mostrar todos los productos 
    controlador.mostrar_productos()
    # Mostrar detalles de un producto especfico
    controlador.mostrar_detalle_producto(2) 
    # Eliminar un producto 
    controlador.eliminar_producto(3) 
    # Mostrar todos los productos despus de la eliminacin 
    controlador.mostrar_productos() 
    
if __name__ == "__main__":
    ejemplo_uso_mvc()