# While function:
i=1
while i < 6 :
    print(i)
    i=i+1

# To Break the chain;
i=1
while i < 6 :
    print(i)
    i=i+1
    if i==3:
        break

# ANOTHER VERSION W/ ANS.3;
i=1
while i < 6 :
    print(i)
    if i==3:
        break
    i=i+1

## Write a programme that keeps asking the user for a POSITIVE INTEGER if the user enters a NEGATIVE NUMBER OR ZERO, the programme should invalid input & continue asking for VALID INPUT. Once the POSITIE INTEGER is entered, the programme should bring "THANK YOU".;
x=int(input("Enter a number : "))
while x<=0:
    print("You Have Entered An Invalid Input. Enter A Positive Number")
    print("\n")
    x=int(input("Enter a number : "))
if x>=1:
    print("THANK YOU")
    
## Write a programme that asks the user to enter a password. The programme should keep asking for the password until the user enters it correctly. After eact incorrect attempt display "Wrong Password". Once it i correct, display "Access Granted".
x="BTSFOREVER"
y=input("Enter Your Password  :  ")
while x!=y:
    print("WRONG PASSWORD ; ACCESS DENIED")
    print("\n")
    y=input("Enter Your Password  :  ")
if x==y:
    print("ACCESS GRANTED ; WELCOME BACK")
    
