""" Air Quality Toolkit
.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""
from tkinter import *
import tkinter.ttk
import os
import csv
import datetime
import pandas as pd
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from CSVFormatter import *
from Stitcher import *
from Factorizer import *
from NO2Processor import *
from Statistics_Generator import *





def _validate(self, P):
        '''Perform input validation.

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

main = Tk()
main.title('Air Quality Toolset')
main.geometry('800x350')

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# Adds tab 1 of the notebook
# gui_style = ttk.Style()
# gui_style.configure('My.TButton', foreground='red')
# gui_style.configure('My.TFrame', background='yellow')

tabnames = ['Statistics Generator','Stitcher','Factorizer','Mass CSV Formatter','NO2 Processor']

tablist = []


for name,i in zip(tabnames,range(1,len(tabnames)+1)):
    pagenum = "page_" + str(i)
    pagenum = ttk.Frame(nb)
    nb.add(pagenum,text=name)
    tablist.append(pagenum)


# page1 = ttk.Frame(nb)
# nb.add(page1, text='NO2 Processor')

# page2 = ttk.Frame(nb,style="My.TFrame")
# nb.add(page2, text='Stitcher')




class NO2Processor(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.olm_state = IntVar()
        self.olm_state.set(0)
        self.inputlbl = Label(self,text="File to format as CSV: ")
        self.filename = Entry(self,width=40)
        self.outputlbl = Label(self,text="File name of output CSV: ")
        self.outpname = Entry(self,width=40)
        self.olm = Checkbutton(self,text="CALPUFF Output Format?",var=self.olm_state)
        self.processlbl= Label(self,text="Filename of CSV to process: ")
        self.processname = Entry(self,width=40)
        self.backlbl = Label(self,text="File name of Background NO2 CSV: ")
        self.backname = Entry(self,width=40)
        self.initiallbl= Label(self,text="Initial % to process (eg 0.1): ")
        self.initialnum = Entry(self,width=40)
        self.initialnum.insert(0,"0.1")
        self.exceedlbl= Label(self,text="Number of exceedances limit (eg 246): ")
        self.exceednum = Entry(self,width=40)
        self.exceednum.insert(0,"246")
        self.headerlbl = Label(self,text="Number of header columns in dataset (eg 3): ")
        self.headernum = Entry(self,width=40)
        self.headernum.insert(0,"3")
        self.outputstatlbl= Label(self,text="File name of output statistics CSV: ")
        self.outputstatname = Entry(self,width=40)

        self.inputlbl.grid(column=0,row=0)
        self.outputlbl.grid(column=0,row=1)
        self.olm.grid(column=0,row=2)
        self.processlbl.grid(column=0,row=3)
        self.backlbl.grid(column=0,row=4)
        self.initiallbl.grid(column=0,row=5)
        self.exceedlbl.grid(column=0,row=6)
        self.headerlbl.grid(column=0,row=7)
        self.outputstatlbl.grid(column=0,row=8)

        self.filename.grid(column=1,row=0)
        self.outpname.grid(column=1,row=1)
        # self.bar.grid(column=1, row=2)
        self.processname.grid(column=1,row=3)
        self.backname.grid(column=1,row=4)
        self.initialnum.grid(column=1,row=5)
        self.exceednum.grid(column=1,row=6)
        self.headernum.grid(column=1,row=7)
        self.outputstatname.grid(column=1,row=8)

        self.browsebtn = Button(self,text="Browse",command=self.BrowseClicked)
        self.browsebtn.config(width=20)
        self.formatbtn = Button(self,text="Format As CSV",command=self.csvformatclicked)
        self.formatbtn.config(width=20)
        self.browseout = Button(self,text='Browse',command=self.browseout)
        self.browseout.config(width=20)
        self.browsecsv = Button(self,text='Browse',command=self.browseback)
        self.browsecsv.config(width=20)
        self.processbtn = Button(self,text='Process CSV',command=self.processClicked)
        self.processbtn.config(width=20)

        self.browsebtn.grid(column=2,row=0)
        self.formatbtn.grid(column=2,row=1)
        self.browseout.grid(column=2,row=3)
        self.browsecsv.grid(column=2,row=4)
        self.processbtn.grid(column=2,row=8)

    def BrowseClicked(self):
        self.filename.delete(0,'end')
        self.outpname.delete(0,'end')
        file = filedialog.askopenfilename(filetypes = (("Dat files","*.dat"),("Text files","*.txt"),("all files","*.*")))
        self.filename.insert(0,os.path.split(file)[1])
        self.outpname.insert(0,os.path.split(file)[1].split('.')[0] + ".csv")

    def processClicked(self):
        try:
            process(headernum.get(),initialnum.get(),exceednum.get(),backname.get(),processname.get(),outputstatname.get())

        except:
            messagebox.showerror("Error","An error has occured while processing")
            raise


    def browseback(self):
        self.backname.delete(0,END)
        file = filedialog.askopenfilename(filetypes = (("CSV files","*.csv"),("all files","*.*")))
        self.backname.insert(0,os.path.split(file)[1])

    def csvformatclicked(self):
        if(olm_state.get() == 1):
            csvformatter(filename.get(),1,outpname.get())
        else:
            csvformatter(filename.get(),0,outpname.get())

    def browseout(self):
        self.processname.delete(0,END)
        self.outputstatname.delete(0,END)
        file = filedialog.askopenfilename(filetypes = (("CSV files","*.csv"),("all files","*.*")))
        self.processname.insert(0,os.path.split(file)[1])
        self.outputstatname.insert(0,os.path.split(file)[1].split('.')[0] + "_Statistics.csv")

NO2Processor(tablist[-1]).grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# Adds tab 2 of the notebook
filesl = []
filesp = []
scalesl = []
headers = []

class SimpleTableInput(Frame):
    def __init__(self, parent, rows, columns,labels):
        Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows

        self.columns = columns
        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")
        column = 0
        for labelname in labels:
            lbl = Label(self,text=labelname)
            lbl.grid(row=0,column=column)
            column += 1
        # create the table of widgets
        for row in range(1,self.rows+1):
            for column in range(self.columns):
                index = (row, column)
                e = Entry(self)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        #self.grid_rowconfigure(rows, weight=1)

    def get(self):
        filesl[:] = []
        filesp[:] = []
        scalesl[:] = []
        headers[:] = []
        '''Return a list of lists, containing the data in the table'''
        for row in range(1,self.rows):
            for column in range(self.columns):
                index = (row, column)
                if column == 0:
                    if self._entry[index].get() != "":
                        filesp.append(self._entry[index].get())
                elif column == 1:
                    if self._entry[index].get() not in filesl:
                        filesl.append(self._entry[index].get())
                elif column == 2:
                    if self._entry[index].get() != "":
                        scalesl.append(self._entry[index].get())
                elif column == 3:
                    if self._entry[index].get() != "":
                        headers.append(self._entry[index].get())
                #current_row.append(self._entry[index].get())
        return filesl

    def getcsvs(self):
        csvsl[:] = []
        olmsl[:] = []
        outpsl[:] = []
        '''Return a list of lists, containing the data in the table'''
        for row in range(1,self.rows):
            for column in range(self.columns):
                index = (row, column)
                if column == 0:
                    if self._entry[index].get() != "":
                        csvsl.append(self._entry[index].get())
                elif column == 1:
                    if self._entry[index].get() != "":
                        olmsl.append(self._entry[index].get())
                elif column == 2:
                    if self._entry[index].get() != "":
                        outpsl.append(self._entry[index].get())
                #current_row.append(self._entry[index].get())

    def getfactors(self):
        factorfilesl[:] = []
        factorsl[:] = []
        outputfactorsl[:] = []
        '''Return a list of lists, containing the data in the table'''
        for row in range(1,self.rows):
            for column in range(self.columns):
                index = (row, column)
                if column == 0:
                    if self._entry[index].get() != "":
                        factorfilesl.append(self._entry[index].get())
                elif column == 1:
                    if self._entry[index].get() != "":
                        factorsl.append(self._entry[index].get())
                elif column == 2:
                    if self._entry[index].get() != "":
                        outputfactorsl.append(self._entry[index].get())

    def addname(self,name):
        for row in range(1,self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                folname = os.path.split(name)[0]
                self._entry[index].insert(0,folname)
            index = (row,1)
            if len(self._entry[index].get()) == 0:
                filname = os.path.split(name)[1]
                self._entry[index].insert(0,filname)
                return

    def addfactor(self,name):
        for row in range(1,self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                self._entry[index].insert(0,name)
            index = (row,2)
            if len(self._entry[index].get()) == 0:
                filname = name.split('.')[0] + "_Factorized.csv"
                self._entry[index].insert(0,filname)
                return

    def addcsv(self,name):
        for row in range(1,self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                self._entry[index].insert(0,name)
            index = (row,2)
            if len(self._entry[index].get()) == 0:
                filname = name.split('.')[0] + ".csv"
                self._entry[index].insert(0,filname)
                return

    def addsettings(self,folder,filename,scale,header):
        folder = folder.replace('\\','/')
        for row in range(1,self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                self._entry[index].insert(0,folder)
                index = (row,1)
                self._entry[index].insert(0,filename)
                index = (row,2)
                self._entry[index].insert(0,scale)
                index = (row, 3)
                self._entry[index].insert(0,header)
                return

    def addfactors(self,filename,factor):
        for row in range(1,self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                self._entry[index].insert(0,filename)
                index = (row,1)
                self._entry[index].insert(0,factor)
                index = (row,2)
                outpuzname = filename.split('.')[0] + "_Factorized.csv"
                self._entry[index].insert(0,outpuzname)
                return

    def addcsvs(self,filename,olmz):
        for row in range(1,self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                self._entry[index].insert(0,filename)
                index = (row,1)
                self._entry[index].insert(0,olmz)
                index = (row,2)
                outpuzname = filename.split('.')[0] + ".csv"
                self._entry[index].insert(0,outpuzname)
                return

    def addrow(self):
        self.rows += 1
        vcmd = (self.register(self._validate), "%P")
        for column in range(self.columns):
                index = (self.rows, column)
                e = Entry(self)
                e.grid(row=self.rows, column=column, stick="nsew")
                self._entry[index] = e

    def clear(self):
        destroyed = 0
        for row in range(1,self.rows+1):
            for column in range(self.columns):
                index = (row, column)
                if(row == 1):
                    self._entry[index].delete(0,'end')
                else:
                    self._entry[index].destroy()
                    destroyed = 1
            if(destroyed):
                self.rows -= 1
                destroyed = 0


    def _validate(self, P):
        '''Perform input validation.

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

class StitcherFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.table = SimpleTableInput(self,1,4,["Folder","Filename","Scale","Columns To Exclude"])
        self.submit = Button(self, text="Stitch", command=self.on_submit)
        self.file = Button(self, text='Browse', command=self.askopenfile)
        self.importe = Button(self, text='Import Settings CSV', command=self.importcsv)
        self.clear = Button(self, text='Clear', command=self.clearset)
        self.addr = Button(self, text='Add Row', command=self.addrow)
        self.outf = Entry(self)
        self.outp = Entry(self, text='output.csv')
        self.table.pack(side="top", fill="both", expand=True)
        self.file.pack(side="left",fill="both",expand=True)
        self.importe.pack(side="left",fill="both",expand=True)
        self.clear.pack(side="left",fill="both",expand=True)
        self.submit.pack(side="left",fill="both",expand=True)
        #self.addr.pack(side="left",fill="both",expand=True)
        self.outf.pack(side="top")
        self.outf.insert(0,str(os.getcwd()))
        self.outp.pack(side="top")


    def addrow(self):
        self.table.addrow()

    def on_submit(self):
        self.table.get()
        try:
            Stitcher(filesp,filesl,scalesl,headers,os.path.join(self.outf.get(),self.outp.get()))
        except TypeError:
            messagebox.showerror("Incorrect Settings","Incorrect settings, please review input table for errors")
            raise

    def askopenfile(self):
        filenamep = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        try:
            self.table.addname(filenamep)
            self.table.addrow()
        except KeyError:
            self.table.addrow()
            self.table.addname(filenamep)

    def importcsv(self):
        colnames = ['filepath','filename','scale','headers']
        try:
            filenamep = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            files = pd.read_csv(filenamep)
            files = files.loc[:,~files.columns.str.contains('^Unnamed')]
            try:
                files.columns = colnames
                folders = files.filepath.tolist()
                filesl = files.filename.tolist()
                scales = files.scale.tolist()
                headers = files.headers.tolist()
                for folder,filename, scale, header in zip(folders,filesl,scales,headers):
                    self.table.addsettings(folder,filename, scale, header)
                    self.table.addrow()
            except ValueError:
                messagebox.showerror("CSV Format Incompatible","Format of settings file is incompatible, refer to how-to on format required\n FORMAT: [Folder,Filename,Scale,Header]")
        except FileNotFoundError:
            messagebox.showerror("File Not Found","Please specify file")

    def clearset(self):
        self.table.clear()

StitcherFrame(tablist[1]).pack(side="top", fill="both", expand=True)


# page3 = ttk.Frame(nb)
# nb.add(page3, text='Factorizer')

factorfilesl = []
factorsl = []
outputfactorsl = []



class Factorizer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 1,3,["Filename","Factor","Output Filename"])
        self.submit = Button(self, text="Factorize", command=self.on_submit)
        self.file = Button(self, text='Browse', command=self.askopenfile)
        self.importe = Button(self, text='Import Settings CSV', command=self.importcsv)
        self.clear = Button(self, text='Clear', command=self.clearset)
        self.addr = Button(self, text='Add Row', command=self.addrow)
        self.table.pack(side="top", fill="both", expand=True)
        self.file.pack(side="left",fill="both",expand=True)
        self.importe.pack(side="left",fill="both",expand=True)
        self.clear.pack(side="left",fill="both",expand=True)
        self.submit.pack(side="left",fill="both",expand=True)



    def addrow(self):
        self.table.addrow()

    def on_submit(self):
        self.table.getfactors()
        for factor, filename, outputname in zip(factorsl,factorfilesl,outputfactorsl):
            factorizer(filename,factor,outputname)

    def askopenfile(self):
        filenamep = filedialog.askopenfilename(title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        try:
            self.table.addfactor(filenamep)
        except KeyError:
            self.table.addrow()
            self.table.addfactor(filenamep)

    def importcsv(self):
        colnames = ['filename','factors']
        try:
            filenamep = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            files = pd.read_csv(filenamep)
            files = files.loc[:,~files.columns.str.contains('^Unnamed')]
            files.columns = colnames
            filesl = files.filename.tolist()
            factors = files.factors.tolist()
            for filename, factor in zip(filesl,factors):
                self.table.addrow()
                self.table.addfactors(filename, factor)
        except FileNotFoundError:
            messagebox.showerror("File Not Found","Please specify file")

    def clearset(self):
        self.table.clear()

Factorizer(tablist[2]).pack(side="top", fill="both", expand=True)

# page4 = ttk.Frame(nb)
# nb.add(page4, text='Mass CSV Formatter')

csvsl = []
olmsl = []
outpsl = []

class MassCSV(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 1,3,["Filename","CALPUFF Output Format? (0/1)","Output Filename"])
        self.submit = Button(self, text="Convert", command=self.on_submit)
        self.file = Button(self, text='Browse', command=self.askopenfile)
        self.importe = Button(self, text='Import Settings CSV', command=self.importcsv)
        self.clear = Button(self, text='Clear', command=self.clearset)
        self.addr = Button(self, text='Add Row', command=self.addrow)
        self.table.pack(side="top", fill="both", expand=True)
        self.file.pack(side="left",fill="both",expand=True)
        self.importe.pack(side="left",fill="both",expand=True)
        self.clear.pack(side="left",fill="both",expand=True)
        self.submit.pack(side="left",fill="both",expand=True)

    def addrow(self):
        self.table.addrow()

    def on_submit(self):
        self.table.getcsvs()
        for filename,olm,output_filename in zip(csvsl,olmsl,outpsl):
            csvformatter(filename,olm,output_filename)
            page4.update_idletasks()
        messagebox.showinfo("Format Complete","All files converted to csv")

    def askopenfile(self):
        filenamep = filedialog.askopenfilename(title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        try:
            self.table.addcsv(filenamep)
        except KeyError:
            self.table.addrow()
            self.table.addcsv(filenamep)

    def importcsv(self):
        colnames = ['filename','OLM']
        try:
            filenamep = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            files = pd.read_csv(filenamep)
            files = files.loc[:,~files.columns.str.contains('^Unnamed')]
            files.columns = colnames
            filesl = files.filename.tolist()
            olms = files.OLM.tolist()
            for filename, olm in zip(filesl,olms):
                self.table.addrow()
                self.table.addcsvs(filename, olm)
        except FileNotFoundError:
            messagebox.showerror("File Not Found","Please specify file")


    def clearset(self):
        self.table.clear()

MassCSV(tablist[3]).pack(side="top", fill="both", expand=True)

# page5 = ttk.Frame(nb)
# nb.add(page5,text="Statistics Generator")

class Statistics_Generator(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.statlbl= Label(self,text="Filename of CSV to process: ")
        self.statname = Entry(self,width=40)
        self.header2lbl = Label(self,text="Number of header columns in dataset (eg 3): ")
        self.header2num = Entry(self,width=40)
        self.header2num.insert(0,"3")
        self.outputstat2lbl= Label(self,text="File name of output statistics CSV: ")
        self.outputstat2name = Entry(self,width=40)

        self.percentilelbl = Label(self,text="Percentile to compute (eg 99.9): ")
        self.percentilename = Entry(self,width=40)
        self.percentilename.insert(0,"99.9")

        self.rollinglbl = Label(self,text="Rolling average window (eg 8): ")
        self.rollingname = Entry(self,width=40)
        self.rollingname.insert(0,"8")

        self.settingslbl = Label(self,text='Settings for Statistics Output')

        self.browsestatbtn = Button(self,text="Browse",command=self.browsestatclicked)
        self.browsestatbtn.config(width=20)

        self.runstatsbtn = Button(self,text="Run",command=self.runstats)
        self.runstatsbtn.config(width=20)

        self.mean_state = IntVar()
        self.mean_state.set(1)
        self.mean = Checkbutton(self,text="Average of Sensor",var=self.mean_state)
        self.max_mean_state = IntVar()
        self.max_mean_state.set(1)
        self.max_mean = Checkbutton(self,text="Max Average of Sensors",var=self.max_mean_state)
        self.max_sens_state = IntVar()
        self.max_sens_state.set(1)
        self.max_sens = Checkbutton(self,text="Max of Sensor",var=self.max_sens_state)
        self.max_state = IntVar()
        self.max_state.set(1)
        self.maxbut = Checkbutton(self,text="Max of All Sensors",var=self.max_state)
        self.percentile_state = IntVar()
        self.percentile_en = Checkbutton(self,text="Enable Percentile",var=self.percentile_state)
        self.max_of_percentile = IntVar()
        self.max_of_percentile.set(0)
        self.max_percentile = Checkbutton(self,text="Max of Percentile",var=self.max_of_percentile)

        self.rolling_state = IntVar()
        self.rolling_en = Checkbutton(self,text="Enable Rolling",var=self.rolling_state)
        self.rolling_max_state = IntVar()
        self.rolling_max_en = Checkbutton(self,text="Max of Rolling",var=self.rolling_max_state)

        self.statlbl.grid(column=0,row=0)
        self.header2lbl.grid(column=0,row=1)
        self.outputstat2lbl.grid(column=0,row=2)
        self.settingslbl.grid(column=1,row=3)
        self.percentilelbl.grid(column=0,row=6)
        self.rollinglbl.grid(column=0,row=8)

        self.statname.grid(column = 1,row = 0)
        self.header2num.grid(column= 1,row = 1)
        self.outputstat2name.grid(column=1,row=2)
        self.percentilename.grid(column=1,row=6)
        self.rollingname.grid(column=1,row=8)

        self.browsestatbtn.grid(column=2,row=0)
        self.runstatsbtn.grid(column=2,row=2)
        self.mean.grid(column=0,row = 4)
        self.max_mean.grid(column=1,row=4)
        self.maxbut.grid(column=2,row=4)
        self.max_sens.grid(column=0,row=5)
        self.percentile_en.grid(column=2,row=6)
        self.max_percentile.grid(column=2,row=7)
        self.rolling_en.grid(column=2,row=8)
        self.rolling_max_en.grid(column=2,row=9)


    def browsestatclicked(self):
        self.statname.delete(0,'end')
        self.outputstat2name.delete(0,'end')
        file = filedialog.askopenfilename(filetypes = (("CSV files","*.csv"),("all files","*.*")))
        self.statname.insert(0,os.path.split(file)[1])
        self.outputstat2name.insert(0,os.path.split(file)[1].split('.')[0] + "_Statistics.csv")

    def runstats(self):
        settings = {}
        settings['max_of_sensor'] = self.max_sens_state.get()
        settings['mean'] = self.mean_state.get()
        settings['max_mean'] = self.max_mean_state.get()
        settings['max'] = self.max_state.get()
        settings['percentile'] = self.percentile_state.get()
        if self.percentile_state.get() == 1:
            settings['percentile_value'] = float(self.percentilename.get()) / 100
        settings['max_percentile'] = self.max_of_percentile.get()
        settings['rolling'] = self.rolling_state.get()
        if self.rolling_state.get() == 1:
            settings['rolling_value'] = int(self.rollingname.get())
        settings['max_rolling'] = self.rolling_max_state.get()

        Statistics_Generator(settings,self.header2num.get(),self.statname.get(),self.outputstat2name.get())


Statistics_Generator(tablist[0]).grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')





main.mainloop()
