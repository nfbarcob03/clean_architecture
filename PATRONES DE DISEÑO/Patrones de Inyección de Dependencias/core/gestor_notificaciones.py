from interfaces.notificador import Notificador 
class GestorNotificaciones: 
    def __init__(self, notificador: Notificador): 
        self.notificador = notificador 
    def notificar(self, mensaje: str, destinatario: str) -> None: 
        self.notificador.enviar(mensaje, destinatario)