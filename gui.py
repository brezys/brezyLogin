import customtkinter as ck
import numba
import sys
import socket
import time
import hashlib
import os

#Connect to server

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9999))

ck.set_appearance_mode("System")
ck.set_default_color_theme("green")


def login_function(u, p):
    username = u
    password = p
    
    query = f"LOGIN|{username}|{password}"
    cli.sendall(query)
    msg = cli.recv(1024).decode()
    time.sleep(1)
    '''
    msg = cli.recv(1024).decode()
    cli.send(username.encode())
    msg = cli.recv(1024).decode()
    cli.send(password.encode())
    '''
    print("login sent")


def sign_up_function(frame):
    print("sign up page")
    print("signed up")

class loginFrame(ck.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(pady=20, padx=60, fill="both", expand=False)

        label = ck.CTkLabel(master=self, text="Login")
        label.pack(pady=12,padx=10)

        self.username_entry = ck.CTkEntry(master=self, placeholder_text="Username")
        self.username_entry.pack(pady=12,padx=10)
        self.password_entry = ck.CTkEntry(master=self, placeholder_text="Password", show="•")
        self.password_entry.pack(pady=12,padx=10)

        self.login_button = ck.CTkButton(master=self, text="Login", command=self.login)
        self.login_button.pack()

        cb = ck.CTkCheckBox(master=self, text="Remember Me")
        cb.pack(pady=12,padx=10)

        sign_up_button = ck.CTkButton(master=self, text="Sign up", fg_color="red",command=self.sign_up)
        sign_up_button.pack(pady=20)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        query = f"LOGIN|{username}|{password}"
        cli.sendall(query.encode())
        msg = cli.recv(1024).decode()
        if(msg == "Login Successful"):
            app.firstpage_frame()
    
    def sign_up(self):
        app.swap_frame()
    
    

class signupFrame(ck.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(pady=20, padx=60, fill="both", expand=False)

        self.label = ck.CTkLabel(master=self, text="Sign up")
        self.label.pack(pady=12,padx=10)

        self.username_entry = ck.CTkEntry(master=self, placeholder_text="Username")
        self.username_entry.pack(pady=12,padx=10)
        self.password_entry = ck.CTkEntry(master=self, placeholder_text="Password", show="•")
        self.password_entry.pack(pady=12,padx=10)

        self.progressbar = ck.CTkProgressBar(master=self, orientation="horizontal")
        self.progressbar.pack(pady=12,padx=10)

        sign_up_button = ck.CTkButton(master=self, text="Sign up", command=self.loginPage)
        sign_up_button.pack(pady=20)
           
    def loginPage(self):
        username = self.username_entry.get()
        print(username)
        password = self.password_entry.get()
        print(password)
        if(username is not None and password is not None):
            #Send data to server and into database
            #password = hashlib.sha256(password.encode()).hexdigest()

            query = f"ADD_LOGIN|{username}|{password}"
            cli.sendall(query.encode())
            
            time.sleep(1)
    
            print("Query Sent")
            msg = cli.recv(1024).decode()
            if("Username taken" in msg):
                print("Username taken, choose another")
            elif("Username cannot be empty" in msg):
                print("Username Null, enter valid input")
            else:
                #Fancy widget (does nothing)
                i = 0.00
                self.progressbar.set(i)
                while(i< 1):
                    i+=0.05
                    time.sleep(0.05)
                    self.progressbar.set(i)
                    self.update_idletasks()
                self.label.configure(require_redraw=True, text="Sign up successful!")
                self.label.update()
                time.sleep(2)

                #Change frame to first page frame
                app.firstpage_frame()
        else:
            print("Null values, enter valid inputs")
        
class firstpageFrame(ck.CTkFrame):
    print("Start Here Tmw") 

class MainApplication(ck.CTk):
    def __init__(self):
        super().__init__()
        #Define Window itself and params
        self.title("LanGAP")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "images", "iconimage.ico")
        self.iconbitmap(file_path)
        self.geometry("400x400")
        self.resizable(False, False)
       
        self.loginFramevar = loginFrame(self)
        self.signupFramevar = signupFrame(self)
        self.firstpageFramevar = firstpageFrame(self)

        self.current_frame = None
        self.show_frame(self.loginFramevar)

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()

        frame.pack()
        self.current_frame = frame

    def swap_frame(self):
        if self.current_frame == self.loginFramevar:
            self.show_frame(self.signupFramevar)
        else:
            self.show_frame(self.loginFramevar)
    
    def firstpage_frame(self):
        self.show_frame(self.firstpageFramevar)

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
