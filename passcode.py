def login(names, passcodes):
    """
    Perfomrs the magic of handling login logic
    """
    flag = False
    i = 3
    n = 3
    while (i > 0):
        name = input("enter your name\n")
        if (name in names):
            while (n > 0):
                passcode = input('enter your PIN\n')
                if (passcode == passcodes[names.index(name)]):
                    print('ACCESS GRANTED\n')
                    flag = True
                    break
                else: 
                    print(F'wrong PIN\n{n-1} attempts left')
                n-=1
        else: 
            print(f'wrong name\n{i-1} attempts left')
        i-=1
    return flag

print("WELCOME\nLOGIN")
names = ["steve", "jona", "deric"]
passcodes = ["1234", "5678", "9090"]

flag = login(names, passcodes)
if (flag):
    print("THANK YOU FOR CHOSING ANGURA BANK")
else:
    print("YOU ARE A FOOL JUST GO AWAY")
    
