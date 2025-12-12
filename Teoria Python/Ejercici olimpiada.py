#Passar a majuscules

def llegir_frases(n):
    llista=llista()
    for i in range(n):
        llista.append(input(''))
    return llista

def escriure_frases(llista):
    for e in llista:
        print(e)

def convertir_majuscules(s):
    vocal='aeiuoAEIOU'
    llista=list(s)
    for i,e in enumerate(s):
        if e not in vocal:
            llista[i]=e.upper()
    return "".join(llista)


#Programa principal
n=int(input(""))
llista=llegir_frases(n)
for i,e in llista:
    llista[i]=convertir_majuscules(e)
escriure_frases(llista)















#Sumar Uno
"""def suma_uno(num):
    while num>0:
        return num

num=int(input('nombre: '))
suma_uno(num)
print(num+1)"""