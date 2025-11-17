text = input("Enter text: ")
stack = []

for ch in text:
    stack.append(ch)

rev = ""
while stack:
    rev += stack.pop()

print("Reversed:", rev)
