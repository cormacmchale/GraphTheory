#Author - Cormac McHale
#G00262708- Graph Theory Project/Assignment
#Program that creates NFA's from regular expressions. (hopefully)
def shunt(infix):

    specials = {'*':50,'+':45,'.':40, '|':30}

    postfix=""
    stack=""

    for c in infix:
        #always push ( to the stack
        if c == '(':
            stack=stack+c
        #when you encounter a (
        elif c ==')':
            #while the last character in the stack is not (
            while stack[-1]!='(':
                #postfix gets the character
                #stack shortens to stack[:-1]
                postfix , stack = postfix + stack[-1], stack[:-1]
            #finally also remove the ( when you exit the while loop
            stack = stack[:-1]
        #when you encounter a special character (see dictionary)
        elif c in specials:
            #while you have things on the stack and the precednce of the current character is less then the thing on the end of the stack
            #add this to the postfix
            #if not a special character, return zero
            while stack and specials.get(c,0) <= specials.get(stack[-1],0):
                postfix , stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        #regular characters
        else:
            postfix= postfix+c

    #anything left on the stack should be added to the postfix
    while stack:
        postfix , stack = postfix + stack[-1], stack[:-1]

    #should be empty
    #print(stack)
    #return expression in postfix notation
    print (postfix)
    return postfix
#validation
#print(shunt("(a.a)*"))