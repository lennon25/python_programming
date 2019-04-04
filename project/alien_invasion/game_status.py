#!/usr/bin/env python3


class GameStatus():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_status()
        self.game_active = False

        # 在任何情况下都不重置最高得分
        self.high_score = 0

    def reset_status(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

