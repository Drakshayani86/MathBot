def to_char():
    #takes choice as input from user
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        #finds the ascii value of a character
        value = input("Enter your character : ")
        print("Result :", ord(value))
    elif(choice == 2):
        value = int(input("Enter your number : ")) 
        #finds the character from a given number
        if(value>=0 and value<=127):
            print("Result :", chr(value))
        else:
            print("Enter a correct number")
    #invalid choice
    else:
        print("Enter valid choice")