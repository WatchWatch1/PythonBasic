import random
com = random.randint(0,100)
print("0부터 100까지의 숫자중 하나를 입력해라 ㅋㅋㄹㅃㅃ")
number = 0
while True:
    number = number + 1
    print("{}번째 도전임! 노력해보삼ㅋ".format(number))
    user = int(input("이제 답 말해라 ㅋㅋㄹㅃㅃ "))
    print(user)
    if user < com:
        print("정답보다 큼 ㅅㄱ 다시 입력하삼")

    elif user > com:
        print("정답보다 작음 ㅅㄱ 다시 입력하셈")
    else:
        print("정답임 ㅋㅋ")
        break
