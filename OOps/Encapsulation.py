
# Encapsulation means keeping data and methods together inside a class and controlling access to data .
# Python uses _ and _ conventions for protected/private members.

# Define a Bank Account class
class BankAccount:
    
    # Constructor
    def __init__(self, balance):
        
        # Private variable
        self.__balance = balance 
        
    # Method to display balance
    def show_balance(self):
        print("Balance:", self.__balance)
        
# Create an object 
account = BankAccount(5000)
account2 = BankAccount(2999)

# Access balance through a class method 
account.show_balance()                      # show_balance() provides controlled access             
account2.show_balance()       