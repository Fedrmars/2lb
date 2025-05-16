from Character import Character

class Enemy(Character):
    def __init__(self, hp, arm):
        super().__init__(hp, arm, map_char='E')
