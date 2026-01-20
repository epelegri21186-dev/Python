n=int(input())
for i in range(n):
    s= input()
    x=s.split()
    h=int(x[0])*int(x[0])
    h2=int(x[1])*int(x[1])
    c=h+h2
    print(int(c**0.5))