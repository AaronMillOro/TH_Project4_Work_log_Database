"""
Python Web Development Techdegree
Project 4 - Work log using SQL databases
and unittests
--------------------------------
"""
from tools import clean, add_task, search_options

MAIN_MENU = ("""
*******   WORK LOG   *******\n
What would you like to do?\n
a) Add an entry
s) Search existing entries
q) Quit program\n
> """)

def main_menu():
    """Main loop with options"""
    while True:
        choice = input(MAIN_MENU)
        clean()
        if choice.lower() == "a":
            add_task()
        elif choice.lower() == "s":
            search_options()
        elif choice.lower() == "q":
            break
        else:
            print("'{}' invalid option! Please try again".format(choice))


if __name__ == "__main__":
    main_menu()
