''' Hitbox module '''

class Hitbox:
    ''' Creates hitbox'''

    def __init__(self, game, x_pos, y_pos):
        self.game = game
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.kill_count = 0

    def collide_with_enemy(self):
        ''' Check for enemy collision '''

        for enemy in self.game.enemy_sprites:
            if enemy.x_pos == self.x_pos and enemy.y_pos == self.y_pos:
                if self.kill_count > len(self.game.enemy_sprites):
                    print('Attacked Boss')
                    self.game.playing = False
                print('Attacked enemy')
                self.game.enemy_sprites.remove(enemy)
                self.kill_count += 1
               