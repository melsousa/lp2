from Notification import Notification
class CadastroUsuario():
    
    def execute(self, Usuario):
        print('Usuário salvo com sucesso')
        Notification.execute(self,Usuario)