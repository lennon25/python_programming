#!/usr/bin/env python3

import pygame
from pygame.sprite import Group

from settings import Settings
from game_status import GameStatus
from ship import Ship
import game_functions as gf
from scoreboard import Scoreboard


"""开发《外星人入侵》游戏"""


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮

    status = GameStatus(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建用于存储积分牌的实例
    sb = Scoreboard(ai_settings, screen, status)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, status, sb, play_button, ship, aliens, bullets)

        if status.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, status, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, status, sb, ship, aliens, bullets)
            # 更新绘制新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, status, sb, ship, aliens, bullets, play_button)


run_game()
