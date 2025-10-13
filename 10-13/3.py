scores = []
name,score,grade = '',0,'A'
while True:
    
    score = int(input("Score : "))

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

for i in scores:
    print(i[0],":",i[1],":",i[2])
