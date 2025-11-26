'''Definir una funció crear_repetits() que agafi un número enter i 
un caràcter i retorni el caràcter multiplicat pel número enter. 
Ex: crear_repetits(5, “a”), retorni “aaaaa”
'''
insertit=0
repit=0

def crear_repetits(inserit):
    print(insertit*repit)

#Programa principal
insertit=input('Insereix el caracter a repetir: ')
repit=int(input('Insereix el nombre de vegades a repetir el caracter: '))
crear_repetits(insertit)

