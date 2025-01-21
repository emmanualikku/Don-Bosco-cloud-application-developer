# write a programme to check if a number is positive negetive or zero and further categorize positive number's as either even or

a = int(input("Enter the number to check: "))
if a < 0:
    print(a, "is a negative number")
elif a == 0:
    print(a, "is zero")
elif a > 0:
    print(a, "is a positive number")
    b = a % 2
    if b == 0:
        print(a, "is an even number")
    else:
        print(a, "is an odd number")