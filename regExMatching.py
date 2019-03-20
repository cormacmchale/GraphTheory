#Author - Cormac McHale
#G00262708- Graph Theory Project/Assignment
#Program that creates NFA's from regular expressions. (hopefully)

#imports
from shunt import shunt
from thompsons import compile, state, nfa

#Follow all empty string paths and keep track of the states reached
def followE(state):
    states = {state}
    #check for E arrows 'empty string'
    if state.label is None:
        #follow the edges from the accept empty string
        if state.edge1 is not None:       
            states |= followE(state.edge1)
        if state.edge2 is not None:
            states |= followE(state.edge2)
    #return all states you are now in the automaton
    return states

#Expression matching function
def match(infix, string):
    postfix = shunt(infix)
    nfa = compile(postfix)
    #print(nfa)
    
    #these will keep track of the current set of state and the next set of states to determine if string is in except state
    currentState = set()
    nextState = set()

    #initilise current state
    currentState |= followE(nfa.initial)

    #for every character in the string
    for s in string:
        #loop through the states that you ar in
        for c in currentState:
            if c.label ==s:
                nextState |= followE(c.edge1)
    #loop through states
    currentState = nextState
    nextState = set()

    #check for accept state in current
    return (nfa.accept in currentState)

checkString = input("Enter String to check: ") 

while(checkString!= "stop"):
    print(match("a.b.c*",checkString))
    checkString = input("Enter String to check: ")

print("Initial Basic Project implementation complete")
