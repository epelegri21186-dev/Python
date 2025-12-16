def contara(): 
    a=0
    for e in nom:
        if e in 'aeiouAEIOUàéèíóòú':
            a=a+1
    if a>=0:
        a='Te vocals'
    else:
        a='No te vocals'
    return a

nom=input()
print("Hola, {}, tens {} caracters que daquestes hi ha {} vocals".format(nom, len(nom), contara()))