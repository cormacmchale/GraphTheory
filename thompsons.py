#Author - Cormac McHale
#G00262708- Graph Theory Project/Assignment
#Program that creates NFA's from regular expressions. (hopefully)
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
        if c=='.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            nfa1.accept.edge1 = nfa2.initial
            nfastack.append(nfa(nfa1.initial, nfa2.accept))
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
        elif c =='*':
            nfa1 = nfastack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            nfastack.append(nfa(initial, accept))   
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial,accept))
     
    return nfastack.pop()

print(compile(shunt("(a.b)|(c*.d)")))  
   

