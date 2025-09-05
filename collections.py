def contar_palabras(texto):
    # Paso 1: Preparar el texto.
    # Convertimos todo a minúsculas y lo dividimos en una lista de palabras.
    palabras = texto.lower().split()
    
    # Paso 2: Crear un diccionario vacío para usar como contador.
    frecuencias = {}
    
    # Paso 3: Recorrer cada palabra en la lista 'palabras'
    for palabra in palabras:
        # Paso 4: Comprobar si la palabra ya es una clave en el diccionario.
        if palabra in frecuencias:
            # Si ya existe, incrementamos su valor (el contador) en 1.
            frecuencias[palabra] += 1
        else:
            # Si no existe, la añadimos al diccionario con un valor de 1.
            frecuencias[palabra] = 1
            
    # Paso 5: Devolver el diccionario con todas las cuentas.
    return frecuencias

# --- Ejemplo de uso con el assert ---
texto_ejemplo = "hola mundo hola"
conteo_ejemplo = contar_palabras(texto_ejemplo)

# Al ejecutar esto, el assert comprobará que el resultado es el esperado.
assert conteo_ejemplo["hola"] == 2
assert conteo_ejemplo["mundo"] == 1

print("¡La función contar_palabras funciona correctamente!")
print(f"El resultado para '{texto_ejemplo}' es: {conteo_ejemplo}")

# eliminar duplicados
print("\n---eliminar duplicados---")
def eliminar_duplicados(lista_original):
    # 1. Preparamos el material
    elementos_vistos = set()   # Nuestra "hoja de papel" para recordar (rápido)
    lista_resultado = []       # La "nueva fila" que mantendrá el orden (lento)

    # 2. Procesamos elemento por elemento de la lista original
    for elemento in lista_original:
        # 3. Pregunta clave: ¿Hemos visto este elemento antes?
        # La búsqueda en un set es casi instantánea (O(1))
        if elemento not in elementos_vistos:
            # 4. Acción: Si es nuevo, lo anotamos y lo añadimos a la fila
            elementos_vistos.add(elemento)    # Anotamos en nuestra "hoja"
            lista_resultado.append(elemento)  # Lo ponemos en la "nueva fila"
    
    # 5. Devolvemos la nueva lista, que no tiene duplicados y mantiene el orden
    return lista_resultado

# --- Ejemplo de uso ---
mi_lista = [1, 2, 3, 2, 4, 1, 5]
resultado_final = eliminar_duplicados(mi_lista)
print(f"La lista original era: {mi_lista}")
print(f"La lista sin duplicados es: {resultado_final}") # -> [1, 2, 3, 4, 5]

# fusionar diccionarios
print("\n---fusionar diccionarios---")
def fusionar_diccionarios(dict1, dict2):
    # 1. Empezar con una copia del primer diccionario.
    #    Esto ya pone todas las claves y valores de dict1 en nuestro resultado.
    dict_final = dict1.copy()

    # 2. Recorrer el segundo diccionario obteniendo la clave y el valor.
    #    ¡La magia de .items()!
    for clave, valor in dict2.items():
        # 3. Añadir o sobrescribir en el diccionario final.
        #    Esta simple línea añade la clave si es nueva,
        #    o actualiza el valor si la clave ya existía.
        dict_final[clave] = valor

    # 4. Devolver el resultado.
    return dict_final

# --- Ejemplo de uso ---
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
resultado = fusionar_diccionarios(d1, d2)
print(f"La fusión de {d1} y {d2} es: {resultado}")
# El resultado esperado es: {'a': 1, 'b': 3, 'c': 4}