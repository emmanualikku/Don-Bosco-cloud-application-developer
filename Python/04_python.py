#Write a programme to find the second largest element in a tuple
x=tuple(input("Enter any elements : ").split(','))
y=max(x)
z=None
for i in x:
    if i<y:
        if z==None or i>z:
            z=i
print(z)