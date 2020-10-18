#converts octal to binary/deciaml/hexadecimal
def octal_conversion():
    print("1.Octal to Binary")
    print("2.Octal to Decimal")
    print("3.Octal to Hexadecimal")
    #takes choice as input
    choice = int(input("Enter your choice : "))
    if(choice>=1 and choice<=3):
        #takes ictal number as input
        octal_num = input("Enter an octal number : ")
        if(choice == 1):
            try:
                #octal to decimal
                decimal_val = int(octal_num, 8)
                #decimal to octal
                binary_val = bin(decimal_val).replace("0b", "")
                print("The binary value is :", binary_val)
            except ValueError:
                print("Invalid octal number..")
        elif(choice == 2):
            try:
                #octal to decimal
                decimal_val = int(octal_num, 8)
                print("The decimal value is :", decimal_val)
            except ValueError:
                print("Invalid octal number.. ")
        else:
            try:
                #octal to decimal
                decimal_val = int(octal_num, 8)
                #octal to hexadecimal
                hex_val = hex(decimal_val).replace("0x", "")
                print("The hexadecimal value is :", hex_val)
            except ValueError:
                print("Invalid octal number.. ")
    #invalid choice
    else:
        print("Enter a valid choice")