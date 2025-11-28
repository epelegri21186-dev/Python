def ex18(c):
    v= 'aeiouáéíóúàèòÁÉÍÓÚÀÈÒAEIOU'
    if c in v:
        return True
    else:
        return False

c=input('Escri vocal: ')
print(ex18(c))
