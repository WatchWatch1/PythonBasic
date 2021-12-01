import random
com = random.randint(0,100)
com2 = random.randint(0,100)
prinnt = 0
string = com + com2
print("더하기 게임임 ㅋ 잘 해보셈")
while True:
     prinnt = prinnt + 1
     print("{}번째 도전임ㅋ 열심히 해보셈ㅋ".format(prinnt))
     user = int(input("숫자 {}와 {}를 더해보셈ㅋㅋ ".format(com, com2)))
     if string < user:
         print("답보다 큼 ㅅㄱㅋ")
     elif string > user:
         print("답보다 작음 ㅅㄱㅋ")
     else:
         print("어,,,, 맞았네")
         break
com11 = random.randint(60,100)
com22 = random.randint(0,50)
d = 0
sstring = com11 - com22
print("이번엔 빼기 게임임 ㅋ 잘해보삼")
while True:
    d = d + 1
    print("{}번째 도전임 잘 해보셈ㅋ".format(d))
    uuser = int(input("숫자를 {}와 {}를 빼보셈ㅋㅋ ".format(com11, com22)))
    if sstring < uuser:
        print("답보다 큼 ㅅㄱㅋㅋ")
    elif sstring < uuser:
        print("답보다 작음 ㅅㄱㅋㅋ")
    else:
        print("어,, 맞았네,, 게임 끝임 ㅃ")
        break
