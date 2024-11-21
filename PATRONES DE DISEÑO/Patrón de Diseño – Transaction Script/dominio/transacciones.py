class Transaccion: 
    def __init__(self): 
        self._operaciones = [] 
        self._estado_activo = True 
        
    def agregar_operacion(self, operacion): 
        if self._estado_activo: 
            self._operaciones.append(operacion) 
            
    def commit(self): 
        if self._estado_activo: 
            print("Commit exitoso. Todas las operaciones han sido aplicadas.") 
            self._estado_activo = False 
            self._operaciones.clear() 

    def rollback(self): 
        if self._estado_activo: 
            print("Rollback. Revirtiendo operaciones.") 
            for operacion in reversed(self._operaciones): 
                operacion() 
                self._estado_activo = False 
                self._operaciones.clear() 
    
def realizar_deposito(cuenta, monto, transaccion): 
    try: 
        cuenta.depositar(monto)
        print(f"Depsito de {monto} realizado a la cuenta {cuenta.numero_cuenta}. Nuevo saldo: {cuenta.saldo}") 
        transaccion.agregar_operacion(lambda: cuenta.retirar(monto)) 
    except Exception as e: 
        print(f"Error en depsito: {e}") 
        transaccion.rollback() 
        
def realizar_retiro(cuenta, monto, transaccion): 
    try: 
        cuenta.retirar(monto) 
        print(f"Retiro de {monto} realizado de la cuenta {cuenta.numero_cuenta}. Nuevo saldo: {cuenta.saldo}") 
        transaccion.agregar_operacion(lambda: cuenta.depositar(monto)) 
    except Exception as e: 
        print(f"Error en retiro: {e}") 
        transaccion.rollback() 

def realizar_transferencia(cuenta_origen, cuenta_destino, monto, transaccion): 
    try: 
        realizar_retiro(cuenta_origen, monto, transaccion) 
        realizar_deposito(cuenta_destino, monto, transaccion) 
    except Exception as e: 
        print(f"Error en transferencia: {e}") 
        transaccion.rollback()