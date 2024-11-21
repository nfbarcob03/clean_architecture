from core.gestor_notificaciones import GestorNotificaciones 
from servicios.notificador_email import NotificadorEmail 
from servicios.notificador_sms import NotificadorSMS 
from servicios.notificador_push import NotificadorPush 

def main():
     mensaje = "Tienes un nuevo mensaje" 
     destinatario = "user@example.com" 
     # Se puede elegir cualquier implementacin de Notificador 
     #notificador = NotificadorEmail() 
     #notificador = NotificadorSMS()
     notificador = NotificadorPush() 
     gestor = GestorNotificaciones(notificador) 
     gestor.notificar(mensaje, destinatario) 

if __name__ == "__main__": main()