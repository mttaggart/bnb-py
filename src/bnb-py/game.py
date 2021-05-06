import random
from card import Card

class Game:

    config = {
        "procs": 1,
        "special_procs": 1,
        "max_turns": 10
    }

    GAME_OPTIONS = [
        "View Procedures",
        "Quit"
    ]

    def __init__(self):
        INIT_STATE = {
            "turns": 0,
            "kill_chain": [],
            "procs": [],
            "special_procs": []
        }
        self.state = INIT_STATE
        self.cards = Card.load_cards()
        self.deal_cards()

    def deal_cards(self):
        procedures = list(filter(lambda c: c.card_type == Card.PROCEDURE, self.cards))
        for i in range(Game.config["special_procs"]):
            proc = procedures.pop(random.randint(0, len(procedures) - 1))
            self.state["special_procs"].append(proc)
        
        for i in range(Game.config["procs"]):
            proc = procedures.pop(random.randint(0, len(procedures) - 1))
            self.state["procs"].append(proc)

    def game_menu(self):
        print("===GAME MENU===")
        for i in range(len(Game.GAME_OPTIONS)):
            print(f"{i + 1}: {Game.GAME_OPTIONS[i]}")

    def print_procedures(self):
        print("\nSpecial Procedures (+3):")
        procs = self.state["procs"]
        special_procs = self.state["special_procs"]
        for i in range(len(special_procs)):
            print(f"{i + 1}: {special_procs[i].title}")
        print("\nNormal Procedures:")
        for i in range(len(procs)):
            print(f"{i + 1}: {procs[i].title}")
            print("\n")


    def game_loop(self):
        while True:
            self.game_menu()
            try:
                game_choice = int(input("\nChoose: "))
                if game_choice > len(Game.GAME_OPTIONS):
                    print("Not an option!")
                elif game_choice == 1:
                    self.print_procedures()
                else:
                    return
            except ValueError:
                print("Not a number!")


        


