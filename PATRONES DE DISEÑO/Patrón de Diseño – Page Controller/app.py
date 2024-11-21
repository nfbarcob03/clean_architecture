from flask import Flask 
from controladores.producto_controller import ProductoController 

app = Flask(__name__) 
# Crear una instancia del controlador de productos 
producto_controller = ProductoController() 
# Ruta para la lista de productos 
# 
@app.route('/') 
def lista_productos(): 
    return producto_controller.lista_productos() # Ruta para el detalle de un producto especfico

@app.route('/producto/<int:id_producto>') 
def detalle_producto(id_producto): 
    return producto_controller.detalle_producto(id_producto) 

if __name__ == '__main__': app.run(debug=True)