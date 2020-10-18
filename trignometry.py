#importing required modules and files
import math

#finds the trignometic values
def trignometric_val():
    #takes user choice as input
    value = int(input("Enter your value : "))
    if(value>=1 and value<=6):
        #takes the user input in degrees
        deg = int(input("Enter value of degree: "))
        #converting degrees into radians
        radian = math.radians(deg)
        if(value == 1):
            print("Result : ",math.sin(radian))
        elif(value == 2):
            print("Result : ",math.cos(radian))    
        elif(value == 3):
            print("Result : ",math.tan(radian)) 
        elif(value == 4):
            print("Result : ",(1/math.tan(radian)))
        elif(value == 5):
            print("Result : ",(1/math.cos(radian)))
        else:
            print("Result : ",(1/math.sin(radian)))
    #invalid choice
    else:
        print("Enter a valid number")