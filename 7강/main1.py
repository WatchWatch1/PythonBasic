print("나무를 1번 찍었습니다.")
print("나무를 2번 찍었습니다.")
print("나무를 3번 찍었습니다.")
print("나무를 4번 찍었습니다.")
print("나무를 5번 찍었습니다.")
print("나무를 6번 찍었습니다.")
print("나무를 7번 찍었습니다.")
print("나무를 8번 찍었습니다.")
print("나무를 9번 찍었습니다.")
print("나무를 10번 찍었습니다.")
hit = 0
while hit < 10:
    hit = hit + 1
    print("나무를 {}번 찍었습니다.".format(hit ))
hit = 0
while hit < 10:
    hit = hit +1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어갔어요오")
    elif hit == 8:
        print ("나무가 곧 넘어갈거 같아요")
number = 0
prompt = """"""
while number != 10:
    print("다시 입력해주세요.")
    number = int(input())
#while True:
    #print("Ctrl+C를 눌러야 While문을 빠져나갈 수 있습니다.")
number = 0
while number < 10:
    number = number + 1
    print(number)
number = 1
while number <= 10:
    print(number)
    number = number + 1
number = 0
while number < 100:
    number = number + 1
    print (number)
number = 1
while number <= 100:
    print (number)
    number = number + 1
number = 0
max = int(input())
while number < max:
    number = number + 1
    print (number)
#while 3<5:
    #print("3은 5보다 적다")
print("숫자 두 개를 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
while min <= max:
    print(min)
    min = min + 1
for number in range(1, 21 , 1):
    print(number)
for number in range(1, 10):
    string = '{}x{}= {}'.format(2, number, 2 * number)
    print(string)
for number in range(1, 10):
    string = '{}x{}= {}'.format(19, number, 19 * number)
    print(string)
    단 = int(input('구구단을 출력합니다. 몇 단인지 입력해주세요.'))
for number in range(1, 10):
   string = '{}x{}= {}'.format(단, number, 단 * number)
   print(string)
