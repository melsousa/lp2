class Subject:
    def __init__(self):
        self._observers = []

    # Se houver uma nova modificação os
    # "observadores receberam" uma notificação
    def notify(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    # Anexar o observador na lista
    def register(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    # Remove os observadores da lista
    def unregister(self, observer):

        try:
            
            self._observers.remove(observer)
            print('observer deleted')
        except ValueError as e:
            print(e)
