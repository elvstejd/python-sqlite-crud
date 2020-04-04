import sqlite3
import db

global game_on
game_on = True

def create():
    item = input("Enter the name of the item you want to insert: \n")
    db.insert(item)


def display():
    print()
    print("This is your current list: ")
    n = 1
    for i in db.read():
        print(f"{n}. {i[0]}")
        n+=1
    print()


def ask():
    ans = input("Add, Remove, Update or Exit? \n")
    ans = ans[0].lower()

    if ans in "aeur":
        if ans == "a":
            create()
        elif ans == "r":
            pass
        elif ans == "u":
            pass
        elif ans == "e":
            print("Goodbye.")
            exit()
    else:
        print("I'm sorry, what? \n")
        ask()
        




if __name__ == "__main__":
    db.make_table()

    while game_on:
        display()
        ask()
    