def duramor(a):
    s= a.lower()
    if 'amol' in a:
        return True
    else:
        return False
corregida=[]
n=int(input())
for _ in range(n):
    frase=input().split()
    while len(frase)>len(corregida):
        for e in frase:
            for a in e:
                if duramor(a)==False:
                    if a == 'r':
                        l='l'
                        corregida.append(l)
                    elif a=='l':
                        r='r'
                        corregida.append(r)
                    elif a=='L':
                        R='R'
                        corregida.append(r)
                    elif a=='R':
                        L='L'
                    else:
                        corregida.append(a)
                else:
                    x=corregida
        print("".join(corregida))