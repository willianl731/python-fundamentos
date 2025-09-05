# Queremos imprimir los números del 1 al 5
# range(1, 6) genera los números desde el 1 hasta JUSTO ANTES del 6
print("Contando del 1 al 5:")
for numero in range(1, 6):
    # Este bloque de código se repetirá por cada número en el rango
    print(f"Número actual: {numero}")

# También podemos recorrer los caracteres de un string
print("\nLetras en la palabra 'hola':")
for letra in "hola":
    print(letra)

# Un contador que se detiene al llegar a 5
contador = 0
while contador < 5:
    print(f"El contador vale {contador}, ¡aún no hemos llegado a 5!")
    # ¡Importante! Modificamos el contador para que la condición eventualmente sea falsa.
    contador = contador + 1  # También se puede escribir como: contador += 1

print(f"\n¡Listo! El contador ahora vale {contador}.")

# Buscamos el número 7 en una lista, pero ignoramos los números impares.
for numero in range(1, 11):  # Números del 1 al 10
    if numero % 2 != 0:  # Si el número no es par...
        continue  # ...saltamos al siguiente número, ignorando el resto del código.
    
    print(f"Revisando el número par: {numero}")
    
    if numero == 8:
        print("¡Encontramos el 8! ¡Salimos del bucle!")
        break # Terminamos el bucle por completo.

print("Fin del bucle.")

print("---Ejercicio 1: suma acumulada---")
#suma acumulada de los numeros de 1 a 10
#iniciamos una variable total en cero, para empezar a contar desde ahi
total = 0
# range(1, 11) crea una secuencia del 1 al 10 (el 11 no se incluye).
for numero in range(1,11):
    total = total + numero
 #imprimimos el resultado de la suma de nemero + acumulado
print(f"la suma total de los numeros es: {total}")

print("\n=== Ejercicio 2: Filtro de Números Pares ===")
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pares = []

for num in numeros:
    #si el numero es par
    if num % 2 != 0:
        continue
    #agregue a la lista de pares
    pares.append (num)

print(f"Lista original: {numeros}")
print(f"Lista de pares: {pares}")

print("\n=== Ejercicio 3: Con Comprensión de Listas ===")
pares_v2 = [num for num in numeros if num % 2 == 0]

print(f"Números pares (con comprensión): {pares_v2}")

# Ejeccio #4: Busqueda con brake

print("\n---Ejercicio #4: Busqueda con Brake---")

lista_de_busqueda = [4, 6, 8, 3, 5, 9, 23, 12, 2, 7]
objetivo = 6
encontrado = False
for numero in lista_de_busqueda:
    print(f"revisando el numero: {numero}")
    if numero == objetivo:
        print("numero encontrado!")
        encontrado = True
        break
if not encontrado:
    print("El numero no esta en la lista!")

# Ejercicio #5: Tabla de multiplicar
print("\n---Ejercicio #5:Tabla de multiplicar---")

numero_de_tabla = 6
# 1. crea una tabla vacia para guardar los resultados
resultado_de_la_tabla = []
print(f"tabla de multiplicar del {numero_de_tabla}:")
for i in range(1, 11): #tabla del 1 al 10
    resultado_actual = numero_de_tabla * i
    # 2. agrega cada resultado a la lista
    resultado_de_la_tabla.append(resultado_actual)
    print(f"{numero_de_tabla} * {i} = {resultado_actual}")

    # --- PRUEBAS CON ASSERT (AGREGA ESTO AL FINAL) ---
print("\n--- Probando con asserts ---")

# Afirmamos que los resultados en las posiciones específicas son correctos.
# Recuerda: la lista 'resultados' empieza en el índice 0.
# resultados[0] es 6x1 = 6
# resultados[4] es 6x5 = 30
# resultados[9] es 6x10 = 60

assert resultado_de_la_tabla[0] == 6, f"Error: 6x1 debería ser 6, pero fue {resultado_de_la_tabla[0]}"
assert resultado_de_la_tabla[4] == 30, f"Error: 6x5 debería ser 30, pero fue {resultado_de_la_tabla[4]}"
assert resultado_de_la_tabla[9] == 60, f"Error: 6x10 debería ser 60, pero fue {resultado_de_la_tabla[9]}"

print("✅ ¡Todas las pruebas pasaron! La tabla del 6 es correcta.")