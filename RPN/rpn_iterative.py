#need math for square root
import math

#all the operators the user can enter
valid_operators = ("+", "-", "*", "/","^","sqrt","cs","ce")

#Global variables to keep the current result, and the last entered token to evaluate
currentResult, stackTop, workingRegister = 0

# test method
def intro():
    print("Welcome to the RPN calculator")
    print("2 ENTER 3 x 1 + = 5")

intro()

#get the expression to evaluate, with each token separated by a space and stored in a list
def getExpressionInput():
    exp = [str(segment) for segment in input("Please enter an expression:").split()]
    return exp

#sanitize the input to ensure plausible expressions are evaluated
def sanitizeInput(rawTokens):

    #make a new list and initilize it every time we run this
    sanitizedTokens = []
    #less than ideal solution to control flow; initilize a binary value to determine when to break out of the token sanitizing loop
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
        workingRegister = expression[0]
    elif len(expression) > 1:
        for cntr in len(expression):
            for op in valid_operators:
                if expression[cntr] == op:
                    workingRegister = expression[cntr]

            if workingRegister == "+":
                currentResult += expression[cntr+1]
            elif workingRegister == "-":
                currentResult -= expression[cntr+1]
            elif workingRegister == "*":
                currentResult *= expression[cntr+1]
            elif workingRegister == "/":
                currentResult /= expression[cntr+1]
            elif workingRegister == "^":
                currentResult = currentResult**expression[cntr+1]
            elif workingRegister == "sqrt":
                currentResult = math.sqrt(currentResult)
            elif workingRegister == "cs":
                
            elif workingRegister == "ce":





        
    