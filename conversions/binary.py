#converts binary to decimal/octal/hexadecimal
def binary_conversion():
    print("1.Binary to Decimal")
    print("2.Binary to Octal")
    print("3.Binary to Hexadecimal")
    #takes user's choice
    choice = int(input("Enter your choice : "))
    if(choice>=1 and choice<=3):
        #takes the binary number as input
        bin_string = input("Enter a binary number : ")
        if(choice == 1):
            try:
                #binary to decimal
                decimal_val = int(bin_string, 2)
                print("The decimal value is :", decimal_val)
            except ValueError:
                print("Invalid binary number..")
        elif(choice == 2):
            try:
                #binary to decimal
                decimal_val = int(bin_string, 2)
                #decimal to octal
                print("The octal value is :", oct(decimal_val).replace("0o", ""))
            except ValueError:
                print("Invalid binary number..")
        else:
            try:
                #binary to decimal
                decimal_val = int(bin_string, 2)
                #decimal to hexadecimal
                print("The hexadecimal value is :", hex(decimal_val).replace("0x", ""))
            except ValueError:
                print("Invalid binary number..")
    
    #invalid choice
    else:
        print("Enter a valid choice")