a = int(input("ENTER THE SECRET NUMBER: "))

b = 25
c = 1

print("\n")

while c == 1:
    if a < 20:
        print("THE NUMBER GUESSED IS TOO LOW")
    elif 20 <= a < 25:
        print("THE NUMBER GUESSED IS LOW")
    elif 25 < a < 30:
        print("THE NUMBER GUESSED IS HIGH")
    elif a > 30:
        print("THE NUMBER GUESSED IS TOO HIGH")
    elif a == 25:
        print("NUMBER ENTERED IS CORRECT")
        break

    a = int(input("ENTER THE SECRET NUMBER: "))
