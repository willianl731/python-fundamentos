def validar_contrasena(contrasena):
    # Asumimos que no es válida hasta que demostremos lo contrario
    tiene_longitud_suficiente = False
    tiene_numero = False
    tiene_mayuscula = False

    # 1. Comprueba la longitud
    if len(contrasena) >= 8:
        tiene_longitud_suficiente = True
    
    # 2. Recorremos la contrasena en busqueda de numeros y mayusculas
    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True

        if caracter.isupper():
            tiene_mayuscula = True

     # 3. Usa 'and' para asegurarte de que todas las condiciones son verdaderas
    if tiene_longitud_suficiente and tiene_numero and tiene_mayuscula:
        return True
    else:
        return False
    
# --- Casos de prueba ---
# Este bloque solo se ejecuta cuando corres el archivo directamente
if __name__ == "__main__":
    print("Ejecutando pruebas para validar_contrasena...")
    # Casos que deberían ser True
    assert validar_contrasena("ClaveSegura1") == True
    assert validar_contrasena("M1contrasena") == True
    # Casos que deberían ser False
    assert validar_contrasena("clave") == False         # Muy corta
    assert validar_contrasena("clavesegura") == False   # Sin número ni mayúscula
    assert validar_contrasena("Clavesegura") == False   # Sin número
    assert validar_contrasena("clavesegura1") == False  # Sin mayúscula
    print("✅ Todas las pruebas de contraseña pasaron.")

def categorizar_por_edad(edad):
    if edad < 0:
        return "Edad inválida"
    elif edad <= 12:
        return "Niño"
    elif edad <= 19:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:  # Si no es ninguna de las anteriores, por descarte es >= 65
        return "Adulto Mayor"
    
print("\nEjecutando pruebas para categorizar_por_edad...")
# Casos de prueba para cada categoría
assert categorizar_por_edad(-1) == "Edad inválida"
assert categorizar_por_edad(5) == "Niño"
assert categorizar_por_edad(12) == "Niño"
assert categorizar_por_edad(13) == "Adolescente"
assert categorizar_por_edad(19) == "Adolescente"
assert categorizar_por_edad(25) == "Adulto"
assert categorizar_por_edad(64) == "Adulto"
assert categorizar_por_edad(65) == "Adulto Mayor"
assert categorizar_por_edad(100) == "Adulto Mayor"
print("✅ Todas las pruebas de edad pasaron.")


    
