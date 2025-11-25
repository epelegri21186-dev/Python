def es_palindrom(parula):
    parula=list(a)
    b= parula.copy()
    parula.reverse()
    if parula==b:
        print('TRUE')
    else:
        print('FALSE')

# Programa principal
paraula =0
a=input('introdureix una parula: ')
es_palindrom(paraula)