a = float(input("Escriure el primer nombre: "))
b = float(input("Escriure el segon nombre: "))
d=float(input("nombre:"))
c = a + b + d
print("El resultat de la suma és {}".format(c))
if c>20:
    print("El resultat de {} + {} + {} es major a 20".format(a, b, d))
else:
    print("El resultat de {} + {} + {} es menor a 20".format(a,b,d))

c = a * b * d
if c>100:
    print("El resultat de {} + {} + {} es major a 100".format(a, b, d))
else:
    print("El resultat de {} + {} + {} es menor a 100".format(a,b,d))
