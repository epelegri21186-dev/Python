def esta_ordenada(llista):

    if len(llista) <= 1:
        return "està ordenada de forma ascendent"
    
    # Comprovem si està ordenada ascendent
    ascendent = True
    for i in range(len(llista) - 1):
        if llista[i] > llista[i + 1]:
            ascendent = False
            break
    
    if ascendent:
        return "està ordenada de forma ascendent"
    
    # Comprovem si està ordenada descendent
    descendent = True
    for i in range(len(llista) - 1):
        if llista[i] < llista[i + 1]:
            descendent = False
            break
    
    if descendent:
        return "està ordenada de forma descendent"
    
    return "no està ordenada"

# Proves amb diferents llistes
print(f"Llista [100, 50, 25]: {esta_ordenada([9, 8, 7])}")
print(f"Llista [4, 5, 6]: {esta_ordenada([4, 5, 6])}")
print(f"Llista [4, 6, 5]: {esta_ordenada([4, 6, 5])}")