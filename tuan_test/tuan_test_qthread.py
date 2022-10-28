import math
import sys
from  sqlite3 import *
import os
import serial
from time import sleep
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtNetwork import QTcpSocket,QTcpServer,QHostAddress

from UI_ import Ui_MainWindow
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
         # SOCKEt
        self.server = QTcpServer()
        if self.server.listen(QHostAddress.Any, 8080):
            print("Server Start")
        else:
            QMessageBox.critical(self, "QTCPServer", f"Unable to start the server: {self.server.errorString()}.")

            self.server.close()
            self.server.deleteLater()
    def new_connection(self) -> None:
        while self.server.hasPendingConnections():
            self.append_to_socket_list(self.server.nextPendingConnection())
       
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


