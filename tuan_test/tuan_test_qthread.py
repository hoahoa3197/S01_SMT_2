import math
import sys
from  sqlite3 import *
import socket
import os
import serial
from time import sleep
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QTableWidgetItem
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QThreadPool
from PyQt6.QtGui import QPixmap,QImage
from datetime import datetime 
from UI_ import Ui_MainWindow
from time import sleep
from qthreadCustom import CSWorker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(5000)
        self.uic.btnClick.clicked.connect(self.btnClicked)
    def btnClicked(self):
        worker = CSWorker(self.btnClickTask)
        worker.signals.result.connect(self.btnClickTaskResult)
        self.threadpool.start(worker)
        
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


