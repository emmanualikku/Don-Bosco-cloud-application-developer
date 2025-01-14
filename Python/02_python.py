x=("apple", "banana", "orange", 55, 13, 180, 1802, "cap", "tanum fax", "vintage era")
print(type(x))
y=list(x)
print(y)
print(y[2:7])
y[8]="blogilates"
x=tuple(y)
print(y)
print("\n")


#write a programme to find longest string in a tuple using [user input]
a=tuple(input("Enter the values : ").split(','))
print(a)
b=list(b)
print(len(b))
c=" "
for i in a :
    if len(i)>len(c):
        c=i
print("The longest string is ",(c))
