class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{}가 간식을 먹고있다! 정말 맛있게 먹는다 ㅋㅋ".format(self.name))

    def move(self):
        print("{}가 움직이고 있다! 정말 귀엽게 움직인다ㅋㅋ".format(self.name))
    
class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner

    def bark(self):
        print("{}가 짖고 있다! 주인이 좋아서 짖나보다 ㅋㅋ".format(self.name))

    def shake(self):
        print("{}가 꼬리를 살랑살랑 흔들고 있다! 기분이 좋은가보다 ㅎㅎ".format(self.name))

    def __str__(self):
        sentence = '이름 = {}, 나이 = {}, 주인 = {}'.format(self.name, self.age, self.owner)
        return sentence
    
dog = Dog('루키', 5, 'ㅇㅈㅎ')
dog.eat()
dog.move()
dog.bark()
dog.shake()
print(dog)

class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def eat(self):
        print("{}가 와구와구 먹는다 ㅋㅋ 배가 고팠나 보다 ㅋㅋ".format(self.name))

    def move(self):
        print("{}가 주인한테로 움직인다! 주인이 좋은가보다 ㅎ".format(self.name))

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print("{}가 짖는다! 밥달라고 짖는것 같다 ㅋㅋ".format(self.name))

    def shake(self):
        print("{}가 꼬리를 살랑살랑 흔들고 있다! 바람을 쐬고 있나보다 ㅋㅋ".format(self.name))

    def __str__(self):
        sentence = "이름 = {}, 나이 = {}".format(self.name, self.age)
        return sentence

dog = Dog("루키", 5)
print(dog)

dog2 = Dog("또또", 17)
print(dog2)

dog3 = Dog("재롬이", 3)
print(dog3)

class Animal:

    def eat(self):
        print("아주 맛있게 먹고 있다!")
    
    def move(self):
        print("움직이고 있다!")

class Dog(Animal):
    def eat(self):
        print("루키가 밥을 먹는다!")

    def move(self):
        print("루키가 움직이고 있다!")

class Bird(Animal):
    def eat(self):
        print("망고와 탱고가 모이를 먹는다!")

    def move(self):
        print("망고와 탱고가 같이 움직인다!")

animal = Animal()
animal.eat()
animal.move()

dog = Dog()
dog.eat()
dog.move()

bird = Bird()
bird.eat()
bird.move()

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def 먹기(self):
        print("맛있게 먹고 있다!")

    def 잠자기(self):
        print("잠을 자고 있다! 코골며 자고 있다.....")

    def 움직이기(self):
        print("뛰어가고 있다! 정말  빠른속도로 뛴다!")

    def 쉬기(self):
        print("쉬고 있다! 힘든가 보다 ㅋㅋ")

class Student(Human):
    def __init__(self, name, age, 학년, 전번, 학교, 취미, 성별, 반, 좋아하는과목):
        super().__init__(name, age)
        self.학년 = 학년
        self.전번 = 전번
        self.학교 = 학교
        self.취미 = 취미
        self.성별 = 성별
        self.반 = 반
        self.좋아하는과목 = 좋아하는과목

    def 공부하기(self):
        print("열심히 공부하고 있다!")

    def __str__(self):
        sentence = '이름 = {}, 나이 = {}, 학년 = {}, 전화번호 = {}, 학교 = {}, 취미 = {}, 성별 = {}, 반 = {}, 좋아하는 과목 = {}'.format(self.name, self.age, self.학년, self.전번, self.학교, self.취미, self.성별, self.반, self.좋아하는과목)
        return sentence

student = Student("ㅇㅈㅎ", 13, 6, "010-****-1854", "파이썬초등학교", "줄넘기", "남자", 7, "체육")
student.먹기()
student.잠자기()
student.움직이기()
student.쉬기()
student.공부하기()
print(student)
student2 = Student("오재혁", 11, 4, "010-****-1848", "파이썬초등학교", "음악듣기", "남자", 6, "미술")
print(student2)
student3 = Student("김도윤", 13, 6, "010-****-1902", "엔트리초등학교", "춤추기", "남자", 8, "음악")
print(student3)

class Teacher(Human):
    def __init__(self, name, age, 학년속성, 성별):
        super().__init__(name, age)
        self.학년속성 = 학년속성
        self.성별 = 성별

    def 수업하기(self):
        print("선생님이 부르신다! 수업을 시작한다!")

    def __str__(self):
        sentence = "선생님 이름 = {}, 선생님 나이 = {}, 선생님 담당학년 = {}, 선생님 성별 = {}".format(self.name, self.age, self.학년속성, self.성별)
        return sentence

teach = Teacher("김선생", 30, 3, "여자")
teach.수업하기()
teach.쉬기()
teach.움직이기()
teach.먹기()
teach.잠자기()
print(teach)
