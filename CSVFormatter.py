import os
import csv
import pandas as pd
import traceback
from PyQt5.QtWidgets import QMessageBox
from DialogBoxes import ErrorBox,InfoBox

"""
.. module:: CSVFormatter
    :platform: Windows
    :synopsis: A module containing functionality for formatting air quality modelling dumps.

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""


def csvformatter(filename,calpuff_state,output_filename):
    """This function formats dataset outputs from air quality modelling software to CSV format.

    :param filename: This should be a string of the filename to convert to CSV.
    :type filename: str.
    :param calpuff_state: This should be a boolean value specifying if the file is CALPUFF format (x and y information header).
    :type calpuff_state: bool.
    :param output_filename: Output filename.
    :type output_filename: str.

    """
    try:
        calpuff_state = int(calpuff_state)
        outpath = os.path.join(os.getcwd(),output_filename)
        csv_file = outpath
        if(calpuff_state == 1):
            location_output_filename = os.path.splitext(output_filename)[0] + "_Locations.csv"
            loc_csv = csv.writer(open(location_output_filename, 'w',newline=''))
            out_csv = csv.writer(open(outpath,'w',newline=''))
            for i,line in enumerate(open(filename)):
                if i == 3:
                    out_header = ['YYYY','JDY','HHMM']
                    loc_header = ["X or Y"]
                    for recepternum in range(1,int(line.split()[0])+1):
                        out_header.append(recepternum)
                        loc_header.append(recepternum)
                    loc_csv.writerow(loc_header)
                    out_csv.writerow(out_header)
                elif i == 9 or i == 10:
                    row = line.split()
                    loc_csv.writerow(row)
                elif i > 13:
                    row = line.split()
                    out_csv.writerow(row)
        else:
            txt_file = filename
            in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
            delimquestion = 0
            if "Output" in next(in_txt)[0]:
                InfoBox("Possibly OLM Format","Please ensure this file has no header information")
                delimquestion = QMessageBox.question(None,'Tab Delimited File?',"Is the input file Tab Delimited?", QMessageBox.Yes | QMessageBox.No)
            if(delimquestion == QMessageBox.Yes or delimquestion != 0):
                in_txt = csv.reader(open(txt_file,"r"),delimiter='\t')
                out_csv = csv.writer(open(outpath, 'w',newline=''))
                out_csv.writerows(in_txt)
            else:
                sniffer = csv.Sniffer()
                delimter = sniffer.sniff(next(in_txt)[0])
                in_txt = csv.reader(open(txt_file,"r"),delimiter=delimter.delimiter)
                out_csv = csv.writer(open(outpath, 'w',newline=''))
                out_csv.writerows(in_txt)
    except OSError as err:
        err = traceback.format_exc()
        ErrorBox("File Not Found","File not found, please specify file to format", err)
    except Exception as err:
        err = traceback.format_exc()
        ErrorBox("Error","An error has occured",err)




### DEPRECATED BY NEW CODE

# def old_csvformatter():
#     """This function formats dataset outputs from air quality modelling software to CSV format.

#     TODO REFACTOR CODE TO BE USED FOR MASS CSV, MAKE INPUT FILENAME, OLM_STATE

#     """
#     # bar['value'] = 0
#     try:
#         file = open(os.path.join(os.getcwd(),filename.get()))
#         outpath = os.path.join(os.getcwd(),outpname.get())
#         reader = csv.reader(file)
#         x = 1
#         # TODO Optimize using next()
#         if(olm_state.get()):
#             for i, row in enumerate(reader):
#                 if i == 8:
#                     length = int(len(row[0].split())) - 1
#                     writer = csv.writer(open(outpath, "w"), delimiter = ',', lineterminator='\n')
#                     header = ['year','day','hour']
#                     header.extend(list(range(1,length)))
#                     writer.writerow(header)
#                 if i==9:
#                     new_row = []
#                     if x == 1:
#                         for j in range(1,len(filter(None,str(row).split(" "))[2:]) + 1):
#                             new_row.append("Rec " + str(j))
#                         loclist = pd.DataFrame(new_row)
#                         new_row = []
#                         x = 0
#                     for j in filter(None,str(row).split(" "))[2:]:
#                         new_row.append(float(j.strip("']")))
#                     loclist['x'] = new_row
#                 if i==10:
#                     new_row = []
#                     for j in filter(None,str(row).split(" "))[2:]:
#                         new_row.append(float(j.strip("']")))
#                     loclist['y'] = new_row
#                     locname = filename.get() + "_Locations.csv"
#                     loclist.to_csv(locname)

#                 if i>15 and row[0] is not "":
#                     year = row[0].split()[0]
#                     day = row[0].split()[1]
#                     hour = row[0].split()[2]
#                     columns = []
#                     new_row = [year,day,hour]
#                     length = int(len(row[0].split()))
#                     for j in range(3,length):
#                         value = float(row[0].split()[j])
#                         if value is not "":
#                             #value = (value*initial + min(0.9*value,(46/48)*ozone))
#                             columns.append(value)
#                     new_row.extend(columns)
#                     writer = csv.writer(open(outpath, "a+"), delimiter = ',', lineterminator='\n')
#                     writer.writerow(new_row)
#                     # bar['value'] += 0.2739726027397260273972602739726
#                     page1.update()
#         else:
#             txt_file = filename.get()
#             csv_file = outpath
#             in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
#             out_csv = csv.writer(open(outpath, 'wb'))
#             out_csv.writerows(in_txt)
#             # bar['value'] = 100
#             page1.update()
#             processname.delete(0,END)
#             processname.insert(0,outpname.get())
#     except OSError:
#         messagebox.showerror("File Not Found","File not found, please specify file to format")

