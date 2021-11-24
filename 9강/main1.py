list = [1, 5, 3, 6]
print(list[-3])
print(list[1])
print(list[1:3])
print(list[2:])
print(list[:2])
과목 = ['국어', '수학', '영어', '과학', '컴퓨터실']
print(과목)
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
last_color = rainbow[6]
print('무지개의 마지막 색은 {}이다.'.format(last_color))
점수= int(input("당신의 점수는 몇점입니까?"))
if 점수>60:
    print("축하합니다. 당신은 수능에 합격하였습니다!")
else:
    print("당신은 수능에 불합격하였습니다.")

while True:
    한국인 = input("한국의 수도는 무엇입니까?")
    if 한국인=="그만":
        print("프로그램을 종료합니다.")
        break
    if 한국인=="서울":
        print("정답입니다!")
    else:
        print("정답이 아닙니다.")
    
    
list = [1,5,3,6]
list.insert(2,4)
print(list)
list = [1,5,3,6]
list.append(8)
print(list)
list=[1,2,3]
list.append(4)
print(list)
list=[1,2,3,5]
list.insert(3,4)
print(list)
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

while True:
    점수 = int(input("점수를 알려주세요! "))
    if 점수<21:
        print("E등급입니다. 많이 노력하셔야겠군요.")
    elif 점수<41:
        print("D등급입니다. 노력하셔야겠군요.")
    elif 점수<61:
        print("C등급입니다. 좀 더 실력을 발휘해야겠네요!")
    elif 점수<81:
        print("B등급입니다. 조금만 더 힘내세요!!")
    elif 점수<101:
        print("A등급입니다! 완벽하군요!")
    else:
        print("점수를 계산할수 있는 값이 아닙니다. 프로그램을 종료합니다.")
        break
음식 = ('떡볶이', '햄버거', '피자', '김밥')
print(음식)
t = (1,2,3,4,5,6,6,7,8,9,10)
print(t*10)
t = (1,2,3,4,5,6,7,8,9,10)
t2 = t*10
print(t2)
print(len(t2))
for number in range(3,7,1):
    number = number + 1
    print(number)
for number in range(1,10,1):
     string= '{}x{}={}'.format(3, number, 3 * number)
     print(string)
