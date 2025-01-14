#Write a python programme that accepts an integer representing a person'ds age & dtermines the category they belong to. The programme should use Nested IF statements to classify the person based on their age as follows ;
# if age <0 - print 'invalid age'
# if age is in bw 0 & 12 - print 'you are a child'
# if age is in bw 13 & 19 - print 'you are a teenager'
# if age is in bw 20 & 59, check further
# if age is in bw 20 & 29; print 'you are in yoiur twenties'
# if age is in bw 30 & 39; print 'you are in your thirties'
# if age is in bw 40 & 59; print 'you are in your middle age'
# if age is >60; print 'you are a senior citizen'

x=int(input("Enter your age : "))
if x<0:
    print("Invalid Age")
elif x<=12:
    print("You are a child")
elif x<=19:
    print("You are a teenager")
if x<=59:    
    if x<=29:
        print("You are in your twenties")
    elif x<=39:
        print("You are in your thirties")
    elif x<=59:
        print("You are in your middle age")
else:
    print("You are a Senior Citizen")