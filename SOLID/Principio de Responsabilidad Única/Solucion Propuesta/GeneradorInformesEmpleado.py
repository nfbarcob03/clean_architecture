from Empleado import Empleado 
from FormatoInforme import FormatoInformeEmpleado 
class GeneradorInformesEmpleado: 
    @staticmethod 
    def generar(empleado: Empleado): 
        return FormatoInformeEmpleado.formatear(empleado) 

# Uso 
if __name__ == "__main__": 
    empleado = Empleado("Rodrigo Silva", "Ingeniero de Software", 90000) 
    informe = GeneradorInformesEmpleado.generar(empleado) 
    print(informe)