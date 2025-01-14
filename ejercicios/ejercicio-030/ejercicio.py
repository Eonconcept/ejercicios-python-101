"""
La siguiente funcion busca contar cuantas veces se repite cada palabra.
Por ejemplo de "Hola Juan. Hola Pedro" devuelve {"Hola": 2, "Juan.": 1, "Pedro": 1}
Tarea: Corregir el error de la función para que devuelva el resultado correcto
"""


def contar_palabras(frase):
    """ 
    Esta funcion toma una frase y devuelve un diccionario
    con una llave por cada palabra y un valor igual a la
    cantidad de veces que aparece en la frase
    """
    palabras = frase.split()
    resultados = {}
    for palabra in palabras:
        if palabra in resultados.keys():
            # si existe, sumarle 1
            resultados[palabra] += 1
        else:
            # si no existe, inicializarla
            resultados[palabra] = 0
    return resultados


# NO BORRAR LASLINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' crear un PR

f1 = contar_palabras("Hola dijo Juan. Hola dijo pedro")
assert f1['Hola'] == 2, f"La función devolvió {f1['Hola']} y esperamos 2"

print('Ejercicio terminado OK')