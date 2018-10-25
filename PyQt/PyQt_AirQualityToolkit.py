# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AirQualityToolkit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import logging
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem

from DialogBoxes import ErrorBox
from CSVFormatter import *
from Stitcher import *
from Factorizer import *
from NO2Processor import *
from Statistics_Generator import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 573)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(25, -1, 25, -1)
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Max = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Max.setChecked(True)
        self.Stat_Max.setObjectName("Stat_Max")
        self.gridLayout_2.addWidget(self.Stat_Max, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Average = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Average.setChecked(True)
        self.Stat_Average.setObjectName("Stat_Average")
        self.gridLayout_2.addWidget(self.Stat_Average, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Max_Average = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Max_Average.setChecked(True)
        self.Stat_Max_Average.setTristate(False)
        self.Stat_Max_Average.setObjectName("Stat_Max_Average")
        self.gridLayout_2.addWidget(self.Stat_Max_Average, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Max_Max = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Max_Max.setChecked(True)
        self.Stat_Max_Max.setObjectName("Stat_Max_Max")
        self.gridLayout_2.addWidget(self.Stat_Max_Max, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Stat_Percentile_En = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Percentile_En.setObjectName("Stat_Percentile_En")
        self.gridLayout_7.addWidget(self.Stat_Percentile_En, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Percentile_Max = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Percentile_Max.setObjectName("Stat_Percentile_Max")
        self.gridLayout_7.addWidget(self.Stat_Percentile_Max, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout_7, 3, 2, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Stat_Rolling_En = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Rolling_En.setObjectName("Stat_Rolling_En")
        self.gridLayout_8.addWidget(self.Stat_Rolling_En, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Rolling_Max = QtWidgets.QCheckBox(self.groupBox)
        self.Stat_Rolling_Max.setObjectName("Stat_Rolling_Max")
        self.gridLayout_8.addWidget(self.Stat_Rolling_Max, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout_8, 4, 2, 1, 1)
        self.Stat_Percentile_Num = QtWidgets.QLineEdit(self.groupBox)
        self.Stat_Percentile_Num.setObjectName("Stat_Percentile_Num")
        self.gridLayout_2.addWidget(self.Stat_Percentile_Num, 3, 1, 1, 1)
        self.Stat_Rolling_Num = QtWidgets.QLineEdit(self.groupBox)
        self.Stat_Rolling_Num.setObjectName("Stat_Rolling_Num")
        self.gridLayout_2.addWidget(self.Stat_Rolling_Num, 4, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(25, 0, 25, 0)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Browse_1 = QtWidgets.QPushButton(self.groupBox)
        self.Stat_Browse_1.setObjectName("Stat_Browse_1")
        self.gridLayout.addWidget(self.Stat_Browse_1, 0, 2, 1, 1)
        self.Stat_Run_1 = QtWidgets.QPushButton(self.groupBox)
        self.Stat_Run_1.setObjectName("Stat_Run_1")
        self.gridLayout.addWidget(self.Stat_Run_1, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Stat_Header = QtWidgets.QLineEdit(self.groupBox)
        self.Stat_Header.setObjectName("Stat_Header")
        self.gridLayout.addWidget(self.Stat_Header, 1, 1, 1, 1)
        self.Stat_To_Convert = QtWidgets.QLineEdit(self.groupBox)
        self.Stat_To_Convert.setObjectName("Stat_To_Convert")
        self.gridLayout.addWidget(self.Stat_To_Convert, 0, 1, 1, 1)
        self.Stat_Output = QtWidgets.QLineEdit(self.groupBox)
        self.Stat_Output.setObjectName("Stat_Output")
        self.gridLayout.addWidget(self.Stat_Output, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Stitcher_Out_File = QtWidgets.QLineEdit(self.tab_2)
        self.Stitcher_Out_File.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Stitcher_Out_File.setObjectName("Stitcher_Out_File")
        self.gridLayout_6.addWidget(self.Stitcher_Out_File, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Stitcher_Out_Folder = QtWidgets.QLineEdit(self.tab_2)
        self.Stitcher_Out_Folder.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Stitcher_Out_Folder.setObjectName("Stitcher_Out_Folder")
        self.gridLayout_6.addWidget(self.Stitcher_Out_Folder, 1, 1, 1, 1)
        self.Stitcher_Import = QtWidgets.QPushButton(self.tab_2)
        self.Stitcher_Import.setObjectName("Stitcher_Import")
        self.gridLayout_6.addWidget(self.Stitcher_Import, 0, 1, 1, 1)
        self.Stitcher_Clear = QtWidgets.QPushButton(self.tab_2)
        self.Stitcher_Clear.setObjectName("Stitcher_Clear")
        self.gridLayout_6.addWidget(self.Stitcher_Clear, 0, 2, 1, 1)
        self.Stitcher_Run = QtWidgets.QPushButton(self.tab_2)
        self.Stitcher_Run.setObjectName("Stitcher_Run")
        self.gridLayout_6.addWidget(self.Stitcher_Run, 0, 3, 1, 1)
        self.Stitcher_Browse = QtWidgets.QPushButton(self.tab_2)
        self.Stitcher_Browse.setObjectName("Stitcher_Browse")
        self.gridLayout_6.addWidget(self.Stitcher_Browse, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_5.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.Stitcher_Table = QtWidgets.QTableWidget(self.tab_2)
        self.Stitcher_Table.setRowCount(5)
        self.Stitcher_Table.setObjectName("Stitcher_Table")
        self.Stitcher_Table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.Stitcher_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stitcher_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stitcher_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stitcher_Table.setHorizontalHeaderItem(3, item)
        self.Stitcher_Table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.Stitcher_Table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Factorizer_Table = QtWidgets.QTableWidget(self.tab_3)
        self.Factorizer_Table.setRowCount(5)
        self.Factorizer_Table.setObjectName("Factorizer_Table")
        self.Factorizer_Table.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.Factorizer_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Factorizer_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Factorizer_Table.setHorizontalHeaderItem(2, item)
        self.Factorizer_Table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.Factorizer_Table)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.Factorizer_Import = QtWidgets.QPushButton(self.tab_3)
        self.Factorizer_Import.setObjectName("Factorizer_Import")
        self.gridLayout_18.addWidget(self.Factorizer_Import, 0, 2, 1, 1)
        self.Factorizer_Clear = QtWidgets.QPushButton(self.tab_3)
        self.Factorizer_Clear.setObjectName("Factorizer_Clear")
        self.gridLayout_18.addWidget(self.Factorizer_Clear, 0, 3, 1, 1)
        self.Factorizer_Run = QtWidgets.QPushButton(self.tab_3)
        self.Factorizer_Run.setObjectName("Factorizer_Run")
        self.gridLayout_18.addWidget(self.Factorizer_Run, 0, 4, 1, 1)
        self.Factorizer_Browse_Input = QtWidgets.QPushButton(self.tab_3)
        self.Factorizer_Browse_Input.setObjectName("Factorizer_Browse_Input")
        self.gridLayout_18.addWidget(self.Factorizer_Browse_Input, 0, 0, 1, 1)
        self.Factorizer_Browse_Factor = QtWidgets.QPushButton(self.tab_3)
        self.Factorizer_Browse_Factor.setObjectName("Factorizer_Browse_Factor")
        self.gridLayout_18.addWidget(self.Factorizer_Browse_Factor, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_18)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.MassCSV_Table = QtWidgets.QTableWidget(self.tab_7)
        self.MassCSV_Table.setRowCount(5)
        self.MassCSV_Table.setObjectName("MassCSV_Table")
        self.MassCSV_Table.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.MassCSV_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MassCSV_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MassCSV_Table.setHorizontalHeaderItem(2, item)
        self.MassCSV_Table.horizontalHeader().setDefaultSectionSize(259)
        self.MassCSV_Table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_21.addWidget(self.MassCSV_Table, 0, 0, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.MassCSV_Browse = QtWidgets.QPushButton(self.tab_7)
        self.MassCSV_Browse.setObjectName("MassCSV_Browse")
        self.gridLayout_20.addWidget(self.MassCSV_Browse, 0, 0, 1, 1)
        self.MassCSV_Run = QtWidgets.QPushButton(self.tab_7)
        self.MassCSV_Run.setObjectName("MassCSV_Run")
        self.gridLayout_20.addWidget(self.MassCSV_Run, 0, 3, 1, 1)
        self.MassCSV_Import = QtWidgets.QPushButton(self.tab_7)
        self.MassCSV_Import.setObjectName("MassCSV_Import")
        self.gridLayout_20.addWidget(self.MassCSV_Import, 0, 1, 1, 1)
        self.MassCSV_Clear = QtWidgets.QPushButton(self.tab_7)
        self.MassCSV_Clear.setObjectName("MassCSV_Clear")
        self.gridLayout_20.addWidget(self.MassCSV_Clear, 0, 2, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_27.setObjectName("gridLayout_27")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_27.addItem(spacerItem1, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_26.setContentsMargins(25, 0, 25, 0)
        self.gridLayout_26.setHorizontalSpacing(100)
        self.gridLayout_26.setVerticalSpacing(7)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_26.addWidget(self.label_24, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_26.addWidget(self.label_25, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NO2_Browse_Format_CSV = QtWidgets.QPushButton(self.groupBox_3)
        self.NO2_Browse_Format_CSV.setObjectName("NO2_Browse_Format_CSV")
        self.gridLayout_26.addWidget(self.NO2_Browse_Format_CSV, 0, 2, 1, 1)
        self.NO2_Output_Format = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Output_Format.setObjectName("NO2_Output_Format")
        self.gridLayout_26.addWidget(self.NO2_Output_Format, 1, 1, 1, 1)
        self.NO2_File_To_Format = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_File_To_Format.setObjectName("NO2_File_To_Format")
        self.gridLayout_26.addWidget(self.NO2_File_To_Format, 0, 1, 1, 1)
        self.NO2_Calpuff_Format = QtWidgets.QCheckBox(self.groupBox_3)
        self.NO2_Calpuff_Format.setObjectName("NO2_Calpuff_Format")
        self.gridLayout_26.addWidget(self.NO2_Calpuff_Format, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NO2_Convert_To_CSV = QtWidgets.QPushButton(self.groupBox_3)
        self.NO2_Convert_To_CSV.setObjectName("NO2_Convert_To_CSV")
        self.gridLayout_26.addWidget(self.NO2_Convert_To_CSV, 1, 2, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_26, 1, 0, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setContentsMargins(25, -1, 25, -1)
        self.gridLayout_23.setHorizontalSpacing(100)
        self.gridLayout_23.setVerticalSpacing(7)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.NO2_Process_CSV_Browse = QtWidgets.QPushButton(self.groupBox_3)
        self.NO2_Process_CSV_Browse.setObjectName("NO2_Process_CSV_Browse")
        self.gridLayout_23.addWidget(self.NO2_Process_CSV_Browse, 0, 2, 1, 1)
        self.NO2_Background_Browse = QtWidgets.QPushButton(self.groupBox_3)
        self.NO2_Background_Browse.setObjectName("NO2_Background_Browse")
        self.gridLayout_23.addWidget(self.NO2_Background_Browse, 1, 2, 1, 1)
        self.NO2_Background_File = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Background_File.setObjectName("NO2_Background_File")
        self.gridLayout_23.addWidget(self.NO2_Background_File, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_23.addWidget(self.label_26, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NO2_Initial_Percent = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Initial_Percent.setObjectName("NO2_Initial_Percent")
        self.gridLayout_23.addWidget(self.NO2_Initial_Percent, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_23.addWidget(self.label_22, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_23.addWidget(self.label_21, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_23.addWidget(self.label_23, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NO2_Process_CSV = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Process_CSV.setObjectName("NO2_Process_CSV")
        self.gridLayout_23.addWidget(self.NO2_Process_CSV, 0, 1, 1, 1)
        self.NO2_Exceedances = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Exceedances.setObjectName("NO2_Exceedances")
        self.gridLayout_23.addWidget(self.NO2_Exceedances, 3, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_23.addWidget(self.label_27, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_23.addWidget(self.label_28, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NO2_Header_Columns = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Header_Columns.setObjectName("NO2_Header_Columns")
        self.gridLayout_23.addWidget(self.NO2_Header_Columns, 4, 1, 1, 1)
        self.NO2_Output_Statistics = QtWidgets.QLineEdit(self.groupBox_3)
        self.NO2_Output_Statistics.setObjectName("NO2_Output_Statistics")
        self.gridLayout_23.addWidget(self.NO2_Output_Statistics, 5, 1, 1, 1)
        self.NO2_Run_Stats = QtWidgets.QPushButton(self.groupBox_3)
        self.NO2_Run_Stats.setObjectName("NO2_Run_Stats")
        self.gridLayout_23.addWidget(self.NO2_Run_Stats, 5, 2, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_23, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_22.addWidget(self.line, 2, 0, 1, 1)
        self.gridLayout_27.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Air Quality Toolkit - 25/10/18"))
        self.groupBox.setTitle(_translate("MainWindow", "Statistics Tools"))
        self.label_4.setText(_translate("MainWindow", "Settings for Statistics"))
        self.Stat_Max.setText(_translate("MainWindow", "Max of Sensor"))
        self.label_5.setText(_translate("MainWindow", "Percentile to compute (eg 99.9)"))
        self.Stat_Average.setText(_translate("MainWindow", "Average of Sensor"))
        self.Stat_Max_Average.setText(_translate("MainWindow", "Max Average of Sensors"))
        self.label_6.setText(_translate("MainWindow", "Rolling average window (eg 8)"))
        self.Stat_Max_Max.setText(_translate("MainWindow", "Max of All Sensors"))
        self.Stat_Percentile_En.setText(_translate("MainWindow", "Enable Percentile"))
        self.Stat_Percentile_Max.setText(_translate("MainWindow", "Max of Percentile"))
        self.Stat_Rolling_En.setText(_translate("MainWindow", "Enable Rolling"))
        self.Stat_Rolling_Max.setText(_translate("MainWindow", "Max of Rolling"))
        self.label.setText(_translate("MainWindow", "Filename of CSV to process:"))
        self.label_2.setText(_translate("MainWindow", "Number of header columns in dataset (eg 3):"))
        self.Stat_Browse_1.setText(_translate("MainWindow", "Browse"))
        self.Stat_Run_1.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "File name of output statistics CSV:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Statistics Generator"))
        self.Stitcher_Out_File.setText(_translate("MainWindow", "Stitcher_Output.csv"))
        self.label_7.setText(_translate("MainWindow", "Output File Name:"))
        self.Stitcher_Import.setText(_translate("MainWindow", "Import Settings CSV"))
        self.Stitcher_Clear.setText(_translate("MainWindow", "Clear"))
        self.Stitcher_Run.setText(_translate("MainWindow", "Stitch"))
        self.Stitcher_Browse.setText(_translate("MainWindow", "Browse"))
        self.label_8.setText(_translate("MainWindow", "Output Folder:"))
        item = self.Stitcher_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folder"))
        item = self.Stitcher_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.Stitcher_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Scale"))
        item = self.Stitcher_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Columns to Exclude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Stitcher"))
        item = self.Factorizer_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.Factorizer_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Factor"))
        item = self.Factorizer_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Output File Name"))
        self.Factorizer_Import.setText(_translate("MainWindow", "Import Settings CSV"))
        self.Factorizer_Clear.setText(_translate("MainWindow", "Clear"))
        self.Factorizer_Run.setText(_translate("MainWindow", "Factorize"))
        self.Factorizer_Browse_Input.setText(_translate("MainWindow", "Browse Input File"))
        self.Factorizer_Browse_Factor.setText(_translate("MainWindow", "Browse Factor File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Factorizer"))
        item = self.MassCSV_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.MassCSV_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CALPUFF Output Format? (0/1)"))
        item = self.MassCSV_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Output File Name"))
        self.MassCSV_Browse.setText(_translate("MainWindow", "Browse"))
        self.MassCSV_Run.setText(_translate("MainWindow", "Convert"))
        self.MassCSV_Import.setText(_translate("MainWindow", "Import Settings CSV"))
        self.MassCSV_Clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Mass CSV Formatter"))
        self.groupBox_3.setTitle(_translate("MainWindow", "NO2 Processor Tools"))
        self.label_24.setText(_translate("MainWindow", "File to format as CSV:"))
        self.label_25.setText(_translate("MainWindow", "File name of output CSV:"))
        self.NO2_Browse_Format_CSV.setText(_translate("MainWindow", "Browse"))
        self.NO2_Calpuff_Format.setText(_translate("MainWindow", "CALPUFF Output Format?"))
        self.NO2_Convert_To_CSV.setText(_translate("MainWindow", "Convert to CSV"))
        self.NO2_Process_CSV_Browse.setText(_translate("MainWindow", "Browse"))
        self.NO2_Background_Browse.setText(_translate("MainWindow", "Browse"))
        self.label_26.setText(_translate("MainWindow", "File name of CSV to process:"))
        self.NO2_Initial_Percent.setText(_translate("MainWindow", "0.1"))
        self.label_22.setText(_translate("MainWindow", "Initial % to process (eg 0.1)"))
        self.label_21.setText(_translate("MainWindow", "File name of Background NO2 CSV:"))
        self.label_23.setText(_translate("MainWindow", "Number of exceedances limit (eg 246)"))
        self.NO2_Exceedances.setText(_translate("MainWindow", "246"))
        self.label_27.setText(_translate("MainWindow", "Number of header columns in dataset (eg 3)"))
        self.label_28.setText(_translate("MainWindow", "File name of output statistics CSV:"))
        self.NO2_Header_Columns.setText(_translate("MainWindow", "3"))
        self.NO2_Run_Stats.setText(_translate("MainWindow", "Process CSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "NO2 Processor"))



#USER DEFINED BUTTONS
        #STATISTICS BUTTONS
        self.Stat_Browse_1.clicked.connect(self.Stat_Browse_Clicked)
        self.Stat_Run_1.clicked.connect(self.Stat_Run_Clicked)

        #STITCHER BUTTONS
        self.Stitcher_Browse.clicked.connect(self.Stitcher_Browse_Clicked)
        self.Stitcher_Import.clicked.connect(self.Stitcher_Import_Clicked)
        self.Stitcher_Clear.clicked.connect(self.Stitcher_Clear_Clicked)
        self.Stitcher_Run.clicked.connect(self.Stitcher_Run_Clicked)

        #FACTORIZER BUTTONS
        self.Factorizer_Browse_Input.clicked.connect(self.Factorizer_Browse_Input_Clicked)
        self.Factorizer_Browse_Factor.clicked.connect(self.Factorizer_Browse_Factor_Clicked)
        self.Factorizer_Import.clicked.connect(self.Factorizer_Import_Clicked)
        self.Factorizer_Clear.clicked.connect(self.Factorizer_Clear_Clicked)
        self.Factorizer_Run.clicked.connect(self.Factorizer_Run_Clicked)

        #MASS CSV BUTTONS
        self.MassCSV_Browse.clicked.connect(self.MassCSV_Browse_Clicked)
        self.MassCSV_Import.clicked.connect(self.MassCSV_Import_Clicked)
        self.MassCSV_Clear.clicked.connect(self.MassCSV_Clear_Clicked)
        self.MassCSV_Run.clicked.connect(self.MassCSV_Run_Clicked)

        #NO2 PROCESSOR BUTTONS
        self.NO2_Browse_Format_CSV.clicked.connect(self.NO2_Browse_Format_CSV_Clicked)
        self.NO2_Convert_To_CSV.clicked.connect(self.NO2_Convert_To_CSV_Clicked)
        self.NO2_Background_Browse.clicked.connect(self.NO2_Background_Browse_Clicked)
        self.NO2_Process_CSV_Browse.clicked.connect(self.NO2_Process_CSV_Browse_Clicked)
        self.NO2_Run_Stats.clicked.connect(self.NO2_Run_Stats_Clicked)


#### GENERAL FUNCTIONS
    @staticmethod
    def Get_Table(table):
        tbl = []
        for row in range(table.rowCount()):
            tbl.append([])
            for col in range(table.columnCount()):
                if table.item(row,col) != None:
                    value = table.item(row,col).text()
                    tbl[row].append(str(value))
        return tbl



#### STATISTICS GENERATOR FUNCTIONS

    def Stat_Browse_Clicked(self):
        try:
            self.Stat_To_Convert.setText("")
            self.Stat_Output.setText("")
            options = QFileDialog.Options()
            # options |= QFileDialog.DontUseNativeDialog
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            self.Stat_To_Convert.setText(filename[0])
            self.Stat_Output.setText(filename[0].split('.')[0]+ "_Statistics.csv")
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def Stat_Run_Clicked(self):
        settings = {}
        settings['mean'] = self.Stat_Average.isChecked()
        settings['max_of_sensor'] = self.Stat_Max.isChecked()
        settings['max_mean'] = self.Stat_Max_Average.isChecked()
        settings['max'] = self.Stat_Max_Max.isChecked()
        settings['percentile'] = self.Stat_Percentile_En.isChecked()
        if self.Stat_Percentile_En.isChecked():
            settings['percentile_value'] = float(self.Stat_Percentile_Num.text()) / 100
        settings['max_percentile'] = self.Stat_Percentile_Max.isChecked()
        settings['rolling'] = self.Stat_Rolling_En.isChecked()
        if self.Stat_Rolling_En.isChecked():
            settings['rolling_value'] = int(self.Stat_Rolling_Num.text())
        settings['max_rolling'] = self.Stat_Rolling_Max.isChecked()
        try:
            Statistics_Generator(settings,self.Stat_Header.text(),self.Stat_To_Convert.text(),self.Stat_Output.text())
        except ValueError as error:
            error = traceback.format_exc()
            ErrorBox("Input Settings Invalid","Please check input settings",error)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)


#### STITCHER FUNCTIONS

    def Stitcher_Browse_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            for row in range(self.Stitcher_Table.rowCount()):
                if self.Stitcher_Table.item(row,0) == None and row == self.Stitcher_Table.rowCount() - 1:
                    self.Stitcher_Table.insertRow(row)
                if self.Stitcher_Table.item(row,0) == None:
                    self.Stitcher_Table.setItem(row,0,QTableWidgetItem(os.path.split(filename[0])[0]))
                    self.Stitcher_Table.setItem(row,1,QTableWidgetItem(os.path.split(filename[0])[1]))
                    if row == 0:
                        self.Stitcher_Out_Folder.setText(os.path.split(filename[0])[0])
                    break
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def Stitcher_Import_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            settings = pd.read_csv(filename[0])
            settings = settings.loc[:,~settings.columns.str.contains('^Unnamed')]
            for folder,filename,scale,header,row in zip(settings.loc[:,'Folder'],settings.loc[:,'Filename'],settings.loc[:,'Scale'],settings.loc[:,'Headers'],range(len(settings.loc[:,'Folder']))):
                    if self.Stitcher_Table.item(row,0) == None and row == self.Stitcher_Table.rowCount() - 1:
                        self.Stitcher_Table.insertRow(row)
                    if self.Stitcher_Table.item(row,0) == None:
                        self.Stitcher_Table.setItem(row,0,QTableWidgetItem(folder))
                        self.Stitcher_Table.setItem(row,1,QTableWidgetItem(filename))
                        self.Stitcher_Table.setItem(row,2,QTableWidgetItem(str(scale)))
                        self.Stitcher_Table.setItem(row,3,QTableWidgetItem(str(header)))
                        if row == 0:
                            self.Stitcher_Out_Folder.setText(folder)
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def Stitcher_Clear_Clicked(self):
        self.Stitcher_Table.clearContents()
        self.Stitcher_Out_Folder.clear()

    def Stitcher_Run_Clicked(self):
        filesp = []
        filesl = []
        scalesl = []
        headers = []
        try:
            for row in self.Get_Table(self.Stitcher_Table):
                if row:
                    filesp.append(row[0])
                    filesl.append(row[1])
                    scalesl.append(row[2])
                    headers.append(row[3])
        except IndexError as err:
            ErrorBox("Invalid Settings","Invalid settings, please review input table for errors",err)
        except Exception as err:
            ErrorBox("Error","An error has occured",err)
        try:
            Stitcher(filesp,filesl,scalesl,headers,os.path.join(self.Stitcher_Out_Folder.text(),self.Stitcher_Out_File.text()))
        except TypeError as error:
            error = traceback.format_exc()
            ErrorBox("Incorrect Settings","Incorrect settings, please review input table for errors",error)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

#### FACTORIZER FUNCTIONS
    def Factorizer_Browse_Input_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            for row in range(self.Factorizer_Table.rowCount()):
                if self.Factorizer_Table.item(row,0) == None and row == self.Factorizer_Table.rowCount() - 1:
                    self.Factorizer_Table.insertRow(row)
                if self.Factorizer_Table.item(row,0) == None:
                    self.Factorizer_Table.setItem(row,0,QTableWidgetItem(filename[0]))
                    self.Factorizer_Table.setItem(row,2,QTableWidgetItem(filename[0].split(".")[0] + "_Factorized.csv"))
                    break
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def Factorizer_Browse_Factor_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            for row in range(self.Factorizer_Table.rowCount()):
                if self.Factorizer_Table.item(row,1) == None and row == self.Factorizer_Table.rowCount() - 1:
                    self.Factorizer_Table.insertRow(row)
                if self.Factorizer_Table.item(row,1) == None:
                    self.Factorizer_Table.setItem(row,1,QTableWidgetItem(filename[0]))
                    break
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)


    def Factorizer_Import_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            settings = pd.read_csv(filename[0])
            settings = settings.loc[:,~settings.columns.str.contains('^Unnamed')]
            for filename,factor,row in zip(settings.loc[:,'Filename'],settings.loc[:,'Factors'],range(len(settings.loc[:,'Filename']))):
                    if self.Factorizer_Table.item(row,0) == None and row == self.Factorizer_Table.rowCount() - 1:
                        self.Factorizer_Table.insertRow(row)
                    if self.Factorizer_Table.item(row,0) == None:
                        self.Factorizer_Table.setItem(row,0,QTableWidgetItem(filename))
                        self.Factorizer_Table.setItem(row,1,QTableWidgetItem(factor))
                        self.Factorizer_Table.setItem(row,2,QTableWidgetItem(filename.split('.')[0] + "_Factorized.csv"))
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def Factorizer_Clear_Clicked(self):
            self.Factorizer_Table.clearContents()

    def Factorizer_Run_Clicked(self):
        for row in self.Get_Table(self.Factorizer_Table):
            try:
                if row:
                    factorizer(row[0],row[1],row[2])
            except Exception as err:
                err = traceback.format_exc()
                ErrorBox("Error","An error has occured",err)

#### MASS CSV FUNCTIONS
    def MassCSV_Browse_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"DAT File to Process","","Dat Files (*.dat);;Txt Files (*.txt);;All Files (*);", options=options)
            for row in range(self.MassCSV_Table.rowCount()):
                if self.MassCSV_Table.item(row,0) == None and row == self.MassCSV_Table.rowCount() - 1:
                    self.MassCSV_Table.insertRow(row)
                if self.MassCSV_Table.item(row,0) == None:
                    self.MassCSV_Table.setItem(row,0,QTableWidgetItem(filename[0]))
                    self.MassCSV_Table.setItem(row,2,QTableWidgetItem(filename[0].split('.')[0] + "_Formatted.csv"))
                    break
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)


    def MassCSV_Import_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            settings = pd.read_csv(filename[0])
            settings = settings.loc[:,~settings.columns.str.contains('^Unnamed')]
            for filename,calpuff,row in zip(settings.loc[:,'Filename'],settings.loc[:,'XY Included'],range(len(settings.loc[:,'Filename']))):
                    if self.MassCSV_Table.item(row,0) == None and row == self.MassCSV_Table.rowCount() - 1:
                        self.MassCSV_Table.insertRow(row)
                    if self.MassCSV_Table.item(row,0) == None:
                        self.MassCSV_Table.setItem(row,0,QTableWidgetItem(filename))
                        self.MassCSV_Table.setItem(row,1,QTableWidgetItem(str(calpuff)))
                        self.MassCSV_Table.setItem(row,2,QTableWidgetItem(filename.split('.')[0] + "_Formatted.csv"))
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def MassCSV_Clear_Clicked(self):
            self.MassCSV_Table.clearContents()

    def MassCSV_Run_Clicked(self):
        for row in self.Get_Table(self.MassCSV_Table):
            try:
                if row:
                    csvformatter(row[0],row[1],row[2])
            except FileNotFoundError as error:
                error = traceback.format_exc()
                ErrorBox("File Not Found","File not found, please specify file to format",error)
            except Exception as err:
                err = traceback.format_exc()
                ErrorBox("Error","An error has occured",err)
        InfoBox("Complete","Please find files located in their corresponding output location (output file name column)")

### NO2 PROCESSOR FUNCTIONS
    def NO2_Browse_Format_CSV_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"DAT File to Process","","Dat Files (*.dat);;All Files (*);", options=options)
            self.NO2_File_To_Format.setText(filename[0])
            self.NO2_Output_Format.setText(filename[0].split('.')[0] + "_Formatted.csv")
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def NO2_Convert_To_CSV_Clicked(self):
        try:
            csvformatter(self.NO2_File_To_Format.text(),self.NO2_Calpuff_Format.isChecked(),self.NO2_Output_Format.text())
            InfoBox("Complete","Please find output file located: " + self.NO2_Output_Format.text())
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def NO2_Process_CSV_Browse_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            self.NO2_Process_CSV.setText(filename[0])
            self.NO2_Output_Statistics.setText(filename[0].split('.')[0] + "_Statistics.csv")
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def NO2_Background_Browse_Clicked(self):
        try:
            options = QFileDialog.Options()
            filename,_ = QFileDialog.getOpenFileNames(None,"CSV File to Process","","CSV Files (*.csv);;All Files (*);", options=options)
            self.NO2_Background_File.setText(filename[0])
        except IndexError as err:
            err = traceback.format_exc()
            ErrorBox("No File Selected","Please select a file",err)
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)

    def NO2_Run_Stats_Clicked(self):
        try:
            process(int(self.NO2_Header_Columns.text()),float(self.NO2_Initial_Percent.text()),int(self.NO2_Exceedances.text()),self.NO2_Background_File.text(),self.NO2_Process_CSV.text(),self.NO2_Output_Statistics.text())
        except Exception as err:
            err = traceback.format_exc()
            ErrorBox("Error","An error has occured",err)




