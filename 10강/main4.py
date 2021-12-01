import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
com = num1 / num2
count = 0
while True:
    count += 1
    print("{}번째 도전임! 나눗셈 문제다 잘 풀어보셈ㅋ".format(count))
    user = int(input("{}와 {}를 나눠보셈ㅋ ".format(num1, num2)))
    if user > com:
        print("정답보다 큼 ㅅㄱㅋㅋ")
    elif user < com:
        print("정답보다 작음 ㅅㄱㅋㅋ")
    else:
        print("어케했누,, 프로그램 종료")
        break
