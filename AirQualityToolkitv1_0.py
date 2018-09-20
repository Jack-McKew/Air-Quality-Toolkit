#!/usr/bin/python
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


def BrowseClicked():
    filename.delete(0,'end')
    outpname.delete(0,'end')
    file = filedialog.askopenfilename(filetypes = (("Dat files","*.dat"),("Text files","*.txt"),("all files","*.*")))
    filename.insert(0,os.path.split(file)[1])
    outpname.insert(0,os.path.split(file)[1].split('.')[0] + ".csv")

def csvformatter():
    bar['value'] = 0
    try:
        file = open(os.path.join(os.getcwd(),filename.get()))
        outpath = os.path.join(os.getcwd(),outpname.get())
        reader = csv.reader(file)
        x = 1
        if(olm_state.get()):
            for i, row in enumerate(reader):
                if i == 8:
                    length = int(len(row[0].split())) - 1
                    writer = csv.writer(open(outpath, "w"), delimiter = ',', lineterminator='\n')
                    header = ['year','day','hour']
                    header.extend(list(range(1,length)))
                    writer.writerow(header)
                if i==9:
                    new_row = []
                    if x == 1:
                        for j in range(1,len(filter(None,str(row).split(" "))[2:]) + 1):
                            new_row.append("Rec " + str(j))
                        loclist = pd.DataFrame(new_row)
                        new_row = []
                        x = 0
                    for j in filter(None,str(row).split(" "))[2:]:
                        new_row.append(float(j.strip("']")))
                    loclist['x'] = new_row
                if i==10:
                    new_row = []
                    for j in filter(None,str(row).split(" "))[2:]:
                        new_row.append(float(j.strip("']")))
                    loclist['y'] = new_row
                    locname = filename.get() + "_Locations.csv"
                    loclist.to_csv(locname)

                if i>15 and row[0] is not "":
                    year = row[0].split()[0]
                    day = row[0].split()[1]
                    hour = row[0].split()[2]
                    columns = []
                    new_row = [year,day,hour]
                    length = int(len(row[0].split()))
                    for j in range(3,length):
                        value = float(row[0].split()[j])
                        if value is not "":
                            #value = (value*initial + min(0.9*value,(46/48)*ozone))
                            columns.append(value)
                    new_row.extend(columns)
                    writer = csv.writer(open(outpath, "a+"), delimiter = ',', lineterminator='\n')
                    writer.writerow(new_row)
                    bar['value'] += 0.2739726027397260273972602739726
                    page1.update()
        else:
            txt_file = filename.get()
            csv_file = outpath
            in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
            out_csv = csv.writer(open(outpath, 'wb'))
            out_csv.writerows(in_txt)
            bar['value'] = 100
            page1.update()
            processname.delete(0,END)
            processname.insert(0,outpname.get())
    except OSError:
        messagebox.showerror("File Not Found","File not found, please specify file to format")

def browseback():
    backname.delete(0,END)
    file = filedialog.askopenfilename(filetypes = (("CSV files","*.csv"),("all files","*.*")))
    backname.insert(0,os.path.split(file)[1])

def browseout():
    processname.delete(0,END)
    outputstatname.delete(0,END)
    file = filedialog.askopenfilename(filetypes = (("CSV files","*.csv"),("all files","*.*")))
    processname.insert(0,os.path.split(file)[1])
    outputstatname.insert(0,os.path.split(file)[1].split('.')[0] + "_Statistics.csv")

def process():
    initial = float(initialnum.get())
    exceed = float(exceednum.get())
    backpath = os.path.join(os.getcwd(),backname.get())
    outpath = os.path.join(os.getcwd(),processname.get())
    try:
        background = pd.read_csv(backpath)
        data = pd.read_csv(outpath,index_col=1)

        data['background'] = list(map(lambda x: float(x*0.9583333),background['Ozone']))

        def test(row):
            back = float(row[-1])
            new_row = []
            for value in row[2:-1]:
                value = value*initial + min(0.9*value,back)
                new_row.append(value)
            return pd.Series(new_row)


        data = data.apply(test,axis=1)

        outdf = pd.DataFrame({  'Max of Sensor':data.max(),'Average of Sensor':data.mean(),
                                'Number of Exceedances':data[data > exceed].count(),
                                'Average Max Column':data.max().mean(),
                                'Max Value':data.values.max()})
        outdf.index.name = 'Sensor ID'
        outdf.to_csv(outputstatname.get())
    except OSError:
        messagebox.showerror("File Not Found","File not found, please specify CSV and/or Background NO2 CSV")


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
main.geometry('800x300')

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
gui_style = ttk.Style()
gui_style.configure('My.TButton', foreground='red')
gui_style.configure('My.TFrame', background='pink')
page1 = ttk.Frame(nb,style='My.TFrame')
nb.add(page1, text='NO2 Processor')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(page1, length=200, style='black.Horizontal.TProgressbar')

olm_state = IntVar()
olm_state.set(0)

inputlbl = Label(page1,text="File to format as CSV: ")
filename = Entry(page1,width=40)
outputlbl = Label(page1,text="File name of output CSV: ")
outpname = Entry(page1,width=40)
olm = Checkbutton(page1,text="OLM?",var=olm_state)
processlbl= Label(page1,text="Filename of CSV to process: ")
processname = Entry(page1,width=40)
backlbl = Label(page1,text="File name of Background NO2 CSV: ")
backname = Entry(page1,width=40)
initiallbl= Label(page1,text="Initial % to process (eg 0.1): ")
initialnum = Entry(page1,width=40)
initialnum.insert(0,"0.1")
exceedlbl= Label(page1,text="Number of exceedances limit (eg 246): ")
exceednum = Entry(page1,width=40)
exceednum.insert(0,"246")
outputstatlbl= Label(page1,text="File name of output statistics CSV: ")
outputstatname = Entry(page1,width=40)

browsebtn = Button(page1,text="Browse",command=BrowseClicked)
browsebtn.config(width=20)
formatbtn = Button(page1,text="Format As CSV",command=csvformatter)
formatbtn.config(width=20)
browseout = Button(page1,text='Browse',command=browseout)
browseout.config(width=20)
browsecsv = Button(page1,text='Browse',command=browseback)
browsecsv.config(width=20)
processbtn = Button(page1,text='Process CSV',command=process)
processbtn.config(width=20)

inputlbl.grid(column=0,row=0)
outputlbl.grid(column=0,row=1)
olm.grid(column=0,row=2)
processlbl.grid(column=0,row=3)
backlbl.grid(column=0,row=4)
initiallbl.grid(column=0,row=5)
exceedlbl.grid(column=0,row=6)
outputstatlbl.grid(column=0,row=7)


filename.grid(column=1,row=0)
outpname.grid(column=1,row=1)
bar.grid(column=1, row=2)
processname.grid(column=1,row=3)
backname.grid(column=1,row=4)
initialnum.grid(column=1,row=5)
exceednum.grid(column=1,row=6)
outputstatname.grid(column=1,row=7)

browsebtn.grid(column=2,row=0)
formatbtn.grid(column=2,row=1)
browseout.grid(column=2,row=3)
browsecsv.grid(column=2,row=4)
processbtn.grid(column=2,row=7)


# Adds tab 2 of the notebook
page2 = ttk.Frame(nb,style="My.TFrame")
nb.add(page2, text='Stitcher')
filesl = []
filesp = []
scalesl = []
headers = []

def Stitcher(folders,filename,scale,headerz,outp):
    x = 1
    for folder, filename, scale, header in zip(folders,filename,scale,headerz):
        filename = os.path.join(folder,filename)
        print("Processing: " + filename + " Scale: " + scale + " Header: " + header)
        try:
            float(scale)
        except ValueError:
            print("Invalid Scale for: " + filename + " Scale: " + scale + " is not a number")
            continue
        try:
            int(header)
        except ValueError:
            print("Invalid Scale for: " + filename + " Header: " + header + " is not a number")
            continue
        headlen = int(header)
        data = pd.read_csv(filename,index_col=0)
        data = data.loc[:,~data.columns.str.contains('^Unnamed')]
        data = data.dropna()
        data.update(data.iloc[:,headlen:].astype(float).multiply((float(scale))))
        if x == 1:
            dataout = data
            x += 1
        else:
            dataout.update(dataout.iloc[:,headlen:].add(data.iloc[:,headlen:]))
    dataout.to_csv(outp)
    print("Complete: File Path " + str(outp))


class SimpleTableInput(Frame):
    def __init__(self, parent, rows, columns):
        Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows

        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
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
        for row in range(self.rows):
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
        '''Return a list of lists, containing the data in the table'''
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                if column == 0:
                    if self._entry[index].get() != "":
                        csvsl.append(self._entry[index].get())
                elif column == 1:
                    if self._entry[index].get() not in filesl:
                        olmsl.append(self._entry[index].get())
                #current_row.append(self._entry[index].get())

    def getfactors(self):
        factorfilesl[:] = []
        factorsl[:] = []
        '''Return a list of lists, containing the data in the table'''
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                if column == 0:
                    if self._entry[index].get() != "":
                        factorfilesl.append(self._entry[index].get())
                elif column == 1:
                    if self._entry[index].get() not in filesl:
                        factorsl.append(self._entry[index].get())
                #current_row.append(self._entry[index].get())

    def addname(self,name):
        for row in range(self.rows+1):
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
        for row in range(self.rows+1):
            index = (row,0)
            if len(self._entry[index].get()) == 0:
                self._entry[index].insert(0,name)
            index = (row,2)
            if len(self._entry[index].get()) == 0:
                filname = name.split('.')[0] + "_Factorized.csv"
                self._entry[index].insert(0,filname)
                return

    def addcsv(self,name):
        for row in range(self.rows+1):
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
        for row in range(self.rows+1):
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
        for row in range(self.rows+1):
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
        for row in range(self.rows+1):
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
                index = (self.rows-1, column)
                e = Entry(self)
                e.grid(row=self.rows, column=column, stick="nsew")
                self._entry[index] = e

    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                self._entry[index].delete(0,'end')


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

class Stitcher(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 1,4)
        self.hdrlbl = Label(self,text="Folder                              Filename                                  Scale                                          Columns to exclude")
        self.submit = Button(self, text="Stitch", command=self.on_submit)
        self.file = Button(self, text='Browse', command=self.askopenfile)
        self.importe = Button(self, text='Import Settings CSV', command=self.importcsv)
        self.clear = Button(self, text='Clear', command=self.clearset)
        self.addr = Button(self, text='Add Row', command=self.addrow)
        self.outf = Entry(self)
        self.outp = Entry(self, text='output.csv')
        self.hdrlbl.pack(side="top",fill="both")
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

    def askopenfile(self):
        filenamep = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        try:
            self.table.addname(filenamep)
        except KeyError:
            self.table.addrow()
            self.table.addname(filenamep)

    def importcsv(self):
        colnames = ['filepath','filename','scale','headers']
        try:
            filenamep = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            files = pd.read_csv(filenamep)
            files = files.loc[:,~files.columns.str.contains('^Unnamed')]
            files.columns = colnames
            folders = files.filepath.tolist()
            filesl = files.filename.tolist()
            scales = files.scale.tolist()
            headers = files.headers.tolist()
            for folder,filename, scale, header in zip(folders,filesl,scales,headers):
                self.table.addrow()
                self.table.addsettings(folder,filename, scale, header)
        except FileNotFoundError:
            messagebox.showerror("File Not Found","Please specify file")

    def clearset(self):
        self.table.clear()

Stitcher(page2).pack(side="top", fill="both", expand=True)


page3 = ttk.Frame(nb)
nb.add(page3, text='Factorizer')

factorfilesl = []
factorsl = []

def calcrow(row):
        factor = float(row[-1])
        new_row = []
        for value in row[:-1]:
                value = value*factor
                new_row.append(value)
        return pd.Series(new_row)

def factorize(factorsname,inputname):
    page3.update_idletasks()
    for factorname,filename in zip(factorsname,inputname):
        outpname = filename.split('.')[0] + "_Factorized.csv"
        factors1path = os.path.join(os.getcwd(),factorname)
        factors = pd.read_csv(factors1path)
        inputpath = os.path.join(os.getcwd(),filename)
        data = pd.read_csv(inputpath)
        data['factor'] = factors.iloc[:,2]
        outdata = data.iloc[:,2:].apply(calcrow,axis=1)
        outdata = pd.concat([factors.iloc[:,:2],outdata,data.iloc[:,-1]],axis=1)
        outdata.columns = data.columns
        outdata.iloc[:,:-1].to_csv(os.path.join(os.getcwd(),outpname),index=False)

class Factorizer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 1,3)
        self.hdrlbl = Label(self,text="Filename                              Factor                                                   Output Filename")
        self.submit = Button(self, text="Factorize", command=self.on_submit)
        self.file = Button(self, text='Browse', command=self.askopenfile)
        self.importe = Button(self, text='Import Settings CSV', command=self.importcsv)
        self.clear = Button(self, text='Clear', command=self.clearset)
        self.addr = Button(self, text='Add Row', command=self.addrow)
        self.hdrlbl.pack(side="top",fill="both")
        self.table.pack(side="top", fill="both", expand=True)
        self.file.pack(side="left",fill="both",expand=True)
        self.importe.pack(side="left",fill="both",expand=True)
        self.clear.pack(side="left",fill="both",expand=True)
        self.submit.pack(side="left",fill="both",expand=True)



    def addrow(self):
        self.table.addrow()

    def on_submit(self):
        self.table.getfactors()
        factorize(factorsl,factorfilesl)

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

Factorizer(page3).pack(side="top", fill="both", expand=True)

page4 = ttk.Frame(nb)
nb.add(page4, text='Mass CSV Formatter')

csvsl = []
olmsl = []

def masscsvformatter(filename,olm):
    print("Formatting " + filename)
    page4.update_idletasks()
    file = open(os.path.join(os.getcwd(),filename))
    outpname = filename.split('.')[0] + ".csv"
    outpath = os.path.join(os.getcwd(),outpname)
    reader = csv.reader(file)
    x = 1
    if(olm == 1):
        for i, row in enumerate(reader):
            if i == 8:
                length = int(len(row[0].split())) - 1
                writer = csv.writer(open(outpath, "w"), delimiter = ',', lineterminator='\n')
                header = ['year','day','hour']
                header.extend(list(range(1,length)))
                writer.writerow(header)
            if i==9:
                new_row = []
                if x == 1:
                    for j in range(1,len(filter(None,str(row).split(" "))[2:]) + 1):
                        new_row.append("Rec " + str(j))
                    loclist = pd.DataFrame(new_row)
                    new_row = []
                    x = 0
                for j in filter(None,str(row).split(" "))[2:]:
                    new_row.append(float(j.strip("']")))
                loclist['x'] = new_row
            if i==10:
                new_row = []
                for j in filter(None,str(row).split(" "))[2:]:
                    new_row.append(float(j.strip("']")))
                loclist['y'] = new_row
                locname = filename + "_Locations.csv"
                loclist.to_csv(locname)

            if i>15 and row[0] is not "":
                year = row[0].split()[0]
                day = row[0].split()[1]
                hour = row[0].split()[2]
                columns = []
                new_row = [year,day,hour]
                length = int(len(row[0].split()))
                for j in range(3,length):
                    value = float(row[0].split()[j])
                    if value is not "":
                        columns.append(value)
                new_row.extend(columns)
                writer = csv.writer(open(outpath, "a+"), delimiter = ',', lineterminator='\n')
                writer.writerow(new_row)
    else:
        txt_file = filename
        csv_file = outpath
        in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
        out_csv = csv.writer(open(outpath, 'wb'))
        out_csv.writerows(in_txt)

class MassCSV(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 1,3)
        self.hdrlbl = Label(self,text="Filename                              OLM? (0/1)                      Output Filename")
        self.submit = Button(self, text="Convert", command=self.on_submit)
        self.file = Button(self, text='Browse', command=self.askopenfile)
        self.importe = Button(self, text='Import Settings CSV', command=self.importcsv)
        self.clear = Button(self, text='Clear', command=self.clearset)
        self.addr = Button(self, text='Add Row', command=self.addrow)
        self.hdrlbl.pack(side="top",fill="both")
        self.table.pack(side="top", fill="both", expand=True)
        self.file.pack(side="left",fill="both",expand=True)
        self.importe.pack(side="left",fill="both",expand=True)
        self.clear.pack(side="left",fill="both",expand=True)
        self.submit.pack(side="left",fill="both",expand=True)



    def addrow(self):
        self.table.addrow()

    def on_submit(self):
        self.table.getcsvs()
        for filename,olm in zip(csvsl,olmsl):
            masscsvformatter(filename,olm)

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

MassCSV(page4).pack(side="top", fill="both", expand=True)

main.mainloop()
