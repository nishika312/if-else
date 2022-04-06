


print (" WELCOME TO THE FACEBOOK")
name=input("enter the frist name")
if name=="ishika":
    print ("yes its a name")
    name=input("enter the last name")
    if name=="das":
        print("yes its a last name")
        birth=input("enter the date of birth")
        if birth=="12/02/2001":
            print("yes its date of birth")
            gender=input("enter the gender")
            if gender=="male" or gender=="female":
                print("yes it's a gender")
                phone=input("enter the phone number")
                if phone=="9999044109":
                    print("yes it's a phone number")
                    emai=input("enter the emai")
                    if emai=="ishika1222001@gmail.com":
                        print ("yes it's emai")
                        password=int(input("enter the password"))
                        if password=="ishu@123":
                            print("yes it's a password thankyou")
                        else:
                            print("error")  
                    else:
                        print("invalid")  
                else:
                    print("invaild number")  
            else:
                print("choose selected one") 
        else:
            print("enter full date of birth")  
    else:
        print("enter full name")    
else:
    print("error")                                    


