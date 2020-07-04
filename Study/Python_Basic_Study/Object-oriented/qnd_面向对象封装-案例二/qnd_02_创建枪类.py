# 先定义一个枪类：
#     class  Gun:
#     model
#     bullet_count
#     __init__(self, model):
#     add_bullet(self, count):
#     shoot(self):

class Gun:

    def __init__(self, model):

        # 1.枪的型号
        self.model = model

        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹数量：
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了...." % self.model)

            return

        # 2.发射子弹 -1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s] biu biu biu... [剩余：%d 发]" % (self.model, self.bullet_count))


# 创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet_count(40)
ak47.shoot()