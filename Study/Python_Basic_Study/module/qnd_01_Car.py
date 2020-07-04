"""
汽车类
"""


class Car(object):
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def show_car(self):
        print("品牌：%s\n型号：%s\n颜色：%s\n年份：%s"
              % (self.brand, self.model, self.color, self.year))

    # 定义一个print_line函数打印组成一条分割线


    def print_line(self):

        print("=" * 50)


def main():
    my_car = Car("Audi", "A4L", "White", 2020)
    my_car.show_car()
    # my_car.print_line()

if __name__ == '__main__':
    main()