import random
num1 = random.randint(2,15)
num2 = random.randint(2,15)
com = num1 * num2
count = 0
while True:
    count += 1
    print ("{}번째 도전임! 곱셈 문제 나간다 ㅋ".format(count))
    user = int(input("{}하고 {}을 곱해보셈ㅋ ".format(num1, num2)))
    if user > com:
        print("정답보다 큼 ㅅㄱㅋㅋ")
    elif user < com:
        print("정답보다 작음 ㅅㄱㅋㅋ")
    else:
        print ("어,,,, 맞았네,,, 프로그램 종료")
        break
