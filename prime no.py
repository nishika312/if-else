'''prime=int(input("enter the number"))

for i in range(2, prime):
    if prime%i==0:
        print("not prime")
        break
    if i==prime-1:
        print("prime")'''



'''for i in range(2, prime):
    if prime%i==0:
        print("not prime")
        break
else:
    print("prime")



for i in range(2, int((prime)**(1/2))+1):
    if prime%i==0:
        print("not prime")
        break
else:
    print("prime")


i=2
while i<prime:
    if prime%i==0:
        print("not prime")
        break
    if i==prime-1:
        print("prime")

    i+=1
if prime%i==0:
        print("not prime")
        break
    if i==prime-1:
        print("prime")'''

num=int(input("enter the number:"))
if num!=1 and num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0 or num==2 or num==3 or num==5 or num==7:
    print(num,"prime number")
else:
    print("not prime no")