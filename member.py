from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import timedelta, date
class member:
  def member_db(self):

    global id

    mid=id.get()

    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor(buffered=True)

    sqlquery= "select * from members where mid='"+mid+"';"
    print(sqlquery)

    try:
      cursor.execute(sqlquery)
      db.commit()
      L = Label(self.Frame2)
      L.place(relx=0.410, rely=0.08, height=41, width=100)
      L.configure(background="#d9d9d9")
      L.configure(disabledforeground="#a3a3a3")
      L.configure(font="-family {Poppins Medium} -size 18")
      L.configure(foreground="#000000")
      flag=0
      for i in cursor:
            flag=1
            L.configure(text=i[1])
            x=1
            sqlquery= "select issue.issue_date,books.btitle,issue.return_date,issue.due_date,issue.fine,issue.issue_id from books,issue where issue.bid=books.bid and bStudentName='"+mid+"';"
            print(sqlquery)
            newcursor=cursor
            newcursor.execute(sqlquery)
            self.Frame3 = Frame(self.Frame2)
            self.Frame3.place(relx=0.02, rely=0.26, relheight=0.700, relwidth=0.960)

            self.Frame3.configure(relief='groove')
            self.Frame3.configure(borderwidth="0")
            self.Frame3.configure(relief="groove")
            self.Frame3.configure(background="#d9d9d9")
            k=["issue date","book name","return date","Due date","fine"]
            
            L = Entry(self.Frame3, font = ('arial', 12),width=10)
            L.grid(row = x,column = 0)
            L.insert(END, k[0])
            L.configure(state=DISABLED)

            L = Entry(self.Frame3, font = ('arial', 12),width=10)
            L.grid(row = x,column = 1)
            L.insert(END, k[1])
            L.configure(state=DISABLED)

            L = Entry(self.Frame3, font = ('arial', 12),width=10)
            L.grid(row = x,column = 2)
            L.insert(END, k[2])
            L.configure(state=DISABLED)
            
            L = Entry(self.Frame3, font = ('arial', 12),width=10)
            L.grid(row = x,column = 3)
            L.insert(END, k[3])
            L.configure(state=DISABLED)

            L = Entry(self.Frame3, font = ('arial', 12),width=5)
            L.grid(row = x,column = 4)
            L.insert(END, k[4])
            L.configure(state=DISABLED)           
            
            x=x+1
            for i in newcursor:
               L = Entry(self.Frame3, font = ('arial', 12),width=10)
               L.grid(row = x,column = 0)
               L.insert(END, i[0])
               L.configure(state=DISABLED)

               L = Entry(self.Frame3, font = ('arial', 12),width=10)
               L.grid(row = x,column = 1)
               L.insert(END, i[1])
               L.configure(state=DISABLED)

               L = Entry(self.Frame3, font = ('arial', 12),width=10)
               L.grid(row = x,column = 2)
               if i[2]==None:
                 L.insert(END, "Due")
               else:
                 L.insert(END, i[2])
               L.configure(state=DISABLED)            

               L = Entry(self.Frame3, font = ('arial', 12),width=10)
               L.grid(row = x,column = 3)
               L.insert(END, i[3])
               L.configure(state=DISABLED)

               L = Entry(self.Frame3, font = ('arial', 12),width=5)
               L.grid(row = x,column = 4)
               if i[4]==None:
                 if i[2]==None:
                   if i[3]<date.today():
                     num=((date.today()-i[3]).days)*5
                     L.insert(END, num)
                   else:
                     L.insert(END, "0")
                 else:
                    L.insert(END, "0")
               else:
                 L.insert(END, i[4])
               L.configure(state=DISABLED)
               
               submitbtn = Button(self.Frame3)
               submitbtn.grid(row = x,column = 5)
               submitbtn.configure(takefocus="")
               submitbtn.configure(text='''  Pay  ''')
               if i[2]==None or i[4]==None:
                 submitbtn.configure(state=DISABLED)
               submitbtn.configure(command=lambda: self.payfine_db(i[5]))
               
               x+=1
      if(flag==0):
          messagebox.showinfo("Error","Cannot find the member")
    except:
      messagebox.showinfo("Error","Cannot fetch the result")
      
  def memberDetails(self):

    global id

    for widgets in self.Frame1.winfo_children():
      widgets.destroy()
    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=174)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Member''')

    L = Label(self.Frame1)
    L.place(relx=0.098, rely=0.200, height=41, width=100)
    L.configure(background="#d9d9d9")
    L.configure(disabledforeground="#a3a3a3")
    L.configure(font="-family {Segoe UI} -size 10")
    L.configure(foreground="#000000")
    L.configure(text='''Enter member ID''')

    id = Entry(self.Frame1)
    id.place(relx=0.320, rely=0.210, height=30, relwidth=0.38)
    id.configure(background="white")
    id.configure(disabledforeground="#a3a3a3")
    id.configure(font="TkFixedFont")
    id.configure(foreground="#000000")
    id.configure(insertbackground="black")

    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.720, rely=0.215, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Submit''')
    submitbtn.configure(command=self.member_db)
    
    self.Frame2 = Frame(self.Frame1)
    self.Frame2.place(relx=0.02, rely=0.30, relheight=0.670, relwidth=0.960)
    self.Frame2.configure(relief='groove')
    self.Frame2.configure(borderwidth="2")
    self.Frame2.configure(relief="groove")
    self.Frame2.configure(background="#d9d9d9")
    

    
    pass
  def payfine_db(self,isid):
    print(isid)
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor(buffered=True)

    try:
        checkavailability="update issue set fine=NULL where issue_id="+ str(isid) +";"
        print(checkavailability)
        cursor.execute(checkavailability)
        db.commit()
        messagebox.showinfo('Success',"Fne paid Successfully")
    except:
        messagebox.showinfo("Error","Cannot return given book ")
    self.memberDetails()
