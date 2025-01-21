numbers = []

# Input number of elements
n = int(input("Enter the number of elements: "))

# Enter elements into the list
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Separate even and odd numbers
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
