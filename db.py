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
            element VARCHAR(17)
        )
        ''')
    except sqlite3.OperationalError:
        pass



@connectionDB
def insert(element):
    myCursor.execute('INSERT INTO items VALUES(?)', [element])


@connectionDB
def read():
    elemts = []
    for i in myCursor.execute('SELECT * FROM items'):
        elemts.append(i)

    return elemts
