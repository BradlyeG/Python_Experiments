#need math for square root
import math

#all the operators the user can enter
valid_operators = ("+", "-", "*", "/","^","sqrt","ce")

#Global variables to keep the current result, and the last entered token to evaluate
currentResult, stackTop = 0
globalStack = []

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
    
    #we need to iterate through every input separated by a space in the expression we recieved
    for token in rawTokens:

        #break if the expression is not valid
        if needBreak == True: break

        #iterate through every one of our valid operators 
        for op in valid_operators:

            #if the token isn't an operator and we don't need to break
            if token != op and needBreak == False:

                #try to cast the token into a float. The calculator only allows for the given set of expressions or numbers. If it isn't a number it will fail
                try:
                    temp = float(token)

                    #i'm hoping that if token can't be cast as a float then we will move to the except block before actually appending it to the sanitized expression list
                    sanitizedTokens.append(temp)
                except:
                    print("Invalid expression. Please double check your input")
                    needBreak = True
            
            #if the token is an operator then go ahead and append it
            elif token == op and needBreak == False:
                sanitizedTokens.append(token)

            #if we need to break then break out of the loop
            elif needBreak == True:
                break
        
    return sanitizedTokens

def push_stack(stackData):
    globalStack.append(stackData)

def pop_stack(stackData):
    return stackData.pop()

def evaluateExpression(operand, expression):
    stackEmpty = False

    while stackEmpty == True:
        topStack = pop_stack(expression)
        
        for op in valid_operators:
            if topStack == op:


        








        
    