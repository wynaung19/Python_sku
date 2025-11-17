a = input("Person A MBTI: ").upper()
b = input("Person B MBTI: ").upper()

score = 0
for i in range(4):
    if len(a) == 4 and len(b) == 4 and a[i] == b[i]:
        score += 1

print("Matching letters:", score)

if score == 4:
    print("Perfect Match!")
elif score >= 2:
    print("Good Match!")
else:
    print("Low Compatibility.")
