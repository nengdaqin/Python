"""
多态性：指在父类被子类继承后，可以具有不同的状态或表现
"""

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s飞到天上去玩耍..." % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s快乐的玩耍..." % (self.name, dog.name))
        dog.game()

def main():
    # wangcai = Dog("旺财")
    xiaoming = Person("小明")
    wangcai = XiaoTianDog("飞天旺财")

    xiaoming.game_with_dog(wangcai)

if __name__ == '__main__':
    main()




