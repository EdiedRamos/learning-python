"""
Crear una función para multiplar los valores recibidos de tip numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""

def multiplicar(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar(2*6*2))