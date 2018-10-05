import os
import pandas as pd
from tkinter import messagebox

"""
.. module:: Statistics_Generator
    :platform: Windows
    :synopsis: A module containing functionality for formatting air quality modelling dumps.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""

def Statistics_Generator(settings,header_length,input_data,output_filename):
    """This function generates statistics on given input datasets.

    :param settings: This should be a dictionary of settings with their name as the key and state as value.
    :type settings: dict[str:int].
    :param header_length: This should be an integer declaring how many header columns in the dataset
    :type header_length: int.
    :param input_data: This should be a string representing input filename (Must be located in same directory as .exe).
    :type input_data: str.
    :param output_filename: Output filename.
    :type output_filename: str.

    """
    print(settings)

    header_length = int(header_length)
    outpath = os.path.join(os.getcwd(),input_data)
    try:
        temp_list = []
        data = pd.DataFrame
        for chunk in pd.read_csv(outpath,index_col=1,chunksize=2000):
            temp_list.append(chunk)
        data = pd.concat(temp_list)
        del temp_list

        data = data.fillna(0)

        data = data.iloc[:,header_length:]

        if(settings['max_of_sensor'] == 1):
            outdf = pd.DataFrame({'Max of Sensor':data.max()})
        if(settings['max'] == 1):
            temp_df = pd.DataFrame({'Max of All Sensor':data.values.max()},index=[0])
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)
        if(settings['mean'] == 1):
            temp_df = pd.DataFrame({'Average of Sensor':data.mean()})
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)
        if(settings['max_mean'] == 1):
            temp_df = pd.DataFrame({'Average of Max Column':data.max().mean()},index=[0])
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)
        if(settings['percentile'] == 1):
            col_name = str(settings['percentile_value'] * 100) + " Percentile of Sensor"
            temp_df = pd.DataFrame({col_name:data.quantile(settings['percentile_value'])})
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)
        if(settings['percentile'] == 1 and settings['max_percentile'] == 1):
            col_name = str(settings['percentile_value'] * 100) + " Max"
            temp_df = pd.DataFrame({col_name:data.quantile(settings['percentile_value']).max()},index=[0])
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)
        if(settings['rolling'] == 1):
            col_name = str(settings['rolling_value']) + " Hour Average of Sensor"
            temp_df = pd.DataFrame({col_name:data.rolling(window=settings['rolling_value']).mean().max()})
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)
        if(settings['rolling'] == 1 and settings['max_rolling'] == 1):
            col_name = str(settings['rolling_value']) + " Hour Max"
            temp_df = pd.DataFrame({col_name:data.rolling(window=settings['rolling_value']).mean().max().max()},index=[0])
            outdf = pd.concat([temp_df,outdf],axis=1,sort=False)

        outdf.index.name = 'Sensor ID'
        outdf.to_csv(output_filename)
        messagebox.showinfo("Complete","Processing complete, file name is: " + output_filename)

    except OSError:
        messagebox.showerror("File Not Found","File not found, please specify CSV and/or Background NO2 CSV")
        raise
    except ValueError:
        messagebox.showerror("Invalid Dataset","Invalid dataset, please check input datasets")
        raise