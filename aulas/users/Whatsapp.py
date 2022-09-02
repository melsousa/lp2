from Enviar import Enviar
from Usuario import Usuario

class Whatsapp(Enviar):
    
    def execute(self, Usuario):
        print('Whastapp enviado com sucesso')
        print('Usuário', Usuario.username)