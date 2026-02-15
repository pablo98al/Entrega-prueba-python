# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

import math
from functools import reduce


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

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva


print(factorial(3))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función  map()


def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: str(tupla), lista_tuplas))


lista = [(1, 2), (3, 4), (5, 6)]

resultado = tuplas_a_strings(lista)
print(resultado)
print(type(resultado))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2

except ValueError:
    print("Error: Debes introducir valores numéricos válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

else:
    print("División exitosa.")
    print("El resultado es:", resultado)

finally:
    print("Programa finalizado.")

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función  filter()


def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre",
                           "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))


mascotas = ["Perro", "Gato", "Mapache", "Loro", "Oso"]

resultado = filtrar_mascotas(mascotas)
print(resultado)


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass


def calcular_promedio(lista_numeros):
    if not lista_numeros:
        raise ListaVaciaError(
            "La lista está vacía, no se puede calcular el promedio.")

    return sum(lista_numeros) / len(lista_numeros)


#  manejo de excepción
try:
    numeros = [4, 6, 8]
    promedio = calcular_promedio(numeros)
    print("El promedio es:", promedio)

except ListaVaciaError as e:
    print("Error:", e)

else:
    print("Cálculo realizado correctamente.")


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones
# adecuadamente.

while True:
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")

    except ValueError as e:
        print("Error:", e)
        # si el valor no esta dentro del intervalo se repite la pregunta
        print("Por favor, introduce una edad válida.\n")

    else:
        print("Edad registrada correctamente:", edad)
        break

    finally:
        print("Intento finalizado.\n")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función  map()


def longitud_palabras(frase):
    palabras = frase.split()  # Separa la frase en palabras
    return list(map(len, palabras))


texto = "Podriamos ir al parque"
resultado = longitud_palabras(texto)
print(resultado)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función  map()


def letras_mayus_minus(caracteres):
    caracteres_unicos = list(dict.fromkeys(c.lower() for c in caracteres))
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))


entrada = "aAbBcCaa"
resultado = letras_mayus_minus(entrada)
print(resultado)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función  filter()


def palabras_con_inicial(lista_palabras, letra):
    # Convertimos la letra a minúscula para que la comparación no sea sensible a mayúsculas
    letra = letra.lower()
    return list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))


palabras = ["Perro", "Gato", "Pájaro", "pez", "Caballo"]
resultado = palabras_con_inicial(palabras, "p")
print(resultado)

# 15. Crea una función  lambda  que  sume 3 a cada número de una lista dada.
lista_numeros = [1, 4, 7, 10]

# Usamos lambda para sumar 3 a cada elemento
resultado = list(map(lambda x: x + 3, lista_numeros))

print(resultado)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función  filter()


def palabras_mas_largas(cadena, n):
    palabras = cadena.split()  # Separa la cadena en palabras
    return list(filter(lambda palabra: len(palabra) > n, palabras))


texto = "Prodiamos salir a tomar algo a la plaza"
resultado = palabras_mas_largas(texto, 8)
print(resultado)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2
# corresponde al número quinientos setenta y dos 572. Usa la función  reduce()


# Función para acumular los dígitos en un número

def acumular(num, d):
    return num * 10 + d


def lista_a_numero(digitos):
    return reduce(acumular, digitos)


# Ejemplo
digitos = [5, 7, 2]
resultado = lista_a_numero(digitos)
print(resultado)


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función  filter()
# Lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Marta", "edad": 19, "calificacion": 92},
    {"nombre": "Jorge", "edad": 21, "calificacion": 85},
]


def es_destacado(estudiante):
    return estudiante["calificacion"] >= 90


# Filtramos usando la función
estudiantes_destacados = list(filter(es_destacado, estudiantes))

print(estudiantes_destacados)

# 19. Crea una función  lambda  que filtre los números impares de una lista dada.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Filtro los números impares
impares = list(filter(lambda x: x % 2 != 0, lista_numeros))

print(impares)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

lista_mixta = [1, "hola", 2, "Python", 3, "ThePower", 4]


def es_entero(x):
    return isinstance(x, int)


solo_enteros = list(filter(es_entero, lista_mixta))
print(solo_enteros)

# 21. Crea una función que calcule el cubo de un número dado mediante una función  lambda


def cubo(x): return x**3


numero = 3
resultado = cubo(numero)
print(resultado)

# 22.Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función  reduce()

numeros = [2, 3, 4, 5]
producto_total = reduce(lambda x, y: x * y, numeros)
print(producto_total)

# 23. Concatena una lista de palabras.Usa la función  reduce()


def concatenar(x, y):
    return x + " " + y


palabras = ["Python", "es", "complicado"]

frase = reduce(concatenar, palabras)
print(frase)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función  reduce()
numeros = [10, 3, 2, 1]


def restar(x, y):
    return x - y


diferencia_total = reduce(restar, numeros)
print(diferencia_total)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.


def contar_caracteres(cadena):
    return len(cadena)


texto = "Hola que tal"
resultado = contar_caracteres(texto)
print(resultado)

# 26. Crea una función  lambda  que calcule el resto de la división entre dos números dados.
# Función lambda que calcula el resto


def resto(a, b): return a % b


resultado = resto(10, 3)
print(resultado)

# 27.Crea una función que calcule el promedio de una lista de números.


def promedio(lista_numeros):
    if not lista_numeros:  # Evitar división por cero
        return 0
    return sum(lista_numeros) / len(lista_numeros)


numeros = [4, 6, 8, 10]
resultado = promedio(numeros)
print(resultado)

# 28.Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


def primer_duplicado(lista):
    vistos = set()  # Para guardar los elementos ya vistos
    for elemento in lista:
        if elemento in vistos:
            return elemento  # Devolvemos el primer duplicado encontrado
        vistos.add(elemento)
    return None  # Si no hay duplicados


numeros = [3, 5, 2, 4, 5, 6, 2]
resultado = primer_duplicado(numeros)
print(resultado)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el
# carácter '#', excepto los últimos cuatro.


def enmascarar(variable):
    cadena = str(variable)  # Convertimos la variable a string
    if len(cadena) <= 4:
        return cadena
    # Enmascaramos todo menos los últimos 4
    return '#' * (len(cadena) - 4) + cadena[-4:]


numero = 1234567890
resultado = enmascarar(numero)
print(resultado)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.


def son_anagramas(palabra1, palabra2):
    # Eliminamos espacios y convertimos a minúsculas para comparar correctamente
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Comparamos si las letras ordenadas son iguales
    return sorted(palabra1) == sorted(palabra2)


print(son_anagramas("Roma", "Amor"))
print(son_anagramas("Python", "typhon"))
print(son_anagramas("Hola", "Adios"))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.
# Definimos una excepción personalizada


class NombreNoEncontradoError(Exception):
    pass


def buscar_nombre():
    # Pedimos la lista de nombres al usuario
    nombres = input(
        "Introduce una lista de nombres separados por comas: ").split(",")
    # Quitamos espacios en blanco al inicio y final de cada nombre
    nombres = [nombre.strip() for nombre in nombres]

    # Pedimos el nombre a buscar
    nombre_buscar = input("Introduce el nombre a buscar: ").strip()

    # Verificamos si está en la lista
    if nombre_buscar in nombres:
        print(f"{nombre_buscar} fue encontrado en la lista.")
    else:
        raise NombreNoEncontradoError(
            f"{nombre_buscar} no se encontró en la lista.")


try:
    buscar_nombre()
except NombreNoEncontradoError as e:
    print("Error:", e)


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí


def buscar_puesto(nombre_completo, empleados):
    """
    nombre_completo: string con el nombre del empleado a buscar
    empleados: lista de diccionarios con la estructura {"nombre": ..., "puesto": ...}
    """
    # Recorremos la lista de empleados
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    # Si no se encuentra
    return f"{nombre_completo} no trabaja aquí."


empleados = [
    {"nombre": "Ana Pérez", "puesto": "Gerente"},
    {"nombre": "Luis Gómez", "puesto": "Analista"},
    {"nombre": "Marta López", "puesto": "Secretaria"},
]

print(buscar_puesto("Luis Gómez", empleados))
print(buscar_puesto("Juan Torres", empleados))

# 33. Crea una función  lambda  que sume elementos correspondientes de dos listas dadas
# Listas de ejemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Sumar elementos correspondientes usando lambda y map
suma_listas = list(map(lambda x, y: x + y, lista1, lista2))

print(suma_listas)

# 34. Crea la clase  Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco ,  nueva_rama ,  crecer_ramas ,  quitar_rama  e  info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.


class Arbol:
    def __init__(self, altura_tronco=1):
        self.tronco = altura_tronco   # Altura del tronco
        self.ramas = []               # Lista de ramas

    # Método para hacer crecer el tronco
    def crecer_tronco(self, incremento=1):
        self.tronco += incremento
        print(
            f"El tronco creció {incremento} unidad(es). Nueva altura: {self.tronco}")

    # Método para agregar una nueva rama
    def nueva_rama(self, nombre_rama):
        self.ramas.append(nombre_rama)
        print(f"Se añadió la rama: {nombre_rama}")

    # Método para hacer crecer todas las ramas (simbolicamente)
    def crecer_ramas(self):
        if not self.ramas:
            print("No hay ramas que crecer.")
        else:
            self.ramas = [rama + " (crecida)" for rama in self.ramas]
            print("Todas las ramas han crecido.")

    # Método para quitar una rama por nombre
    def quitar_rama(self, nombre_rama):
        if nombre_rama in self.ramas:
            self.ramas.remove(nombre_rama)
            print(f"Se quitó la rama: {nombre_rama}")
        else:
            # por si la rama no existe
            print(f"No se encontró la rama: {nombre_rama}")

    # Método para mostrar información del árbol
    def info_arbol(self):
        print(f"Altura del tronco: {self.tronco}")
        print(f"Ramas: {', '.join(self.ramas) if self.ramas else 'Sin ramas'}")


# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
mi_arbol = Arbol(altura_tronco=1)

mi_arbol.info_arbol()  # Mostrar información inicial del árbol

# 2. Implementar el método  crecer_tronco  para aumentar la longitud del tronco en una unidad

mi_arbol.crecer_tronco()  # El tronco ha crecido. Nueva longitud: 2
mi_arbol.info_arbol()     # Altura del tronco: 2

# 3.Implementar el método  nueva_rama  para agregar una nueva rama de longitud 1 a la lista de ramas.
mi_arbol.nueva_rama('Rama1')
mi_arbol.nueva_rama('Rama2')
mi_arbol.info_arbol()

# 4. Implementar el método  crecer_ramas  para aumentar en una unidad la longitud de todas las ramas existentes.
mi_arbol.crecer_ramas()
mi_arbol.info_arbol()

# 5. Implementar el método  quitar_rama  para eliminar una rama en una posición específica.
mi_arbol.quitar_rama('Rama1 (crecida)')
mi_arbol.info_arbol()

# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.
mi_arbol.info_arbol()


# 1. # Crear un árbol
mi_arbol = Arbol()


# 2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()


# 3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama('1')
mi_arbol.nueva_rama('2')


# 4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()


# 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama('3')
mi_arbol.nueva_rama('4')


# 6. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama('2 (crecida)')
mi_arbol.info_arbol()
print(f"Fin ejercicio 35 :)")
# 36. Crea la clase  UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Inicializa un usuario del banco.
        :param nombre: str, nombre del usuario
        :param saldo: float, saldo inicial
        :param cuenta_corriente: bool, True si tiene cuenta corriente, False si no
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Método para retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > self.saldo:
            raise ValueError(
                f"No se puede retirar {cantidad}. Saldo insuficiente.")
        self.saldo -= cantidad
        print(f"{self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}")

    # Método para transferir dinero desde otro usuario a este usuario
    def transferir_dinero(self, usuario_origen, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser mayor que 0.")
        if cantidad > usuario_origen.saldo:
            raise ValueError(
                f"{usuario_origen.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        # Transferencia
        usuario_origen.saldo -= cantidad
        self.saldo += cantidad
        print(f"{usuario_origen.nombre} transfirió {cantidad} a {self.nombre}.")
        print(f"Saldo de {usuario_origen.nombre}: {usuario_origen.saldo}")
        print(f"Saldo de {self.nombre}: {self.saldo}")

    # Método para agregar dinero al saldo
    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que 0.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")


# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# Usuarios
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)

# Saldo
print(f"{usuario1.nombre}: {usuario1.saldo}, Cuenta corriente: {usuario1.cuenta_corriente}")
print(f"{usuario2.nombre}: {usuario2.saldo}, Cuenta corriente: {usuario2.cuenta_corriente}")

# 2.Agregar 20 unidades de saldo de "Bob"
usuario2.agregar_dinero(20)

# 3.Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".

# Intentar transferir 80 unidades desde Bob a Alicia
try:
    usuario1.transferir_dinero(usuario2, 80)
except ValueError as e:
    print("Error:", e)


print(f"Saldo de {usuario1.nombre}: {usuario1.saldo}")
print(f"Saldo de {usuario2.nombre}: {usuario2.saldo}")

# 4.Retirar 50 unidades de saldo a "Alicia".
# Intentar retirar 50 unidades de Alicia

try:
    usuario1.retirar_dinero(50)
except ValueError as e:
    print("Error:", e)

# 37.Crea una función llamada  procesar_texto  que procesa un texto según la opción especificada:  contar_palabras ,
# reemplazar_palabras ,  eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función  procesar_texto .

# contar palabras


def contar_palabras(texto):
    palabras = texto.split()  # Dividir texto en palabras
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()  # Para contar sin distinguir mayúsculas/minúsculas
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# reemplazar_palabras


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# eliminar palabras


def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    # Filtrar todas las palabras distintas de la que queremos eliminar
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)

# procesar texto


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError(
                "La opción 'reemplazar' requiere dos argumentos: palabra_original, palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError(
                "La opción 'eliminar' requiere un argumento: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(
            "Opción no válida. Use 'contar', 'reemplazar' o 'eliminar'.")


texto = "Hola mundo, hola a todos en el mundo de Python"

# Comprueba el funcionamiento completo de la función  procesar_texto
# Contar palabras
print(procesar_texto(texto, "contar"))

# Reemplazar "mundo" por "universo"
print(procesar_texto(texto, "reemplazar", "mundo", "universo"))

# Eliminar la palabra "hola"
print(procesar_texto(texto, "eliminar", "hola"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.


def determinar_momento_del_dia():
    try:
        # Pedir la hora al usuario
        hora = int(input("Introduce la hora (0-23): "))

        # Verificar que la hora esté en el rango correcto
        if hora < 0 or hora > 23:
            print("Error: La hora debe estar entre 0 y 23.")
            return

        # Determinar el momento del día
        if 6 <= hora < 12:
            print("Es de mañana.")
        elif 12 <= hora < 20:
            print("Es de tarde.")
        else:
            print("Es de noche.")

    except ValueError:
        print("Error: Debes introducir un número entero válido para la hora.")


determinar_momento_del_dia()

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.


def calificacion_texto():
    try:
        # Pedir la calificación al usuario
        nota = float(input("Introduce la calificación del alumno (0-100): "))

        # Verificar que la nota esté en el rango correcto
        if nota < 0 or nota > 100:
            print("Error: La calificación debe estar entre 0 y 100.")
            return

        # Determinar la calificación en texto
        if 0 <= nota <= 69:
            texto = "Insuficiente"
        elif 70 <= nota <= 79:
            texto = "Bien"
        elif 80 <= nota <= 89:
            texto = "Muy bien"
        else:  # 90 <= nota <= 100
            texto = "Excelente"

        print(f"La calificación del alumno es: {texto}")

    except ValueError:
        print("Error: Debes introducir un número válido para la calificación.")


# Ejecutar la función
calificacion_texto()

# 40.Escribe una función que tome dos parámetros:  figura  (una cadena que puede ser  "rectangulo" ,  "circulo"  o
# "triangulo" ) y  datos  (una tupla con los datos necesarios para calcular el área de la figura).


def calcular_area(figura, datos):

    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Rectángulo requiere 2 datos: base y altura.")
        base, altura = datos
        return base * altura

    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("Triángulo requiere 2 datos: base y altura.")
        base, altura = datos
        return (base * altura) / 2

    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("Círculo requiere 1 dato: radio.")
        radio = datos[0]
        return math.pi * radio**2

    else:
        raise ValueError(
            "Figura no válida. Debe ser 'rectangulo', 'triangulo' o 'circulo'.")


# Rectángulo de base 5 y altura 10
print("Área del rectángulo:", calcular_area("rectangulo", (5, 10)))

# Triángulo de base 4 y altura 8
print("Área del triángulo:", calcular_area("triangulo", (4, 8)))

# Círculo de radio 3
print("Área del círculo:", calcular_area("circulo", (3,)))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:


def calcular_precio_final():
    try:
        # 1️ Solicitar precio original
        precio_original = float(
            input("Introduce el precio original del artículo: "))
        if precio_original < 0:
            print("Error: El precio no puede ser negativo.")
            return

        # 2️ Preguntar si tiene cupón de descuento
        tiene_cupon = input(
            "¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        # Inicializamos descuento
        descuento = 0

        # 3️ Si tiene cupón, solicitar el valor del cupón
        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(
                input("Introduce el valor del cupón de descuento: "))
            if valor_cupon > 0:
                descuento = valor_cupon
            else:
                print(
                    "El valor del cupón debe ser mayor que 0. No se aplicará descuento.")
        elif tiene_cupon == "no":
            print("No se aplicará ningún descuento.")
        else:
            print("Respuesta no válida. Se asumirá que no hay descuento.")

        # 4️ Calcular precio final
        precio_final = precio_original - descuento
        if precio_final < 0:
            precio_final = 0  # Evitar precio negativo

        # 5️ Mostrar precio final
        print(f"El precio final de la compra es: {precio_final:.2f} €")

    except ValueError:
        print("Error: Debes introducir un número válido.")


# Ejecutar el programa
calcular_precio_final()
