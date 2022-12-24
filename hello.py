print("WELCOME HERE")
name = []
x = ["FIRST", "SECOND", "THIRD" ]




for a in x:
     
    names = input(F"enter the name of the {a.lower()} born\n\n")
    name.append(names)
name.append("angura")
x.append("FOURTH")

i = 0
for n in x:

    if(i != 3):    
        print(f"your {n.lower()} born is {name[i].capitalize()}")
        i = 1+i
        
    else: 
       print(f"you had forgotten your son {name[i].capitalize()}")



    


