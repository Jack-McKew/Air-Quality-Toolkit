from PyQt5.QtWidgets import QMessageBox
import logging
import sys

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('error.log')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logger = setup_custom_logger('AirQualityToolkit')

def ErrorBox(title_text,error_info,console_error):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(title_text)
    msg.setWindowTitle("Error")
    msg.setInformativeText(error_info)
    msg.setDetailedText("Error from console: \n" + str(console_error))
    logger.exception(console_error,exc_info=True)
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