from tkinter import *
from tkinter import messagebox
import mysql.connector

class home:
  def add_db(self):

    global id
    global title
    global author
    global location
    bid=id.get()
    btitle=title.get()
    bauthor=author.get()
    blocation=location.get()
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor()
    if bid=='' or title=='' or bauthor=='' or blocation=='':
      messagebox.showinfo('Error','One or more fields are empty');
    else:
      print(bid,end='--')
      print(btitle,end='--')
      print(bauthor,end='--')
      print("add")

      sqlquery= "insert into books values('" + bid +"','"+btitle+"','"+bauthor+"','YES','"+blocation+"');"
      print(sqlquery)

      try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book added Successfully")
      except:
        messagebox.showinfo("Error","Cannot add given book data into Database")
    
    self.addBooks()
  def addBooks(self):
    global root
    global id
    global title
    global author
    global location
    for widgets in self.Frame1.winfo_children():
      widgets.destroy()
    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=174)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Add Book''')

    L = Label(self.Frame1)
    L.place(relx=0.098, rely=0.225, height=41, width=94)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Book ID''')

    id = Entry(self.Frame1)
    id.place(relx=0.294, rely=0.237, height=30, relwidth=0.38)
    id.configure(background="white")
    id.configure(disabledforeground="#a3a3a3")
    id.configure(font="TkFixedFont")
    id.configure(foreground="#000000")
    id.configure(insertbackground="black")

    title = Entry(self.Frame1)
    title.place(relx=0.294, rely=0.367, height=30, relwidth=0.38)
    title.configure(background="white")
    title.configure(disabledforeground="#a3a3a3")
    title.configure(font="TkFixedFont")
    title.configure(foreground="#000000")
    title.configure(highlightbackground="#d9d9d9")
    title.configure(highlightcolor="black")
    title.configure(insertbackground="black")
    title.configure(selectbackground="blue")
    title.configure(selectforeground="white")

    author = Entry(self.Frame1)
    author.place(relx=0.294, rely=0.498, height=30, relwidth=0.38)
    author.configure(background="white")
    author.configure(disabledforeground="#a3a3a3")
    author.configure(font="TkFixedFont")
    author.configure(foreground="#000000")
    author.configure(highlightbackground="#d9d9d9")
    author.configure(highlightcolor="black")
    author.configure(insertbackground="black")
    author.configure(selectbackground="blue")
    author.configure(selectforeground="white")

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
    Label2_1.configure(text='''Title''')

    Label2_2 = Label(self.Frame1)
    Label2_2.place(relx=0.1, rely=0.491, height=41, width=94)
    Label2_2.configure(activebackground="#f9f9f9")
    Label2_2.configure(activeforeground="black")
    Label2_2.configure(background="#d9d9d9")
    Label2_2.configure(disabledforeground="#a3a3a3")
    Label2_2.configure(font="-family {Segoe UI} -size 10")
    Label2_2.configure(foreground="#000000")
    Label2_2.configure(highlightbackground="#d9d9d9")
    Label2_2.configure(highlightcolor="black")
    Label2_2.configure(text='''Author''')

    location = Entry(self.Frame1)
    location.place(relx=0.294, rely=0.626, height=30, relwidth=0.38)
    location.configure(background="white")
    location.configure(disabledforeground="#a3a3a3")
    location.configure(font="TkFixedFont")
    location.configure(foreground="#000000")
    location.configure(highlightbackground="#d9d9d9")
    location.configure(highlightcolor="black")
    location.configure(insertbackground="black")
    location.configure(selectbackground="blue")
    location.configure(selectforeground="white")
    
    Label2_2 = Label(self.Frame1)
    Label2_2.place(relx=0.1, rely=0.620, height=41, width=94)
    Label2_2.configure(activebackground="#f9f9f9")
    Label2_2.configure(activeforeground="black")
    Label2_2.configure(background="#d9d9d9")
    Label2_2.configure(disabledforeground="#a3a3a3")
    Label2_2.configure(font="-family {Segoe UI} -size 10")
    Label2_2.configure(foreground="#000000")
    Label2_2.configure(highlightbackground="#d9d9d9")
    Label2_2.configure(highlightcolor="black")
    Label2_2.configure(text='''Location''')
    
    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.750, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Add''')
    submitbtn.configure(command=self.add_db)

    
    print("add")
    pass
