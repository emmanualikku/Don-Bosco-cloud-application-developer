## Write a programme that continuously ask the user to input a number. The programme should keep a running total of sum of all even numbers & count of odd numbers while it it should only stop if the user enters ZERO & then the programme should print "the total sum of all even numbers & total count of odd numbers"
a=0
b=0
z=None
while z!=0:
    z=int(input("Enter a number : "))
    y=z%2
    if y!=0:
        a=a+y
    if y==0:
        b=b+1
print("The sum of all EVEN NUMBERS is",a)
print("The sum of all ODD NUMBERS is",b)


#LIST___#REPLACE___#SLICING__#TUPLE   
x=["apple","orange",0,2,4,5,True,False]
y=["apple","orange",0,2,4,5,True,False]
print(y)
print(x[1])
print(x[5])
print(x[-2])
print(x[1:4])
print(x[1:])
print(x[0: :3])
x[0]="blue berry"
print(x)
print("\n")
a=list(x)
print(a)
W=(input("Enter to check : "))
if W in x:
    print("Yes")
else:
    print("Not right")