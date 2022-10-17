def saludar(nombre):
    # return 'Hola {}'.format(nombre)
    return f'Hola {nombre}'
# print(saludar('Edied'))

# valores por defualt
def saludar2(nombre='Isaías'):
    return f'Hola {nombre}'
# print(saludar2())

# definición completa
def suma(numero1: int = 0, numero2: int = 0) -> int:
    return numero1 + numero2
# print(suma(5,5))
# print(suma())

# argumentos variables
def mayor(*numeros):
    result = numeros[0]
    for i in numeros:
        if i > result:
            result = i
    return result
# print(mayor(200,1,2,3,4,5))

# argumentso variables diccionario
def diccionario(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')
# diccionario(PK='Primary Key', ER='Edied Ramos')

# funciones recursivas
def decrementar(tope):
    if (tope == 0): return
    print(tope)
    decrementar(tope-1)
decrementar(5)