import sqlite3
import db


items = db.read()

def create():
    item = input("Enter the name of the item you want to insert: \n")
    db.insert(item)

def update():
    try:
        n = input("Enter the number of the item you want to update: ")
        item_id = items[int(n)-1][0]
        new = input("Enter the new name: ")
        db.update(item_id, new)
    except IndexError:
        print()
        print("Sorry, that number is not on the list, try again")

def remove():
    try:
        n = input("Enter the number of the item you want to remove: ")
        item_id = items[int(n)-1][0]
        db.delete(item_id)
    except IndexError:
        print()
        print("Sorry, that number is not on the list, try again")



def display():
    print()
    print("This is your current list: ")
    print()
    n = 1
    for i in items:
        print(f"{n}. {i[1]}")
        n+=1
    print()


def ask():
    ans = input("Add, update, remove or exit? \n")
    ans = ans[0].lower()

    if ans in "aeur":
        if ans == "a":
            create()
        elif ans == "r":
            remove()
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
        items = db.read()
        display()
        ask()
    