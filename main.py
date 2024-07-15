#python as a claculator
#taking value from user
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
#taking operations that user have to perform
operation=(input("choose : + , - , * , / , % , ** , // :"))
#conditions
if(operation=='+'):
    print("Addition :",num1+num2)
if(operation=='-'):
    print("Subtraction :",num1-num2)
if(operation=='*'):
    print("Multiplication :",num1*num2)
if(operation=='/'):
    print("Division :",num1/num2)
if(operation=='%'):
    print("Remainder:",num1%num2)
if(operation=='**'):
    print("Exponential :",num1**num2)
if(operation=='//'):
    print("Floor Division :",num1//num2)