oracion = input ("Escribe tu Oracion: ")

lista_de_palabras = oracion.split
print("Lista de Palabras: ", lista_de_palabras)

print("\nPalabras en MAYUSCULAS: ")
for palabra in lista_de_palabras:
    print(palabra.upper()) 

    buscar = input("\n¿Qué palabra quieres contar en la Oracion?: ")
cantidad = palabra.count(buscar)
print(f"La palabra '{buscar}' aparece {cantidad} veces.")

reemplazar = input("\n¿Qué palabra quieres reemplazar?: ")
nueva = input("¿Por cuál palabra la quieres reemplazar?: ")
frase_modificada = palabra.replace(reemplazar, nueva)
print("Frase modificada:", frase_modificada)