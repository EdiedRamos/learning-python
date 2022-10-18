from Persona import Persona
from Empleado import Empleado

class Celador(Persona, Empleado):
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, salario)
    
    def __str__(self):
        return f'{Persona.__str__(self)}{Empleado.__str__(self)}'

if __name__ == '__main__':
    instancia = Celador('Antonio', 45, 1000)
    print(instancia)
    # print(Celador.mro())