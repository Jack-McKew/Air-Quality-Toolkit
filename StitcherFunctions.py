import os
import pandas as pd
from tkinter import messagebox

"""
.. module:: StitcherFunctions
    :platform: Windows
    :synopsis: A module containing all functionality with Stitcher frame.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""

def Stitcher(folders,filename,scale,headerz,outp):
    """This function sums multiple dataframes together and outputs a csv of the result.

    :param folders: This should be a list of filepaths to assosciated filename list.
    :type folders: list[str].
    :param filename: This should be a list of filenames to assosciated filepath (folders) list.
    :type filename: list[str].
    :param scale: This should be a list of scalars to scale assosicated filename dataframe by.
    :type scale: list[float].
    :param headerz: This should be a list of numbers to exclude number of columns from dataframes.
    :type headerz: list[int].
    :param outp: Output filename.
    :type state: str.

    """
    x = 1
    for folder, filename, scale, header in zip(folders,filename,scale,headerz):
        filename = os.path.join(folder,filename)
        filename = filename.replace('\\','/')
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
        try:
            data = pd.read_csv(filename,index_col=0)
            data = data.loc[:,~data.columns.str.contains('^Unnamed')]
            data = data.dropna()
            data.update(data.iloc[:,headlen:].astype(float).multiply((float(scale))))
            if x == 1:
                dataout = data
                x += 1
            else:
                dataout.update(dataout.iloc[:,headlen:].add(data.iloc[:,headlen:]))
        except:
            messagebox.showerror("File Not Found","File not found, please specify file \nFile not found: " + filename)
    try:
        dataout.to_csv(outp)
        print("Complete: File Path " + str(outp))
        messagebox.showinfo("Complete","File Path: " + str(outp))
    except UnboundLocalError:
        messagebox.showwarning("Output Data Empty","Output dataset empty, please check input datasets")
    except OSError:
        messagebox.showerror("Output Data Name","Invalid output dataset filename, please specify output dataset name")
