a = int(input("ENTER THE NUMBER TO CHECK: "))

print("\n")

if a < 0 or a > 100:
    print("THE SCORE ENTERED IS NOT VALID")
    print("\n")
else:
    print("\n")
    if a <= 100 and a >= 90:
        print("A GRADE")
    elif a >= 75 and a < 90:
        print("B GRADE")
    elif a >= 60 and a < 75:
        print("C GRADE")
    elif a >= 50 and a < 60:
        print("D GRADE")
    elif a < 50 and a >= 0:
        print("FAILED")

print("\n")
