#Author - Cormac McHale
#G00262708- Graph Theory Project/Assignment
#Program that creates NFA's from regular expressions. (hopefully)

#imports
from shunt import shunt
from thompsons import compile, state, nfa

def follows(state):
    states = {state}

    if state.label is None:
        
        states |= follows(state.edge1)

        states |= follows(state.edge2)
    
    return states

#testing
nfa = compile(shunt("(a.a)*"))
#print(nfa)
current = set()
nexts = set()

for s in string:

    for c in current:
        next |= follows (c.edge1)
