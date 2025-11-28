def filtrar_paraules(llista, x):

    paraules_filtrades = []
    for paraula in llista:
        if len(paraula) > x:
            paraules_filtrades.append(paraula)
    return paraules_filtrades


def paraula_mes_llarga(llista):
   
    if not llista:  
        return None
    
    mes_llarga = llista[0]
    for paraula in llista:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga

print("FILTRAR PARAULES")
paraules = ['IES', 'Joan', 'Ramis', 'i' ,'Ramis', 'don', 'pepito', 'de', 'los', 'palotes']
print("Paraules originals: {}".format(paraules))
print("Paraules amb més de 3 caràcters: {}".format(filtrar_paraules(paraules, 3)))
print("Paraules amb més de 5 caràcters: {}".format(filtrar_paraules(paraules, 5)))
