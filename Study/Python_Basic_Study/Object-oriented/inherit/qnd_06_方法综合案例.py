# 需求：设计一个游戏(game)类
# 1.属性
#     定义一个类属性 top_score记录历史最高分
#     定义一个实例属性 player_name记录当前玩家姓名
# 2.方法
#     静态方法 show_help 显示游戏帮助
#     类方法 show_top_score 显示历史最高分
#     实例方法 start_game 开始游戏

class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name
    # 静态方法
    @staticmethod
    def show_help():
        print("游戏帮助：....")
    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史最高分为：%d" % cls.top_score)

    def start_game(self):
        print("%s开始游戏了..." % self.player_name)


def main():
    # 1.查看帮助信息
    Game.show_help()
    # 2.查看历史最高分
    Game.show_top_score()
    # 3.创建游戏对象，开始游戏
    game = Game("小明")
    game.start_game()

if __name__ == '__main__':
    main()


