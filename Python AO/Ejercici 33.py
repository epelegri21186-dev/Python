def nums_que_comencen_per(llista_noms):
   
    comptador = 0
    for nom in llista_noms:
        if nom and nom[0].lower() == 'a':
            comptador += 1
    return comptador


noms = ["Anna", "Bernat", "Albert", "Carla", "antonio"]
print(nums_que_comencen_per(noms))