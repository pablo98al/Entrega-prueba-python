# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(cadena):
    frecuencias = {}

    for caracter in cadena:  # Para cada caracter en cadena
        if caracter != " ":  # si no esta vacio
            if caracter in frecuencias:  # si el caracter está en diccionario frecuencias
                frecuencias[caracter] += 1  # si esta añade 1
            else:
                # si no el conteo permanece como está
                frecuencias[caracter] = 1

    return frecuencias  # devuelve el diccionario con las frecuencias de cada letra


texto = "Hola que tal, ¿Te gustaría tomar algo?"
resultado = frecuencias_letras(texto)
print(resultado)


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función  map()

lista_numeros = [1, 5, 6, 4, 3]

nueva_lista = list(map(lambda x: x*2, lista_numeros))
print(nueva_lista)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan
# la palabra objetivo.


def buscar_palabras(lista_palabras, palabra_objetivo):
    resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            # si la palabra objetivo esta en la lista se se añade a la lista de resultado
            resultado.append(palabra)

    return resultado


palabras = ['ordenador', 'partido', 'teclado',
            'ventana', 'venta', 'partidario', 'partidesco']
objetivos = 'partid'

print(buscar_palabras(palabras, objetivos))

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función  map()


def diferencia_listas(lista1, lista2):
    # map para aplicar función para cada elemento de la lista, y lambda para indicar resta
    return list(map(lambda x, y: x - y, lista1, lista2))


lista_a = [10, 20, 30, 40]
lista_b = [1, 2, 3, 4]

resultado = diferencia_listas(lista_a, lista_b)
print(resultado)

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.


def evaluar_notas(lista_numeros, nota_aprobado=5):
    media = sum(lista_numeros) / len(lista_numeros)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)


notas = [7, 8, 3, 1, 6.5]

resultado = evaluar_notas(notas)
print(resultado)
