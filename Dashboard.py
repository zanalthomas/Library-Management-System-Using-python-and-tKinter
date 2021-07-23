
import sys

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

from add import *
from issue import *
from Return import *
from view import *
from member import *
from control import *
from renew import *
w = None

    
def create_Toplevel1(rt):
    global w, w_win, root,top
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init(w, top)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1(home,issue,Return,view,member,control,renew):
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

        top.geometry("704x480+352+105")
        top.minsize(116, 1)
        top.maxsize(1366, 746)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.267, rely=0.11, relheight=0.879, relwidth=0.724)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        greet = Label(self.Frame1)
        greet.place(relx=0.314, rely=0.271, height=31, width=174)
        greet.configure(background="#d9d9d9")
        greet.configure(disabledforeground="#a3a3a3")
        greet.configure(font="-family {Poppins Medium} -size 24")
        greet.configure(foreground="#000000")
        greet.configure(text='''Welcome''')

        L = Label(self.Frame1)
        L.place(relx=0.200, rely=0.335, height=41, width=294)
        L.configure(background="#d9d9d9")
        L.configure(disabledforeground="#a3a3a3")
        L.configure(font="-family {Segoe UI} -size 10")
        L.configure(foreground="#000000")
        L.configure(text='''Manage your library easily and efficiently''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.028, rely=0.125, height=44, width=127)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.addBooks)
        self.Button1.configure(text='''Add Book''')

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.028, rely=0.25, height=44, width=127)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#000000")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(command=self.issueBooks)
        self.Button1_1.configure(text='''Issue Book''')

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.028, rely=0.375, height=44, width=127)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#000000")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1_2.configure(foreground="#ffffff")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Renew Book''')
        self.Button1_2.configure(command=self.renewBooks)

        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.028, rely=0.5, height=44, width=127)
        self.Button1_3.configure(activebackground="#ececec")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#000000")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1_3.configure(foreground="#ffffff")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(command=self.returnBooks)
        self.Button1_3.configure(text='''Return Book''')

        self.Button1_4 = tk.Button(top)
        self.Button1_4.place(relx=0.028, rely=0.625, height=44, width=127)
        self.Button1_4.configure(activebackground="#ececec")
        self.Button1_4.configure(activeforeground="#000000")
        self.Button1_4.configure(background="#000000")
        self.Button1_4.configure(disabledforeground="#a3a3a3")
        self.Button1_4.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1_4.configure(foreground="#ffffff")
        self.Button1_4.configure(highlightbackground="#d9d9d9")
        self.Button1_4.configure(highlightcolor="black")
        self.Button1_4.configure(pady="0")
        self.Button1_4.configure(command=self.viewBooks)
        self.Button1_4.configure(text='''Search Book''')

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=-0.017, rely=-0.023, relheight=0.119
                , relwidth=1.038)
        self.Canvas1.configure(background="#000000")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Message1 = tk.Message(self.Canvas1)
        self.Message1.place(relx=0.178, rely=0.351, relheight=0.404
                , relwidth=0.726)
        self.Message1.configure(background="#000000")
        self.Message1.configure(font="-family {Poppins Medium} -size 16 -weight bold")
        self.Message1.configure(foreground="#ffffff")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Library Management System''')
        self.Message1.configure(width=531)

        self.Button1_5 = tk.Button(top)
        self.Button1_5.place(relx=0.028, rely=0.75, height=44, width=127)
        self.Button1_5.configure(activebackground="#ececec")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#000000")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1_5.configure(foreground="#ffffff")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(command=self.memberDetails)
        self.Button1_5.configure(text='''Members''')

        self.Button1_5_1 = tk.Button(top)
        self.Button1_5_1.place(relx=0.028, rely=0.875, height=44, width=127)
        self.Button1_5_1.configure(activebackground="#ececec")
        self.Button1_5_1.configure(activeforeground="#000000")
        self.Button1_5_1.configure(background="#000000")
        self.Button1_5_1.configure(disabledforeground="#a3a3a3")
        self.Button1_5_1.configure(font="-family {Poppins SemiBold} -size 13 -weight bold")
        self.Button1_5_1.configure(foreground="#ffffff")
        self.Button1_5_1.configure(highlightbackground="#d9d9d9")
        self.Button1_5_1.configure(highlightcolor="black")
        self.Button1_5_1.configure(pady="0")
        self.Button1_5_1.configure(command=self.adminControl)
        self.Button1_5_1.configure(text='''Controls''')


def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None





