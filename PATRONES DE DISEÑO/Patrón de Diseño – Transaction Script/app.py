from dominio.cuenta import Cuenta 
from dominio.transacciones import realizar_deposito, realizar_retiro, realizar_transferencia, Transaccion 
def main(): 
    # Crear cuentas 
    cuenta_1 = Cuenta("123456789", "Rodrigo Silva", 5000) 
    cuenta_2 = Cuenta("987654321", "Maria Lopez", 3000) 
    # Crear transaccin 
    transaccion = Transaccion() 
    # Realizar transacciones 
    realizar_deposito(cuenta_1, 1000, transaccion) 
    realizar_retiro(cuenta_2, 500, transaccion) 
    realizar_transferencia(cuenta_1, cuenta_2, 1500, transaccion) 
    # Confirmar la transaccin 
    transaccion.commit() 
if __name__ == "__main__": main()