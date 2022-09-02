from abc import ABC, abstractmethod

class Enviar(ABC):
    
    @abstractmethod
    def execute(self, Usuario):
        pass