import os
from cryptography.fernet import Fernet
class Password_Manager:
    def __init__(self,name,application="",password=""):
        self.name=name
        self.application=application
        self.password=password
        if not os.path.exists(self.name):
            with open(self.name,"w") as f:
                pass

    def menu(self):
       choice=" "
       while choice not in ["1", "2", "3"]:
           choice=input("1.Chose a new password:\n"
                 "2.Chose the application to view the password:\n"
                 "3.View all the passwords\n"
                 "Choice:")
       return choice

    def app(self):
        self.application=input("Insert the application:")

    def get_password(self):
        self.password=input("Insert the password:")


    def read_file(self,mode,line=False):
         if line==False:
             with open(self.name, mode) as fr:
                 file_content = fr.readlines()
                 return file_content
         else:
            with open(self.name,mode) as fr:
                file_content=fr.read()
                return file_content

    def write(self,mode,content):
        with open(self.name,mode) as fw:
            fw.write(content)

    def save_file(self):
        content=self.read_file("r",True)
        if self.application in content:
            print("The application exists")
        else:
            self.write("a",f"{self.application}:{self.password}\n")

    def encrypt(self):
        # Generate or read encryption key
        if not os.path.exists("mykey.key"):
            key = Fernet.generate_key()
            with open("mykey.key", "wb") as filekey:
                filekey.write(key)
            print("Encryption key generated.")
        else:
            with open("mykey.key", "rb") as filekey:
                key = filekey.read()

        f = Fernet(key)

        # Encrypt the file
        with open(self.name, "rb") as file:
            pass_file = file.read()

        encrypt_data = f.encrypt(pass_file)

        with open(self.name, "wb") as file:
            file.write(encrypt_data)

        print(f"File '{self.name}' encrypted successfully.")

    def decrypt(self):
        if not os.path.exists("mykey.key"):
            print("Encryption key not found.")
            return

        # Read the encryption key
        with open("mykey.key", "rb") as filekey:
            key = filekey.read()

        f = Fernet(key)

        # Read the encrypted file
        with open(self.name, "rb") as file:
            encrypted = file.read()

        try:
            # Decrypt the file
            decrypt_data = f.decrypt(encrypted)

            # Write the decrypted data back to the file
            with open(self.name, "wb") as file:
                file.write(decrypt_data)

            print(f"File '{self.name}' decrypted successfully.")

        except Exception as e:
            print()


