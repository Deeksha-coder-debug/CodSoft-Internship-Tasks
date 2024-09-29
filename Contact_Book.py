#asks the user whether they want to continue or not
#if yes it will continue else it will exit the program
def ask():
    a=input("Do you want to continue: y or n   ")
    a=a.lower()
    if(a=="y" or a=="yes"):
        opt=message()
        return opt
    elif(a=='n' or a=='no'):
        print("Closing Contact Book")
        exit()  #we can also use quit() or sys.exit() of sys module
    else:
        print("Invalid answer\nTry again ...")
        ask()    
      
        
#displaying options available and asking for input of choice
def message():
    print("What do you want?\nPress\n1 for Add contact\n2 for view contacts\n3 for Search Contact\n4 for Update \n5 for Delete contact")
    print()
    opt=int(input("Enter your choice:"))
    return opt

        
# calls functions according to user's choice by match stmt
def view(opt,count):
   
    match opt:
        case 1:
            # keeps count of no. of contacts
            count+=1 
            # input of required fields
            name=input("Enter name:")
            ph=input("Enter phone number:")
            # checks if ph no. is valid or not 
            #if not then asks again
            if(len(ph)>10 or len(ph)<10):
                ph=input("Please enter correct phone number:")
            email=input("Enter email id:")
            city=input("Enter city:")
            # updates the dictionary with new data 
            # here key is contact1 ,etc
            #inside is a nested dict
            book.update({f"Contact{count}":{"name":name,"ph":ph,"email":email,"city":city}})
            print()
            print(f"Contact details are saved successfully\n{count} contacts")
            print()
            # call for func to continue or not
            opt=ask()
            # if yes then calls itself recursively
            view(opt,count)
            
        case 2:
            # checks if dict is empty
            if not book:
                print("No contacts")
            else:
                # views all available contacts in dict
                for i in book:
                    print(f"{i}:\n{book[i]}")
            print()
            opt=ask()
            view(opt,count)
        case 3:
            if not book:
                print("No contacts")
            else:
                # field by which you want to search contacts
                search=input("enter by which info you want to search contact :  by name or ph(phone no.):")
                # input value of specified field
                val=input(f"enter {search} for that contact:")
                print()
                # changing field name to lower as it is stored as lower in dict
                search=search.lower()
                #variable to keep track of contacts i.e. if it have reached to the last contact and no more contacts are present
                c=0
                for i in book:
                    #for every contact, it is incremented by 1
                    c+=1
                    #comparing values of contact book with user entered value
                    if(((book[i][search]).upper())==val.upper()):
                    
                        # if yes then display details
                        print(f"Contact found \nDetails are:\n{book[i]}")
                    else:
                        #checks for if reached to end of contact book
                        if(c==len(book)):
                            print("Not found")
            print()
            opt=ask()
            view(opt,count)
        case 4:
            if not book:
                print("No contacts")
            else:
                search=input("enter by which info you want to search contact : by name or ph(phone no.):")
                val=input(f"enter {search} for that contact:")
                search=search.lower()
                c=0
                print()
                for i in book:
                    c+=1
                    if(((book[i][search]).upper())==val.upper()):
                        
                        print(f"Contact found \n\nDetails are:\n{book[i]}")
                        print()
                        #asking for field to be updated
                        up=input("which information do you want to edit:")
                        # asks for updated value of specified field
                        val=input(f"enter updated {up} :")
                        # assigned the updated value i.e. value is updated
                        book[i][up]=val
                        print()
                        print("Contact details updated successfully")
                    else:
                        if(c==len(book)):
                            print("Contact not found")
            print()    
            opt=ask()
            view(opt,count)
        case 5:
            if not book:
                print("No contacts")
            else:
                search=input("enter by which info you want to search contact : by name or ph:")
                val=input(f"enter {search} for that contact:")
                print()
                search=search.lower()
                c=0
                for key in list(book.keys()):
                    c+=1
                    #checks for if specified contact exists or not
                    if(((book[key][search]).upper())==val.upper()):
                        print("Contact found")
                        # asks for confirmation to delete contact
                        ch=input("Do you want to delete that contact y or n :")
                        ch=ch.lower()
                        if(ch=='y' or ch=='yes'):
                            # if yes then delete is performed
                            del book[key]
                            print()
                            print("Contact deleted successfully")
                    else:
                        if c==len(book):
                            print("\nNot found")
            print()
            opt=ask()
            view(opt,count)
        case _:
            print("Invalid choice")
book={}

print("Opening Contact Book\n")
opt=message()
count=0
view(opt,count)
# end of the project