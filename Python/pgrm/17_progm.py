def rectangle_area_perimeter(a, q):
    w = a * q
    x = 2 * (a + q)
    return w, x
def square_area_perimeter(z):
    s = z ** 2
    f = 4 * z
    return s, f
a = int(input("Enter the length of the rectangle: "))
q = int(input("Enter the width of the rectangle: "))
z = int(input("Enter the side length of the square: "))
w, x = rectangle_area_perimeter(a, q)
s, f = square_area_perimeter(z)
print(f"Rectangle Area: {w}, Perimeter: {x}")
print(f"Square Area: {s}, Perimeter: {f}")
