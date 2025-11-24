def ex18():
    v= 'aeiouáéíóúàèìòùÁÉÍÓÚÀÈÌÒÙAEIOU'
    if c in v:
        return True
    else:
        return False

c=input('Escri vocal: ')
print(ex18(c))
