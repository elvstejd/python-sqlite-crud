import sqlite3


def connectionDB(func):

    def wrapper(*args, **kwargs):
        global myConnection
        global myCursor

        myConnection = sqlite3.connect("elements.db")
        myCursor = myConnection.cursor()
        result = func(*args, **kwargs)
        myConnection.commit()
        myConnection.close()

        return result
    return wrapper

@connectionDB
def make_table():
    try:
        myCursor.execute('''
        CREATE TABLE items (
            element_id INTEGER PRIMARY KEY AUTOINCREMENT,
            element VARCHAR(17)
        )
        ''')
    except:
        pass



@connectionDB
def insert(element):
    myCursor.execute('INSERT INTO items(element) VALUES(?)', [element])


@connectionDB
def update(x, y):
    id = x
    data = [y]
    myCursor.execute(f'UPDATE items SET element = ? WHERE element_id = {id}', data)
    


@connectionDB
def read():
    elemts = []
    for i in myCursor.execute('SELECT * FROM items'):
        elemts.append(i)

    return elemts
