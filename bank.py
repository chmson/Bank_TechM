"""
1.create acnt 
2.View Acnt details by Acno 
3.Deposit
4.Withdraw
5.Fund tranfer
6.print transactions
7.exit 

"""

class BankAcc:
    def __init__(self,acc_num,acc_holder,balance=0.0):
        self.acc_num = acc_num
        self.acc_holder = acc_holder
        self.balance = balance
        self.transactions = [ ]

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            print(f"\n\n Deposited {amount}. New Balance is {self.balance}.")
        else:
            print("\n Deposit amount must be positive")

    def withdraw(self,amount):
        if amount > 0 :
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrew {amount}")
                print(f" \n\n Withdrew {amount}. New Blance is {self.balance}.")
            else:
                print(f"\n\n Insufficient Funds in account, current balance is {self.balance}.")
        else:
            print("\n Withdraw amount should be positive")

    def get_balance(self):
        return self.balance
    
    def transfer(self,target_acc, amount):
        if amount > 0 :
            if amount <= self.balance :
                self.balance -= amount
                target_acc.balance += amount
                self.transactions.append(f"Transfered {amount} to {target_acc.acc_num}.")
                target_acc.transactions.append(f"Recieved {amount} from {self.acc_num}.")

                print(f"\n\n Transferred {amount} to {target_acc.acc_num}. New balance is {self.balance}.")

        else:
            print("\n\n enter a valid transfer amount")

    def print_transactions(self):
        print(f"\n\n\nTransaction history for account {self.acc_num} :")
        for transaction in self.transactions :
            print(transaction)





    

    
accounts = {}

while True:
    print("\n Bank Operations :\n1.Create account \n 2.View Acnt details by Acno\n 3.Deposit\n 4.Withdarw\n 5.Fund tranfer\n 6.print transactions\n 7.exit" )

    choice = input("Enter your choice (1-7): ")

    if choice == "1" :
        acc_num = input("Enter acc num : ")
        acc_holder = input("Enter acc holder name: ")

        accounts[acc_num] = BankAcc(acc_num,acc_holder)
        print("\n \n Account created succesfully.")

    elif choice == "2" :
        acc_num = input("Enter acc num: ")
        if acc_num in accounts:
            account = accounts[acc_num]
            print(f"\n \n Account number: {account.acc_num}") 
            print(f"\nAccount Holder : {account.acc_holder}")
            print(f"\nAccount Balance : {account.get_balance()}")

        else:
            print("\n\nAccount not found.")
            
    elif choice == "3" :
        acc_num = input("Enter acc num :")
        if acc_num in accounts:
            amount = int(input("Enter amount to deposit: "))
            accounts[acc_num].deposit(amount)
        else:
            print("\n\nAcc not found")

    elif choice == "4" :
        acc_num = input("Enter acc num: ")
        if acc_num in accounts:
            amount = int(input("Enter amount to Withdraw: "))
            accounts[acc_num].withdraw(amount)
        else:
            print("\n\nAcc not found")

    elif choice == "5" :
        from_acc_num = input("Enter your acc num: ")
        to_acc_num = input("Enter target acc num : ")
                
        if from_acc_num in accounts and to_acc_num in accounts :
            amount = int(input("Enter amount to transfer: "))

            from_acc = accounts[from_acc_num]
            to_acc = accounts[to_acc_num]

            from_acc.transfer(to_acc,amount)

        else:
            print("\n\nPls re-check the Acc numbers.")

    elif choice == "6" :
        acc_num = input("Enter acc num: ")
        if acc_num in accounts:
            accounts[acc_num].print_transactions()
        else:
            print("Acc not found.")

    elif choice == "7" :
        print(".......Exiting.........")
        break

    else:
        print("Invalid choice, Enter a valid option btwm 1-7.")







    
        
