#Create a tuple, add values as in no.s through user input. Output should have the following;Tuple, Sum of odd no.s, Sum of even no.s 
x=input("Enter the numbers : ").split(',')
y=tuple(x)
print(y)
even=0
odd=0
for i in y:
    i=int(i)
    if i%2==0:
        even=even+i
    elif i%2!=0:
        odd=odd+i
print("Sum of even no.s are",even)
print("Sum of odd no.s are",odd)

#Find 
x=tuple(input("Enter any words : ").split(','))
print(type(x))
print(x)
z=" "
for i in x:
    if len(i) > len(z):
        z=i
print("The longest string in tuple is",z)