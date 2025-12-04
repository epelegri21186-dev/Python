
'''
y=lambda x:x[1]
d={'examen':9, 'tasca':5, 'tasca2':6}
l=d.items()
print(l)
y=dict(sorted(l,key=lambda x:x[0]), reverse=True)
print(y)

y=lambda x:x[1]
d={'examen':9, 'tasca':5, 'tasca2':6}
l=d.items()
print(l)
y=dict(sorted(l,key=lambda x:x[1]), reverse=True)
print(y)

l=['hola', 'loca', 'casa', 'califasticoespialidoso']
y=sorted(l,key=lambda x:x.count('a'), reverse=True)
print(y)

x=(lambda x:x.count('a'))('hola, guapa')
print(x)


x=(lambda n1, n2: n1+ n2)(3,7)

def f(n):
    return lambda a:a*n
#Programa principal
doble=f(2)
print(doble(10))

from functools import reduce
l=[3,5,4,2]
x=reduce(lambda n1, n2:n1+n2,l)
print(x)

l=[-1,3, 0, 25, -2, 4]
x=list(filter(lambda a:a>0, l))
print(x)


l=[3, 25,8,9]
x= list(map(lambda x:x+10, l))
print(x)'''