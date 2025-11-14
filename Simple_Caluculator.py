print("Simple Caluculator")
Number1=float("enter first number:")
Number2=float("enter second number:")
print("The first Number is",Number1)
print("The second Number is",Number2)
choice =input("Enter your choice(+,-,*,/,%):")
if choice=='+':
print("Addition of" ,Number1,"and",Number2,"is:",Number1+Number2)
elif choice=='-':
print("Substration of" ,Number1,"and",Number2,"is:",Number1-Number2)
elif choice=="*":
print("Multiplication of" ,Number1,"and",Number2,"is:",Number1*Number2)
elif choice=="/":
if Number2!=0:
    print("Divison of" ,Number1,"and",Number2,"is:",Number1/Number2)
    else:
    print("division my zero is error!")
elif choice=="%":
    print("Remainder of" ,Number1,"and",Number2,"is:",Number1%Number2)
else:
    print("enter invalid opertion,try again!")



