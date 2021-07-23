from tkinter import *
from tkinter import messagebox
import mysql.connector

class user:
  def user_db(self):

    global userid
    global username

    user=userid.get()
    name=username.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor()
    sqlquery= "insert into members values('" +user+"','"+name+"');"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"User added")
    except:
        messagebox.showinfo("Error","Cannot add user details into Database")
    
    self.addUser()
  def addUser(self):
    global userid
    global username

    for widgets in self.Frame1.winfo_children():
      widgets.destroy()

    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=174)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Add User''')

    L = Label(self.Frame1)
    L.place(relx=0.098, rely=0.225, height=41, width=94)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''User ID''')

    userid = Entry(self.Frame1)
    userid.place(relx=0.294, rely=0.237, height=30, relwidth=0.38)
    userid.configure(background="white")
    userid.configure(disabledforeground="#a3a3a3")
    userid.configure(font="TkFixedFont")
    userid.configure(foreground="#000000")
    userid.configure(insertbackground="black")

    username = Entry(self.Frame1)
    username.place(relx=0.294, rely=0.367, height=30, relwidth=0.38)
    username.configure(background="white")
    username.configure(disabledforeground="#a3a3a3")
    username.configure(font="TkFixedFont")
    username.configure(foreground="#000000")
    username.configure(highlightbackground="#d9d9d9")
    username.configure(highlightcolor="black")
    username.configure(insertbackground="black")
    username.configure(selectbackground="blue")
    username.configure(selectforeground="white")

    Label2_1 = Label(self.Frame1)
    Label2_1.place(relx=0.102, rely=0.351, height=41, width=94)
    Label2_1.configure(activebackground="#f9f9f9")
    Label2_1.configure(activeforeground="black")
    Label2_1.configure(background="#d9d9d9")
    Label2_1.configure(disabledforeground="#a3a3a3")
    Label2_1.configure(font="-family {Segoe UI} -size 10")
    Label2_1.configure(foreground="#000000")
    Label2_1.configure(highlightbackground="#d9d9d9")
    Label2_1.configure(highlightcolor="black")
    Label2_1.configure(text='''Username''')

    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.491, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Add''')
    submitbtn.configure(command=self.user_db)

    pass
