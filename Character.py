from Map import Map, MapObject

class Character(MapObject):
    def __init__(self, hp, arm, map_char):
        super().__init__(map_char)
        self.hp = hp
        self.arm = arm
        self.map : Map = None
        self.character_x = None
        self.character_y = None

    
    def move_up(self):
        self.map.move_character(self, 0, -1)


    def move_left(self):
        self.map.move_character(self, -1, 0)


    def move_down(self):
        self.map.move_character(self, 0, 1)


    def move_right(self):
        self.map.move_character(self, 1, 0)
    

    def kill(self):
        self.map.remove_character(self)
        