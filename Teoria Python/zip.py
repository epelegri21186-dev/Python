


"""
from functools import reduce
def add(x,y):
    return x+y
ln=[]
sortir='n'
while sortir!='s':
    nombre=float(input())
    ln.append(nombre)
    sortir=input('Vols sorti(n/s)? ')

sumapositius=reduce(add, [n for n in ln if n>0])
sumanegatius=reduce(add, [n for n in ln if n<0])
print(f'''
          Suma nombres positius {sumapositius}
          Suma nombre negatius {sumanegatius}
          Mitjana {(sumapositius+sumanegatius)/len(ln)}''')

def convertir(ns):
    vocales='aeiouáéíóúàèìòù'
    return [
        ''.join(l.upper() if l.lower() in vocales else l
                for l in n)
        for n in ns
    ]
n=['joan', 'miquel', 'pere', 'maria']
print(convertir(n))
p=[i for i in range(1,11)]
print(p)
s=[i**3 for i in range(20) if i%2==1]
print(s)
m=[2*i +1 for i in range(20)]
print(m)
l = [1,2,3,4,5]
p = [1,2,3,4,5]
s = list(zip(l,p))
print(s)
"""