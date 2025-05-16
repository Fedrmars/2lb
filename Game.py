from Item import Item
from Player import Player
from Character import Character
from Map import Map
from Map import Map
import keyboard
import time
import os

from Skin import Skin
from maps import MAP1, MAP2


def on_w_click(player):
    player.move_up()


def on_a_click(player):
    player.move_left()

def on_s_click(player):
    player.move_down()


def on_d_click(player):
    player.move_right()

def on_space_click(player):
    player.attack()
    
    
def on_e_click(player):
    player.take()



class Game:
    def __init__(self, player: Player, player_start_x, player_start_y):
        self.maps = {1: Map(self, start_x=6, start_y=12, map_list=MAP1), 2: Map(self, start_x=6, start_y=0, map_list=MAP2)}
        self.map = self.maps[1]
        self.player = player
        self.characters: list[Character] = []
        self.add_character(player, 1, player_start_x, player_start_y)
        self.game_ended = False
        self.interface = f'''
--------------------------------------------------------
Имя {player.name}
Здоровье {player.hp}
Броня {player.arm}
Урон {player.dmg}
--------------------------------------------------------
w - вверх | a - влево | s - вниз | d - вправо | space - атаковать | e - собрать
'''
        


        self.bind_keyboard()
        self.killed_enemies = 0
        self.collected_skins = 0
        self.missions_interface = '''
--------------------------------------------------------
Собери 3 коровьи шкуры [{collected_skins}/3] | Убей 5 врагов [{killed_enemies}/5]
--------------------------------------------------------
'''

    def start(self):
        while True:
            if self.game_ended:
                break
            self.map.render()
            print(self.interface)
            print(self.missions_interface.format(collected_skins=self.collected_skins, killed_enemies=self.killed_enemies))
            self.update()
            time.sleep(0.0001)
            os.system('cls')
        
        os.system('cls')
        print('You ended the game')

    def update(self):
        self.update_characters()
        self.update_missions()
    
    
    def update_missions(self):
        skins = 0
        for item in self.player.inventary:
            if isinstance(item, Skin):
                skins += 1
        
        self.collected_skins = skins
        
        if self.killed_enemies == 5 and self.collected_skins == 3:
            self.game_ended = True
    
    
    def update_characters(self):   
        for character in self.characters:
            if character.hp <= 0:
                character.kill()
                self.characters.remove(character)
                self.killed_enemies += 1

    def add_character(self, character: Character, map_key, x, y):
        self.characters.append(character)
        self.maps[map_key].add_character(character, x, y)
    
    def add_item(self, item: Item, map_key, x, y):
        self.maps[map_key].add_item(item, x, y)
    
    
    def bind_keyboard(self):
        keyboard.add_hotkey('w', lambda: on_w_click(self.player))
        keyboard.add_hotkey('a', lambda: on_a_click(self.player))
        keyboard.add_hotkey('s', lambda: on_s_click(self.player))
        keyboard.add_hotkey('d', lambda: on_d_click(self.player))
        keyboard.add_hotkey('e', lambda: on_e_click(self.player))
        keyboard.add_hotkey('space', lambda: on_space_click(self.player))
        
