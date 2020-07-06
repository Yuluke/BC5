from tkinter import *
from tkinter import ttk

import core

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('CryptoInvest')
        self.geometry("1800x1000")
        self.pack_propagate(False)


        tb = core.table(self)
        tb.pack(side=TOP, fill=BOTH)
        
        ntr = core.new_trans(self)
        ntr.pack(side=TOP, fill=BOTH)

        cur = core.cur_invest(self)
        cur.pack(side=TOP, fill=BOTH)

        lst=core.Listbox(self)
        lst.pack(side=TOP, fill=BOTH)
        
    def main(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.main()