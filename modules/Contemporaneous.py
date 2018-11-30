import os
import pandas as pd
import traceback
from PyQt5.QtWidgets import QMessageBox
from DialogBoxes import ErrorBox, InfoBox

"""
.. module:: Contemporaneous
    :platform: Windows
    :synopsis: A module containing functionality for calculating contemporaneous values with background pollutant

.. moduleauthor:: Jack McKew <jack.mckew@aecom.com>


"""

def contemporaneous(
    header_length, input_data, input_background, output_rows, output_filename
):
    """This function calculates contemporaneous values with background pollutant.

    :param header_length: This should be an integer declaring how many header columns in the dataset
    :type header_length: int.
    :param input_data: This should be a string representing input filename.
    :type input_data: str.
    :param input_data: This should be a string representing input filename.
    :type input_data: str.
    :param output_rows: This should be a an integer declaring how many rows to output.
    :type output_rows: str.
    :param output_filename: Output filename.
    :type output_filename: str.

    """
    try:
        header_length = int(header_length)
        output_rows = int(output_rows)
        background = pd.read_csv(input_background)
        temp_list = []
        data = pd.DataFrame
        for chunk in pd.read_csv(input_data, index_col=1, chunksize=2000):
            temp_list.append(chunk)
        data = pd.concat(temp_list)
        del temp_list

        data["background"] = background.iloc[:, header_length]
        data = data.fillna(0)

        if os.path.isfile(output_filename):
            filequestion = QMessageBox.question(
                None,
                "File Exists",
                "File Exists, would you like to delete before processing?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if filequestion == QMessageBox.Yes:
                os.remove(output_filename)
            else:
                InfoBox(
                    "Please rename before proceeding",
                    "Please rename before proceeding, file name is: " + output_filename,
                )
                return

        with open(output_filename, "a") as f:
            for colnum in range(1, len(data.columns) - 4):
                sorted_data = data.sort_values(by=str(colnum), ascending=False).head(
                    output_rows
                )
                receptor_con = sorted_data.iloc[:, [colnum, -1]]
                receptor_con["pred_index"] = receptor_con.index
                receptor_con["pred_cumulative"] = (
                    receptor_con.iloc[:, 0] + receptor_con["background"]
                )
                sorted_data = data.sort_values(by="background", ascending=False).head(
                    output_rows
                )
                back_con = sorted_data.iloc[:, [-1, colnum]]
                back_con["back_index"] = back_con.index
                back_con["back_cumulative"] = (
                    back_con.iloc[:, 0] + back_con["background"]
                )
                data["Sum"] = data[str(colnum)] + data["background"]
                sorted_data = data.sort_values(by="Sum", ascending=False).head(
                    output_rows
                )
                cumulative_con = sorted_data.iloc[:, [colnum, -2, -1]]
                cumulative_con["cumulative_index"] = cumulative_con.index

                cumulative_con.reset_index(drop=True, inplace=True)
                receptor_con.reset_index(drop=True, inplace=True)
                back_con.reset_index(drop=True, inplace=True)
                result = pd.concat([receptor_con, back_con, cumulative_con], axis=1)

                result.to_csv(f)

                data = data.drop(labels="Sum", axis=1)

        InfoBox("Complete", "Processing complete, file name is: " + output_filename)

    except OSError as err:
        err = traceback.format_exc()
        ErrorBox(
            "File Not Found",
            "File not found, please specify CSV and/or Background NO2 CSV",
            err,
        )
    except ValueError as err:
        err = traceback.format_exc()
        ErrorBox("Invalid Dataset", "Invalid dataset, please check input datasets", err)
    except Exception as err:
        err = traceback.format_exc()
        ErrorBox("Error", "An error has occured", err)

