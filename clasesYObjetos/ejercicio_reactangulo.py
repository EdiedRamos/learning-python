class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def obtenerArea(self):
        return self.base * self.altura

base = input('Ingrese la base: ')
altura = input('Ingrese la altura: ')

rectangulo = Rectangulo(int(base), int(altura))
print(f'El área es {rectangulo.obtenerArea()}')