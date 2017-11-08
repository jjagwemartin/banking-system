##this is the filestore.py program code

##creating empty lists everytime the program is initialized
cusnames=[]
cuspasswords=[]
cusbalance=[]

##opening the storage files to collect old customer data
namefile=open("cusnamefile.txt", "r")
passfile=open("cuspassfile.txt", "r")
balfile=open("cusbalfile.txt", "r")

##populate the empty lists with data from storage files
##check list of customer names
for line in namefile:
        cusnames.append(line[:-1])
namefile.close()

##check list of customer passwords
for line in passfile:
        cuspasswords.append(line[:-1])
passfile.close()

##check list of customer balances
for line in balfile:
        cusbalance.append(line[:-1])
balfile.close()


##function creates a new user
def cusaccountcheck():
        name=""
        pin=""

        name=input("Please type in your first name for this new bank account\n"
                   "And we will use it as your account name:\n")
        cusnames.append(name)
        filewrite(cusnames)

        #getting pin and running conditions to ensure 5 or more digits
        while len(pin)<4:
                pin=input("Please assign a password to this account, pin should be at least 5 characters\n")
                if len(pin)>4:
                        print("your pin has been successfully saved\n"
                              "NB:Always keep your password safe for increased account security")
                        cuspasswords.append(pin)
                        cusbalance.append(0)
                        balance=0
                        #cusbalance[cusnames.index(name)]=balance
                        filewrite(cuspasswords)
                        filewrite(cusbalance)
                        break

                print ("Sorry, get a password with more digits")
        balance = cusbalance[cusnames.index(name)]

        return name,pin, balance

##Function to check existing customer info
def oldcuscheck():
        name=""
        while name not in cusnames:
                name=input("Input your account name?\n")
                if name in cusnames:
                        username=name
                        userpassword=cuspasswords[cusnames.index(name)]
                        balance=float(cusbalance[cusnames.index(name)])
                        return username, userpassword, balance
                else:
                        print("Sorry %s, Check the account name, its not recorgnised in our database"%name)
                        again=input("Type in your account name again? (y/n)")
                        if again.lower()=='y':
                                oldcuscheck()
                        else:
                                print ("exiting............")
                                exit()




##This function writes new data into the storage files whenever called upon.
def filewrite(item):
        if item==cusnames:
                text=open("cusnamefile.txt","w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cuspasswords:
                text=open("cuspassfile.txt", "w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cusbalance:
                text=open("cusbalfile.txt", "w")
                for i in item:
                        text.write(str(i)+"\n")
                text.close()

###This function updates the account balance after a withdraw or deposit transaction
def balupdate(ind, amount):
        accountnumber=cusnames.index(ind)
        accountbal=float(cusbalance[accountnumber])
        accountbal+=amount
        cusbalance[accountnumber]=accountbal
        text=open("cusbalfile.txt", "w")
        for i in cusbalance:
                text.write(str(i)+"\n")
        text.close()

###This function deletes an existing account and any data that was stored about it is cleared
def deleteaccount(name):
        accountnumber=cusnames.index(name)
        del cusnames[accountnumber]
        filewrite(cusnames)
        del cusbalance[accountnumber]
        filewrite(cusbalance)
        del cuspasswords[accountnumber]
        filewrite(cuspasswords)
        return None
