from tkinter.tix import IMMEDIATE
from Usuario import Usuario
from CadastroUsuario import CadastroUsuario
from Whatsapp import Whatsapp

    
# def main(self):
user = Usuario('MEL', 'melissa@gmail.com', '11 99999-2222')
    
CadastroUsuario().execute(user, Whatsapp())