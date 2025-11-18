def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio = int(input(""" Elegeix una opcio:
                      1. Calculadora decimal
                      2. Calculadora real (float)
                      3. Sortir \n"""))
        if opcio>0 and opcio<4:
            return opcio
        else:
            print("L'opcio seleccionada es Errorincorrecta torni a provar\n")
def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio=int(input("""
                1. suma
                2 resta
                3 multiplicacio
                4 divisio
                5 sortir
                """))
        if opcio>0 and opcio<6:
            return opcio
        else:
            print("L'opcio seleccionada es incorrecta torni a provar\n")

def calculadora_decimal(opcio):
    if opcio>0 and opcio<6:
        a = int(input("Introdueix el primer nombre: "))
        b = int(input("Introdueix el segon nombre: "))
    match(opcio):
        case 1:
            #Suma
            print("Prosedeix amb la suma")
            c=a+b
            print("El resultat de suma {} + {} és {}".format(a,b,c))
        case 2:
            #Restaopcio=0
            print("Prosedeix amb la resta")
            c=a-b
            print("El resultat de resta {} - {} és {}".format(a,b,c))
        case 3:
            #Multiplicació
            print("Prosedeix amb la sumultiplicació")
            c=a*b
            print("El resultat de multiplicació {} x {} és {}".format(a,b,c))
        case 4:
            #Divisio
            print("Prosedeix amb la divisió")
            c=a//b
            print("El resultat de dividir {} / {} és {}".format(a,b,c))
        case _:
            print("Error\n")


def calculadora_real(opcio):
    if opcio>0 and opcio<6:
        a = float(input("Introdueix el primer nombre: "))
        b = float(input("Introdueix el primer nombre: "))
    match(opcio):
        case 1:
            #Suma
            print("Prosedeix amb la suma")
            c=a+b
            print("El resultat de suma {} + {} és {}".format(a,b,c))
        case 2:
            #Resta
            print("Prosedeix amb la resta")
            c=a-b
            print("El resultat de resta {} - {} és {}".format(a,b,c))
        case 3:
            #Multiplicació
            print("Prosedeix amb la sumultiplicació")
            c=a*b
            print("El resultat de multiplicació {} x {} és {}".format(a,b,c))
        case 4:
            #Divisio
            print("Prosedeix amb la divisió")
            c=a/b
            print("El resultat de dividir {} / {} és {}".format(a,b,c))
        case _:
            print("Error\n")


# Programa Principal
op = 1
while op!=0:
    op = menu_principal()
    if op==1:
        # Calculadora decimal
        print("Has seleccionat la calculadora decimal\n")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        # Calculadora real
        print("Has seleccionat la calculadora real\n")
        calculadora_real(menu_calculadora())
    else:
        print("Gracies per utilitzar la calculadora\n")
        op=0
