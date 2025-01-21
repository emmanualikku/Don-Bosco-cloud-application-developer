def find_largest_number(a, b, c):
    if (a >= b) and (a >= c):
        q = a
    elif (b >= a) and (b >= c):
        q = b
    else:
        q = c
    return q

a = 10
b = 25
c = 15

print("The largest number is:", find_largest_number(a, b, c))
