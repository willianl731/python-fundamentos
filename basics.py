# 1. Variables y Números
print("--- Calculadora de Área de Rectángulo ---")
ancho = 6
alto = 25

area = ancho * alto

print("El ancho es:", ancho)
print("El alto es:", alto)
print("El área del rectángulo es:", area)
print("-" * 20) # Imprime una línea separadora

# 2. Strings y f-strings
print("--- Generador de Saludos ---")
nombre = "Willian"
profesion = "desarrollador de Python"

# Usando f-string para construir el mensaje
saludo = f"Hola, soy {nombre} y mi objetivo es ser un gran {profesion}."

print(saludo)
print("-" * 20)

# 3. Booleanos y Operadores
print("--- Control de Acceso Sencillo ---")
edad_usuario = 17
edad_minima_requerida = 18

# El operador ">=" comprueba si el valor de la izquierda es mayor o igual que el de la derecha
tiene_acceso = edad_usuario >= edad_minima_requerida

print(f"La edad del usuario es {edad_usuario} años.")
print(f"¿Tiene acceso permitido? {tiene_acceso}")
print("-" * 20)

# 4. Operadores de División
print("--- Repartidor de Porciones ---")
total_rebanadas_pizza = 8
numero_de_amigos = 3

# División entera: cuántas porciones enteras le tocan a cada uno
rebanadas_por_amigo = total_rebanadas_pizza // numero_de_amigos

# Módulo: cuántas porciones sobran después de repartir
rebanadas_sobrantes = total_rebanadas_pizza % numero_de_amigos

print(f"Si hay {total_rebanadas_pizza} rebanadas y {numero_de_amigos} amigos:")
print(f"Cada amigo come {rebanadas_por_amigo} rebanadas.")
print(f"Sobran {rebanadas_sobrantes} rebanadas.")
print("-" * 20)

# 5. Métodos de String
print("--- Procesador de Texto Básico ---")
titulo_noticia = "ÚLTIMA HORA: Un Ciclón Golpea la Costa Oeste"
print(f"Título original: {titulo_noticia}")

# 1. Usamos .lower() para convertir todo el texto a minúsculas.
#    Esto es útil para normalizar el texto y que "Ciclón" y "ciclón" se traten como la misma palabra.
titulo_en_minusculas = titulo_noticia.lower()
print(f"Título en minúsculas: {titulo_en_minusculas}")

# 2. Usamos .split() para dividir el string en una lista de palabras.
#    Por defecto, .split() corta el texto por los espacios.
lista_de_palabras = titulo_en_minusculas.split()
print(f"Palabras en el título: {lista_de_palabras}")

# 3. Usamos f-strings y accedemos a elementos de la lista para crear un resumen.
#    En Python, las listas empiezan en el índice 0.
palabra_clave = lista_de_palabras[4] # La quinta palabra es 'ciclón'
lugar = lista_de_palabras[7]      # La octava palabra es 'costa'

resumen = f"Resumen: La palabra clave del evento es '{palabra_clave}' y ocurrió en la '{lugar}'."
print(resumen)
print("-" * 20)

# 6. Mini-Proyecto: Calculadora de Recibo
print("--- Generador de Recibo de Compra ---")

producto = "Laptop Ultra Pro"
precio = 1200.00
porcentaje_descuento = 20

# Calculamos el descuento y el precio final
descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - descuento
print(precio_final)

# Manipulamos el nombre del producto para crear un ID de transacción
# Convertimos a mayúsculas y reemplazamos espacios con guiones
id_transaccion = producto.upper().replace(" ", "-")

# Formateamos el mensaje final usando un f-string
recibo = f"""
========================================
           RECIBO DE COMPRA
========================================
Producto:       {producto}
ID Transacción: {id_transaccion}
----------------------------------------
Precio Original: ${precio:.2f}
Descuento ({porcentaje_descuento}%):   -${descuento:.2f}
----------------------------------------
TOTAL A PAGAR:  ${precio_final:.2f}
========================================
"""

print(recibo)

# --- Funciones ---

# 1. Suma dos números

def sumar(a, b):
    return a + b
print(5,3)
print(200,350)
print(sumar(5,3))
print(sumar(2489,48948))

def restar(a,b):
    return a - b
print(restar(500,240))

def multiplicar(a,b):
    return a * b
print(multiplicar(8,25))

def dividir(a,b):
    return a / b
print(dividir(64,9))
print(dividir(72,8))

def potencia(base,exponente):
    return base ** exponente
print(potencia(5,3))
print(potencia(7,2))
print(sumar(6,91))
print(restar(25,3))
print(potencia(8,3))
print(sumar(74975,94849))
print(restar(987640,7678))
print(potencia(3,5))

def crear_saludo(nombre):
    return f"hola, {nombre}!"
print(crear_saludo("willian"))

def a_mayusculas(texto):
    return texto.upper()
print(a_mayusculas("hoy es un buen Dia"))
print(a_mayusculas("felicidades"))

def es_par(numero):
    return numero % 2 == 0
print(es_par(676))
print(es_par(690))

def es_mayor(edad):
    return edad >= 18
print(es_mayor(14))
print(es_mayor(74))

def unir_nombre_apellido(nombre,apellido):
    return nombre + "" + apellido
print(unir_nombre_apellido("willian","lucumi"))
print(unir_nombre_apellido("salome","lucumi"))

# --- Tests con asserts ---
# Si alguno de estos 'asserts' falla, el programa se detendrá y mostrará un error.
# Si el programa termina sin errores, significa que todas las funciones pasaron sus tests.

print("\n--- Ejecutando Tests ---")
assert sumar(5, 3) == 8
assert restar(10, 4) == 6
assert multiplicar(3, 4) == 12
assert dividir(10, 2) == 5
assert potencia(2, 3) == 8
assert crear_saludo("Willian") == "hola, Willian!"
assert a_mayusculas("hola") == "HOLA"
assert es_par(10) == True
assert es_par(7) == False
assert es_mayor(20) == True
assert es_mayor(16) == False
assert unir_nombre_apellido("Juan","Perez") == "JuanPerez"

print("✅ ¡Todos los tests pasaron exitosamente!")

    