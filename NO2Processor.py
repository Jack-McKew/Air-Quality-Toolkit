import os
import pandas as pd
import traceback
from PyQt5.QtWidgets import QMessageBox
from DialogBoxes import ErrorBox, InfoBox
"""
.. module:: NO2Processor
    :platform: Windows
    :synopsis: A module containing functionality for formatting air quality modelling dumps.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""






def process(header_length,initial,exceedance,background_name,input_data,output_filename):
    """This function applies air quality modelling functions and generates statistics.

    :param header_length: This should be an integer declaring how many header columns in the dataset
    :type header_length: int.
    :param initial: This should be an float declaring initial percentage to work with eg 0.1 = 10%
    :type initial: float.
    :param exceedance: This should be an integer declaring how many exceedances eg compare if any are greater than 246
    :type exceedance: int.
    :param background_name: This should be a string representing input background NO2 filename (Must be located in same directory as .exe).
    :type background_name: str.
    :param input_data: This should be a string representing input filename (Must be located in same directory as .exe).
    :type input_data: str.
    :param output_filename: Output filename.
    :type output_filename: str.

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
            for value in row[header_length - 1:-1]:
                value = float(value)*initial + min(0.9*float(value),back)
                new_row.append(value)
            return pd.Series(new_row)

        def backfunction(row):
            back = float(row[-1])
            new_row = []
            for value in row[:-1]:
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
        outdf.index += 1
        outdf.to_csv(output_filename)
        InfoBox("Complete","Processing complete, file name is: " + output_filename)
        backquestion = QMessageBox.question(None,'Background NO2 Statistics?',"Would you like to process Background NO2 statistics?", QMessageBox.Yes | QMessageBox.No)

        if backquestion == QMessageBox.Yes:
            data['background'] = list(background['Background NO2'])
            data = data.apply(backfunction,axis=1)
            outdf = pd.DataFrame({  'Max of Sensor':data.max(),'Average of Sensor':data.mean(),
                                'Number of Exceedances':data[data > exceedance].count(),
                                'Average Max Column':data.max().mean(),
                                'Max Value':data.values.max(),
                                '99.9th Percentile of Sensor':data.quantile(0.999),
                                'Max of 99.9th Percentile':data.quantile(0.999).max(),
                                '8 Hour Average of Sensor':data.rolling(window=8).mean().max(),
                                '8 Hour Max':data.rolling(window=8).mean().max().max()})
            outdf.index.name = 'Sensor ID'
            outdf.index += 1
            new_name = output_filename.split('.')[0] + "_BG_NO2.csv"
            outdf.to_csv(new_name)
            InfoBox("Complete","Processing complete, file name is: " + new_name)

    except OSError as err:
        err = traceback.format_exc()
        ErrorBox("File Not Found","File not found, please specify CSV and/or Background NO2 CSV",err)
    except ValueError as err:
        err = traceback.format_exc()
        ErrorBox("Invalid Dataset","Invalid dataset, please check input datasets",err)
    except Exception as err:
        err = traceback.format_exc()
        ErrorBox("Error","An error has occured",err)
