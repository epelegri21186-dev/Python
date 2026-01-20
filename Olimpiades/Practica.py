

#Paraules exercici A si
'''
n=int(input())
for i in range(n):
    paraules=input()
    solucio=paraules.title()
    print(solucio)
'''
#Tirolines exercici B casi
'''
n=int(input())
for i in range(n):
    s=input()
    x=s.split()
    c=int(x[0])*int(x[0])
    c1=int(x[1])*int(x[1])
    h=c+c1
    print(int(h**0.5))
'''
#Maxim exercici C casi
'''
Docstring for Olimpiades.Practica
n=int(input())
for i in range(n):
    s=input()
    x=s.split()
    l=[]
    for e in x:
        l.append(int(e))
    l.sort()
    d=l[-1:]
    q=l.count(d[0])
    """f=[0]
    o=[]
    for e in f:
        o.append(int(e))
    for e in l:
        if e==d:
            f=f+1
            print(e, f)
        else:
            q=0"""
    print(d[0], q)
'''