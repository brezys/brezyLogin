import sqlite3
import hashlib
import socket
import threading

# Initialize Server Connection Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()  # Waits for connection

def insert_database_data(q, client):
    print("Here")
    conn3 = sqlite3.connect("ttsdatabase.db")
    curr = conn3.cursor()
    try:
        print("Try")
        _, u, password = q.split('|')
        username = u.rstrip()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if(username is None or username.strip() == ''):
            print("Null values detected")
            client.sendall("Username cannot be empty".encode())
        else:
        #Checks database for pre existing username (passwords can be duplicated)    
            print("Checking result")
            curr.execute(f"SELECT * FROM userInfo WHERE username = ?",(username,))
            conn3.commit()
            check_result=curr.fetchone()
            
            if(check_result):
                print("Username taken")
                client.sendall("Username taken".encode())
            else:
                #Add to database if not there
                curr.execute("INSERT INTO userInfo (username, password) VALUES (?, ?)", (username, hashed_password))
                conn3.commit()
                client.sendall("Added to database".encode())
    finally:
        conn3.close()
    
def login_successful(q, client):
    _, username, password = q.split('|')
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn2 = sqlite3.connect("ttsdatabase.db")
    curr = conn2.cursor()

    curr.execute("SELECT * FROM userInfo WHERE username = ? AND password = ?", (username, hashed_password))
            
    if curr.fetchall():
        client.send("Login Successful".encode())
    else:
        client.send("Login Failed".encode())
    
    conn2.close()

def query_handle(data, client):
    query = data.decode()
    if query.startswith("ADD_LOGIN"):
        insert_database_data(query, client)
    else:
        if(query.startswith("LOGIN")):
            login_successful(query, client)
            '''
            client.send("Username: ".encode())
            username = client.recv(1024).decode()
            print("Got username")
            client.send("Password: ".encode())
            password = client.recv(1024)  # Don't decode because we need bytes upon reception
            password = hashlib.sha256(password).hexdigest()
            print("Got password")
            if query == "ADD_LOGIN":
                insert_database_data(query, client)
            # Connect to database file itself in the directory of the server
            conn2 = sqlite3.connect("ttsdatabase.db")
            curr = conn2.cursor()

            curr.execute("SELECT * FROM userInfo WHERE username = ? AND password = ?", (username, password))
            
            if curr.fetchall():
                client.send("Login Successful".encode())
            else:
                client.send("Login Failed".encode())
            '''

def handle(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        query_handle(data, client)
        client.sendall("Query Processed Successfully".encode())

    client.close()

while True:
    client, addr = server.accept()
    threading.Thread(target=handle, args=(client,)).start()
