class Empleado:
    def __init__(self, salario):
        self._salario = salario
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    def __str__(self):
        return f'\nSalario: {self.salario}'
    
    
if __name__ == '__main__':
    instancia = Empleado(500000)
    print(instancia.salario)