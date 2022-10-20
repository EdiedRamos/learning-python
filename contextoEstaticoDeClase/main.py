class Clase:
    variableClase = 'Esta es una variable de clase'
    contador = 0
    
    def __init__(self):
        self.variable = 'Esta es una variable de instancia'
    
    # Decorador para identificar un método estático
    @staticmethod
    def verContador():
        return Clase.contador
    
    # Decorador para identificar un método de clase
    @classmethod
    def verContadorCM(cls):
        print(cls.contador)

Clase.contador += 10

test = Clase()
test2 = Clase()

"""
Al modificar una variable de clase desde una instancia se crea una variable de instancia y no se modifica
la variable de clase
"""
test.contador += 5

Clase.contador += 100

# print(test.contador)
# print(test2.contador)

# Variable creada en tiempo de ejecución
Clase.variableNueva = 'Edied'
# Todas las instancias de "Clase" obtienen acceso a la nueva variable :)
# print(test.variableNueva)
# print(test2.variableNueva)

# print(Clase.verContador())

Clase.verContadorCM()