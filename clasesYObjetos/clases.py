class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Nombre:{self.nombre}\nEdad:{self.edad}'

Edied = Persona('Edied', 22)
print(Edied)