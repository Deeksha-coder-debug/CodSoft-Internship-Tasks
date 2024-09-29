tnc=[]
tc=[]
def ask():
    a=input("Do you want to continue: y or n   ")
    a=a.lower()
    if(a=="y" or a=="yes"):
        msg()
    elif(a=='n' or a=='no'):
        print("To do List is closed")
        exit() 
    else:
        print("Invalid answer\nTry again ...")
        ask()
def msg():
    print("\nPress\n1 for Adding tasks\n2 for Removing tasks\n3 for viewing tasks\n4 for Mark Task as Complete ")
    opt=int(input("Enter your choice:  "))
    manage(opt)
def manage(opt):
    match opt:
        case 1:
            tnc.append(input("Enter task:  "))
            print("Task Successfully added")
            
        case 2:
            print("Removing tasks....")
            if not tnc:
                print("No tasks remaining")
            else:
                print("\nYou have these tasks to do ")
                for i,val in enumerate(tnc):
                    print(f"{i+1} - {val}")
                s=int(input("Which one do you want to remove (write its serial no.) : "))
                tnc.pop(s-1)
                print("Removed")
        case 3:
            print("Whick one do you want to view:\n")
            o=int(input("Press \n1 for Completed\n2 for Uncompleted tasks\n3 for Both  --- "))
            if(o==1):
                if not tc:
                    print("No completed tasks")
                else:
                    for i,val in enumerate(tc):
                        print(f"{i+1} - {val}")
            elif(o==2):
                if not tnc:
                    print("No tasks remaining")
                else:
                    for i,val in enumerate(tnc):
                        print(f"{i+1} - {val}")
            elif(o==3):
                print("Completed Tasks ...")
                if not tc:
                    print("None\n")
                else:
                    for i,val in enumerate(tc):
                        print(f"{i+1} - {val}")
                print("Tasks to be completed ...")
                if not tnc:
                    print("None\n")
                else:
                    for i,val in enumerate(tnc):
                        print(f"{i+1} - {val}")
            else:
                print("Invalid option")
        case 4:
            print("Marking tasks as completed ....")
            if not tnc:
                print("No tasks remaining")
            else:
                print("\nYou have these tasks to do ")
                for i,val in enumerate(tnc):
                    print(f"{i+1} - {val}")
                s=int(input("Which task did you complete (write its serial no.) : "))
                tc.append(tnc[s-1])
                tnc.pop(s-1)
                print("Done")
        case _:
            print("Invalid option")
    ask()
print("To do list app welcomes you")
msg()
