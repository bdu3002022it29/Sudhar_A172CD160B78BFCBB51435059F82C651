class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__acccount_balance = initial_balance
    
  def deposit(self, amount):
    if amount > 0:
      self.__acccount_balance += amount
     #self.__account_balance = self.__account_balance + amount
      print("Deposited rupees{}. New balance : rupees {}". format (amount, self_account_balance))
      
    else:
      print("Invalid deposit amount")

  def withrdrawal (self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__acccount_balance -= amount
      print("withdrawal rupees{}. New balance: rupees{}". format(amount, self.__account_balace))
      
    else:
      print("Invalid withdrawal amount or insufficient balance")
      
  def display_balance(self):
    print("Account balance for {} (Account #{}): rupees{}". format(self.__accoun_holder_name, self.__account_number, self.__account_balance ))