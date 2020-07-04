"""导入模块"""
# import qnd_01_Car
# import qnd_02_test
# qnd_01_Car.main()
# qnd_02_test.print_line()
# 导入包
import qnd_message

# # 通过模块名调用模块
# qnd_01_test.print_line()
# qnd_02_test.print_line()

"""
导入模块并起别名
别名要符合大驼峰命名法
"""
# import qnd_01_Car as Car
# import qnd_02_test as Test
# Car.main()
# Test.print_line()

# 局部导入(如果导入同名的工具包，后面的工具包会覆盖前面的)
# from qnd_01_Car import Car




qnd_message.qnd_send_message.send("hell0")
txt = qnd_message.qnd_receive_message.receive()
print(txt)