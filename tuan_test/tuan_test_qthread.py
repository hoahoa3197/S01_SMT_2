import math
import sys
from  sqlite3 import *
import socket
import os
import serial
from time import sleep
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSerialPort import QSerialPort
from UI_ import Ui_MainWindow
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.btnClick.clicked.connect(self.btnClicked)
         # open the serial port
        self.serial = QSerialPort(self)
        self.serial.setPortName("COM6")
        if self.serial.open(QIODevice.ReadWrite):
            self.serial.setBaudRate(QSerialPort.Baud115200)
            self.serial.setDataBits(QSerialPort.Data8)
            self.serial.setParity(QSerialPort.NoParity)
            self.serial.setStopBits(QSerialPort.OneStop)
            self.serial.readyRead.connect(self.reviceData)
            # 
        else:
            raise IOError("Cannot connect to device on port ")
    def btnClicked(self):
        print("Click ed")
    # Revice Data From Serial
    def reviceData(self):
        print("Read data")
        text = self.serial.readLine().data().decode()
        print(text)
        self.serial.write(b'AHAH')
        
    def btnClickTaskResult(self, result):
        print('Task completed')
        print(result)
        self.uic.txtLb.setText('Count completed')
        
    def btnClickTask(self):
        for i in range(5):
            self.uic.txtLb.setText('Count '+str(i))
            sleep(1)
        return 'Run task completed'
        
        
if __name__ == "__main__":
    #######UI#######
  # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


