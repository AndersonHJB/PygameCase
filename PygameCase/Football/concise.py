# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 17:57
# @Author  : AI悦创
# @FileName: concise.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import sys, os
import pygame

pygame.init()

screen_width = 600
screen_height = 400
screen_size = (screen_width, screen_height)
pygame.display.set_caption("足球弹动——AI悦创·编程1v1|微信:Jiabcdefh")

bgcolor = [255, 239, 213]
screen = pygame.display.set_mode(screen_size)


def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def load_image(file):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "img", file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface.convert()


# 使用变量保存载入的图片，图像函数一般在 image 中
football_path = load_image("football.png").convert_alpha()
background_path = load_image("background.jpg")
# 载入的图片会被认为是一层一层的面，称为 surface
football = pygame.transform.smoothscale(football_path, (60, 60))  # 通过 transform 改变 surface 的大小，存回 football 的变量中
background = pygame.transform.smoothscale(background_path, (600, 400))
ball_x = 30  # 设置足球的 x 坐标
ball_y = 20  # 设置足球的 y 坐标
speed_x = 1  # 设置足球的运动速度
speed_y = 1  # 设置足球的运动速度


def run():
    global ball_x, ball_y, speed_y, speed_x
    while True:
        # 在循环中，每循环一次就判断要不要退出
        quit()  # 调用退出处理函数，判断要不要退出
        screen.blit(background, (0, 0))  # 从左上角开始显示背景，pygame 左上角才是坐标原点

        ball_x = ball_x + speed_x  # 循环让坐标发生变化，则足球会运动
        ball_y = ball_y + speed_y
        if ball_x + 60 > screen_width or ball_x < 0:  # 足球碰到左右边界，速度则变成反方向「负数」
            speed_x = -speed_x
        if ball_y + 60 > screen_height or ball_y < 0:  # 上下边界也是一样
            speed_y = -speed_y
        screen.blit(football, (ball_x, ball_y))  # 使用 blit() 显示图片，第二个参数是图片坐标
        pygame.display.update()  # update 意味更新


if __name__ == '__main__':
    run()
