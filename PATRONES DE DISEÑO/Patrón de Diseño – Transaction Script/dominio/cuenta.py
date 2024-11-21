class Cuenta: 
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0.0): 
        self.numero_cuenta = numero_cuenta 
        self.titular = titular 
        self.saldo = saldo 
        
    def __repr__(self): 
        return f"Cuenta({self.numero_cuenta}, {self.titular}, Saldo: {self.saldo})" 
    
    def depositar(self, monto: float): 
        if monto > 0: 
            self.saldo += monto 
        else: 
            raise ValueError("El monto a depositar debe ser positivo.") 
        
    def retirar(self, monto: float):
        if monto > self.saldo: 
            raise ValueError("Fondos insuficientes para realizar el retiro.") 
        elif monto <= 0: 
            raise ValueError("El monto a retirar debe ser positivo.") 
        else: self.saldo -= monto