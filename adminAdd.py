from tkinter import *
from tkinter import messagebox
import mysql.connector

class admin:
  def admin_db(self):

    global username
    global password

    user=username.get()
    passw=password.get()
    if len(passw)<8:
      messagebox.showinfo('Error',"Atleast 8 characters needed")
    else:
      db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
      cursor = db.cursor()

      sqlquery= "insert into admin values('" +user+"','"+passw+"');"
      print(sqlquery)

      try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Admin added")
      except:
        messagebox.showinfo("Error","Cannot add admin details into Database")
    
    self.addAdmin()
  def addAdmin(self):

    global username
    global password

    for widgets in self.Frame1.winfo_children():
      widgets.destroy()

    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=174)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Add Admin''')

    L = Label(self.Frame1)
    L.place(relx=0.098, rely=0.225, height=41, width=94)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Username''')

    username = Entry(self.Frame1)
    username.place(relx=0.294, rely=0.237, height=30, relwidth=0.38)
    username.configure(background="white")
    username.configure(disabledforeground="#a3a3a3")
    username.configure(font="TkFixedFont")
    username.configure(foreground="#000000")
    username.configure(insertbackground="black")

    password = Entry(self.Frame1)
    password.place(relx=0.294, rely=0.367, height=30, relwidth=0.38)
    password.configure(background="white")
    password.configure(disabledforeground="#a3a3a3")
    password.configure(font="TkFixedFont")
    password.configure(foreground="#000000")
    password.configure(highlightbackground="#d9d9d9")
    password.configure(highlightcolor="black")
    password.configure(insertbackground="black")
    password.configure(selectbackground="blue")
    password.configure(selectforeground="white")
    password.configure(show="*")

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
    Label2_1.configure(text='''Password''')

    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.491, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Add''')
    submitbtn.configure(command=self.admin_db)

    

    pass

  def changePass(self):
    global username
    global oldpassword
    global newpassword

    for widgets in self.Frame1.winfo_children():
      widgets.destroy()

    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=174)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Password''')

    L = Label(self.Frame1)
    L.place(relx=0.098, rely=0.225, height=41, width=94)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Username''')

    username = Entry(self.Frame1)
    username.place(relx=0.294, rely=0.237, height=30, relwidth=0.38)
    username.configure(background="white")
    username.configure(disabledforeground="#a3a3a3")
    username.configure(font="TkFixedFont")
    username.configure(foreground="#000000")
    username.configure(insertbackground="black")

    oldpassword = Entry(self.Frame1)
    oldpassword.place(relx=0.294, rely=0.367, height=30, relwidth=0.38)
    oldpassword.configure(background="white")
    oldpassword.configure(disabledforeground="#a3a3a3")
    oldpassword.configure(font="TkFixedFont")
    oldpassword.configure(foreground="#000000")
    oldpassword.configure(highlightbackground="#d9d9d9")
    oldpassword.configure(highlightcolor="black")
    oldpassword.configure(insertbackground="black")
    oldpassword.configure(selectbackground="blue")
    oldpassword.configure(selectforeground="white")
    oldpassword.configure(show="*")

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
    Label2_1.configure(text='''Old Password''')

    L = Label(self.Frame1)
    L.place(relx=0.098, rely=0.480, height=41, width=94)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''New Password''')

    newpassword = Entry(self.Frame1)
    newpassword.place(relx=0.294, rely=0.500, height=30, relwidth=0.38)
    newpassword.configure(background="white")
    newpassword.configure(disabledforeground="#a3a3a3")
    newpassword.configure(font="TkFixedFont")
    newpassword.configure(foreground="#000000")
    newpassword.configure(insertbackground="black")
    newpassword.configure(show="*")
    
    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.650, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Submit''')
    submitbtn.configure(command=self.changePass_db)

    
    print("add")
    pass
  def changePass_db(self):

    global username
    global oldpassword
    global newpassword
    
    user=username.get()
    oldpassw=oldpassword.get()
    newpassw=newpassword.get()
    if len(newpassw)<8:
      messagebox.showinfo('Error',"Atleast 8 characters needed")
    else:
      db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
      cursor = db.cursor()


      sqlquery= "select * from admin where user='"+user+"' and pass='"+oldpassw+"';"
      print(sqlquery)

      try:
        cursor.execute(sqlquery)
        row = cursor.fetchone()
        if row == None:
           messagebox.showinfo('Error',"Invalid Credentials")
        else:
           newcursor=cursor
           sqlquery= "update admin set pass='"+newpassw+"' where user='"+user+"';"
           newcursor.execute(sqlquery)
           db.commit()
           print(sqlquery)
           messagebox.showinfo('Success',"Password changed")
      except:
        messagebox.showinfo("Error","Cannot add admin details into Database")
    
    self.changePass()
