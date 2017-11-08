#i made two program codes necessary to run my banking system namely
#bank sys.py 
#filestore.py 
#READ THROUGH THE INSTRUCTIONS PLEASE AS THEY SHOW HOW THE PROGRAM IS SET TO RUN
#this is my banking system code, it contains the bank sys.py and filestore.py codes together with 4 text files 
#####################################################################################################
#######################################################################################################
################    instructions to run the banking system program below ##############################
#create a new folder
#within this new folder, use notepad software and create 4 new text files namely:
#acc_name.txt, cusbalfile.txt, cusnamefile.txt and cuspassfile.txt
#get the bank sys.py program code below and also save it in the created folder
#get also the filestore.py program code and save it in the same created folder
#i uploded it in the this GITHUB banking system repository
#now you can run bank sys.py to start the banking system proces
############################################################################################################
############################################################################################################



##############################################################################################################
###########################################################################
#############     bank sys.py code        #############################################

#All data of this program is saved in text files and to run it you have to create all the following text files
#these text files include cusbalfile.txt,cuspassfile.txt,acc_name.txt and cusnamefile.txt
#the cusbalfile saves balances corresponding to the specific account name
#the cusnamefile saves the customer/account names
#the cuspassfile saves the users passwords
#the acc_name file saves the loan accounts data
#i created the filestore.py program which contains modules/methods that were imported to bank sys.py
#the modules and methods in filestore.py help manipulate the text files to lists and vice versa
#for ease in making changes and reading them
#####the text files, filestore.py and bank sys.py all have to be in the same folder to run the bank sys.py
#i created two banks namely prestige bank and west wood bank
#NB both these banks share the same database i.e the text files for storage
#for these two banks, one can open up any number of accounts
#it provides acces to savings and loan accounts

#importing filestore.py to bank sys.py
import filestore

#creating the bank class
class Bank(object):
    def __init__(self, BankId,Name, Location):
        self.BankId = BankId
        self.Name = Name
        self.Location = Location
        print("\nwelcome to "+self.Name+ ",bankId:"+self.BankId+ ","+self.Location)

#naming tellers for prestige
class Teller(object):
    def __init__(self,Id,Name):
        self.Id=Id
        self.Name = Name
        print("This is "+Name+", Teller Id: "+Id+ " at your service\n"
                                                "how may we help you today?")

        self.user_directions()

    def user_directions(self):
        print("\nTo make general inquiry press 1\nTo open an account or To apply for a loan and other loan related"
              " services press 2\nTo Deposit money press 3"
              "\nTo check for balance press 4\nTo request for a card press 5\nTo withdraw cash press 6\n"
              "To remove/delete your account from our data base press 7")
        user_need=input("")
        #now i hav started managing the different tasks starting with inquiries
        if user_need == "1":
            print("for better service deliver,use the customer care service desk\n"
                  "You can always use our customer care email for any inquiry and you will still be helped\n")
            exiting()
        #now am handling the both savings and loan account opening
        elif user_need=="2":
            print("We are glad that you are joining us, we offer different types of accounts\nTo open a savings account"
                  " press 1\nTo open a loan account and for other loan services press 2 ")
            acc_select=input(" ")

            #opening up a savings account
            if acc_select=="1":
                print("All Terms and conditions apply for this savings account")
                Account()
                exiting()
            #opening up loan account options to the user
            elif acc_select=="2":
                print("processing..............................\n")
                c=input("Welcome dear customer\nfor loan account opening press 1\n"
                      "for loan payments press 2\nTo check your loan balance remaining press 3:\n")
                #the new loan account is being made/opened
                if c=="1":
                    # loan method comes in
                    loan = loan_acc()
                    loan.accnamefilewrite()
                    exiting()

                #enabling loan account customer to check balance remaining
                elif c=="2":
                    #now making the payments
                    loan_payments()
                    exiting()
                elif c=="3":
                    loan_balance()
                    exiting()
                else:
                    print("you have selected an invalid input\n")
                    exiting()


            else:
                print("you have input an invalid selection")
                exiting()
        #depositing money stuff
        elif user_need=="3":
            deposit_saving()
            exiting()

        #checking balance
        elif user_need=="4":
            checking_balance()
            exiting()
        #processing customer card
        elif user_need=="5":
            print("we are processing your card,we will notify you when its done\n"
                  "Thanks\n")
            exiting()

        #withdraw code
        elif user_need=="6":
            withdraw_money()
            exiting()
        #remove account
        elif user_need=="7":
            delete_acc()
            exiting()

        else:
            print("there is no service matching your input")
            exiting()
            pass
    #finding my way out to open an account
class Account(object):
    def __init__(self):
        self.username, self.userpassword, self.balance = filestore.cusaccountcheck()
        print("We are previlaged, Mr/Mrs/Miss %s to have you join our customer base, your savings "
              "account is set and ready to use,\n" % self.username)

        #creating a list to save additional user data
        cus_details=[]
        cus_details.append(input("we need more additional information kindly answer the questions\n"
                                 "What is your first name:\n"))
        cus_details.append(input("Then your second name:\n"))
        cus_details.append(input("What is your address:\n"))
        cus_details.append(input("Input your phone number:\n"))
        print("Your name is {0} {1}, address:{2}, phoneNo: {3}, thank you for joining Us\nData saved".format(cus_details[0],cus_details[1],
                                                                       cus_details[2],cus_details[3]))

    #cash depositing method
    def depositcash(self):
        amount=float(input("\nPlease enter amount to be deposited\n: "))
        self.balance+=amount
        print("Your new account balance is %.2f shillings\n" %self.balance)
        filestore.balupdate(self.username, amount)

    #checking balance
    def checkbalance(self):
        print("Your account balance is %.2f shillings\n" % self.balance)

    #need to check if stuff inputed is correct
    def passcheck(self):
        """prompts user for password with every transaction and counterchecks it with stored passwords"""
        b=3
        while b>0:
            ans=input("Please type in your password to continue with the transaction\n: ")
            if ans==self.userpassword:
                return True
            else:
                print("wrong password")
                b-=1
                print ("%d more attempt(s) remaining" %b)

        print("you have typed in the wrong password three times,\n contact customer care for help")
        exit()
    #preparing withdraw method
    def withdrawcash(self):
        amount = float(input("Please enter amount to withdraw\n: "))
        self.balance -= amount
        print("Your new account balance is %.2f shillings" % self.balance)
        filestore.balupdate(self.username, -amount)

    #in case of deleting account here is the method
    def delete(self):
        filestore.deleteaccount(self.username)
        print("Your account has been successfuly deleted\n"
              "kindly give us feed back to improve our services")


pass


#since now these account already created need to check in the database, then i need to create another class
#the class to process the deposit function
class deposit_saving(Account):
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.oldcuscheck()
        self.depositcash()


##the class to process the checking balance function
class checking_balance(Account):
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.oldcuscheck()
        self.passcheck()
        self.checkbalance()

##the class to process the withdraw function
class withdraw_money(Account):
    def __init__(self):
        self.username, self.userpassword, self.balance = filestore.oldcuscheck()
        self.passcheck()
        self.withdrawcash()

##the class to process the delete function
class delete_acc(Account):
    def __init__(self):
        self.username, self.userpassword, self.balance = filestore.oldcuscheck()
        self.delete()

#setting the exit code
class exiting(Teller):
    def __init__(self):
        print("To exit this service and go back to main menu press y or n to terminate"
              " all processes")
        E = input(" ")
        if E == "y":
            self.user_directions()
        else:
            exit()


#selecting which teller to use in prestige bank
def first_options_prestige():
    print("For service from\nTeller 1 press 1\nTeller 2 press 2\nTeller 3 press 3")
    a = input("")
    if a == "1":
        teller=Teller("PT001","Prestige Teller 1")
    elif a == "2":
        teller = Teller("PT002", "Prestige Teller 2")
    elif a=="3":
        teller = Teller("PT003", "Prestige Teller 3")
    else:
        print("your input is not recorgonised,try again")
        exit()

#selecting teller for westwood bank
def first_options_westwood():
    print("For service from\nTeller 1 press 1\nTeller 2 press 2\nTeller 3 press 3")
    a = input("")
    if a == "1":
        teller=Teller("WWT001","WestWood Teller 1")
    elif a == "2":
        teller = Teller("WWT002", "WestWood Teller 2")
    elif a =="3":
        teller = Teller("WWT003", "WestWood Teller 3")

    else:
        print("your input is not recorgonised,try again")
        exit()

#initialising the loan stuff
#i saved all loan info in the the acc_name text file
class loan_acc(object):
    def __init__(self):
        # opening empty list
        accountNames = []
        # initialising the loan name file
        acc_name = open("acc_name.txt", "r")
        # updating list with file data
        for line in acc_name:
            accountNames.append(line[:-1])
        acc_name.close()

    # feeding the loan names file-acc_name.txt
    def accnamefilewrite(self):
        accountNames = []
        print("please input the details needed below to open up your loan account\n")
        #getting the loan apllicants account data to be written in the file
        name = input("Input your  loan account name[hint:user your first name for the loan account]:\n")
        acc_name = open("acc_name.txt", "a")
        acc_name.write("\n" + name)
        acc_name.close()
        #enabling him create the password
        password = input("create your loan acc password:\n")
        acc_password = open("acc_name.txt", "a")
        acc_password.write("\n" + password)
        acc_password.close()
        #enabling him take his loan
        balance = input("how much do yo want to borrow from us: \n")
        print("terms and conditions apply for this loan account\nIn case of any failure to pay in time\n"
              "Your security for this loan is taken and other law enforcements may apply\n")
        acc_balance = open("acc_name.txt", "a")
        acc_balance.write("\n" + balance)
        acc_balance.write("\n")
        acc_balance.close()
        accountNames.append(password)
        accountNames.append(name)
        accountNames.append(balance)
        print("your loan account balance is -{0} shillings, see you soon as you pay us\n".format(accountNames[int(accountNames.index(name)) + 1]))
#making loan payments
def loan_payments():
    accountNames = []
    acc_name = open("acc_name.txt", "r")
    for line in acc_name:
        accountNames.append(line[:-1])
    acc_name.close()
    name=input("Input your loan acc name:\n ")
    d=accountNames.index(name)
    e=int(input("how much do you want to deposit\n: "))
    f=d+2
    debit_standing=int(accountNames[f])-e
    print("your standing balance loan date now is -{0} shillings\n".format(debit_standing))
    print("Thank you being responsible and hard working to clear your dates\n")

#checking loan balance remaining
def loan_balance():
    accountNames = []
    acc_name = open("acc_name.txt", "r")
    for line in acc_name:
        accountNames.append(line[:-1])
    acc_name.close()
    name = input("Input your loan acc name:\n ")
    d = accountNames.index(name)
    f = d + 2
    print("your loan balance is -{0} shillings".format(accountNames[f]))


#first function to be run and aids you with which bank to select
def Choosing_bank():
    print("Welcome our dear esteemed customer\nBelow are the different banking service providers that are available\n"
          "For\nPrestige Bank services press 1\n" "westwood Bank services press 2")
    a=input('')
    if a == "1":
        Prestige_bank = Bank("001", "Prestige Bank", "Kasubi main branch\n")
        first_options_prestige()
    elif a == "2":
        Westwood_bank = Bank("002", "WestWood Bank", "Kololo main branch\n")
        first_options_westwood()

    else:
        print("Ooops,The input you have given is wrong boss, try again\n")
        Choosing_bank()
Choosing_bank()


############################## end of bank sys.py code ##################################################################
############################################################################################################
