outFp = None
outStr = ''
outFp = open("C:/Temp/data2.txt",'w')
while True:
    outStr = input("Enter txt : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("-----END----")
