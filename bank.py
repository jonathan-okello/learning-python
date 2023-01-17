print('WELCOME TO ANGURA BANK')

#i = 3
#while (i > 0):
selection = input('LOGIN\nWhat would you like to do\nTo login press L\nTo deposit press D\nTo withdraw press W\n')
if (selection == 'L'):
    print('LOGIN')
elif (selection == 'D'):
    print('DEPOSIT')
elif (selection == 'W'):
    print('WITHDRAW')
elif (selection == 'B'):
    print('CHECK ACCOUNT BALANCE')
else: pass
    #print(f're-enter your option\nyou have only {i-1} chances left\n ')
    #i=i-1
usernames = ['jona', 'deric', 'paul']
passcodes = ['1234', '1245', '1235']
balances = ['20000', '30000', '40000']
#i = 0
#for name in usernames:
#n = 0
#while (n < 3):
if (selection == 'L'):
    name = input('please enter your name\n')
    if name in usernames:
        print('CORRECT USERNAME')
        code = input('please enter your PIN\n')
        if code in passcodes:
            print(f'ACCESS GRANTED\nwhat would you like to do')
            choice = input('to check your account balance press A\nto withdraw press W\nTo deposit press D')
            if (choice == 'A'):
                print(f'your account balance is {balances[0]}\nTHANK YOU FOR CHOSING ANGURA BANK')
            elif (choice == 'W'):
                amount = int(input('How much do you want to withdraw'))
                if (amount < balances[0]):
                print(f'Receive the cash\nYour new balance is {balances[0]-amount}')
            else: print('INSUFFICIENT FUNDS')
else: print('INVALID USERNAME')
        #code = input('enter your passcode\n')
    #n = n+1

# TO LOGIN
def login():
    i = 3
    usernames = ['jona', 'deric', 'paul']
    passcodes = ['1234', '1245', '1235']
    balances = [20000, 30000, 40000]
    print("WELCOME\n TO LOGIN")

    while True:
        name = input("enter your name\n")
        if name in usernames:
            print('CORRECT USERNAME')

            while i > 0:
                code = input('please enter your PIN\n')
                if code == passcodes[usernames.index(name)]:
                    print(f'ACCESS GRANTED\nwhat would you like to do')
                    choice = input('to check your account balance press A\nto withdraw press W\nTo deposit press D\n')
                    break
                else:
                    print(f"wrong passcode please retry left with {i - 1} attempts")
                i -= 1
            break
        else:
            print('INVALID USERNAME\n try again')


print("WOWOWOWOWO")


