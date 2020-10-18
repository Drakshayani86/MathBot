#converts hexadecimal to binary/decimal/octal
def hexa_conversion():
    print("1.Hexadecimal to Binary")
    print("2.Hexadecimal to decimal")
    print("3.Hexadecimal to Octal")
    #takes choice as input from user
    choice = int(input("Enter your choice : "))
    if(choice>=1 and choice<=3):
        #takes hexadecimal(string) as input
        hex_num = input("Enter a hexadecimal number : ")
        if(choice == 1):
            try:
                #hexadecimal to decimal
                decimal_val = str(int(hex_num, 16))
                #decimal to binary
                binary_val = bin(int(decimal_val)).replace("0b", "")
                print("The binary value is :", binary_val)
            except ValueError:
                print("Invalid hexadecimal number..")
        elif(choice == 2):
            try:
                #hexdecimal to decimal
                decimal_val = str(int(hex_num, 16))
                print("The decimal value is :", decimal_val)
            except ValueError:
                print("Invalid hexadecimal number.. ")
        else:
            try:
                #hexdecimal to decimal
                decimal_val = str(int(hex_num, 16))
                #hexdecimal to binary
                octal_val = oct(decimal_val).replace("0o", "")
                print("The octal value is :", octal_val)
            except ValueError:
                print("Invalid hexadecimal number.. ")
    #invalid choice
    else:
        print("Enter a valid choice")