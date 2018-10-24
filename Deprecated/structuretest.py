import tkinter as tk
from tkinter import BOTH
from tkinter.ttk import Style,Frame

class NO2Processor(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
        olm_state = tk.IntVar()
        olm_state.set(0)

        inputlbl = tk.Label(self,text="File to format as CSV: ")

        filename = tk.Entry(self,width=40)

        outputlbl = tk.Label(self,text="File name of output CSV: ")
        outpname = tk.Entry(self,width=40)
        olm = tk.Checkbutton(self,text="CALPUFF Output Format?",var=olm_state)
        processlbl= tk.Label(self,text="Filename of CSV to process: ")
        processname = tk.Entry(self,width=40)
        backlbl = tk.Label(self,text="File name of Background NO2 CSV: ")
        backname = tk.Entry(self,width=40)
        initiallbl= tk.Label(self,text="Initial % to process (eg 0.1): ")
        initialnum = tk.Entry(self,width=40)
        initialnum.insert(0,"0.1")
        exceedlbl= tk.Label(self,text="Number of exceedances limit (eg 246): ")
        exceednum = tk.Entry(self,width=40)
        exceednum.insert(0,"246")
        headerlbl = tk.Label(self,text="Number of header columns in dataset (eg 3): ")
        headernum = tk.Entry(self,width=40)
        headernum.insert(0,"3")
        outputstatlbl= tk.Label(self,text="File name of output statistics CSV: ")
        outputstatname = tk.Entry(self,width=40)


        inputlbl.grid(column=0,row=0)
        outputlbl.grid(column=0,row=1)
        olm.grid(column=0,row=2)
        processlbl.grid(column=0,row=3)
        backlbl.grid(column=0,row=4)
        initiallbl.grid(column=0,row=5)
        exceedlbl.grid(column=0,row=6)
        headerlbl.grid(column=0,row=7)
        outputstatlbl.grid(column=0,row=8)










class Demo3(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Air Quality Toolkit")
        self.pack(fill=BOTH,expand=1)
        Style().configure("TFrame",background="#333")
        B1 = tk.Button(self,text="New Window",width=200,command=self.new_window)
        B1.place(x=20,y=20)
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.geometry("800x350")
    app = NO2Processor()
    root.mainloop()

if __name__ == '__main__':
    main()