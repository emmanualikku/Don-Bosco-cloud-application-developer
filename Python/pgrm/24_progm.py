a = input("ENTER THE PASSWORD: ")

b = "WAKANDA FOR EVER"

while a != b:
    print("THE PASSWORD YOU ENTERED IS", a)
    print("\nTHE PASSWORD IS WRONG")
    a = input("ENTER THE PASSWORD: ")

while a == b:
    print("ACCESS GRANTED TO THE WORLD. WELCOME, BLACK PANTHER!")
    break
