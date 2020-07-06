from tkinter import *
from tkinter import ttk


class new_trans (ttk.Frame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, width=600, height=1000,labelanchor='nw', text='Nueva transacción')
        
        self.lb_Qfrom = Label(self)
        self.Qfrom = Display(self)
        self.lb_Qto = Label(self)
        self.Qto = Display(self)


        self.lb_Qfrom.grid(column=0, row=0)
        self.Qfrom.grid(column=0, row=1)
        self.lb_Qto.grid(column=1, row=0)
        self.Qto.grid(column=1, row=1)


class table (ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=600, height=1000)
        
        self.lb_Qfrom = Label(self)
        self.lb_Qfrom.grid(column=0, row=0)
        

class cur_invest (ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=600, height=1000)
        
        self.lb_inv_E = Label(self)
        self.inv_E = Display(self)
        self.lb_inv_V = Label(self)
        self.inv_V = Display(self)
        

        self.lb_inv_E.grid(column=0, row=0)
        self.inv_E.grid(column=1, row=0)
        self.lb_inv_V.grid(column=2, row=0)
        self.inv_V.grid(column=3, row=0)
        

class Label(ttk.Frame):
    value = "text"

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=200, height=40)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 20', background='white', foreground='grey')

        self.lbl = ttk.Label(self, text=self.value, anchor=E, style='my.TLabel')
        self.lbl.pack(side=TOP, fill=BOTH, expand=True)

class Display(ttk.Frame):
    value = "0"
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=200, height=40)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        self.lbl = ttk.Label(self, text=self.value, anchor=E, style='my.TLabel')
        self.lbl.pack(side=TOP, fill=BOTH, expand=True)

    def paint(self, algo):
        self.value = algo
        self.lbl.config(text=algo)

class Listbox(ttk.Frame):
    
    listado={'texto1':1,'texto2':2}

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=200, height=40)
        self.pack_propagate(0)
        
        self.lst=Listbox (self)
        self.lst.insert (END, listado)


    

