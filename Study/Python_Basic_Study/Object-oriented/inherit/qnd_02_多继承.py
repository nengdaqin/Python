"""
多继承
"""


class Car(object):
    """定义一个汽车类"""

    def __init__(self, brand, model, color, year):
        """
        :param brand: 品牌
        :param model: 型号
        :param color: 颜色
        :param year: 生产日期
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    # 输出汽车信息
    def info_car(self):

        print("汽车品牌: %s\n汽车型号: %s\n汽车颜色: %s\n生产日期: %s"
              % (self.brand, self.model, self.color, self.year))


# 单继承
class ElectricCar(Car):

    def __init__(self, brand, model, color, year, battery):
        """初始化分类的属性"""
        super().__init__(brand, model, color, year)
        self.battery = battery

    def describe_battery(self):

        print("电瓶容量：%d-kwh" % self.battery)

    # 续航能力
    def get_range(self):
        if self.battery == 70:
            print("续航能力为: 300km")
        elif self.battery == 85:
            print("续航能力为: 360km")


def main():
    # 实例1
    my_car = Car("Audi", "A6L", "Black", 2020)
    my_car.info_car()
    print("=" * 50)

    # 实例2
    my_electric_car = ElectricCar("Tesla", "Model S", "White", 2020, 70)
    my_electric_car.info_car()
    my_electric_car.describe_battery()
    my_electric_car.get_range()

if __name__ == '__main__':
    main()

