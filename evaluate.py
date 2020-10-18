#evaluates the given exression 
def evaluate_expression():
    #takes mathematical expression from user as input
    expr = input("Enter an expression: ")
    #throws an exception for invalid expression
    try:
        #displays the result
        print("Result = ", eval(expr))
    except Exception as e:
        print(str(e))