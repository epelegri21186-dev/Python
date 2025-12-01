
for e in range(1, 1001):
    if (e%9==0 or e%7==0) and not (e%5==0 and e%8!=0):
            print(e)












'''
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