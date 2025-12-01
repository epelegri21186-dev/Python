
any_actual = int(input("Introdueix l'any actual: "))

noms = []
anys_naixement = []
edats = []

print("\nIntrodueix les dades de 4 persones:")
for i in range(4):
    print("\nPersona {}:".format(i+1))
    nom = input("  Nom: ")
    any_naixement = int(input("  Any de naixement: "))
    
    edat = any_actual - any_naixement
    
    noms.append(nom)
    anys_naixement.append(any_naixement)
    edats.append(edat)

print("\n")
print("Any actual: {}".format(any_actual))

print(f"{'Nom':<20} {'Data naixement':<20} {'Anys que farà':<15}")


for i in range(4):
    print(f"{noms[i]:<20} {anys_naixement[i]:<20} {edats[i]:<15}")

