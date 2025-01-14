x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Define your list here
for i in x:
    print(x)
print("\n")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(x):
    print(x[i])  # Change y[i] to x[i]
    i += 1
print("\n")

#SORT
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.sort()
print(x)
print("\n") 

#APPEND METHOD
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.append("berries")
print(x) 
print("\n") 

#INSERT
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.insert(3,"olives")
print(x)
print("\n") 

#extend 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=["olives","berries","nuts"]
x.extend(y)
print(x)
print("\n") 

#remove & pop
y=["olives","berries","nuts"]
y.remove("nuts")
print(y)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.pop(6)
print(x)
print("\n") 

#to clear the full list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.clear()
print(x)


#Write a programme for entering the elments into a list by 'user input' & seperate the even & odd numbers into different lists.

x=int(input("Enter a number : "))
even=[]
odd=[]
for i in range(x):
    y=int(input("Enter a number : "))
    if y%2==0:
        even.append(y)
    else:
        odd.append(y)
print(even)
print(odd)