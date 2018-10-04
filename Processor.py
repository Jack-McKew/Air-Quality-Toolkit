import os
import pandas as pd
from tkinter import messagebox

"""
.. module:: NO2Processor
    :platform: Windows
    :synopsis: A module containing functionality for formatting air quality modelling dumps.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""

def process(header_length,initial,exceedance,background_name,input_data,output_filename):
    """[summary]

    Arguments:
        header_length {[type]} -- [description]
        initial {[type]} -- [description]
        exceedance {[type]} -- [description]
        background_name {[type]} -- [description]
        input_data {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    header_length = int(header_length)
    initial = float(initial)
    backpath = os.path.join(os.getcwd(),background_name)
    outpath = os.path.join(os.getcwd(),input_data)
    try:
        background = pd.read_csv(backpath)
        temp_list = []
        data = pd.DataFrame
        for chunk in pd.read_csv(outpath,index_col=1,chunksize=2000):
            temp_list.append(chunk)
        data = pd.concat(temp_list)
        del temp_list
        data['background'] = list(map(lambda x: float(x*0.9583333),background['Ozone']))

        data = data.fillna(0)
        def olmfunction(row):
            back = float(row[-1])
            new_row = []
            for value in row[header_length:-1]:
                value = float(value)*initial + min(0.9*float(value),back)
                new_row.append(value)
            return pd.Series(new_row)

        def backfunction(row):
            back = float(row[-1])
            new_row = []
            for value in row[header_length:-1]:
                value = value + back
                new_row.append(value)
            return pd.Series(new_row)

        data = data.apply(olmfunction,axis=1)
        outdf = pd.DataFrame({  'Max of Sensor':data.max(),'Average of Sensor':data.mean(),
                                'Number of Exceedances':data[data > exceedance].count(),
                                'Average Max Column':data.max().mean(),
                                'Max Value':data.values.max(),
                                '99.9th Percentile of Sensor':data.quantile(0.999),
                                'Max of 99.9th Percentile':data.quantile(0.999).max(),
                                '8 Hour Average of Sensor':data.rolling(window=8).mean().max(),
                                '8 Hour Max':data.rolling(window=8).mean().max().max()})
        outdf.index.name = 'Sensor ID'
        outdf.to_csv(output_filename)
        messagebox.showinfo("Complete","Processing complete, file name is: " + output_filename)
        messagebox.ask
        backquestion = messagebox.askyesno("Background NO2 statistics?","Would you like to process Background NO2 statistics?")

        if backquestion == True:
            data['background'] = list(background['Background NO2'])
            data = data.apply(backfunction,axis=1)
            print(data)
            outdf = pd.DataFrame({  'Max of Sensor':data.max(),'Average of Sensor':data.mean(),
                                'Number of Exceedances':data[data > exceedance].count(),
                                'Average Max Column':data.max().mean(),
                                'Max Value':data.values.max(),
                                '99.9th Percentile of Sensor':data.quantile(0.999),
                                'Max of 99.9th Percentile':data.quantile(0.999).max(),
                                '8 Hour Average of Sensor':data.rolling(window=8).mean().max(),
                                '8 Hour Max':data.rolling(window=8).mean().max().max()})
            outdf.index.name = 'Sensor ID'
            new_name = output_filename.split('.')[0] + "_BG_NO2.csv"
            outdf.to_csv(new_name)
            messagebox.showinfo("Complete","Processing complete, file name is: " + new_name)

    except OSError:
        messagebox.showerror("File Not Found","File not found, please specify CSV and/or Background NO2 CSV")
        raise
    except ValueError:
        messagebox.showerror("Invalid Dataset","Invalid dataset, please check input datasets")
        raise
