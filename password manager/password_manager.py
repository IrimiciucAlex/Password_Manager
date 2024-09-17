from password_manager_structure import Password_Manager
PassManager=Password_Manager("password_file.txt")
choice=PassManager.menu()
decrypt_choice = input("Would you like to decrypt the password file? [Yes/No]: ")
if decrypt_choice.lower() == "yes":
     PassManager.decrypt()
while choice!="Yes":
    if choice=="1":
        PassManager.app()
        PassManager.get_password()
        PassManager.save_file()
        PassManager.encrypt()
    elif choice=="2":
        PassManager.app()
        PassManager.decrypt()
        content=PassManager.read_file("r",False)
        for line in content:
            if PassManager.application in line:
                print(line)
    elif choice=="3":
        PassManager.decrypt()
        content=PassManager.read_file("r",True)
        print(content)
    choice=input("Exit? [Yes/No]:")
    if choice=="Yes":
        PassManager.encrypt()
        print("Goodbye")
    elif choice=="No":
        choice=PassManager.menu()