import sqlite3
import db

items = db.read()

def create():
    item = input("Enter the name of the item you want to insert: \n")
    db.insert(item)

def update():
    n = input("Enter the number of the Item you want to update: ")
    new = input("Enter the new name: ")

    item_id = items[int(n)-1][0]

    db.update(item_id, new)


def display():
    print()
    items = db.read()
    print("This is your current list: ")
    n = 1
    for i in items:
        print(f"{n}. {i[1]}")
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
            update()
        elif ans == "e":
            print()
            print("Goodbye.")
            exit()
    else:
        print("I'm sorry, what? \n")
        ask()
        




if __name__ == "__main__":
    db.make_table()

    while True:
        display()
        ask()
    