from Empleado import Empleado
from Informe import InformeEmpleado
# Uso
if __name__ == "__main__":
    empleado = Empleado("Rodrigo Silva", "Ingeniero de Software", 90000)
    informe = InformeEmpleado.generarInformeEmpleado(empleado)
    print(informe)


