resultat=True
n=int(input())
for i in range(n):
    s=input()
    x=s.split()
    l=[]
    for e in x:
        if int(e)!=0:
            l.append(int(e))
        pila=[]
        for e in l:
            if e > 0:
                pila.append(e)
            else:
                if not pila or pila[-1] != -e:
                    resultat=False
                    break
                else:
                    pila.pop()
    if pila:
        resultat=False
    if resultat:
        print('NORMAL')
    else:
        print('PARANORMAL')