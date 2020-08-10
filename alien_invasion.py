# import sys 由于在game_function中导入了sys，故在此处不再需要导入sys
import pygame
from pygame.sprite import Group
from settings import Settings  # 此处的setting是从settings模块中调用过来的，下面的各种设置包括屏幕尺寸，颜色均有此处调用
from game_stats import GameStats
from button import Button
from ship import Ship
# from alien import Alien
import game_function as gf
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()  # 因为Settings是从Setting模块调用过来的，故需要再次定义使用，创建一个实例
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 设置屏幕的大小尺寸
    pygame.display.set_caption("Alien invasion")  # 屏幕的标题
    play_button = Button(ai_settings, screen, "Play")  # 创建play按钮
    stats = GameStats(ai_settings) # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)   # 创建一艘飞船,在while之前创建，如果在while之内创建会使其一直创建飞船，不符合要求
    bullets = Group()
    # bg_color = (230, 250, 250)  # 定义了屏幕的背景颜色，因为只定义一次故放在while循环之外
    # 创建一个外星人
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,  ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            """
            # 删除已经消失的子弹
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            print(len(bullets))# 此处的函数功能被移植到game_function中，故在此处只进行调用就可以
            """
            gf.update_aliens(ai_settings, stats, screen, sb,  ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,  bullets, play_button)
        """
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                        # 每次循环的时候都将重绘屏幕
        screen.fill(ai_settings.bg_color)  # 填充颜色背景
        ship.blitme()  # 将飞船创建在屏幕上
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        """


run_game()








