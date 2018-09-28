import os
import csv
import pandas as pd
from tkinter import messagebox
"""
.. module:: Factorizer
    :platform: Windows
    :synopsis: A module containing functionality for multiplying air quality datasets with vectors.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""

def factorizer(dataset_filename,factor_filename,output_filename):
    """This function mutiplies air quality datasets with vectors given.

    :param dataset_filename: This should be a string of the filename containing the dataset.
    :type dataset_filename: str.
    :param factor_filename: This should be a string of the filename containing the vector dataset to mutiply with.
    :type factor_filename: str.
    :param output_filename: Output filename.
    :type output_filename: str.

    """
    factor_filepath = os.path.join(os.getcwd(),factor_filename)
    factor_df = pd.read_csv(factor_filepath)
    dataset_filepath = os.path.join(os.getcwd(),dataset_filename)
    data_df = pd.read_csv(dataset_filepath)
    data_df['factor'] = factor_df.iloc[:,2]
    output_df = data_df.iloc[:,2:].apply(calcrow,axis=1)
    output_df = pd.concat([factor_df.iloc[:,:2],output_df,data_df.iloc[:,-1]],axis=1)
    output_df.columns = data_df.columns
    output_df.iloc[:,:-1].to_csv(os.path.join(os.getcwd(),output_filename),index=False)

def calcrow(row):
    """This function is used for multiplying entire pandas dataframe single row by scalar value located in the last column of the dataframe.

    :param row: This should be the slice from the pandas dataframe.
    :type row: float.
    :returns: pd.Series -- The row multiplied by the scalar in the last column of the row
    """
    factor = float(row[-1])
    new_row = []
    for value in row[:-1]:
            value = value*factor
            new_row.append(value)
    return pd.Series(new_row)



##DEPRECATED BY FACTORIZER

# def old_factorize(factorsname,inputname):
#     # page3.update_idletasks()
#     for factorname,filename in zip(factorsname,inputname):
#         outpname = filename.split('.')[0] + "_Factorized.csv"
#         factors1path = os.path.join(os.getcwd(),factorname)
#         factors = pd.read_csv(factors1path)
#         inputpath = os.path.join(os.getcwd(),filename)
#         data = pd.read_csv(inputpath)
#         data['factor'] = factors.iloc[:,2]
#         outdata = data.iloc[:,2:].apply(calcrow,axis=1)
#         outdata = pd.concat([factors.iloc[:,:2],outdata,data.iloc[:,-1]],axis=1)
#         outdata.columns = data.columns
#         outdata.iloc[:,:-1].to_csv(os.path.join(os.getcwd(),outpname),index=False)

