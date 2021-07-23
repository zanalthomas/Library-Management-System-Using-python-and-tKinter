
import sys
import mysql.connector
from tkinter import messagebox
from Dashboard import *
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = TopLevel1 (root)
   
    root.mainloop()

w = None
def destroy_TopLevel1():
    global w
    w.destroy()
    w = None

class TopLevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9' 
        _fgcolor = '#000000' 
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+310+132")
        top.minsize(116, 1)
        top.maxsize(1366, 746)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=-0.017, rely=-0.044, relheight=0.229
                , relwidth=1.038)
        self.Canvas1.configure(background="#000000")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.033, rely=0.022, relheight=0.118
                , relwidth=0.933)
        self.Message1.configure(background="#000000")
        self.Message1.configure(font="-family {Poppins SemiBold} -size 24 -weight bold")
        self.Message1.configure(foreground="#ffffff")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Library Management System''')
        self.Message1.configure(width=560)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.367, rely=0.244, relheight=0.118
                , relwidth=0.233)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(font="-family {Poppins ExtraBold} -size 14 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''LOGIN''')
        self.Message2.configure(width=140)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.317, rely=0.4, height=30, relwidth=0.373)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 13")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.317, rely=0.511, height=30, relwidth=0.373)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 13")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")
        self.Entry2.configure(show="*")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.133, rely=0.422, height=21, width=104)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Poppins Medium} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Username''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.133, rely=0.533, height=21, width=104)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Poppins Medium} -size 9")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Password''')

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.433, rely=0.644, height=25, width=76)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Submit''')
        self.TButton1.configure(command=self.check)

    def check(self):
        user=self.Entry1.get()
        password=self.Entry2.get()
        db = mysql.connector.connect(host ="localhost",user = "root",password = 'sanal',database='library',charset="utf8")
        cursor = db.cursor()
        sqlquery= "select * from admin where user='"+user+"' and pass='"+password+"';"
        print(sqlquery)
        flag=0
        cursor.execute(sqlquery)
        for i in cursor:
            if i[0]==user and i[1]==password:
                flag=1
                break
        if flag==1:
              messagebox.showinfo("success","Login Successfull")
              create_Toplevel1(root)
        else :
              messagebox.showinfo("wrong password","The Credentials you have entered is wrong")
 
if __name__ == '__main__':
    vp_start_gui()





