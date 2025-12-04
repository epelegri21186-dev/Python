def facturial(n):
    if n>0:
        return n*facturial(n-1)
    else:
        return 1
a=int(input('introdueix un nombre: '))
print(facturial(a))
















'''
def sumaun(l):
    for i,e in enumerate(l):
        l[i]=e+1

l=[5, 6, 7, 10]
print(l)
sumaun(l)
print(l)

def ordenr(x,y):
    if x>y:
        return y,x
    elif y>x:
        return x,y
    else:
        return x,y


a=int(input('Insereix el primer nombre: '))
b=int(input('Insereix el segon nombre: '))
a, b=ordenr(a,b)
for e in range(a,b+1):
    if e%2==1:
        print(e)
a=int(input('Insereix el primer nombre: '))
b=int(input('Insereix el segon nombre: '))
c=a*b
if (25<=c) and (c<=35) or (105<=c) and (125>=c):
    print('A')
elif (c<=45) and (c>=65) or  (145<=c) and (c<=165):
    print('B')
else:
    print('C')
for e in range(1, 1001):
    if (e%9==0 or e%7==0) and not (e%5==0 and e%8!=0):
            print(e)
while(5<=v1 and 10>=v1 and v1!=6) or (v1>15 and v1<20 and v1!=16) or (v1>25 and v1<30 and v1!=26):
    print(v1)
    v1=int(input('posa un nombre'))
print('has acabat')
def ordenar(x,y):
#Prec: Donats dos numeros
# post: els retorna amb ordre, primer el ,major i despres el menor
    if x>y:
        return(x,y)
    elif y>x:
        return(y,x)
    else:
        return x,y
v1=int(input('hola'))
v2=int(input('otrA'))

v1,v2=ordenar(v1,v2)
for e in range(v2+1, v1):
    print(e)





r=v1==v2
print(r)
r=v1!=v2
print(r)
r=v1>v2
print(r)
r=v1<v2
print(r)
r=v1>=v2
print(r)
r=v1<=v2
print(r)



v1=int(input('hola'))
v2=int(input('otrA'))
r=v1+v2
print(r)
r=v1-v2
print(r)
r=v1*v2
print(r)
r=v1/v2
print(r)
r=v1//v2
print(r)
r=v1%v2
print(r)
r=v1**v2
print(r)
r=v1+v2**2/v1-v1%v2
print(r)'''