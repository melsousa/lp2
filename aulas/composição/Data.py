from Subject import Subject


class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)  # Construtor
        self.name = name
        self._data = 0

    @property  # decorator
    def data(self):
        return self._data

    @data.setter  # adicionar novas funções a função
    def data(self, value):
        self._data = value
        self.notify()
