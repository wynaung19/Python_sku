# GLOBAL
x = 20
def a():
    #global x #Loc -> global (Can't assign value here)
    # LOCAL
    x=10
    print("a",x)
def b():
    print("b",x)

a()
b()
