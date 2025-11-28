def comptar_majuscules(cadena):

    comptador = 0
    for caracter in cadena:
        if caracter.isupper():
            comptador += 1
    return comptador

text = "Hola, Joan Ramis"
print("Text: '{}'".format(text))
print("Majúscules: {}".format(comptar_majuscules(text)))
print()
