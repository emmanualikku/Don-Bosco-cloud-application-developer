def ap(a, b, c):
    x = c**2
    y = a * b
    z = 2 * (a + b)
    w = 4 * c

    print("\n")
    print('Area of square is', x)
    print('Area of rectangle is', y)
    print('Perimeter of square is', w)
    print('Perimeter of rectangle is', z)

a = int(input("Length of rectangle: "))
b = int(input("Width of rectangle: "))
c = int(input("Side length of square: "))

ap(a, b, c)
