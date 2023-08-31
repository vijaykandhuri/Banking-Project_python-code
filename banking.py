import random

class bank():
    def __init__ (self,Balance,Deposite,Withdraw):
        self.Balance=Balance
        self.Deposite=Deposite
        self.Withdraw=Withdraw
        #self.MiniStatement=Mini
    def displayinfo(self):
        print("--------------")
        print(f"starting balance:{self.Balance}")
        print(f"Deposite amount:{self.Deposite}")
        print(f"Total balance:{self.Withdraw}")       
        print("-----------------")
   
balance=0
        
class UserDetails():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def checkpass(self,password):
        return self.password==password
account=[]
statement=[]
loginaccount = None
while True:
    print("1.Create acount: \n2.Login: \n3.Exit or Cancel")
    select=int(input("Please Select:"))
    if select==1:
        username=input("Username:")
        password=input("Create Password:")
        account.append(UserDetails(username,password))
        print("Account created succesfully")
    elif select==2:
        username=input("Enter User Name:")
        password=input("Enter Password:")
        for i in account:
            if i.username==username and i.checkpass(password):
                loginaccount = i
                print("------------------------")
                print(f"{username} welcome to Python Bank")
                Account_number=[]
                for i in range (1):
                    Account_number.append(random.randint(100000,101100))
                    print("Account number is ",Account_number[i])
                    print("------------------------")
                    
                while True:
                    print("select below options \n 1.Balance \n 2.Deposite \n 3.With Draw \n 4.Mini Statement \n 5.Exit")
                    option=int(input("Select A Option:"))
                    if option==1:
                        print("your balance is:",balance,"rs/-")
                    elif option==2:
                        deposite=int(input("Enter Your Deposite Amount: "))
                        print("your previous balance is:",balance,"rs/-")
                        balance= balance+deposite
                        print("your Updated Balance",balance,"rs/-")
                    elif option==3:
                        withdraw=int(input("Withdra Amount:"))
                        if withdraw<=balance:
                            print("your previous balance is:",balance,"rs/-")
                            balance=balance-withdraw
                            print("your updated balance is:",balance)
                        else:
                            print("Insufficiat ")
                    elif option==4:
                        #Balance=balance
                        #Deposite=deposite
                        #Withdraw=withdraw
                        #totalbalance=balance+Deposite-withdraw
                        statement.append(bank(balance,deposite,withdraw,))
                        #p = bank(Deposite,Withdraw,Balance)
                        #p.displayinfo()
                        print("last transctions\n1.deposite blns:",deposite,"\n2.withdra  blns:",withdraw,"\n3.Remaning blns:",balance )
                    elif option==5:
                        print("Thanks and Login again")
                        break
                    else:
                        print("Invalid option selected Try Again")
                                
            if loginaccount is None:
                print("Invalid username or Password")
            #else:
                #print("login successfull")
            #break
            
    elif select==3:
        print("page closing and Restart again")
        break       
    else:
        print("enter valid details")


            
             
                
        
                
    


            
