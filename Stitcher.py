import os
import pandas as pd
from PyQt5.QtWidgets import QMessageBox

"""
.. module:: Stitcher
    :platform: Windows
    :synopsis: A module containing all functionality with Stitcher frame.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""
def ErrorBox(errortext,console_error):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(errortext)
            msg.setWindowTitle("Error")
            msg.setInformativeText("Please review input settings")
            msg.setDetailedText("Error from console: \n" + console_error)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

def InfoBox(text,log):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(text)
            msg.setWindowTitle("Complete")
            msg.setDetailedText(log)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

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
        except:
            ErrorBox("File Not Found","File not found, please specify file \nFile not found: " + filename)
    try:
        dataout.to_csv(output_filename)
        print("Complete: File Path " + str(output_filename))
        InfoBox("Complete","File Path: " + str(output_filename))
    except FileNotFoundError as err:
        ErrorBox("Output Data File","Invalid output dataset filename, please specify output dataset name \n" + str(err))
    except UnboundLocalError as err:
        ErrorBox("Output Data Empty","Output dataset empty, please check input datasets\n" + str(err))
    except OSError as err:
        ErrorBox("Output Data Name","Invalid output dataset filename, please specify output dataset name\n" + str(err))
    except Exception as err:
        ErrorBox("Error",str(err))
