#all the operators the user can enter
valid_operators = ("+", "-", "*", "/","%","^","sqrt","cs","ce")

#Global variables to keep the current result, and the last entered token to evaluate
currentResult, stackTop = 0

def intro():
    print("Welcome to the RPN calculator")
    print("2 ENTER 3 x 1 + = 5")

intro()

def getExpressionInput():
    exp = [str(segment) for segment in input("Please enter an expression:").split()]
    return exp

def sanitizeInput(rawTokens):

    sanitizedTokens = []
    needBreak = False
    
    for token in rawTokens:
        if needBreak == True: break
        for char in valid_operators:
            if token != char and needBreak == False:
                try:
                    temp = float(token)
                    sanitizedTokens.append(temp)
                except:
                    print("Invalid expression. Please double check your input")
                    needBreak = True
            elif token == char:
                sanitizedTokens.append(token)
        
    return sanitizedTokens

def evaluateExpression(operand, expression):

    if len(expression) == 1:

    elif len(expression) > 1:





        
    