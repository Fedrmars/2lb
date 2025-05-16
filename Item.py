

from Map import MapObject


class Item(MapObject):
    def __init__(self, name, map_char):
        super().__init__(map_char)
        self.x = None
        self.y = None
        self.name = name
        
    