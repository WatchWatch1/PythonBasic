class dog:
    name = "루키"
    age = 5

    def bark(self):
        print('멍멍')

    def move(self):
        print("루키가 나한테로 움직인다!!")

    def ball(self):
        print("루키가 공을 물어오려고 한다~")

    def play(together):
        print("루키가 또또랑 놀고 싶어한다!")

dog1 = dog()

dog1.bark()
dog1.move()
dog1.ball()
dog1.play()
print(type(dog1))


class ddog:
    name = "또또"
    age = 17

    def bark(self):
        print("왈왈")
    
    def jump(self):
        print("또또가 점프한다!")
    
    def spin(self):
        print("또또가 회전한다!")
    
    def playy(together):
        print("또또가 루키랑 놀고 싶어한다!")

dog2 = ddog()

dog2.bark()
dog2.spin()
dog2.spin()
dog2.playy()
print(type(dog2))

a = 10
print(type(a))

b = "10"
print(type(b))

c = [1,2,3,4,5]
print(type(c))

class dddog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("멍멍")

    def move(self):
        print("루키가 나한테 온다!!")

    def jump(self):
        print("루키가 점프한다!")
    
dog11 = dddog("루키", 5)
dog22 = dddog("또또", 17)
print(dog11.name, dog11.age)
print(dog22.name, dog22.age)

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

call = Calculator()

print(call.add(3))
print(call.add(4))

class calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

Call = calculator()

print(Call.add(3))
print(Call.add(4))
print(Call.sub(1))

class ddddog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("\"왈왈\" {}가 짖엊다.".format(self.name))

    def move(self):
        print("{}가 나한테 온다!!".format(self.name))

    def jump(self):
        print("와우! {}가 점프했다!!".format(self.name))

    def __str__(self):
        sentence = "이름: {}, 나이: {}살".format(self.name, self.age)
        return sentence

dog1 = ddddog("루키", 5)
dog2 = ddddog("또또", 17)
print(dog1)
print(dog2)

dog1.bark()
dog2.bark()
dog1.move()
dog2.move()
dog1.jump()
dog2.jump()

class bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def chip(self):
        print("\"짹짹\" {}가 쩩짹거렸다.".format(self.name))

    def move(self):
        print("[휘이이이잉] {}가 날라간다!!".format(self.name))

    def fly(self):
        print("훨훨~ {}가 날아간다!!".format(self.name))

    def __str__(self):
        sentence = "이름: {}, 나이: {}살".format(self.name, self.age)
        return sentence


bird1 = bird("망고" , 2)
bird2 = bird("탱고" , 3)
print(bird1)
print(bird2)

bird1.chip()
bird2.chip()
bird1.move()
bird2.move()
bird1.fly()
bird2.fly()

class Animal:
    def eat(self):
        print("먹는다")
    def move(self):
        print("움직인다")
    
class dog(Animal):
    def bark(self):
        print("멍멍")
    def shake(self):
        print("꼬리를 흔든다")
Dog = dog()
Dog.eat()
Dog.move()
Dog.bark()
Dog.shake()
