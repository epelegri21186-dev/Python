l=[50,100,200]
with open("provafit.txt", "a") as f:
    f.write(str(l))
with open("provafit.txt", "r") as f:
    linias=f.readlines()
    linias=[n[:-1] for n in linias]
    print(linias)



with open("provafit.txt","r") as f:
    linias=f.readlines()
    linias=[n for n in linias[::-2]]
    print(linias)

"""f=open('prova_fit.txt','r')
print(f.read())
f.close()
"""
