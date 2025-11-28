
a=[1,2,3,4,1,2,3,4,5,1,2,4,6,6,4,2,5]
b= set(a)
c=list()
for e in b:
    c.append([e,a.count(e)])
print(c)

'''
a=[1,2,3,4,1]
b= set(a)
if len(a)==len(b):
    print('No hi ha elements repetits')
else:
    print('Hi ha elements repetits')'''