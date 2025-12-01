def es_de_traspas(any):

    if any % 400 == 0:
        return True
    elif any % 100 == 0:
        return False
    elif any % 4 == 0:
        return True
    else:
        return False
    

print(f"2024 és de traspàs? {es_de_traspas(2024)}")  
print(f"2023 és de traspàs? {es_de_traspas(2023)}")  
print(f"2022 és de traspàs? {es_de_traspas(2022)}")  
print(f"400 és de traspàs? {es_de_traspas(400)}")  
print(f"4910 és de traspàs? {es_de_traspas(4910)}")  
print(f"2120 és de traspàs? {es_de_traspas(2120)}")  