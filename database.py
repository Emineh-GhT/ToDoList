import sqlite3

con = sqlite3.connect('database.db')
my_cursor = con.cursor()

# my_cursor.execute('SELECT * FROM tasks')
# result = my_cursor.fetchall()
# print(result)
# my_cursor.execute('INSERT INTO tasks(id, title, done) VALUES(10, "cooking", 0)')
# con.commit() #zakhire taqirat
# my_cursor.execute('UPDATE tasks SET description="with my friend" WHERE id=1')
# con.commit()

def add(title, description, done, time, date, priority):
    my_cursor.execute(f'INSERT INTO tasks ( title, description, done, time, date, priority) VALUES ( "{title}", "{description}", {done}, "{time}", "{date}", {priority})')
    con.commit()

def getAll():
    my_cursor.execute('SELECT * FROM tasks')
    results = my_cursor.fetchall()
    return results

def removeTask(id):
    my_cursor.execute(f'DELETE FROM tasks WHERE id = {id}')
    con.commit()

def DoneUpdate(id, value):
    my_cursor.execute(f'UPDATE tasks SET done = {value} WHERE id = {id}')
    con.commit()