from abc import ABC, abstractmethod 
class Rol(ABC): 
    @abstractmethod 
    def calcular_bonus(self, salario): 
        pass 
    
class Gerente(Rol): 
    def calcular_bonus(self, salario): 
        return salario * 0.20 
    
class Director(Rol): 
    def calcular_bonus(self, salario): 
        return salario * 0.30 
    
class EmpleadoBase(Rol): 
    def calcular_bonus(self, salario): 
        return salario * 0.10