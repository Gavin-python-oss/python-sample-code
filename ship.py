import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()  # ship继承了Sprite
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('D:/python/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船都放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom  # 如果要想将飞船的坐标显示为不同的位置可通过设置坐标点，常用的有top, left, bottom, right
        # topleft, bottomleft, topright, bottomrigh，midtop, midleft, midbottom, midright，center, centerx, centery，size, width, height
        self.center = float(self.rect.centerx)  # 在飞船的属性center中存储小数值
        #self.rect.topleft = self.screen_rect.topleft这句话的意思是将坐标X轴放在屏幕左上角
        #self.rect.bottomleft = self.screen_rect.bottomleft这句话的意思是将坐标y轴放在屏幕左下角

        # 移动标快
        self.moving_right = False
        self.moving_left = False
     # 检测键盘的状态属性，如果按下右键盘则向右移动时间为真，即x 坐标右移

    def update(self):  # 此方法update在前述标志为真的时候向右移动飞船
        """根据移动标志调整飞船位置"""
        """更改飞船的center值而不是rect"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center 更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx

