PI = 3.141592653589793

def cylinder_surface_area(x, y):
    z = 2 * PI * x * y + 2 * PI * x ** 2
    return z

def cylinder_volume(x, y):
    q = PI * x ** 2 * y
    return q

x = float(input("Enter the radius of the cylinder: "))
y = float(input("Enter the height of the cylinder: "))

z = cylinder_surface_area(x, y)
q = cylinder_volume(x, y)

print(f"Surface Area of Cylinder: {z}")
print(f"Volume of Cylinder: {q}")
