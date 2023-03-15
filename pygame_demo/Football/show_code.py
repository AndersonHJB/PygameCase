# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 23:31
# @Author  : AI悦创
# @FileName: show_code.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import os


def load_code(filename: str):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    return os.path.join(main_dir, filename)


def show_code(judge="concise"):
    """
    judge:
        - full:完整的运行代码
        - concise:课程中的简洁代码
    """
    if judge.lower() == "full":
        with open(load_code("football.py"), "r", encoding="utf-8") as f:
            return f.read()
    elif judge.lower() == "concise":
        with open(load_code("concise.py"), "r", encoding="utf-8") as f:
            return f.read()
