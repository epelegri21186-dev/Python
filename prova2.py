"""for i in range(1,10,3):
    print("{} * 5 = {}".format(i, i*5))"""

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
        print("L'opcio seleccionada es incorrecta torni a provar\n")

menu_principal()