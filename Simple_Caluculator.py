print("Simple Caluculator")
number1=float(input("enter first number:"))
number2=float(input("enter second number:"))
print("The first Number is",number1)
print("The second Number is",number2)
choice = input("Enter your choice(+,-,*,/,%):")
if choice=='+':
    print("Addition of" ,number1,"and",number2,"is:",number1+number2)
elif choice=='-':
    print("Substration of" ,number1,"and",number2,"is:",number1-number2)
elif choice=='*':
    print("Multiplication of" ,number1,"and",number2,"is:",number1*number2)
elif choice=='/':
if number2!=0:
    print("Divison of" ,number1,"and",number2,"is:",number1/number2)
    else:
    print("division my zero is error!")
elif choice=="%":
    print("Remainder of" ,number1,"and",number2,"is:",number1%number2)
else:
    print(" invalid opertion,try again!")




