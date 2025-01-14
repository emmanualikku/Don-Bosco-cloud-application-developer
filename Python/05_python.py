#Write a programme to check if a number is POSITIVE,NEGATIVE OR ZERO & further categorize POSITIVE NUMBERS as EVEN/ODD
x=int(input("Enter a number"))
if x>=0:
    if x==0:
        print("ZERO")
    else:
        print("POSITIVE NUMBER")
        if x%2==0:
            print(x,"is EVEN NUMBER")
        else:
            print(x,"is ODD NUMBER")
else:
    print(x,"is a NEGATIVE NUMBER")

##Write a programme that a students score (an integer b/w zero & 100) & determine if the student has passed or failed.
# If the student has passed, (score greater than / equal to 50), the programme should assign grade based on,
# Score >=90 – Grade A
# Score >=75 – Grade B
# Score >=60 – Grade C
# Score >=50 – Grade D
# If the student has failed, display FAIL. Additional the programme should ensure that the score entered is VALID.

x=int(input("Enter a number : "))
if x>100:
    print("IT'S INVALID")
elif x>=50:
    print("PASSED")
    if x>=90:
        print("A GRADE")
    elif x>=75:
        print("B GRADE")
    elif x>=60:
        print("C GRADE")
    elif x>=50:
        print("D GRADE")
elif x<50:
    print("FAILED")
