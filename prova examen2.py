a=int(input('Edad:'))
if a<18 and a>0:
    b='eres menor de edad'
elif a>=18:
    b='eres mayor de edad'
else:
    b='has insertat una edad incorecta'

if a%2==0:
    print('Tens edad parell')
else:
    print('Tens una edad imparell')
if a%5==0:
    print('Es multip de 5')
else:
    print('No es multip de 5')
if a>=0 and a<=10:
    print('Esta entre 0 i 10')
elif a>=11 and a<=20:
    print('Esta entre 11 i 20')
else:
    print('Tens més de 20 anys')
print('Hola tens {} anys, {}'.format(a, b))