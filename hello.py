class bank:
    usernames = []

    def __init__(self, name, password, acc_bal=0):
        self.name = name
        self.password = password
        self.acc_bal = acc_bal
        bank.usernames.append(self)

    def withdraw(self, amount):
        i = 3
        while i > 0:
            if amount <= self.acc_bal:
                self.acc_bal = self.acc_bal - amount
                print(f"Dear {self.name} your new balance is {self.acc_bal}")
                break
            else:
                print("insufficient funds")
            i -= 1
        return self.acc_bal

    def login(self):
        """
        handles login logic for new users with existing accounts with the bank
        """
        pass

    def check_bal(self):
        """
        checking user's account balance
        """
        pass

    def create_account(self):
        """
        create a new account a new user in the bank
        """
        pass

    def __repr__(self):
        return f"{self.name}"


usr1 = bank("Okello Jonathan", 1234, 50000)
usr2 = bank("Angura stephen", 1235, 40000)
usr3 = bank("Ariiko derrick", 1236, 30000)

# usr1.withdraw(49500)
print(bank.usernames)
