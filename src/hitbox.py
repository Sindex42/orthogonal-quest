class Hitbox:
    ''' Creates hitbox'''

    def __init__(self, game, x_pos, y_pos):
        self.game = game
        self.x_pos = x_pos
        self.y_pos = y_pos

    def collide_with_enemy(self, d_x=0, d_y=0):
        ''' Check for enemy collision '''

        for enemy in self.game.enemy_sprites:
            if enemy.x_pos == self.x_pos and enemy.y_pos == self.y_pos:
                self.game.enemy_sprites.remove(enemy)
