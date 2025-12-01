def mostrar_majors_que(tupla, valor):

    print(f"\nNúmeros majors que {valor}:")
    trobats = False
    
    for num in tupla:
        if num > valor:
            print(num)
            trobats = True
    
    if not trobats:
        print("No hi ha cap número major.")


def main():

    print("PROGRAMA PER TROBAR MAJORS DE 18 ANYS")

    
    
    while True:
        try:
            quantitat = int(input("\nQuants valors vols introduir? "))
            if quantitat > 0:
                break
            else:
                print("Has d'introduir un número positiu!")
        except ValueError:
            print("Error! Introdueix un número enter vàlid.")
    
    
    llista_edats = []
    
    
    print(f"\nIntrodueix {quantitat} edats:")
    for i in range(quantitat):
        while True:
            try:
                edat = int(input(f"Edat {i+1}: "))
                llista_edats.append(edat)
                break
            except ValueError:
                print("Error! Introdueix un número enter vàlid.")
    
   
    tupla_edats = tuple(llista_edats)
    
    
    print(f"\nTupla d'edats: {tupla_edats}")
    
    
    mostrar_majors_que(tupla_edats, 18)



if __name__ == "__main__":
    main()