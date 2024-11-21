class Empleado: 
    def __init__(self, nombre: str, puesto: str, salario: float): 
        self.nombre = nombre 
        self.puesto = puesto 
        self.salario = salario 
    def obtener_detalles(self): 
            return f"{self.nombre}, {self.puesto}, Salario: {self.salario}" 
    def generar_informe(self): 
            return f"Informe del Empleado: {self.obtener_detalles()}" 
        # Uso 
if __name__ == "__main__": 
    empleado = Empleado("Rodrigo Silva", "Ingeniero de Software", 90000) 
    informe = empleado.generar_informe() 
    print(informe)