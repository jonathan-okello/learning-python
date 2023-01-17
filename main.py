def transactions(balances, usernames, name):
    """
    gives the different trasanctions
    """
    while True:
        selection = option()
        if selection != False:
            if selection == "W":
                money_left = withdraw(name)
                balances[usernames.index(name)] = money_left
            # print(balances)
            elif selection == "A":
                account_bal(balances)
            elif selection == "D":
                moneyin = deposit(name)
                balances[usernames.index(name)] = moneyin
                # print(balances)
        break


# TO WITHDRAW
def withdraw(name):
    i = 3
    while i > 0:
        while True:
            try:
                amount = int(input("enter the amount\n"))
                break
            except:
                print("entry is not in figures please re-enter")
            i -= 1
        x = balances[usernames.index(name)]
        if amount <= x:
            print(f"take your cash\n Your account balance is {x-amount} \nTHANKS\n\n")
            money_left = x - amount
            break
        else:
            print("..................\n insufficient funds try again")
        i -= 1
    return money_left


# TO DEPOSIT
def deposit(name):
    i = 3
    while i > 0:
        while True:
            try:
                amount = int(input("enter the amount\n"))
                break
            except:
                print("entry is not in figures please re-enter")
            i -= 1
        x = balances[usernames.index(name)]
        print(f"Your new account balance is {x+amount} \nTHANKS\n\n")
        new_amount = x + amount
        break
        i -= 1
    return new_amount


# TO CHECK THE ACCOUNT BALANCE
def account_bal(balances):
    print(f"Your account balance is {balances[usernames.index(name)]}")


# TO LOGIN
i = 3
usernames = ["jona", "deric", "paul"]
passcodes = ["1234", "1245", "1235"]
balances = [20000, 30000, 40000]


def option():
    """
    asks user for the choice he would like to make
    returns choice made by the user
    """
    choice = False
    i = 3
    while i > 0:
        choices = ["A", "W", "D"]
        choce = input(
            "To check your account balance press A\n\nTo withdraw press W\n\nTo deposit press D\n"
        ).upper()
        if choce in choices:
            choice = choce
            break
        else:
            print("Wrong selection please try again")
        i -= 1
    return choice


def login(usernames, passcodes):
    i = 3
    while True:
        name = input("enter your name\n").lower()
        if name in usernames:
            print("CORRECT USERNAME")

            while i > 0:
                code = input("please enter your PIN\n")
                if code == passcodes[usernames.index(name)]:
                    print(f"ACCESS GRANTED\nwhat would you like to do")
                    break
                else:
                    print(f"wrong passcode please retry left with {i - 1} attempts")
                i -= 1
            break
        else:
            print("INVALID USERNAME\n try again")

    return name


while True:
    print("WELCOME TO ARIKO BANK\n\n TO LOGIN")
    name = login(usernames, passcodes)
    transactions(balances, usernames, name)
    to_proceed = input(
        "would you like to do another transactio\n if YES press Y\n if NO press N\n"
    ).lower()
    if to_proceed == "y":
        transactions(balances, usernames, name)


# OPTIONS
