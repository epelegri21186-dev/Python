def elimina_duplicats(llista):
    return list(set(llista))
# Prova de la funció
llista_original = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print("Llista original:", llista_original)
print("Sense duplicats:", elimina_duplicats(llista_original))

# Amb strings
paraules = ["moix", "ca", "tortuga", "peix", "ca", "peix"]
print("\nParaules originals:", paraules)
print("Sense duplicats:", elimina_duplicats(paraules))

# Amb diferents tipus
mixta = [1, "a", 2, "a", 1, 3, "b"]
print("\nLlista mixta:", mixta)
print("Sense duplicats:", elimina_duplicats(mixta))