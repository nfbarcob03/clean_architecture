class Empleado: 
    def __init__(self, nombre: str, puesto: str, salario: float): 
        self.nombre = nombre 
        self.puesto = puesto 
        self.salario = salario 
    def obtener_detalles(self): return f"{self.nombre}, {self.puesto}, Salario: {self.salario}"