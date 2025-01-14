#Write a programme that asks the user to guess a secret number(25). After each guess the programme should give feedback too high if guess is greater than secret no. & too low, vice versa. The programme should keep asking until the correct is guessed.
x=int(input("Enter your secret number : "))
y=25
z=1
while z==1:
    while x>y:
        print("The guessed number is TOO HIGH")
        print("\n")
        x=int(input("Enter your secret number : "))
    while x<y:
        print("The guessed number is TOO LOW")
        print("\n")
        x=int(input("Enter your secret number : "))
    if x==y:
        print("CORRECT GUESS")
        break
