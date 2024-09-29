import random
name=input("enter ur name:")
print(f"Hello {name},")
print("\nEnjoy playing Rock Paper Scissors game\nInstructions for Player are:\n1. In this game, there are 2 players - yourself and computer\n2. The user is allowed to make choice first\n3. Out of the available choices, computer makes its choice\n4. There will be 3 choices in total : Rock, Paper and Scissors\n5.\tRock vs Scissors -> Rock wins\n\tRock vs Paper -> Paper wins\n\tScissors vs Paper -> Scissor wins\n Select your choice : \n Press 1 for Rock\n\t\t2 for Paper\n\t\t3 for Scissors\n")

# function to print and store computer's choice
# also calls win() which decides and prints the winner
def comp(opt,comp_p,user_p):
    # list containing all choices
    listo=[1,2,3]
    # choosing random no. from listo
    n=random.choice(listo)
    # prints computer's choice
    print(f"computer's choice : {n}")
    #user(n,comp_p,user_p,"computer")
    print("Computer chose ",end="")
    print("Rock") if n==1 else print("Paper") if n==2 else print("Scissors")
    print()
    win(opt,n,comp_p,user_p)
def points(comp_p,user_p):
    sc=sum(comp_p)
    su=sum(user_p)
    print(f"Computer scored {sc} points\n{name} scored {su} points\n")
    print("Computer wins") if(sc>su) else print(f"{name} wins") if(sc<su) else print("Both scored equal points")
def ask(comp_p,user_p):
    a=input("\nDo you want to continue: y or n   ")
    a=a.lower()
    if(a=="y" or a=="yes"):
        print("Select your choice : \n Press 1 for Rock\n\t\t2 for Paper\n\t\t3 for Scissors\n")
        opt=int(input("enter ur choice:"))
        user(opt,comp_p,user_p)
        comp(opt,comp_p,user_p)
    elif(a=='n' or a=='no'):
        print("\nGame has been closed")
        points(comp_p,user_p)
        exit()  
    else:
        print("Invalid answer\nTry again ...")
        ask(comp_p,user_p)
# function to decide winner 
# opt is user's choice and n is computer's
def win(opt,n,comp_p,user_p):
    if(opt==1):
        if(n==2):
            print("Paper i.e. computer wins")
            comp_p.append(1)
        elif(opt==n):
            print("It's a tie")
        else:
            print(f"Rock i.e. {name} wins")
            user_p.append(1)
    elif(opt==2):
        if(n==1):
            print(f"Paper i.e. {name} wins")
            user_p.append(1)
        elif(opt==n):
            print("It's a tie")
        else:
            print("Scissors i.e. computer wins")
            comp_p.append(1)
    else:
        if(n==1):
            print("Rock i.e. computer wins")
            comp_p.append(1)
        elif(opt==n):
            print("It's a tie")
        else:
            print(f"Scissors i.e. {name} wins")
            user_p.append(1)
    print()
    print(f"Computer points : {sum(comp_p)}\n{name} points : {sum(user_p)}")
    ask(comp_p,user_p)
    
            
# storing user's choice in integer format
opt=int(input("enter ur choice:"))

# similar to switch case
def user(opt,comp_p,user_p):
    print("User chose ",end="")
    print("Rock") if opt==1 else print("Paper") if opt==2 else print("Scissors") if opt==3 else print("Invalid option") 
    print()
    comp(opt,comp_p,user_p)
    
    
comp_p=[0]
user_p=[0]
user(opt,comp_p,user_p)
