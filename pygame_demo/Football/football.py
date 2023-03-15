import pygame, sys, os

BGCOLOR = pygame.Color('black')  # 创建颜色
SPEED = [1, 1]  # 定义速度
FPS = 300  # 定义刷新频率
FCLOCK = pygame.time.Clock()


class Player(object):
    def __init__(self):
        pygame.init()
        # 创建游戏窗口大小
        self.size = self.width, self.height = 600, 400
        self.screen = pygame.display.set_mode(self.size)
        # 设置窗口标题
        pygame.display.set_caption("我的世界")
        self.prepare()

    def load_image(self, file):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        """loads an image, prepares it for play"""
        file = os.path.join(main_dir, "img", file)
        try:
            surface = pygame.image.load(file)
        except pygame.error:
            raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
        return surface.convert()

    def prepare(self):
        # 加载足球图像
        football_path = self.load_image("football.png")
        # 加载背景图片
        background_path = self.load_image("background.jpg")
        # 调整图像的大小
        self.football = pygame.transform.smoothscale(football_path.convert_alpha(), (self.width // 6, self.height // 4))

        # 调整图像的大小
        self.background = pygame.transform.smoothscale(background_path, (self.width, self.height))
        # 设置游戏的图标
        pygame.display.set_icon(football_path)
        # 获取图像的外切矩形
        self.ball_rect = self.football.get_rect()
        # 创建控制频率的 clock

    def main(self):
        global BGCOLOR, SPEED, FCLOCK
        while True:
            # 处理退出事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 设置背景的颜色
            self.screen.fill(BGCOLOR)
            # 绘制背景图片
            self.screen.blit(self.background, (0, 0))
            # 设定足球的运动
            self.ball_rect = self.ball_rect.move(SPEED[0], SPEED[1])
            # 足球的上边 Y 轴坐标 < 0 或者足球的下边的 Y 轴坐标 > 创建窗口的高度
            if self.ball_rect.top < 0 or self.ball_rect.bottom > self.height:
                SPEED[1] = -SPEED[1]
            # 足球的左边的 X 坐标 < X 轴的 0 坐标或者右边的坐标 > 创建窗口宽度
            if self.ball_rect.left < 0 or self.ball_rect.right > self.width:
                SPEED[0] = -SPEED[0]
            # 在屏幕中的矩形中绘制图形
            self.screen.blit(self.football, self.ball_rect)
            # 刷新游戏场景
            pygame.display.update()
            # 控制游戏场景刷新率
            FCLOCK.tick(FPS)


def run():
    Player().main()


if __name__ == '__main__':
    p = Player().main()
