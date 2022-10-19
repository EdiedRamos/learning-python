from claseAbstracta import ClaseAbstracta

class ClaseHija(ClaseAbstracta):
    def __init__(self, valor):
        super().__init__(valor)
    
    def requerido(self):
        return 'Esto método está siendo implmentando en esta clase hija'

prueba = ClaseHija('Edied')
print(prueba)