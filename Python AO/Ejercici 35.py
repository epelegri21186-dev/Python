def comptar_vocals(paraula):

    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    
    paraula = paraula.lower()
    
 
    for lletra in paraula:
        if lletra in vocals:
            vocals[lletra] += 1
    
    print(f"Hi ha {vocals['a']} a, {vocals['e']} e, {vocals['i']} i, {vocals['o']} o i {vocals['u']} u.")
    
    return vocals

comptar_vocals("Ratatouille, es un pelicula molt clasica de disnei que may pasara de moda")