import datetime
import json
import getpass
import inquirer
import time
import random
import string


# banking system 
class bank:
    with open ("acc.txt","r") as accfile:
        accstr = accfile.read()
        # print(accstr)
        if len(accstr)<1:
            accstr = '{"user":["fname lname","age","gender","city","password"]}'
        else:
            pass
        _acc_DB = {}
        _acc_DB = json.loads(accstr)
        # print(_acc_DB)


    #Constructor
    def __init__(self,user):
        
        self.user = user
        temp = self.user
        if temp.endswith("@bankid"):
            print("Everything is okay")
        else:
            temp = temp + "@bankid"
        self.user = temp

     

        if self.user in self._acc_DB:

            if self._acc_DB[self.user][2] == "male":
                self.gender = "Mr."
            elif self._acc_DB[self.user][2] == "female":
                self.gender = "Ms."
            else:
                self.gender == ""
            self.Welcome = f"Welcome {self.gender}{self._acc_DB[self.user][0]}"
            
            print(self.Welcome)
            # You can start banking
            self.authenticate()

        else:
            print("Looks like you are not our customer.Do you want to create a account to our bank ?\n")
            action = input("Press 0 if you want to create a account ! otherwise press any key to exit.\n")
            if action == "0":
                self.CreateAcc()
            else:
                print("Thank You.")
                __name__

    def CreateAcc(self):
        try:
            # setting new values / new customer data for new accounts creater
            new_username = input("Set your username (it's your user id for banking):\n")
            new_fullname = input("Entre here you name: ")
            new_c_age = int(input("Enter here your age: "))
            genderSelect = [
                inquirer.List("gender",
                              message="Select your gender ? :",
                              choices = ["male","female","Not mentiond"],

                ),
            ]
            new_c_gender = inquirer.prompt(genderSelect)
            new_c_gender = new_c_gender["gender"]
            # print(new_c_gender["gender"])
            new_c_city = input("Enter your city: ")
            print("You are all set Now final step Set your password:\n")
            passwd = input("Set a password : ")
            self.userID = self.user + "@bankid"
            print(f"Your userID is {self.userID}")
            print(new_fullname,new_c_age,new_c_gender,new_c_city)

            confirm = [
                inquirer.List("confirmation",
                                message = "Check you details and confirm to go ahead ?",
                                choices = ["Yes","No"],

                )

            ]
            confirmation = inquirer.prompt(confirm)
            if confirmation["confirmation"] == "Yes":
                print("We are setting up the things...")
                time.sleep(3)
                acc_number = ''.join(random.choices(string.digits,k=11))
                balance = int(input("Initial Deposite Balance::"))
                try:
                    self._acc_DB.update({self.userID:[new_fullname,new_c_age,new_c_gender,new_c_city,passwd,acc_number,balance]})
                    print("Account Created Succesfully.")
                    with open("acc.txt","w") as accfile:
                        acc_writer = json.dumps(self._acc_DB)
                        accfile.write(acc_writer)


                except Exception as e:
                    print("Error",e)

            else:
                self.CreateAcc()

            self.banking()
        except Exception as e:
            print(e)
            print("Something Went Wrong")
            self.CreateAcc()

    def authenticate(self):
        auth = getpass.getpass()
        if auth == self._acc_DB[self.user][4]:
            self.banking()
        else:
            print("Password wrong !")
            __name__


    def banking(self):
        print(self.Welcome)
        self.accN = self._acc_DB[self.user][5]
        self.bal = self._acc_DB[self.user][6]
        bankOpr = [
            inquirer.List("Banking",
            message = "Banking Service :",
            choices = ["View Bank Profile","Check your Bank Balance","Cash Widrawal","close"],
            )
        ]
        activity = inquirer.prompt(bankOpr)
        if activity["Banking"] == "View Bank Profile":  # this will show your profile 
            print(f"Your Name    :{self._acc_DB[self.user][0]}")
            print(f"Your Age     :{self._acc_DB[self.user][1]}")
            print(f"Your Gender  :{self._acc_DB[self.user][2]}")
            print(f"Your City    :{self._acc_DB[self.user][3]}")
            print(f"Your Acc NO  :{self._acc_DB[self.user][5]}\n")
            self.banking()


        elif activity["Banking"] == "Check your Bank Balance":
            print(f"{self.gender}{self._acc_DB[self.user][0]}")
            
            print(f"Your Acc Number :{self.accN}")
            
            print(f"Bank Balance :{self.bal}")
            self.banking()



        elif activity["Banking"] == "Cash Widrawal":
            wid_amt = int(input("Enter here how much amount do you want to widraw: "))
            self.bal = self.bal - wid_amt
            self._acc_DB[self.user][6] = self.bal
            print(f"Remainig Balance :{self.bal}")
            self.banking()
        else:
            __name__


            
         

if __name__ == "__main__":
    while True:
        user = input("Enter your name here: ")
        client = bank(user)
        with open("acc.txt","w") as accfile:

            acc_writer = json.dumps(client._acc_DB)
            accfile.write(acc_writer)  
        quit = [
            inquirer.List("action",
                           message = "Do you want to close ?",
                           choices = ["Yes","No"],
                           )
        ]
        action = inquirer.prompt(quit)
        if action["action"] == "Yes":
            break
        else:
            __name__