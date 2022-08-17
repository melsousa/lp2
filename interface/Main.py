from Usuario import Usuario
from CadastroUsuario import CadastroUsuario

class Main():
    def main(self):
        user = Usuario('MEL', 'melissa@gmail.com', '11 99999-2222')
    
        CadastroUsuario().execute(user, Email)