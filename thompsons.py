#Author - Cormac McHale
#G00262708- Graph Theory Project/Assignment
#Program that creates NFA's from regular expressions. (hopefully)

#imports
from shunt import shunt

class state:
    label = None
    edge1 = None
    edge2 = None

class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(postfix):
    nfastack = []

    for c in postfix:
        #when you encounter the . operator, pop the two smaller NFA's of the statck and concatenates them into one
        #by making the second nfa point towards the initial state of the first nfa that was popped off the stack
        if c=='.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            nfa1.accept.edge1 = nfa2.initial
            nfastack.append(nfa(nfa1.initial, nfa2.accept))
        #when you encounter the | operator again pop the two nfa's that are on the stack off only this time you
        #initilise an initial state that points towards both NFA's and have both NFA's point towards an accept state
        elif c =='|':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            nfastack.append(nfa(initial,accept))
        #when you encounter the * operator you initilise an initial state and have it point towards the accept state 
        #and the NFA, you must also make the NFA point towards the accept state and also loop back towrads itselt to represent 
        #the empty string and the repeating of characters
        elif c =='*':
            nfa1 = nfastack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            nfastack.append(nfa(initial, accept))
        #when you encounter a '+' simply make the NFA point back to itself from both edges so that you can return 
        #for another input, this has now been error handled
        elif c == '+':
            nfaplus = nfastack.pop()
            nfaplus.accept.edge2 = nfaplus.initial
            nfaplus.accept.edge1 = nfaplus.initial
            nfastack.append(nfaplus)
        #every time you read a regular character on the charcter array postfix stack then add in the accept state for 
        #reading that character in an NFA 
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial,accept))
    #return the final NFA which is the only thing in the array
    return nfastack.pop()
#testing
#print(compile(shunt("(a+.a+)*")))
   

