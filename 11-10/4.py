fruits = {"apple":"Pannthee","mango":"Thayetthee","banana":"Ngapyawthee"}
while True:
    inp = input(str(list(fruits.keys())) + " At htal ka select\n")
    if inp in fruits:
        print("%s is %s" % (inp,fruits.get(inp)))
    elif inp == "end":
        break
    else:
        print("404")
