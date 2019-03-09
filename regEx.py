#Author - Cormac McHale
#G00262708- Graph Theory Project/Assignment
#Program that creates NFA's from regular expressions. (hopefully)
def shunt(infix):

    specials = {'*':50, '.':40, '|':30}

    postfix=""
    stack=""

    for c in infix:
        if c == '(':
            stack=stack+c
            print("Debug")
        elif c ==')':
            while stack[-1]!='(':
                postfix= postfix+stack[-1]
                stack = stack[:-1]
            stack = stack[-1]
        elif c in specials:
            while stack and specials.get(c,0) <= specials.get(stack[-1],0):
                postfix= postfix+stack[-1]
                stack = stack[-1]
            stack = stack[:-1]
            stack = stack + c
        else:
            postfix= postfix+c

    #while stack:
        #postfix= postfix+stack[-1]
        #stack = stack[-1]
        #stack = stack[:-1]

    return postfix

print(shunt("(a.b)|(c*.d)"))