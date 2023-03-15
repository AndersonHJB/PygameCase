# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 17:57
# @Author  : AI悦创
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from pygame_demo import football, show_code, concise

football.run()  # 完整代码运行
concise.run()  # 简洁代码运行
print(show_code("concise"))  # 课上代码输出
print(show_code("full"))  # 完整代码输出
