class Empleado: 
    def __init__(self, nombre, salario, rol): 
        self.nombre = nombre 
        self.salario = salario 
        self.rol = rol 
        
    def calcular_bonus(self): 
        return self.rol.calcular_bonus(self.salario) 
    
    def obtener_salario_total(self): 
        return self.salario + self.calcular_bonus() 
    
    def __repr__(self): 
        return f"Empleado({self.nombre}, {self.salario}, {self.rol})"