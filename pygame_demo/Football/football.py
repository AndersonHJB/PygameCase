import pygame, sys

pygame.init()
# 创建游戏窗口大小
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("我的世界")
# 加载足球图像
football = pygame.image.load(r'../Football/football.png')
# 调整图像的大小
football = pygame.transform.smoothscale(football, (width // 6, height // 4))
# 加载背景图片
background = pygame.image.load(r'../Football/background.jpg').convert_alpha()
# 调整图像的大小
background = pygame.transform.smoothscale(background, (width, height))

# 设置游戏的图标
pygame.display.set_icon(football)
# 获取图像的外切矩形
ball_rect = football.get_rect()
# 定义速度
speed = [1, 1]
# 创建颜色
bgcolor = pygame.Color('black')
# 创建控制频率的 clock
fclock = pygame.time.Clock()
# 定义刷新频率
fps = 300


def run():
    while True:
        # 处理退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 设置背景的颜色
        screen.fill(bgcolor)
        # 绘制背景图片
        screen.blit(background, (0, 0))
        # 设定足球的运动
        ball_rect = ball_rect.move(speed[0], speed[1])
        # 足球的上边Y轴坐标<0或者足球的下边的Y轴坐标>创建窗口的高度
        if ball_rect.top < 0 or ball_rect.bottom > height:
            speed[1] = -speed[1]
        # 足球的左边的X坐标<X轴的0坐标或者右边的坐标>创建窗口宽度
        if ball_rect.left < 0 or ball_rect.right > width:
            speed[0] = -speed[0]
        # 在屏幕中的矩形中绘制图形
        screen.blit(football, ball_rect)
        # 刷新游戏场景
        pygame.display.update()
        # 控制游戏场景刷新率
        fclock.tick(fps)
