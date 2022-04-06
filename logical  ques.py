num1=float(input("enter the number"))
num2=float(input("rnter the second number"))
print("operation:+,-,*,/")
select=input("select operation:")
if select == "+":
    print(num1,"+",num2,"=",num1+num2)
elif select=="-":
    print(num1,"-",num2,"=",num1-num2)
elif select=="*":
    print(num1,"*",num2,"=",num1*num2)
elif select=="/":
    print(num1,"/",num2,"=",num1/num2)
else:
    print("pta nhi")    