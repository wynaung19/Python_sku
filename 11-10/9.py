ss = input("Enter : ")
print("==> ",end = '')
if not ss.startswith('('):
    print("(",end='')

print(ss,end='')
if not ss.endswith(')'):
    print(")",end='')
