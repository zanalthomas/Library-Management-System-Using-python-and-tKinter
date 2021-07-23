from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import timedelta, date

class Return:
  def return_db(self):

    global id

    bid=id.get()

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
    cursor = db.cursor(buffered=True)


    try:
        checkavailability=" select * from books where available='NO';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag=0

        for i in cursor:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='YES' where bid='"+bid +"';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            sqlquery= "select * from issue where bid='"+bid+"' and return_date is NULL;"
            print(sqlquery)

            cursor.execute(sqlquery)
            row=cursor.fetchone()
            print(row[2],date.today())
            if row[4]<date.today():
                     num=((date.today()-row[4]).days)*5
                     print("num=",num)
                     MsgBox = messagebox.askquestion ('Payment','There is a fine of '+str(num)+' rupees. do you want to pay now?',icon = 'warning')
                     if MsgBox == 'yes':
                        sqlquery= "update issue set return_date='"+ str(date.today()) +"' where issue_id=" + str(row[6]) +";"
                     else:
                        sqlquery= "update issue set return_date='"+ str(date.today()) +"',fine="+str(num)+" where issue_id=" + str(row[6]) +";"
            else:
              print("else")
              sqlquery= "update issue set return_date='"+ str(date.today()) +"' where issue_id=" + str(row[6]) +";"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()
            messagebox.showinfo('Success',"Book returned Successfully")
        else:
            messagebox.showinfo("Error","Invalid Book id")
    except:
        messagebox.showinfo("Error","Cannot return given book ")
    self.returnBooks()
  def returnBooks(self):

    global id

    for widgets in self.Frame1.winfo_children():
      widgets.destroy()
    greet = Label(self.Frame1)
    greet.place(relx=0.314, rely=0.071, height=31, width=190)
    greet.configure(background="#d9d9d9")
    greet.configure(disabledforeground="#a3a3a3")
    greet.configure(font="-family {Poppins Medium} -size 24")
    greet.configure(foreground="#000000")
    greet.configure(text='''Return Book''')

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

  
    submitbtn = Button(self.Frame1)
    submitbtn.place(relx=0.42, rely=0.356, height=25, width=76)
    submitbtn.configure(takefocus="")
    submitbtn.configure(text='''Submit''')
    submitbtn.configure(command=self.return_db)
    
    pass
