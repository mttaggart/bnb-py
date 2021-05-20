import sys
from game import Game

MENU_OPTIONS = [
    "New Game",
    "Quit!"
]

def main_menu():
    for i in range(len(MENU_OPTIONS)):
        print(f"{i + 1}: {MENU_OPTIONS[i]}")

def menu_handler(menu_choice):
    if menu_choice == 1:
        g = Game()
        g.game_loop()
        print("Thanks for playing!")
        sys.exit()
    else:
        sys.exit()


def main():
    main_menu()
    # Menu sanity check
    try:
        menu_choice = int(input("\nChoose: "))
        if menu_choice > len(MENU_OPTIONS):
            print("Not an option!")
            main()
        menu_handler(menu_choice)
    except ValueError:
        print("Not a number!")
        main()

if __name__ == "__main__":
    main()