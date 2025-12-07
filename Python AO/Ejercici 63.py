def paraules_que_comencen_per_llletra(llista_paraules, lletra):
    return list(filter(lambda paraula: paraula.startswith(lletra), llista_paraules))

llista = ["maria", "panda", "peu", "mà"]
lletra = input("introdueix una lletra: ")
resultat = paraules_que_comencen_per_llletra(llista, lletra)
print(resultat)     