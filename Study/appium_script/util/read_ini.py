# coding=utf-8
import configparser
from io import StringIO

read_ini = configparser.ConfigParser()
read_ini.read("E:/Python_Basic_Study/appium_script/config/LocalElement.ini")
# print(data)
print(read_ini.get("element", "username"))