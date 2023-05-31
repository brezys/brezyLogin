# GUI Login - Client to Server Authentication
I am developing an open-source GUI login forum in Python, equipped with a from scratch server hosting a database file. This system handles login and sign-up queries from the client. It efficiently parses these queries, providing the clients with appropriate responses to guide their actions. The combination of a user-friendly interface and a robust server infrastructure ensures a secure and seamless authentication process.

## VIDEO DEMONSTRATION
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/MN-zepaJXXM/0.jpg)](https://www.youtube.com/watch?v=MN-zepaJXXM)

## REQUIREMENTS:
1st - /cd into the folder where your 'requirements.txt' is located

2nd - Run this in the terminal: 'pip install -r requirements.txt'

## SET UP
1st - /cd into the folder and run the 'createDatabase.py' script and if you see a 'ttsdatabase.db' file spawn then you're good.

2nd - If not then download the empty 'ttsdatabase.db' and then connect to the file and then run the 'createDatabase.py' to make the table 'userInfo'

3rd - Check if it worked by uncommenting and putting these above the 'connect.commit()':
'#username1, password1 = "testUser", hashlib.sha256("testPassword".encode()).hexdigest()'
'#cur.execute("INSERT INTO userInfo (username, password) VALUES (?, ?)", (username1, password1))'

4th - Run the file to execute the changes, then comment out those above

5th - Uncomment from #rows = cur.fetchall() to the print(row) statement

4th - Replace the 'CREATE TABLE IF NOT...' with 'SELECT * FROM userInfo' *keep the syntax*

5th - Run the 'createDatabase.py' script in the terminal and if you get an output containing something like '(1, testUser, *encryption string*)' then you're good

## RUN.BAT
1st - Make a '.txt' file and inside it make the 'server.py' script run first, then the 'gui.py' script (one line after the other)

2nd - Rename it to 'run.bat' and make sure to select 'all files' as 'save file type'
