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