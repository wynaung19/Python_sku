i,k = 0,0



while True:

    j=int(input("숫자를 입력하세요(나가기:0)"))



    if j == 0:

          break

    

    for i in range(j//2):

        print("  "*(j//2-i+1),'\u2665'*(1+2*i))

    for i in range(j//2,-1,-1):

        print("  "*(j//2-i+1),'\u2665'*(1+2*i))
