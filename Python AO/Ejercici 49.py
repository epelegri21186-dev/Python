def hi_ha_duplicats(llista, conjunt):
    if len(llista)==len(conjunt):
        print(f'No hi ha cap repetit en la llista {llista}')
    else:
        print(f'Hi ha caracters repetits en la llista {llista}')


llista=[1,2,3,4,5,7,8,6]
conjunt=set(llista)
llista2=[1,2,2,4,5,7,8]
conjunt2=set(llista2)
hi_ha_duplicats(llista, conjunt)
hi_ha_duplicats(llista2, conjunt2)