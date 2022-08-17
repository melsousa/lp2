import abc

class Enviar(abc.ABC):
    
    @abc.abstractmethod
    def execute(self, Usuario):
        pass
