def hello(): print ("안녕하세요 ㅋㅋ")
hello()
def hi(): print ("Hello")
hi()
def message() :
    print("A")
    print("B")
message()
print("C")
message()
def say1(name):
    string = '안녕하세요? ' + name + '님!'
    return string
def say2(name):
    string = '안녕하세요? ' + name + '님!'
    print(string)
name = "홍길동"
string = say1(name)
print(string)
name = input('당신의 이름은?')
print(name)
age = input('당신의 나이는?')
print(age)
print ("이름 =", name)
print ("나이 =", age)
name = input('당신의 이름은?')
age = (int(input('당신의 나이는?')))
print('당신은 ' + name + '이고 ' + str(age) + '살입니다.')
print('당신은', name, '이고 ', age, '살입니다.')
print('당신은 {}이고 {}살 입니다.'.format(name,age))
print('가위 바위 보 중 하나를 내주세요>')
# print('가위 바위 보 중 하나를 내주세요>', end = ' ')
mine = input()
print('mine:', mine)
mine = input('가위 바위 보 중 하나를 내주세요>')
print('mine:', mine)
date = input('오늘 날짜 : ')
print('오늘 날짜는' , date , '입니다.')
date = input ('오늘 날짜: ')
year = date[0:4]
month = date[4:6]
day = date[6:]
print('년: ', year)
print('월: ', month)
print('일: ', day)
