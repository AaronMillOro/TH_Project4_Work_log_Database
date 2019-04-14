import datetime
import itertools
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
    # info variable is the input from user
    info = data
    presence_log = os.path.isfile("work_log.db")
    if presence_log == False:
        conn = sqlite3.connect("work_log.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE Tasks(
                                       user_name text,
                                       task_name text,
                                       task_date text,
                                       task_time integer,
                                       notes text
                                       )""")
    else:
        conn = sqlite3.connect("work_log.db")
        with conn:
            c = conn.cursor()
            c.execute("""INSERT INTO Tasks VALUES(
                                                  :user_name,
                                                  :task_name,
                                                  :task_date,
                                                  :task_time,
                                                  :notes)""",info)
        conn.commit()
        conn.close()


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
    # Ask the user if the entry should be stored
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
    clean()


def search_options():
    """Menu with options to search items"""
    while True:
        presence_log = os.path.isfile("work_log.db")
        if presence_log == True:
            next_action = input(MENU_SEARCH)
            clean()

            if next_action.lower() == "a":
                search_name = input("Name of employee: ")
                search_employee(search_name)

            elif next_action.lower() == "b":
                while True:
                    s_date = input("Date [DD/MM/YYYY]: ")
                    try:
                        s_date = datetime.datetime.strptime(s_date,"%d/%m/%Y")
                        break
                    except ValueError:
                        print("That's not a valid format. Please try again")
                s_date = str(s_date)
                search_date(s_date)

            elif next_action.lower() == "c":
                while True:
                    timing = input("Time spent (rounded minutes): ")
                    try:
                        timing = int(timing)
                        if timing <= 0:
                            zero_validation = timing / 0
                        break
                    except ValueError:
                        print("Please enter a valid number")
                    except ZeroDivisionError:
                        print("Please enter a positive number")
                search_time(timing)

            elif next_action.lower() == "d":
                search_word = input("Enter keyword to search: ")
                search_string(search_word)

            elif next_action.lower() == "e":
                break

            else:
                print("'{}' Invalid option! Try again".format(next_action))
        else:
            exit = input("Please add a task first. ")
            break
    clean()


def search_employee(self):
    """Search an entry in SQL database by employee name"""
    conn = sqlite3.connect("work_log.db")
    c = conn.cursor()
    c.execute("""
              SELECT user_name,task_name
              FROM Tasks
              WHERE user_name LIKE '%{}%'""".format(self))
    rows = c.fetchall()
    i = 0
    print("Task performed by '{}':\n".format(self))
    for row in rows:
      i += 1
      print(i,")", ' | '.join(str(string) for string in row))
    # control of selection
    if i == 0:
        exit = input("No match!\nPress anything to continue. ")
    else:
        while True:
            item_selected = input("\nSelect a number for details: ")
            try:
                item_selected = int(item_selected)
                if item_selected <= 0:
                    zero_validation = item_selected / 0
                elif item_selected > len(rows):
                    print("Please enter a valid number")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
            except ZeroDivisionError:
                print("Please enter a valid number")
        # Show item details
        c.execute("""
                  SELECT user_name,task_name,task_date,task_time,notes
                  FROM Tasks
                  WHERE user_name LIKE '%{}%'
                  """.format(self))
        rows = c.fetchall()
        i = ["Employee","Task","Date","Time (min)","Notes"]
        print("\n","="*35)
        for (key,item) in zip(i,rows[item_selected-1]):
            print(key,":",item)
        exit = input("\nPress anything to continue. ")
    clean()
    # this return step is to perfom Unit tests
    return rows


def search_time(self):
    """Search entry by time spent"""
    _timing = (str(self),)
    conn = sqlite3.connect("work_log.db")
    c = conn.cursor()
    c.execute("""
              SELECT task_name
              FROM Tasks
              WHERE task_time = ?""", _timing)
    rows = c.fetchall()
    i = 0
    print("\nTasks of {} minutes:\n".format(self))
    for row in rows:
      i += 1
      print(i,")", ' | '.join(str(string) for string in row))
    # control of selection
    if i == 0:
        exit = input("No match found!\nPress anything to continue. ")
    else:
        while True:
            item_selected = input("\nSelect a number for details: ")
            try:
                item_selected = int(item_selected)
                if item_selected <= 0:
                    zero_validation = item_selected / 0
                elif item_selected > len(rows):
                    print("Please enter a valid number")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
            except ZeroDivisionError:
                print("Please enter a valid number")
        # Show item details
        c.execute("""
                  SELECT user_name,task_name,task_date,task_time,notes
                  FROM Tasks
                  WHERE task_time = ?""",_timing)
        rows = c.fetchall()
        i = ["Employee","Task","Date","Time (min)","Notes"]
        print("\n","="*35)
        for (key,item) in zip(i,rows[item_selected-1]):
            print(key,":",item)
        exit = input("\nPress anything to continue. ")
    clean()
    return rows


def search_date(self):
    """Search by specific date in a defined format"""
    _date = self
    conn = sqlite3.connect("work_log.db")
    c = conn.cursor()
    c.execute("""
              SELECT task_name
              FROM Tasks
              WHERE task_date LIKE '%{}%'
              """.format(_date))
    rows = c.fetchall()
    i = 0
    print("Tasks conducted on '{}':\n".format(_date))
    for row in rows:
      i += 1
      print(i,")", ' | '.join(str(string) for string in row))
    # control of selection
    if i == 0:
        exit = input("No match!\nPress anything to continue. ")
    else:
        while True:
            item_selected = input("\nSelect a number for details: ")
            try:
                item_selected = int(item_selected)
                if item_selected <= 0:
                    zero_validation = item_selected / 0
                elif item_selected > len(rows):
                    print("Please enter a valid number")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
            except ZeroDivisionError:
                print("Please enter a valid number")
        # Show item details
        c.execute("""
                  SELECT user_name,task_name,task_date,task_time,notes
                  FROM Tasks
                  WHERE task_date LIKE '%{}%'
                  """.format(_date))
        rows = c.fetchall()
        i = ["Employee","Task","Date","Time (min)","Notes"]
        print("\n","="*35)
        for (key,item) in zip(i,rows[item_selected-1]):
            print(key,":",item)
        exit = input("\nPress anything to continue. ")
    clean()
    return rows


def search_string(self):
    """Search an entry in SQL database by keyword"""
    conn = sqlite3.connect("work_log.db")
    c = conn.cursor()
    c.execute("""
              SELECT task_name
              FROM Tasks
              WHERE task_name LIKE '%{}%'
              OR notes LIKE '%{}%'""".format(self, self))
    rows = c.fetchall()
    i = 0
    print("Tasks containing '{}':\n".format(self))
    for row in rows:
      i += 1
      print(i,")", ' | '.join(str(string) for string in row))
    # control of selection
    if i == 0:
        exit = input("No match!\nPress anything to continue. ")
    else:
        while True:
            item_selected = input("\nSelect a number for details: ")
            try:
                item_selected = int(item_selected)
                if item_selected <= 0:
                    zero_validation = item_selected / 0
                elif item_selected > len(rows):
                    print("Please enter a valid number")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
            except ZeroDivisionError:
                print("Please enter a valid number")
        # Show item details
        c.execute("""
                  SELECT user_name,task_name,task_date,task_time,notes
                  FROM Tasks
                  WHERE task_name LIKE '%{}%'
                  OR notes LIKE '%{}%'""".format(self, self))
        rows = c.fetchall()
        i = ["Employee","Task","Date","Time (min)","Notes"]
        print("\n","="*35)
        for (key,item) in zip(i,rows[item_selected-1]):
            print(key,":",item)
        exit = input("\nPress anything to continue. ")
    clean()
    return rows
