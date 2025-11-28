a={1:'H', 2:'o', 3:'l', 4:'a', 5:',', 6:[1,2,3,4]}
b={7: 'pepe', 8:'Miquel'}
a.update(b)#Afejeix el que hi haviga
a.popitem()#Elimina un aleatori(majoritariament el darrer)
a.pop()#Elimina un valor
b=a.keys()#Mstra els nombres
b=a.values()#Mostra els volors
print(a.get(1))#Retorna el valor de la pocisio
a.clear()#Buida el diccionaari
print(a[1]) # Retorna H
print(a[4])# Retorna a
print(a[5])# Retorna ,
a[1]='M' #H --> M
for e in a:
    print(e)#Retorna 1 2 3 4 5 6
    print(a[e])#Retorna els valors
for x,y in a.items():
    print('{}:{}, '.format(x,y))# Mosta cada posisio amb el seu valor
print(a)