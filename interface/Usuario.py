class Usuario ():
    def __init__(self, username, email, telefone):
        self.username = username
        self.email = email
        self.telefone = telefone
        
        self.validation()
        
    @staticmethod
    def Usuario(username, email, telefone):
        return Usuario(username, email, telefone)   
    
    def validation(self):
        
        if self.username is None or not self.username:
            raise Exception('Nome é Obrigatório')
        
        if self.email is None or not self.email:
            raise Exception('Email é obrigatório')
        
        if self.telefone is None or not self.telefone:
            raise Exception('Telefone é obrigatório')

    def username(self):
        return self.username

    def email(self):
        return self.email

    def telefone(self):
        return self.telefone
