from tkinter import *
from tkinter import messagebox
import mysql.connector

from adminAdd import *
from userAdd import *

class control(admin,user):
  def adminControl(self):

    for widgets in self.Frame1.winfo_children():
      widgets.destroy()
    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=190)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Controls''')

    L = Label(self.Frame1)
    L.place(relx=0.130, rely=0.225, height=41, width=110)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Add admin user''')

  
    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.250, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Add admin''')
    submitbtn.configure(command=self.addAdmin)

    L = Label(self.Frame1)
    L.place(relx=0.130, rely=0.350, height=41, width=110)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Add user''')

  
    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.375, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Add''')
    submitbtn.configure(command=self.addUser)

    L = Label(self.Frame1)
    L.place(relx=0.130, rely=0.475, height=41, width=110)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Change Password''')

  
    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.500, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Change''')
    submitbtn.configure(command=self.changePass)
    pass
