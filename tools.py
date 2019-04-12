import datetime
import sqlite3
import os

MENU_SEARCH = ("""
*******   WORK LOG   *******\n
Do you want to search by:\n
a) Employee
b) Date
c) Time spent
d) Search term
e) Return to main menu\n
> """)


def initialize(data):
    """Store data in SQL database """
    info = data
    presence_log = os.path.isfile("work_log.db")
    if presence_log == False:
        # Creates table
        conn = sqlite3.connect("work_log.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE tasks (
                                        user_name text,
                                        task_name text,
                                        task_date text,
                                        task_time integer,
                                        notes text
                                        )""")
    else:
        # Insert row with data
        conn = sqlite3.connect("work_log.db")
        with conn:
            c = conn.cursor()
            c.execute("""INSERT INTO tasks VALUES (
                                              :user_name,
                                              :task_name,
                                              :task_date,
                                              :task_time,
                                              :notes)""",info)
        conn.commit()
        conn.close()


def read_db():
    pass


def clean():
    """Clean screen for better user experience"""
    os.system('cls' if os.name == 'nt' else 'clear')


def add_task():
    """Add new entry """
    clean()
    while True:
        user_name = input("User name: ")
        if not user_name.strip():
            print("Empty String! Please write a name")
        else:
            break
    while True:
        task_name = input("Title of task: ")
        if not task_name.strip():
            print("Empty String! Please write task's title")
        else:
            break
    while True:
        task_date = input("Date of task. Please use DD/MM/YYYY format: ")
        try:
            task_date = datetime.datetime.strptime(task_date, "%d/%m/%Y")
            break
        except ValueError:
            print("That's not a valid format. Please try again")
    while True:
        task_time = input("Time spent (rounded minutes): ")
        try:
            task_time = int(task_time)
            if task_time < 0:
                zero_validation = task_time / 0
            break
        except ValueError:
            print("Please enter a valid number")
        except ZeroDivisionError:
            print("Please enter a positive number")
    notes = input("Notes: ")
    save = input("\nDo you want to save the entry [y] :").lower()
    if save != "y":
        exit = input("Entry not recorded. ")
    else:
        data = {
                "user_name": user_name,
                "task_name": task_name,
                "task_date": task_date,
                "task_time": task_time,
                "notes": notes
                }
        # Add entry into SQL db
        initialize(data)
        exit = input("Entry recorded! ")


def search_options():
    """Menu with options to search items"""
    while True:
        presence_log = os.path.isfile("work_log.db")
        if presence_log == True:
            next_action = input(MENU_SEARCH)
            read_db()

            if next_action.lower() == "a":
                # search_employee(task_log)
                search_employee()
            elif next_action.lower() == "b":
                search_date()
            elif next_action.lower() == "c":
                search_time()
            elif next_action.lower() == "d":
                search_string()
            elif next_action.lower() == "e":
                break
            else:
                print("'{}' Invalid option! Try again".format(next_action))
        else:
            exit = input("Please add a task first. ")
            break


def search_employee():
    pass


def search_date():
    pass


def search_time():
    pass


def search_string():
    pass
