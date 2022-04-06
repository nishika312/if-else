no_of_class=int(input("Enter the no. of classes held:"))
class_attended=int(input("Enter the no. of classes attended:"))

percentage = class_attended /no_of_class *100
if percentage>=75:
    print("allowed to sit")
else:
    Medical=input("Enter the medical issue y/n:")
    if Medical == "y":
        print("Allow to sit because of medical issue")
    else:
        print("Not allowed to sit.")
