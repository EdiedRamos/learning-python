class Persona():
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # utilizando un decorador
    @property
    def nombre(self):
        return self._nombre
    
    # utilizando un decorador
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f'Nombre:{self._nombre}\nApellido:{self.apellido}\nEdad:{self.edad}'

if __name__ == '__main__':

    Edied = Persona('Edied', 'Ramos', 22)
    print(Edied)

    print(Edied.nombre)

    # imprimir el nombre del módulo
    print(__name__)