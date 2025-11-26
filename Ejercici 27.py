def paraula_mes_llarga(llista):
    llarga=llista[0]
    for paraula in llista:
        if len(paraula) > len(llarga):
            llarga = paraula

    return llarga

print(paraula_mes_llarga(['papa', 'holas', 'lo']))