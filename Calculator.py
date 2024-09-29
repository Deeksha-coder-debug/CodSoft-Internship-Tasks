#function to input 2 no.s for operation
def ask():
    a=int(input("Enter 1st no. : "))
    b=int(input("Enter 2nd no. : "))
    return a,b    #returns no.s to 
def forward():
    ask=input("\nDo you want to continue: y or n   ")
    ask=ask.lower()
    if(ask=="y" or ask=="yes"):
        call()
    else:
        print("\nCalculator is closed")
        exit() 

def msg():
    print("Press\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n")
    opt=int(input("Enter your choice :"))
    return opt
def operation(opt):
    match opt:
        case 1:
            print("Addition")
            a,b=ask()
            print(f"Addition of {a} and {b} is {a+b}")
        case 2:
            print("Subtraction")
            a,b=ask()
            print(f"Subtraction of {a} and {b} is {a-b}")
        case 3:
            print("Multiplication")
            a,b=ask()
            print(f"Multiplication of {a} and {b} is {a*b}")
        case 4:
            print("Division")
            a,b=ask()
            print(f"Division of {a} and {b} is {a/b}")
        case _:
            print("Invalid option")
    forward()
def call():
    opt=msg()
    operation(opt)
print("Welcome to Calculator")
call()