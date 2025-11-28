def divisio_per_zero(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        print('No es pot dividir entre zero')
        return None
    else:
        return resultat

#Programa Principal
x = 10
y = 2
res = divisio_per_zero(x, y) 
if res is not None:
    print("El resultat de {}/ {} és: {}".format(x, y, res))
