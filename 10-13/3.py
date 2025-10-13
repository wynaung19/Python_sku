scores = []
name,score,grade = '',0,'A'
while True:
    
    score = int(input("Enter more than 100 or less than 0 to exit.\nScore : "))

    if score > 100 or score < 0:
        print("END")
        break
    
    name = input("Name : ")
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    scores.append([name,score,grade])
    print('\n')
for i in scores:
    print(i[2],":",i[1],":",i[0])

a,b,c,d,f = 0,0,0,0,0
for i in scores:
    if i[2] == "A":
        a+=1
    if i[2] == "B":
        b+=1
    if i[2] == "C":
        c+=1
    if i[2] == "D":
        d+=1
    if i[2] == "F":
        f+=1

print("\nA : ",a)
print("B : ",b)
print("C : ",c)
print("D : ",d)
print("F : ",f)
