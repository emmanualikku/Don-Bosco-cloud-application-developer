d = 0
c = 0
a = None

while a != 0:
    a = int(input("Enter the number to check: "))
    b = a % 2
    if b == 0:
        if a != 0:
            c += a
    else:
        d += 1

print("THE SUM OF EVEN NUMBERS IS", c)
print("THE NUMBER OF ODD NUMBERS IS", d)
