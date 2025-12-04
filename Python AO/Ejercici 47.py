def eliminarcapicua(llista):
    if len(llista) <= 2:
        return []
    else:
        return llista[1:-1]
    
llista = ['j', 'o', 'r', 'b', 'a']
print(eliminarcapicua(llista))