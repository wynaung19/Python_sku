def myFunc():
    print("WYN")

gVar = 100

def main():
    print("Main Fun")
    myFunc()
    print("Global var :",gVar)

if __name__ == '__main__':
    print("SAME")
    main()
