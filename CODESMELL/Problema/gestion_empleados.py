class Empleado: 
    def __init__(self, nombre, salario): 
        self.nombre = nombre 
        self.salario = salario
        self.bonus = 0 
        
    def calcular_salario(self): 
        if "gerente" in self.nombre.lower(): 
            self.bonus = self.salario * 0.20 
        elif "director" in self.nombre.lower(): 
            self.bonus = self.salario * 0.30 
        else: 
            self.bonus = self.salario * 0.10 
        return self.salario + self.bonus 
    
    def imprimir_detalles_empleado(self): 
        print(f"Empleado: {self.nombre}, Salario: {self.salario}, Bonus: {self.bonus}") 
        
    def guardar_en_base_de_datos(self): 
        # Simulacin de guardar en base de datos 
        print(f"Guardando {self.nombre} en la base de datos.") 
        # Cdigo ejecutable para probar la clase 
        # 
if __name__ == "__main__": 
    empleado = Empleado("Gerente de Ventas", 5000) 
    empleado.calcular_salario() 
    empleado.imprimir_detalles_empleado() 
    empleado.guardar_en_base_de_datos()