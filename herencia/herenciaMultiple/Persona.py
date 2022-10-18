class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'


if __name__ == '__main__':
    instancia = Persona('Edied', 22)
    print(instancia.nombre)
    print(instancia.edad)