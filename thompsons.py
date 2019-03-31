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
        #for implicit concatenation
        #if the stack has two nfa's and you don't have a conctenate operator
        #then concatenate the two things and go back to the operator you were on
        #if len(nfastack)==2 and (c!='|' or c!='.'):
        #leaving this out for last commit for deadline - will re-visit
         #   nfa2 = nfastack.pop()
         #   nfa1 = nfastack.pop()
         #   initial = state()
         #   accept = state()
         #   initial.edge1 = nfa1.initial
         #   initial.edge2 = nfa2.initial
         #   nfa1.accept.edge1 = accept
         #   nfa2.accept.edge2 = accept
         #   nfastack.append(nfa(initial,accept)) 
         #   print("test")           
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
        #when you encounter a '+' make a new NFA and make the old NFA point towards itself and the new NFA
        #connect the new NFA to itself to accept and append an NFA with the old initial and the new accept to the stack. 
        elif c == '+':
            nfaplus = nfastack.pop()
            accept = state()
            initial = state()
            nfaNew = nfa(initial,accept)
            nfaplus.accept.edge1 = nfaplus.initial
            nfaplus.accept.edge2 = nfaNew.initial
            nfaNew.initial.edge1 = nfaNew.accept
            nfastack.append(nfa(nfaplus.initial, nfaNew.accept))
        #pop the NFA of the stack and make a new initial state make this initial state point towards the initial and accept 
        #state of the NFA and append an NFA with the new initial and old a`ccept to the stack
        elif c == '?':
            nfaquestion = nfastack.pop()
            initial = state()
            initial.edge1 = nfaquestion.initial
            initial.edge2 = nfaquestion.accept
            nfastack.append(nfa(initial, nfaquestion.accept))
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
   

