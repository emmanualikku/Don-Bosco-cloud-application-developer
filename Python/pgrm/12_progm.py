a = input("Enter the characters: ")
b = a.split()
vov = []
cons = []
waa = 'aeiouAEIOU'
for pos in b:
    if pos[0] in waa:
        vov.append(pos)
    else:
        cons.append(pos)
print(vov)
print(cons)
