from Empleado import Empleado 
class FormatoInformeEmpleado: 
    @staticmethod 
    def formatear(empleado: Empleado): 
        return f"Informe del Empleado: {empleado.obtener_detalles()}"