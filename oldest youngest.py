age1=int(input("enter the age"))
age2=int(input("enter the age"))
age3=int(input("enter the age"))
if age1>age2 and age2<age3:
    print("yungest")
elif age2<age1 and age1<age3:
    print("oldest")
elif age2>age3 and age3<age1:
    print("yungest")
elif age3<age2 and age2>age3:
    print("oldest")
elif age3>age2 and age2<age1:
    print("youngest")
else:
    print("oldest")