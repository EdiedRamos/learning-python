"""
Imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir:
3
2
1

Si se pasan valores negativos no imprime nada
"""

def imprimir(numero):
    if numero < 1: return
    print(numero)
    imprimir(numero-1)
# imprimir(5)
# imprimir(3)
# imprimir(-3)
# imprimir(0)