from interfaces.notificador import Notificador 
class NotificadorSMS(Notificador): 
    def enviar(self, mensaje: str, destinatario: str) -> None: 
        print(f"Enviando SMS a {destinatario}: {mensaje}")