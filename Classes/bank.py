class BankAccount:
  def __init__(self, account_holder = None, savings = 20, chequing = 0):
    self.account_holder = account_holder
    self.savings = savings
    self.chequing = chequing

  def deposit(self, amount):
    self.chequing += amount
    return self.chequing
  
  def withdraw(self, amount):
    if self.chequing >= amount:
      self.chequing -= amount
    else:
      print('you too broke man')
    return self.chequing
  
  def displayBalance(self, account):
    if account == 'savings':
      return self.savings
    else:
      return self.chequing
  
  def transferTo(self, amount, account):
    if account == "savings" and self.chequing >= amount:
      self.savings += amount
      self.chequing -= amount
    elif account == "chequing" and self.savings >= amount:
      self.savings -= amount
      self.chequing += amount
    else:
      print('you too broke man')

  def terminate(self):
    total = self.savings + self.chequing

    self.savings, self.chequing, self.account_holder = 0, 0 , None

    print(f"you will recieve ${total} \nyour account has been terminated")


veersBankAccount = BankAccount("Veer", 10000, 20)

veersBankAccount.transferTo(100, 'chequing')

print(veersBankAccount.displayBalance('chequing'))

veersBankAccount.terminate()