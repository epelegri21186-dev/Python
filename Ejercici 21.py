'''Definir una funció es_palindrom() que retorni vertader si li passem 
un palíndrom i fals en cas contrari. Un palíndrom és una paraula 
 que s’escriu igual d’esquerra a dreta i de dreta a esquerra. 
 Per exemple: radar, ara, civic, rallar, tapat, simis, refer'''

def es_palindrom(para):
    para=list(a)
    b= para.copy()
    para.reverse()
    if para==b:
        print('TRUE')
    else:
        print('FALSE')




#Program principal
para=0
a=input('introdureix una parula: ')
es_palindrom(para)