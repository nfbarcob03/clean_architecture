from interfaces.notificador import Notificador
class NotificadorPush(Notificador):
    def enviar(self, mensaje: str, destinatario: str) -> None: 
        print(f"Enviando Notificacin Push a {destinatario}: {mensaje}")