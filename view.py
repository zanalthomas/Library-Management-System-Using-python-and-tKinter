from tkinter import *
from tkinter import messagebox
import mysql.connector
class view:
  def viewBooks(self):

    global id,se
    global sv
    global cursor
    sv = StringVar()
    for widgets in self.Frame1.winfo_children():
      widgets.destroy()

    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.051, height=31, width=190)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''View Books''')

    self.Frame2 = Frame(self.Frame1)
    self.Frame2.place(relx=0.02, rely=0.15, relheight=0.840, relwidth=0.960)

    self.Frame2.configure(relief='groove')
    self.Frame2.configure(borderwidth="2")
    self.Frame2.configure(relief="groove")
    self.Frame2.configure(background="#d9d9d9")


    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor()

    sqlquery= "select * from books ;"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        # db.commit()
        L = Label(self.Frame1, font = ('arial', 12), text = "Search",background="#d9d9d9")
        L.grid(row = 3,columnspan = 1)
        se = Entry(self.Frame1, font = ('arial', 15))
        se.grid(row = 3,columnspan = 4)
        se.bind('<Key>', self.refill)

        L = Label(self.Frame1, font = ('arial', 20), text = "----------------------------------------------------------------",background="#d9d9d9")
        L.grid(row = 4,columnspan = 4)

        x=5
        k=["Book ID","book name","Author name","Available","Location"]
        L = Entry(self.Frame2, font = ('arial', 12),width=10)
        L.grid(row = x,column = 0)
        L.insert(END, k[0])
        L.configure(state=DISABLED)
        
        L = Entry(self.Frame2, font = ('arial', 12),width=10)
        L.grid(row = x,column = 1)
        L.insert(END, k[1])
        L.configure(state=DISABLED)

        L = Entry(self.Frame2, font = ('arial', 12),width=10)
        L.grid(row = x,column = 2)
        L.insert(END, k[2])
        L.configure(state=DISABLED)

        L = Entry(self.Frame2, font = ('arial', 12),width=10)
        L.grid(row = x,column = 3)
        L.insert(END, k[3])
        L.configure(state=DISABLED)
        
        L = Entry(self.Frame2, font = ('arial', 12),width=10)
        L.grid(row = x,column = 4)
        L.insert(END, k[4])
        L.configure(state=DISABLED)
        x+=1           
        for i in cursor:
          for j in range(5):
            L = Entry(self.Frame2, font = ('arial', 12),width=10)
            L.grid(row = x,column = j)
            L.insert(END, i[j])
            L.configure(state=DISABLED)
          x+=1   
    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    pass
  def refill(self,event):
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor()
    if(event.char==''):
       val=se.get()
       val=val[:len(val)-1]
    else:
      val=se.get()+event.char
    sqlquery= "select * from books where btitle like '"+val+"%' or bauthor like '"+val+"%';"
    cursor.execute(sqlquery)
    for widgets in self.Frame2.winfo_children():
      widgets.destroy()
    k=["Book ID","book name","Author name","Available","Location"]
    x=5
    L = Entry(self.Frame2, font = ('arial', 12),width=10)
    L.grid(row = x,column = 0)
    L.insert(END, k[0])
    L.configure(state=DISABLED)
        
    L = Entry(self.Frame2, font = ('arial', 12),width=10)
    L.grid(row = x,column = 1)
    L.insert(END, k[1])
    L.configure(state=DISABLED)

    L = Entry(self.Frame2, font = ('arial', 12),width=10)
    L.grid(row = x,column = 2)
    L.insert(END, k[2])
    L.configure(state=DISABLED)

    L = Entry(self.Frame2, font = ('arial', 12),width=10)
    L.grid(row = x,column = 3)
    L.insert(END, k[3])
    L.configure(state=DISABLED)
        
    L = Entry(self.Frame2, font = ('arial', 12),width=10)
    L.grid(row = x,column = 4)
    L.insert(END, k[4])
    L.configure(state=DISABLED)
    x=x+1
    for i in cursor:
     for j in range(5):
            L = Entry(self.Frame2, font = ('arial', 12),width=10)
            L.grid(row = x,column = j)
            L.insert(END, i[j])
            L.configure(state=DISABLED)
     x+=1   
