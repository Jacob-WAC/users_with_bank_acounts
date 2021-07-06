class BankAccount:
    bankName = "Turtle Bank"
    masterAccountList = []

    def __init__(self, accountName, intRate='1%', balance=0):
        self.accountName = accountName
        self.intrestRate = BankAccount.convertPer2Dec(intRate)
        self.accountBalance = balance
        BankAccount.masterAccountList.append(self)

    def checkBalance(self):
        print(self.accountBalance)

    def deposit(self, amount):
        self.accountBalance += amount
        return self

    def withdraw(self, amount):
        self.accountBalance -= amount
        return self

    def displayAccountInfo(self):
        print(f'Account name is {self.accountName}')
        print(
            f'Current balance of account {self.accountName} is: {self.accountBalance}$')
        return self

    def yieldInterest(self):
        self.accountBalance += self.accountBalance * self.intrestRate
        return self

    @classmethod
    def sumOfAllAccounts(cls):
        sum = 0
        for x in cls.masterAccountList:
            sum += x.accountBalance
        print(sum)
        return sum

    @staticmethod
    def convertPer2Dec(percentage):
        temp = float(percentage.strip('%')) / 100.0
        return temp


class user:
    def __init__(self, name, accountName, intRate='1%', balance=0):
        self.name = name
        self.account = [BankAccount(accountName, intRate, balance)]

    def newAccount(self, accountName, intRate, balance):
        self.account.append(BankAccount(accountName, intRate, balance))


jacob = user('jacob', '0', '1%', 200)
jacob.account[0].displayAccountInfo()
jacob.newAccount('1', '2%', 500)
jacob.account[1].displayAccountInfo()
jacob.account[1].deposit(499)
jacob.account[1].checkBalance()
