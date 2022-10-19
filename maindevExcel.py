########################################################
# 1. 1 PN có 2 NCU
# 2. Mã QR không có tiền tố đứng trước

import sys
from  sqlite3 import *
import os
from time import sleep
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt6.QtGui import QPixmap,QImage
from datetime import datetime 
from UI import Ui_MainWindow
import cv2
import numpy as np
import zxingcpp
from pyzbar.pyzbar import decode
from PIL import Image
from pylibdmtx.pylibdmtx import encode,decode
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,2048)
        self.cap.set(4,2048)
    def run(self):
        # capture from web cam
        while self._run_flag:
            ret, cv_img = self.cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
                # self.findLocationTem(cv_img)
            
        # shut down capture system
        self.cap.release()  
    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()        
    def findLocationTem(self,cv_img):
        imgageGray = cv2.cvtColor(cv_img,cv2.COLOR_RGB2GRAY)
        _,img_thresh1 = cv2.threshold(imgageGray,200,255,cv2.THRESH_BINARY)
        imgResize = cv2.resize(img_thresh1,(0,0),fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)
        cv2.imshow("img_thresh1",imgResize)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return
class MainWindow:
    def __init__(self):
        self.mainWindow = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.mainWindow)
        self.mainWindow.show()
          # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.uic.btnPrint.clicked.connect(self.btnPrintClicked)
        # start the thread
        self.thread.start()
        self.oldDataResult = []
        self.counter = 0
        self.listBarcode  = []
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.image_label.setPixmap(qt_img)
        self.processImage(cv_img)
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        resize = cv2.resize(cv_img,(360,360),interpolation = cv2.INTER_CUBIC)
        h, w, ch = resize.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(resize.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(360, 360, Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)
    def closeEvent(self, event):
        self.thread.stop()
        event.accept()
    ##########################################APPLICATION##########################################
    def read_barcode(self, frame, gray):
        pass

    def read_barcode_zxing(self, frame):
        resultScanCode = zxingcpp.read_barcodes(frame)
        for result in resultScanCode:
            if str(result.format) == "BarcodeFormat.DataMatrix" or str(result.format) == "BarcodeFormat.QRCode":
                self.location = result.position
                return result.text.split(",")
            else:
                # Append list if not exist
                if result.text not in self.listBarcode:
                    self.listBarcode.append(result.text)
            # DataMaxtrix format : PN_Vendor_LOT_DateCode_Quantity_MaCongDon_CreateDate(timestamp)
        
               
    def processImage(self,cv_img):
        """ Process Image, Return data of Image (QRcode data or DataMatrix data)"""
        dataResult = self.read_barcode_zxing(cv_img)
        if dataResult is not None:
            if self.oldDataResult != dataResult:
                self.oldDataResult = dataResult
                dataResult = [data.replace('"','') for data in dataResult]
                self.processData(dataResult)
    def processData(self,listData):
        print("===================")
        print(listData)
        if len(listData) == 6:
            self.formatDataOne(listData)
          #type 1
        elif len(listData)==7:
            self.formatDataTwo(listData)
  
        
    def formatDataOne(self,listData):
        defaultFormat  = "1-5-4-2"
        self.dataCode = [""]*7
        # DataMaxtrix format : PN_Vendor_LOT_DateCode_Quantity_MaCongDon_CreateDate(timestamp)
        for data in listData:
            if data[0] == "P":
                self.dataCode[0] = data[1:]
            elif data[0] == "L":
                self.dataCode[2] = data[1:]   
            elif data[0] == "D":
                self.dataCode[3] = data[1:]
            elif data[0] =="Q":
                self.dataCode[4] = data[1:]
        query = "SELECT * from NCU WHERE PN = '"+self.dataCode[0]+"'"
        dataSQL = self.getNCU(query)
        for dt in dataSQL :
            print(dt)
            if dt[3] == defaultFormat or listData[0] == dt[0] and dt[3]!= '':
               self.dataCode[1] = dt[2]
               
        self.dataCode[5] = datetime.today().strftime('%Y%m%d%H%M%S')
        self.dataCode[6] = str(self.counter)
        self.dataPrint =""
        for dt in self.dataCode:
            self.dataPrint += dt +"_"
        self.dataPrint = self.dataPrint[:-1]
        print(self.dataCode)
        # self.getVendor = self.getNCU("SELECT ncu from NCU WHERE PN = '"+self.dataCode[0]+"'")

        self.dumpData(self.dataCode)
        
    def formatDataTwo(self,listData):
        self.dataCode = [""]*7
        query = "SELECT format from NCU WHERE PN = '"+listData[1]+"'"
        typeFormat  = self.getNCU(query)
      
            
       
        if typeFormat == []:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Not found data in SQLite!")
            msg.setText('Bạn có muốn thêm mã này vào CSDL không ? ')
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                print("Click ok ")
            else:
                print("Cancel")
            return
        else:
            typeFormat  = self.getNCU(query)[0][0].split('-')
        self.getVendor = self.getNCU("SELECT ncu from NCU WHERE PN = '"+listData[1]+"'")
        self.dataCode [0] = listData[int(typeFormat[0])-1]
        self.dataCode [2] = listData[int(typeFormat[1])-1]
        self.dataCode [3] = listData[int(typeFormat[2])-1]
        self.dataCode [4] = listData[int(typeFormat[3])-1]
        self.dataCode [5] = datetime.today().strftime('%Y%m%d%H%M%S')
        self.dataCode [6] = str(self.counter)
        
        dataSQL = self.getNCU("SELECT * from NCU WHERE PN = '"+listData[1]+"'")
        for dt in dataSQL :
            print(dt)
            if listData[0] == dt[0]:
                self.dataCode[1] = dt[2]
        
        
        self.dataPrint =""
        print(self.dataCode)
        for dt in self.dataCode:
            self.dataPrint += dt +"_"
        self.dataPrint = self.dataPrint[:-1]
        self.dumpData(self.dataCode)

        
    def msgBtnClick(self):
        print("OK Click ! ")

    def dumpData(self, dataCode):
        self.uic.lbLog.setText("")
        # if len(self.getVendor) >1:
        #     print(self.getVendor)
        #     self.uic.lbLog.setText("MÃ PN có 2 NCU")

        self.uic.txtPN.setText(dataCode[0])
        self.uic.txtVendor.setText(dataCode[1])
        self.uic.txtLOT.setText(dataCode[2])
        self.uic.txtDATE.setText(dataCode[3])
        self.uic.txtQTY.setText(dataCode[4])
        self.uic.txtPRINTDATE.setText(dataCode[5])
        self.uic.txtCount.setText(dataCode[6])
        self.uic.textArea.setPlainText("")
        self.uic.textArea.setPlainText(str(self.dataPrint))
        self.counter +=1
        # encoded = encode(self.dataPrint.encode('utf8'))
        # img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        # img.save(pathImgage + self.dataCode[0]+".png")
        # print(decode(Image.open(pathImgage + self.dataCode[0]+".png")))
    def btnPrintClicked(self):
        print("CLicked !! ")
       
    
    def getNCU(self,query):
        try:
            conn = connect(dbDir)
            curs = conn.cursor()
            result = curs.execute(query).fetchall()
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            return 'False'
if __name__ == "__main__":
    ####CONFIG####
    curDir = os.path.dirname(os.path.realpath(__file__))
    dbDir = os.path.join(curDir, './Data/DB/dataNCU.db')
    pathImgage = os.path.join(curDir, './Data/image/')
    print(dbDir)
    
    #######UI#######
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
