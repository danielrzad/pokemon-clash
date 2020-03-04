from dataclasses import make_dataclass
from random import randint

import pokemon
import trainer
import time

GameConfig = make_dataclass(
    "GameConfig", 
    ["starting_points", 
    "potion_cost",
    "pokeball_cost",
    ]
)
game_config = GameConfig(starting_points=50, potion_cost=15, pokeball_cost=5)

def players_creator():
    print(
        "We will roll our magic dice once. If we will get odd number first "
        "player will start else second player starts the game.\n"
        "And the lucky number is...")
    n = randint(1, 10)
    #time.sleep(3)
    print(n)
    if n % 2 == 1:
        print("First Player starts.")
        player1 = trainer.Trainer()
        print("Now lets create second Player.")
        player2 = trainer.Trainer()
    else:
        print("Second Player starts.")
        player2 = trainer.Trainer()
        print("Now lets create first Player.")        
        player1 = trainer.Trainer()

def game():
    print(
        f"Welcome to the 'The Pocemon Game ver. 1.0. This game is turn-based "
        f"strategy. Rules: \n"
        f"1) First players needs to create their Trainers.\n"
        f"2) Each Trainer has {game_config.starting_points} to choose "
        f"Pokemons(their is based on Pokemon stats like level, hp etc., buy "
        f"health potions(costs {game_config.potion_cost}) or "
        f"pokeballs(costs {game_config.pokeball_cost}.\n"
        f"Lets roll players order."
    )
    players_creator()



def main():
    # czarmander = pocemon.Pocemon(
    #     name="Czarmander", 
    #     level=100, 
    #     p_type="Fire", 
    #     current_health=100,
    #     ko_status=False,
    #     )
    # print(czarmander)
    # ------Actions------
    game()



if __name__ == '__main__':
    main()
