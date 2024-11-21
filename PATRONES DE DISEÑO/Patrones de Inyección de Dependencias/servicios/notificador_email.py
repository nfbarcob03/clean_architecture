from interfaces.notificador import Notificador 
class NotificadorEmail(Notificador): 
    def enviar(self, mensaje: str, destinatario: str) -> None: 
        print(f"Enviando Email a {destinatario}: {mensaje}")