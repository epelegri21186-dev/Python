
numero = input("Introdueix un número: ")

suma = 0
for digit in numero:
    if digit.isdigit(): 
        suma += int(digit)


if suma % 2 == 0:
    resultat = "parell"
else:
    resultat = "impar"

# Mostrar el resultat
print(f"La suma dels dígits de {numero} és {suma}")
print(f"El resultat és {resultat}")