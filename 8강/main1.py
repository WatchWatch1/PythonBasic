for number in range(1, 21, 1):
    print(number)
for number in range(10, 101, 1):
    print(number)
max = int(input())
for number in range(0, max+1, 1):
    print(number)
for number in range(3, 7, 1):
    print(number)
for number in range(1, 11, 1):
    print(number)
number = 0
while number <5:
    number = number + 1
    print (number)
number = 3
while number <6:
    number = number + 1
    print (number)
for number in range(1, 10):
    string = '{}x{}={}'.format(9, number, 9 * number)
    print(string)
단 = int(input("구구단을 외자~ 구구단을 외자~ 구구단을 알려주세요!"))
for number in range(1, 10):
    string = '{}x{}={}'.format(단, number, 단 * number)
    print(string)
for 단 in range(2, 10):
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단 * number)
        print(string)
for 단 in range(2,10):
    print('{}단 시작'.format(단))
    for number in range(1,10):
        string = '{}x{}={}'.format(단, number, 단 * number)
        print(string)
    print('{}단 종료'.format(단))
number = 0
for number in range (3, 1001, 3):
    print(number)
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print (a)
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        print("{}입니다.".format(a))
        break
    print(a)
number = 2
while number <6:
    number = number + 1
    print (number)
    print("------")
