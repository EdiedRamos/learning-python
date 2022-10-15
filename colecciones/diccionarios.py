contadores = {
    'primero': 0,
    'segundo': 5,
    'tercero': 10
}

# obtener el tamaño del diccionario
# print(len(contadores))

# obtener el contenido en un diccionario
# print(contadores['tercero']) # Si no existe arroja un error
# print(contadores.get('segundo')) # Si no existe NO arroja un error

# cambiar el contenido
# contadores['primero'] += 10
# print(contadores)

# obtener el par (llave, valor) del diccionario
# print(contadores.items())

# obtener las llaves del diccionario
# print(contadores.keys())

# obtener los valores del diccionario
# print(contadores.values())

contadores['cuarto'] = 20
# contadores['cuarto'] = 50
# print(contadores)

# limpiar el diccionario
# contadores.clear()
# print(contadores)

# eliminar un elemento del diccionario por su key
contadores.pop('cuarto')
print(contadores)