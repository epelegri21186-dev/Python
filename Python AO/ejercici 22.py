'''Definir una funció superposicio() que agafi dues llistes i retorni vertader 
si hi ha un element en comú, en cas contrari, que retorni fals.'''

def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False


print(superposicio([1, 5, 8], [0, 6, 6]))  
print(superposicio([6, 9, 8], [8, 6, 6]))  
