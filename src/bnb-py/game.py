import random
from card import Card

class Game:

    config = {
        "procs": 4,
        "special_procs": 2,
        "max_turns": 10
    }

    GAME_OPTIONS = [
        "View Procedures",
        "View Kill Chain",
        "Run Procedure",
        "Quit"
    ]

    def __init__(self):
        INIT_STATE = {
            "turns": 0,
            "killchain": [],
            "procs": [],
        }
        self.state = INIT_STATE
        self.cards = Card.load_cards()
        self.deal_cards()

    def deal_cards(self):
        """
        Sets up deck and kill chain for gameplay
        """
        
        # Load procs
        procedures = Card.filter_cards(Card.PROCEDURE, self.cards)

        # Deal special procs
        for i in range(Game.config["special_procs"]):
            proc = procedures.pop(random.randint(0, len(procedures) - 1))
            proc.special = True
            self.state["procs"].append(proc)
        
        # Deal the rest of procs
        for i in range(Game.config["procs"]):
            proc = procedures.pop(random.randint(0, len(procedures) - 1))
            self.state["procs"].append(proc)

        # Load kill chain
        for c in Card.KILLCHAIN:
            filtered_cards = Card.filter_cards(c, self.cards)
            self.state["killchain"].append(random.choice(filtered_cards))
        

    def game_menu(self):
        print("===GAME MENU===")
        turns = self.state["turns"]
        print(f"Turns completed: {turns}")
        for i in range(len(Game.GAME_OPTIONS)):
            print(f"{i + 1}: {Game.GAME_OPTIONS[i]}")

    def print_procedures(self):
        procs = self.state["procs"]
        for i in range(len(procs)):
            proc = procs[i]
            msg = f"{i + 1}: {proc.title}"
            if proc.special:
                msg += " [+3]"
            if proc.disabled > 0:
                msg += f"[Disabled: {proc.disabled}]"
            print(msg)
        print("\n")

    def print_killchain(self):
        print("===KILL CHAIN===")
        killchain = self.state["killchain"]
        msg = ""
        for i in range(len(killchain)):
            kc_card = killchain[i]
            msg += str(i + 1) + ": "
            if kc_card.revealed:
                msg += kc_card.title
            else:
                msg += "????"
            msg += "\n"
        msg += "================\n"
    
        print(msg)

    def run_proc(self):
        self.print_procedures()
        proc_choice = int(input("Choose a Procedure: ")) - 1
        # TODO: safety check for proc choice
        proc = self.state["procs"][proc_choice]
        if proc.disabled > 0:
            print("Procedure still disabled!")
            return

        print(f"Chose {proc.title}; rolling d20...")
        roll = random.randint(1, 20)
        print(f"Rolled {roll}")
        if proc.special:
            print("Special procedure; +3!")
            roll += 3
        else:
            print("Not a special procedure :(")
        
        if roll >= 10:
            print("Success!")
            detected = self.check_killchain(proc)
            if detected:
                detected.revealed = True
                print("Found a Killchain element!\n")
            else:
                print("No detections this time...\n")
        else:
            print("Failure!")
            proc.disabled = 3
    
    def check_killchain(self, proc):
        """
        Checks proc against killchain for detection matches.
        If proc matches, first match is revealed.
        """
        matches = list(filter(lambda k: proc.title in k.detections and not k.revealed, self.state["killchain"]))
        if len(matches) > 0:
            return random.choice(matches)
        
        return None
    
    def advance_turn(self):
        """
        Housekeeping for every turn
        """

        # Advance turn count
        # TODO: Check for end of game
        self.state["turns"] += 1

        # Handle disabled procs
        disabled_procs = filter(lambda p: p.disabled > 0, self.state["procs"])
        for d in disabled_procs:
            d.disabled -= 1

    def game_loop(self):
        while True:
            if self.state["turns"] >= 10:
                print("GAME OVER!")
                return
            elif all([k.revealed for k in self.state["killchain"]]):
                print("Congratulations! You win!")
                return
            else:
                self.game_menu()
                try:
                    game_choice = int(input("\nChoose: "))
                    if game_choice > len(Game.GAME_OPTIONS):
                        print("Not an option!")
                    elif game_choice == 1:
                        self.print_procedures()
                    elif game_choice == 2:
                        self.print_killchain()
                    elif game_choice == 3:
                        self.advance_turn()
                        self.run_proc()
                    else:
                        return
                except ValueError:
                    print("Not a number!")


        



