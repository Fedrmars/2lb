


class MapObject:
    def __init__(self, map_char):
        self.map_char = map_char



class Map:
    def __init__(self, game, start_x, start_y, x_size=10, y_size=10, map_list = None):
        if map_list == None:
            self.map_list = []
            for i in range(y_size + 1):
                self.map_list.append([])
                for j in range( + 1):
                    if i == 0 or i == y_size or j == 0 or j == x_size:
                        self.map_list[i].append('#')
                    else:
                        self.map_list[i].append('.')
        else:
            self.map_list = map_list
            
        self.game = game
        self.starting_x = start_x
        self.starting_y = start_y
    
    def add_item(self, item, x, y):
        if self.map_list[y][x] != '.':
            return False
        self.map_list[y][x] = item
        
        item.x = x
        item.y = y
        
    def remove_item(self, item):
        self.map_list[item.y][item.x] = '.'
    
    def add_character(self, character, x, y):
        if self.map_list[y][x] != '.':
            return False
        
        self.map_list[y][x] = character
        
        character.map = self
        character.character_x = x
        character.character_y = y
    
    def remove_character(self, character):
        x = character.character_x
        y = character.character_y

        self.map_list[y][x] = '.'
        

    def move_character(self, character, x_move, y_move):
        current_x = character.character_x
        current_y = character.character_y
        

        new_x = character.character_x + x_move
        new_y = character.character_y + y_move


        if new_x > len(self.map_list[0]) - 1 or new_x < 0 or new_y > len(self.map_list) - 1 or new_y < 0:
            next_map = None
            for key, map in self.game.maps.items():
                if self == map:
                    if key == 2:
                        next_map = self.game.maps.get(1)
                    else:
                        next_map = self.game.maps.get(key+1)
                    break
            self.remove_character(character)
            self.game.map = next_map
            character.map = next_map
            next_map.add_character(character, next_map.starting_x, next_map.starting_y)
            return


        if self.map_list[new_y][new_x] != '.':
            return
        self.map_list[current_y][current_x], self.map_list[new_y][new_x] = self.map_list[new_y][new_x], self.map_list[current_y][current_x]
        character.character_x = new_x
        character.character_y = new_y
        
            
        
        
                    
                    
        
        


    def render(self):
        from Character import Character
        for string in self.map_list:
            for el in string:
                if isinstance(el, MapObject):
                    print(el.map_char, end=' ')
                else:
                    print(el, end=' ')
            print()
        
