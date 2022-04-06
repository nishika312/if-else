
student_name=input("enter the student name")
medical_sertificate=input("why not have medical certificate")
if medical_sertificate=="yes":
    print(student_name,"allow to sit")
elif medical_sertificate=="no":
    print(student_name,"not allow to sit")
else:
    print("error")