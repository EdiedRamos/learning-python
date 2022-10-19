from abc import ABC, abstractmethod

class ClaseAbstracta(ABC):
    def __init__(self, valor):
        self._valor = valor;
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    
    @abstractmethod
    def requerido(self):
        pass
    
    def __str__(self):
        return f'Valor: {self._valor}'