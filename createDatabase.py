import sqlite3
import hashlib

connection = sqlite3.connect('ttsdatabase.db')
cur = connection.cursor()



cur.execute('''
CREATE TABLE IF NOT EXISTS userInfo (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
''')

connection.commit()
#DELETE FROM userInfo WHERE id = 3
#SELECT * FROM userInfo
#rows = cur.fetchall()

#for row in rows:
#    print(row)
    

#username1, password1 = "testUser", hashlib.sha256("testPassword".encode()).hexdigest()
#cur.execute("INSERT INTO userInfo (username, password) VALUES (?, ?)", (username1, password1))

connection.close()

'''
SELECT * FROM userInfo
'''

'''
CREATE TABLE IF NOT EXISTS userInfo (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
'''