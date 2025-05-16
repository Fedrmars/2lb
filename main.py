from Item import Item
from Player import Player
from Enemy import Enemy
from Game import Game
import random
import time

from Skin import Skin

random.seed(time.time_ns())


player_name = input('Enter player`s name: ')

map_size = (12, 12)


player = Player(player_name, hp=100, arm=10, dmg=60)




enemy = Enemy(hp=200, arm=10)
enemy2 = Enemy(hp=100, arm=20)
enemy3 = Enemy(hp=200, arm=10)
enemy4 = Enemy(hp=100, arm=20)
enemy5 = Enemy(hp=200, arm=10)
enemy6 = Enemy(hp=100, arm=20)

skin1 = Skin()
skin2 = Skin()
skin3 = Skin()

game = Game(player, 4, 2)

def random_cords(map_size):
    x = random.randint(1, map_size[0])
    y = random.randint(1, map_size[1])

    while x == player.character_x and y == player.character_y:
        x = random.randint(1, map_size[0])
        y = random.randint(1, map_size[1])
    return (x, y)



game.add_character(enemy, 1, *random_cords(map_size))
game.add_character(enemy2, 1, *random_cords(map_size))
game.add_character(enemy3, 1, *random_cords(map_size))
game.add_character(enemy4, 2, *random_cords(map_size))
game.add_character(enemy5, 2, *random_cords(map_size))
game.add_character(enemy6, 2, *random_cords(map_size))


game.add_item(skin1, 1, 8, 7)
game.add_item(skin2, 1, 4, 8)
game.add_item(skin3, 2, 4, 11)


game.start()




    
