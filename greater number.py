num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1>num2 and num1>num3:
    print("num1 is greater")
if num1<num2 and num2>num3:
    print("num2 is greater")
if num1<num3 and num2<num3:
    print("num3 is greater")