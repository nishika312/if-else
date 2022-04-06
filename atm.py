
print("WELCOME TO SBI BANK")
atm=input("enter the card")
if atm=="credit card" or atm=="debit card":
    print("card")
    language=input("enter the language")
    if  language=="english" or language=="hindi" or language=="panjabi":
        pin=input("enter the pin")
        if  pin=="9560" or "1234":
            print("number")
            bank=input("select your bank")
            if bank=="SBI" or bank=="HDFC":
                print("bank")
                transaction=input("enter the transaction")
                if transaction=="withdrow" or transaction=="balance inquire":
                    print("transacton")
                    account=input("enter the account type")
                    if account=="current" or account=="saving":
                        print("account type")
                        amount=(input("enter the amount"))
                        if amount=="100" or amount=="500" or amount=="2000" or amount=="200":
                              print("amount thankyou")
                        else:
                            print(" nothing")
                    else:
                        print(" no")   
                else:
                    print("never")   
            else:
                print("bank not available") 
        else:
            print("bhag ja")   
    else:
        print("chal be") 
else:
    print("jaa naa")                                   
        


    
        


