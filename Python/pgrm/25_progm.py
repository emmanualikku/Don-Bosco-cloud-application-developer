a = int(input("ENTER THE SECRET NUMBER: "))

b = 25

print("\n")

while a != b:
    if a < b:
        print("THE NUMBER GUESSED IS LOW")
        a = int(input("ENTER THE SECRET NUMBER: "))
    elif a > b:
        print("THE NUMBER GUESSED IS HIGH")
        a = int(input("ENTER THE SECRET NUMBER: "))

print("CONGRATULATIONS! YOU'VE GUESSED THE CORRECT NUMBER.")
