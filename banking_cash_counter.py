""""
Create a Program which creates Banking Cash Counter where people come in to deposit Cash and withdraw Cash.
Have an input panel to add people to Queue to either deposit or withdraw money and dequeue the people.
Maintain the Cash Balance.

"""
from queue import Queue
from queue import Node

"""Creating object for Queue class"""
obj=Queue()

"""defining function """
def simulate_banking_cash_counter():
    """initially bank balance"""
    cash_balance=100000
    deposit=0
    withdraw=0
    while True:
        print("Welcome sir,We have following services!!")
        print("1.Deposit amount!!")
        print("2.withdraw amount!!")
        print("3.Exit")
        while True:
            try:
                choice=int(input("Enter a appropriate choice :"))
                if choice==1 or choice==2 or choice==3:
                    break
                else:
                    print("Enter a valid choice!!")
            except ValueError:
                print("Enter a valid choice!!")

        if choice==1:
            """Adding the person into queue"""
            add=Node(1)
            obj.enqueqe(add)
            while True:
                try:
                    amount=int(input("Enter the amount to be deposited:"))
                    if amount > 0:
                        break
                    else:
                        print("Amount should be more then zero!!")
                except ValueError:
                    print("Invalid input!!")
            """Updating bank balance"""
            cash_balance+=amount
            deposit+=amount
            print(f"You have successfully deposited :{amount}rs")
            obj.dequeue()

        elif choice==2:
            """Adding the person into queue"""
            add=Node(1)
            obj.enqueqe(add)
            while True:
                try:
                    amount_withdraw=int(input("Enter the amount to be withdraw:"))
                    if amount_withdraw > 0:
                        break
                    else:
                        print("Amount should be more then zero!!")
                except ValueError:
                    print("Invalid input!!")
            if cash_balance >= amount_withdraw:
                """Updating bamk balance"""
                cash_balance-=amount_withdraw
                withdraw+=amount_withdraw
                print(f"You have successfully withdraw :{amount_withdraw}rs")
                obj.dequeue()
            else:
                print("Sorry Insufficient balance!! ")
                obj.dequeue()

        else:
            return False

simulate_banking_cash_counter()