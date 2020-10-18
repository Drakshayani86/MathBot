#converts decimal to binary/decimal/hexadecimal
def decimal_conversion():
    print("1.Decimal to Binary")
    print("2.Decimal to Hexadecimal")
    print("3.Decimal to Octal")
    #takes choice as input from user
    choice = int(input("Enter your choice : "))
    if(choice>=1 and choice<=3):
        #takes decimal number as input
        decimal_num = int(input("Enter a decimal number : "))
        if(choice == 1):
            try:
                #decimal to binary
                binary_val = bin(decimal_num).replace("0b", "")
                print("The binary value is :", binary_val)
            except ValueError:
                print("Invalid decimal number..")
        elif(choice == 2):
            try:
                #decimal to octal
                print("The octal value is :", oct(decimal_num))
            except ValueError:
                print("Invalid decimal number.. ")
        else:
            try:
                #decimal to hexadecimal
                print("The hexadecimal value is :", hex(decimal_num))
            except ValueError:
                print("Invalid decimal number.. ")
    
    #invalid choice
    else:
        print("Enter a valid choice")