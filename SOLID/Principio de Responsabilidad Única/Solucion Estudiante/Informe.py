from Empleado import Empleado
class InformeEmpleado: 
    def generarInformeEmpleado(empleado:Empleado):
        return f"Informe del Empleado: {empleado.obtener_detalles()}"
