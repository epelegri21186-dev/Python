'''Definir una funció gran_de_tres(), donats tres números, 
retorni el major. Prova-la amb diferents exemples.'''

def gran_de_tres():
    if a>b and a>c:
        if b>c:
            print('{} > {} > {}'.format(a,b,c))
        else:
            print('{} > {} > {}'.format(a,c,b))
    elif b>a and b>c:
        if a>c:
            print('{} > {} > {}'.format(b,a,c))
        else:
            print('{} > {} > {}'.format(b,c,a))
    else:
        if a>b:
            print('{} > {} > {}'.format(c,a,b))
        else:
            print('{} > {} > {}'.format(c,b,a))


#Programa principal

a=int(input('Introdueix un nombre: '))
b=int(input('Introdueix un nombre: '))
c=int(input('Introdueix un nombre: '))
gran_de_tres()  