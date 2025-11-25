def nombre_major():
    a=int(input('introdueix el primer nombre: '))
    b=int(input('introdueix el segon nombre: '))
    if a>b:
        print('{} es el major de {} i {}'.format(a,a,b))
    else:
        print('{} es el major de {} i {}'.format(b,a,b))
nombre_major()
