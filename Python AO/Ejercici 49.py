def hi_ha_duplicats(llista, conjunt):
    if len(llista)==len(conjunt):
        print('No hi ha cap repetit')
    else:
        print('Hi ha caracters repetits')


llista=[1,2,3,4,5,7,8,6]
conjunt=set(llista)
hi_ha_duplicats(llista, conjunt)