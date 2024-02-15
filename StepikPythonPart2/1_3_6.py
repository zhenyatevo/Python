#CORRECT
def printab(a, b): # function with
    print(a)       # two positional arguments
    print(b)

def printab(a, b=10): # one of arguments has
    print(a)          # a default value
    print(b)

def printab(a=10, b=10): # both arguments have
    print(a)             # a default value
    print(b)

#INCORRECT
def printab(a=10,b): # non-default argument
    print(a)         # follows default argument
    print(b)
