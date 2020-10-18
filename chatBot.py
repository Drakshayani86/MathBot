"""
    This is a program for a chatbot...
    1. The bot will start with a greeting and self introduction and ask for name of the user
    2. The bot will greet and welcome the person
    3. Bot will ask what a person want to do, it will offer a set of choices based upon what the bot is designed for
    4. It will respond to the user input appropriately

Author: Mannam Drakshayani
"""

#importing required modules and files
import random
import math
from datetime import datetime
from greetings import greet_and_introduce, welcome
from trignometry import trignometric_val
from evaluate import evaluate_expression
from ascii import to_char
from conversions.binary import binary_conversion
from conversions.decimal import decimal_conversion
from conversions.octal import octal_conversion
from conversions.hexadecimal import hexa_conversion


#Displays the set of operations for which the bot is designed for
def show_operations():
    print("1.Expression")
    print("2.Trignometric")
    print("3.ASCII")
    print("4.Conversions")
    print("5.Quit")
    #throws an exception when the user chooses invalid option
    try:
        return int(input("Enter your choice [1-5]: "))
    except:
        print("Only enter choice between 1 to 5")
        return 0;
   
#bot performs respective operations according to the user choice
def bot():
    #calling greet_and_introduce function from greetings.py
    greet_and_introduce()
    #takes user name as input
    name = input("Your name: ")
    #calling welcome function from greetings.py
    welcome(name)
    #calling show_operations function
    choice = show_operations()
    while choice != 5 :
        if choice == 1 :
            #calling evaluate_expression() from evaluate.py
            evaluate_expression()
        elif choice == 2 :
            #displaying all the trigometric functions
            print("1.Sin")
            print("2.Cos")
            print("3.Tan")
            print("4.Cot")
            print("5.Sec")
            print("6.Csc")
            #calling trignometric_val function trigometry.py
            trignometric_val();
        elif choice == 3:
            #displaying the possible conversions
            print("1.char to int")
            print("2.int to char")
            #calling the to_char function from ascii.py
            to_char()
        elif choice == 4:
            #displaying the possible conversions in number system
            print("1.Binary Coversion")
            print("2.Decimal Coversion")
            print("3.Octal Coversion")
            print("4.Hexadecimal Coversion")
            #takes choice from user
            option = int(input("Enter your option : "))
            if(option == 1):
                binary_conversion()
            elif(option == 2):
                decimal_conversion()
            elif(option == 3):
                octal_conversion()
            elif(option == 4):
                hexa_conversion()
            #invalid choice
            else:
                print("Enter valid choice.. ")
        
        #invalid choice
        else:
            print("You entered a wrong choice")
        choice = show_operations()

#calling the bot function
bot()