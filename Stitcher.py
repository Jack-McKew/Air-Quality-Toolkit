import os
import pandas as pd
import traceback
from PyQt5.QtWidgets import QMessageBox
from DialogBoxes import ErrorBox,InfoBox

"""
.. module:: Stitcher
    :platform: Windows
    :synopsis: A module containing all functionality with Stitcher frame.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""


def Stitcher(filepath_list,filename,scale,headers_list,output_filename):
    """This function sums multiple dataframes together and outputs a csv of the result.

    :param filepath_list: This should be a list of filepaths to assosciated filename list.
    :type filepath_list: list[str].
    :param filename: This should be a list of filenames to assosciated filepath (filepath_list) list.
    :type filename: list[str].
    :param scale: This should be a list of scalars to scale assosicated filename dataframe by.
    :type scale: list[float].
    :param headers_list: This should be a list of numbers to exclude number of columns from dataframes.
    :type headers_list: list[int].
    :param output_filename: Output filename.
    :type output_filename: str.

    """
    x = 1
    for folder, filename, scale, header in zip(filepath_list,filename,scale,headers_list):
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
            temp_list = []
            for chunk in pd.read_csv(filename,chunksize=2000):
                temp_list.append(chunk)
            data = pd.concat(temp_list)
            del temp_list
            data = data.loc[:,~data.columns.str.contains('^Unnamed')]
            data = data.dropna()
            data.update(data.iloc[:,headlen:].astype(float).multiply((float(scale))))
            if x == 1:
                dataout = data
                x += 1
            else:
                dataout.update(dataout.iloc[:,headlen:].add(data.iloc[:,headlen:]))
            del data
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("File Not Found","File not found, please specify file \nFile not found: " + filename,err)
    try:
        dataout.to_csv(output_filename)
        print("Complete: File Path " + str(output_filename))
        InfoBox("Complete","File Path: " + str(output_filename))
    except FileNotFoundError as err:
        err = traceback.format_exc()
        ErrorBox("Output Data File","Invalid output dataset filename, please specify output dataset name",err)
    except UnboundLocalError as err:
        err = traceback.format_exc()
        ErrorBox("Output Data Empty","Output dataset empty, please check input datasets", err)
    except OSError as err:
        err = traceback.format_exc()
        ErrorBox("Output Data Name","Invalid output dataset filename, please specify output dataset name", err)
    except Exception as err:
        err = traceback.format_exc()
        ErrorBox("Error","An error has occured",err)
