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
