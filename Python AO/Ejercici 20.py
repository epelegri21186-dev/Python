"""Definir una funció invertir() que calculi 
la inversa d’una cadena. Ex: invertir
(“Soc del Ramis”) hauria de tornar la cadena 
“simaR led coS”."""
def invertir(s):
    return s[::-1]

#Programa principal
cadena="Hola, Joan Ramis i Ramis"
print('la inversa de {} és {}'.format(cadena, invertir(cadena)))