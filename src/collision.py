def collide(subject, sprites, d_x=0, d_y=0 , callback=None):
    ''' Check for collision '''

    for sprite in sprites:
        if sprite.x_pos == subject.x_pos + d_x and sprite.y_pos == subject.y_pos + d_y:
            if callback is not None:
                callback()
            return True
    return False
