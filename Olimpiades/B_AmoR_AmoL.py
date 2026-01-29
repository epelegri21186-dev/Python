def canvi(s):
    x=''
    for e in s:
        if e=='L':
            x+='R'
        elif e=='l':
            x+='r'
        elif e=='R':
            x+='L'
        elif e=='r':
            x+='l'
        else:
            x+=e
    return x
def duramor(s):
    a= s.lower()
    if 'amol' ==a:
        return s
    elif 'amol' in a:
        p=0
        prefix=''
        posfix=''
        amol=''
        while a[p]!='a':
            p+=1
        if p>0:
            prefix=canvi(s[:p])
        p=0
        while a[p]!='o':
            p+=1
        p+=2
        if p<len(s):
            posfix=canvi(s[p:])
        return prefix+'amol'+posfix
    else:
        return canvi(s)
def Arreglar(a):
    s=[]
    for e in a:
        s.append(duramor(e))
    return s
n=int(input())
for _ in range(n):
    a=input().split()
    s=Arreglar(a)
    print(" ".join(s))