# Form implementation generated from reading ui file '.\ScanVT2.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is

import math
import sys
from  sqlite3 import *
import socket
import os
import serial
from time import sleep
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox,QTableWidgetItem
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap,QImage
from datetime import datetime 
from UI import Ui_MainWindow
import cv2
import numpy as np
import zxingcpp
from PIL import Image
from pylibdmtx.pylibdmtx import encode,decode
from PIL import Image
import zpl
class VideoThread(QThread):
    #pyqtSignal (Kiểu tín hiệu trả về)
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,2048)
        self.cap.set(4,2048)
    def run(self):
        while True:
            ret, cv_img = self.cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img) 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.btn_Home.clicked.connect(self.btn_Home_Clicked)
        self.uic.stackedWidget.setCurrentWidget(self.uic.homePage)
        self.uic.btn_Home.clicked.connect(self.btn_Home_Clicked)
        self.uic.btn_SQL.clicked.connect(self.btn_SQL_Clicked)
        self.uic.btnPrintConf.clicked.connect(self.btn_Printer_Clicked)
        self.uic.btnConnectPrinter.clicked.connect(self.btn_Connect_Printer)
        self.uic.btnUpload.clicked.connect(self.btn_Upload_Clicked)
        self.uic.btnAdd.clicked.connect(self.btn_Add_Clicked)
        self.uic.btnPrint.clicked.connect(self.btnPrintClicked)
        self.uic.dataTableWidget.verticalHeader().sectionClicked.connect(self.verticalHeaderClicked)
        self.uic.btnCapture.clicked.connect(self.btnCaptureClicked)
         # create the video capture thread
        self.camera = VideoThread()
        self.camera.start()
        # connect its signal to the update_image slo
        self.camera.change_pixmap_signal.connect(self.update_image)
        self.oldDataResult = []
        self.dataCode = []
        self.counter = 0
        self.listBarcode  = []
        self.flag =False
        self.port = "COM6"
        self.serial = QSerialPort(self)
        self.serial.setPortName(self.port)
        if self.serial.open(QIODevice.ReadWrite):
            self.serial.setBaudRate(QSerialPort.Baud115200)
            self.serial.setDataBits(QSerialPort.Data8)
            self.serial.setParity(QSerialPort.NoParity)
            self.serial.setStopBits(QSerialPort.OneStop)
            self.serial.readyRead.connect(self.reviceDataSerial)
            # 
        else:
            raise IOError("Cannot connect to device on port: ",self.port)
    @QtCore.Slot()
    def reviceDataSerial(self):
        dataRevice = self.serial.readLine().data().decode()
        if dataRevice == "PLC":
            self.flag = True
            
    @QtCore.Slot()
    def sendDataSerial(self,data):
        self.serial.write(data.encode())
        
    def keyPressEvent(self, e):
        print(e.key())
        if e.key() == Qt.Key.Key_Escape.value:
            print("Pressed !!  clOSE")
            self.close()
        if e.key() == Qt.Key.Key_F1.value:
            self.sendDataSerial("PLC")

    def btnCaptureClicked(self):
        print("Capture Clicked")

    def btn_Connect_Printer(self):
        self.host = self.uic.txtHost.text()
        self.port = self.uic.txtPort.text()
        print(self.host)
        print(self.port)
        
        self.printerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # try:           
        self.printerSocket.connect((self.host, int(self.port))) #connecting to host
        self.printerSocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
        self.printerSocket.close () #closing connection
        # except:
        #     print("Error with the connection")
        
    def verticalHeaderClicked(self):
        self.dataShow = []
        numcol = self.uic.dataTableWidget.columnCount()
        currentRow = self.uic.dataTableWidget.currentRow()
        print(currentRow)
        for col in range(numcol):
            it = self.uic.dataTableWidget.item(currentRow, col)
            self.dataShow.append(it.text())
        print(self.dataShow)
        self.uic.txtMaNCU.setText(self.dataShow[0])
        self.uic.txt_PN.setText(self.dataShow[1])
        self.uic.txtnameNCU.setText(self.dataShow[2])
        self.uic.txtformat.setText(self.dataShow[3])

    def btn_Printer_Clicked(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.pagePrinterConfig)

    def btnCancelClicked(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.homePage)
        
    def btn_Home_Clicked(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.homePage)
        print("Home Page Pressed ! ")

    def btn_SQL_Clicked(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.dataPage)
        self.loadDataToTable()

    def btn_Upload_Clicked(self):
        mancc = self.uic.txtMaNCU.text()
        pn = self.uic.txt_PN.text()
        ncu = self.uic.txtnameNCU.text()
        type_format = self.uic.txtformat.text()
        query = """
        UPDATE tbNCU
        SET mancc = '{0}',
            pn = '{1}',
            ncu = '{2}',
            Format = '{3}'
        WHERE
            mancc = '{4}'
            AND 
             pn ='{5}'
            
        """.format(mancc,pn,ncu,type_format,self.dataShow[0],self.dataShow[1])
        conn = connect(dbDir)
        curs = conn.cursor()
        curs.execute(query).fetchall()
        conn.commit()
        if  curs.rowcount >0:
            print("ADD data OK")
        conn.close()
        self.loadDataToTable()

    def btn_Add_Clicked(self):
        mancc = self.uic.txtMaNCU.text()
        pn = self.uic.txt_PN.text()
        ncu = self.uic.txtnameNCU.text()
        type_format = self.uic.txtformat.text()
        query = """
        INSERT INTO tbNCU(mancc,pn,ncu,Format) 
        SELECT "{0}","{1}","{2}","{3}"
        WHERE NOT EXISTS(SELECT * FROM tbNCU WHERE mancc = "{0}" AND pn = '{1}');
                """.format(mancc,pn,ncu,type_format)
        conn = connect(dbDir)
        curs = conn.cursor()
        curs.execute(query).fetchall()
        conn.commit()
        if  curs.rowcount >0:
            print("ADD data OK")
        conn.close()
        self.loadDataToTable()
        
    def loadDataToTable(self):
        data = self.excuteSQL("SELECT * from tbNCU")
        for column, item in enumerate(data):
            row = self.uic.dataTableWidget.rowCount()
            self.uic.dataTableWidget.setItem(column,0, QTableWidgetItem(item[0]))
            self.uic.dataTableWidget.setItem(column,1, QTableWidgetItem(item[1]))
            self.uic.dataTableWidget.setItem(column,2, QTableWidgetItem(item[2]))
            self.uic.dataTableWidget.setItem(column,3, QTableWidgetItem(item[3]))
            if row < len(data):
                self.uic.dataTableWidget.setRowCount(row+1)
               
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        self.cv_img = cv_img
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.image_label.setPixmap(qt_img)
        self.processImage()
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        resize = cv2.resize(cv_img,(360,360),interpolation = cv2.INTER_CUBIC)
        h, w, ch = resize.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(resize.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(360, 360, Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)
    ########################################## APPLICATION ##########################################
    def read_barcode_zxing(self, frame):
        resultScanCode = zxingcpp.read_barcodes(frame)
        for result in resultScanCode:
            if str(result.format) == "BarcodeFormat.DataMatrix" or str(result.format) == "BarcodeFormat.QRCode":
                [x1,y1] = result.position.bottom_left.x,result.position.bottom_left.y
                [x2,y2] = result.position.bottom_right.x,result.position.bottom_right.y
                [x3,y3] = result.position.top_right.x,result.position.top_right.y
                [x4,y4] = result.position.top_left.x,result.position.top_left.y
                return {'data' :result.text.split(","),'pos1': [x1,y1],'pos2': [x2,y2],'pos3': [x3,y3],'pos4': [x4,y4]}
            # DataMaxtrix format : PN_Vendor_LOT_DateCode_Quantity_MaCongDon_CreateDate(timestamp)
    def get_distance(self,start_point, dest_point):
        x1, y1 = start_point
        x2, y2 = dest_point
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist
    def linePoints(self, x0,  y0,  x1,  y1):
        pointsOfLine=[]
        dx = abs(x1-x0)
        sx =  1 if x0<x1 else -1
        dy = abs(y1-y0)
        sy = 1 if y0<y1 else -1
        err = (dx if dx>dy else  -dy)/2
        while 1:
            pointsOfLine.append((x0,y0))
            if x0==x1 and y0==y1:
                break
            e2 = err
            if e2 >-dx:
                err -= dy
                x0 += sx
            if e2 < dy:
                err += dx
                y0 += sy
        return pointsOfLine
    
    def getDesPoint(self,start_point,dest_point):
        res_point=None
        end_points=None
        theta = np.arctan2(start_point[1]-dest_point[1], start_point[0]-dest_point[0])
        endpt_x = int(start_point[0] - 2048*np.cos(theta))
        endpt_y = int(start_point[1] - 2048*np.sin(theta))
        end_points= (endpt_x, endpt_y)
        print("End_point:" ,end_points)
        Points=self.linePoints(start_point[0],start_point[1],end_points[0],end_points[1])
        
        for point in Points:
            if abs(self.get_distance(dest_point,point)-self.get_distance(start_point,dest_point))<=0.5:
                if point!=start_point:
                    res_point=point
        return res_point
    def findOppositePoint(self,image,val_thresh,areaTem = 10000):
        """
        Find stamp position, Centroid Axis and return opposite point paste stamp print
            Return : - Data QR of tem
                    - Opposite point (x,y)
        """
        #Stamp Process
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        _,thresh_tem = cv2.threshold(gray.copy(),val_thresh,255,cv2.THRESH_BINARY)
        kernel = np.ones((1,1), np.uint8)
        thresh_tem = cv2.erode(thresh_tem, kernel, cv2.BORDER_REFLECT)
        contours, _ = cv2.findContours(thresh_tem,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        #Axis Process
        blur_img = cv2.medianBlur(gray,171)
        thresh_meanC = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(thresh_meanC, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        detected_circles = cv2.HoughCircles(dilation, method=cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30,minRadius=0, maxRadius=75)
        pointCenterTem=None
        Point_Cirle=None


        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > areaTem:
                
                x,y,w,h=cv2.boundingRect(cnt)
                tem_ROI=image[y:y+h,x:x+w]
                dataResult = self.read_barcode_zxing(tem_ROI)
                if dataResult is not None:
                    self.dataCode = dataResult['data'] #Global data
                    pos1 = ( dataResult['pos1'][0]+x, dataResult['pos1'][1]+y)
                    pos2 = ( dataResult['pos2'][0]+x, dataResult['pos2'][1]+y)
                    pos3 = ( dataResult['pos3'][0]+x, dataResult['pos3'][1]+y)
                    pos4 = ( dataResult['pos4'][0]+x, dataResult['pos4'][1]+y)
                    resultPoint1 = cv2.pointPolygonTest(cnt, pos1, False) 
                    resultPoint2 = cv2.pointPolygonTest(cnt, pos2, False)
                    resultPoint3 = cv2.pointPolygonTest(cnt, pos3, False)
                    resultPoint4 = cv2.pointPolygonTest(cnt, pos4, False)
                    print("Result position : ",resultPoint1,resultPoint2,resultPoint3,resultPoint4)
                    if int(resultPoint1) == 1 and int(resultPoint2) == 1 and int(resultPoint3) == 1 and int(resultPoint4) == 1:
                        rect = cv2.minAreaRect(cnt)
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        M = cv2.moments(box)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        print("Finded Centroid : ", (cX,cY))
                        pointCenterTem = (cX,cY)
        # Draw circles that are detected.
        if detected_circles is not None:
            print('The axis centroid has been found !')
            # Convert the circle parameters a, b and r to integers.
            detected_circles = np.uint16(np.around(detected_circles))
            print(detected_circles)
            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
                Point_Cirle = (a, b)
                # Draw the circumference of the circle.
                cv2.circle(image, (a, b), r, (0, 255, 0), 5)
                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(image, (a, b), 1, (0, 0, 255), 5)
            if  Point_Cirle is not None and pointCenterTem is not None:
                    # cv2.drawContours(image,[box],-1, (255, 255, 0),5)
                    # cv2.circle(image, (cX, cY), 10, (0, 255, 0),10)
                    # cv2.putText(image, str((cX, cY)), (cX - 30, cY -30),cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 5)
                    # cv2.line(image,(cX,cY),(a,b),(255,255,0),5)
                    end_point = self.getDesPoint((cX,cY),(a,b))
                    # cv2.circle(image, end_point, 5, (0, 0, 255), -1)
                    # cv2.line(image,(a,b),(end_point),(255,255,255),5)
                    return end_point


            # imageOrigin= cv2.resize(image,(500,500))
            # threshStamp = cv2.resize(thresh_tem ,(500,500))
            # houghCircle = cv2.resize(dilation ,(500,500))  
            # cv2.imshow('imageOrigin', imageOrigin)
            # cv2.imshow('threshStamp',threshStamp)
            # cv2.imshow('houghCircle',houghCircle)
            # cv2.waitKey(0)
        else:
            print("Can't find the axis center !")
            return False
    def processImage(self):
        if self.flag == True:
            self.dataCode =[]
            for i in range(5):
                print("Run number: ", i)
                image = cv2.imread(r'C:\Users\BOSS\Desktop\S01_SMT_2\Data\image\CT4.png')
                endPoint = self.findOppositePoint(image,190)
                if endPoint:
                    self.processData(self.dataCode)
                    self.sendDataSerial("OK")
                    break
                else:
                    self.sendDataSerial("Error")
                    return


            
        self.flag = False
    def processData(self,listData):
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
        #Khong tien to dung truoc
        if listData[0][0]!="P":
            dataSQL = self.excuteSQL("SELECT * from tbNCU WHERE PN = '"+listData[0]+"'")
            for dt in dataSQL :
                print(dt[2])
                if dt[3]== '':
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Icon.Critical)
                        msg.setWindowTitle("Not found data in SQLite!")
                        msg.setText('Bạn có muốn thêm mã này vào CSDL không ? ')
                        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                        result = msg.exec()
                        if result == QMessageBox.StandardButton.Yes:
                            self.uic.stackedWidget.setCurrentWidget(self.uic.dataPage)
                            self.loadDataToTable()
                if dt[3] == defaultFormat:
                    self.dataCode[1] = dt[2]
                    typeFormat1 = dt[3].split("-")  
                self.dataCode [0] = listData[int(typeFormat1[0])-1]
                self.dataCode [2] = listData[int(typeFormat1[1])-1]
                self.dataCode [3] = listData[int(typeFormat1[2])-1]
                self.dataCode [4] = listData[int(typeFormat1[3])-1]
                self.dataCode [5] = datetime.today().strftime('%Y%m%d%H%M%S')[:-2]
                self.dataCode [6] = str(self.counter)
                self.dataPrint =""
                for dt in self.dataCode:
                    self.dataPrint += dt +"_"
                self.dataPrint = self.dataPrint[:-1]
                self.dumpData(self.dataCode)
        else:
            
            for data in listData:
                if data[0] == "P":
                    self.dataCode[0] = data[1:]
                elif data[0] == "L":
                    self.dataCode[2] = data[1:]   
                elif data[0] == "D":
                    self.dataCode[3] = data[1:]
                elif data[0] =="Q":
                    self.dataCode[4] = data[1:]
            dataSQL = self.excuteSQL("SELECT * from tbNCU WHERE PN = '"+self.dataCode[0]+"'")
            for dt in dataSQL :
                print(dt[2])
                if dt[3]== '':
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Icon.Critical)
                        msg.setWindowTitle("Not found data in SQLite!")
                        msg.setText('Bạn có muốn thêm mã này vào CSDL không ? ')
                        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                        result = msg.exec()
                        if result == QMessageBox.StandardButton.Yes:
                            self.uic.stackedWidget.setCurrentWidget(self.uic.dataPage)
                            self.loadDataToTable()
                if dt[3] == defaultFormat:
                    self.dataCode[1] = dt[2]
            self.dataCode[5] = datetime.today().strftime('%Y%m%d%H%M%S')[:-2]
            self.dataCode[6] = str(self.counter)
            self.dataPrint =""
            for dt in self.dataCode:
                self.dataPrint += dt +"_"
            self.dataPrint = self.dataPrint[:-1]
            self.dumpData(self.dataCode)
            return
    def formatDataTwo(self,listData):
        self.dataCode = [""]*7
        dataResultSQL = self.excuteSQL("SELECT * from tbNCU WHERE PN = '"+listData[1]+"'")
        if dataResultSQL ==[]:
            print("NODATA IN SQL")
        else:
            # print(dataResultSQL)
            for index, data in enumerate(dataResultSQL[0]):
                print(data)
                if data == "":
                    print("Du lieu cot {0} thieu , vui long cap nhat ! ",index)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Critical)
                    msg.setWindowTitle("Not found data in SQLite!")
                    msg.setText('Bạn có muốn thêm mã này vào CSDL không ? ')
                    msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    result = msg.exec()
                    if result == QMessageBox.StandardButton.Yes:
                        self.uic.stackedWidget.setCurrentWidget(self.uic.dataPage)
                        self.loadDataToTable()
                    else:
                        print("Cancel")
            self.typeFormat = dataResultSQL[0][3].split("-")
            self.getVendor = self.excuteSQL("SELECT ncu from tbNCU WHERE PN = '"+listData[1]+"'")
            self.dataCode [0] = listData[int(self.typeFormat[0])-1]
            # self.dataCode [1] = self.excuteSQL("SELECT ncu from tbNCU WHERE PN = '"+listData[1]+"'")[0][0]
            self.dataCode [2] = listData[int(self.typeFormat[1])-1]
            self.dataCode [3] = listData[int(self.typeFormat[2])-1]
            self.dataCode [4] = listData[int(self.typeFormat[3])-1]
            self.dataCode [5] = datetime.today().strftime('%Y%m%d%H%M%S')[:-2]
            self.dataCode [6] = str(self.counter)
            
            dataSQL = self.excuteSQL("SELECT * from tbNCU WHERE PN = '"+listData[1]+"'")
            # Check MaNCU neu ma PN co 2 NCU
            for dt in dataSQL :
                print(dt)
                if listData[0] == dt[0]:
                    self.dataCode[1] = dt[2]
            
            
            self.dataPrint =""
            for dt in self.dataCode:
                self.dataPrint += dt +"_"
            self.dataPrint = self.dataPrint[:-1]
            self.dumpData(self.dataCode)
        
    def msgBtnClick(self):
        print("OK Click ! ")

    def dumpData(self, dataCode):
        self.uic.lbLog.setText("")

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
        self.printData()
    def btnPrintClicked(self):
        print("Printer Clicked ! ")
        self.dataPN = self.uic.txtPN.text()
        self.dataVendor = self.uic.txtVendor.text()
        self.dataLOT = self.uic.txtLOT.text()
        self.dataDate = self.uic.txtDATE.text()
        self.dataQTY = self.uic.txtQTY.text()
        self.dataPrintDate = self.uic.txtPRINTDATE.text()
        self.dataCount = self.uic.txtCount.text()
        self.dataPrint = self.dataPN + "_" + self.dataVendor +"_"+ self.dataLOT +"_"+ self.dataDate + "_" + self.dataQTY+"_" + self.dataPrintDate +"_" +  self.dataCount
        encoded = encode(self.dataPrint.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        imagePrint = pathImage + self.dataPN+".png"
        img.save(imagePrint)
        # Send Data To Printer
        
        l = zpl.Label(10,50)
        image_width = 9
        l.origin(.5,.5)
        l.write_graphic(Image.open(imagePrint),image_width)
        l.endorigin()
        l.origin(12, 1.5)
        l.write_text(self.dataPrint,char_width = 1.5,char_height = 1.5,line_width=36,max_line=10,line_spaces = 10)
        l.endorigin()
        print(l.dumpZPL().encode())
        self.printerSocket.connect((self.host, int(self.port)))
        self.printerSocket.send(l.dumpZPL().encode())
        self.printerSocket.close()
    # Remove File Image when send to Printer
        os.remove(imagePrint)
    def printData(self):
        print("Printing")
        dataPN = self.uic.txtPN.text()
        dataVendor = self.uic.txtVendor.text()
        dataLOT = self.uic.txtLOT.text()
        dataDate = self.uic.txtDATE.text()
        dataQTY = self.uic.txtQTY.text()
        dataPrintDate = self.uic.txtPRINTDATE.text()
        dataCount = self.uic.txtCount.text()
        dataPrint = dataPN + "_" + dataVendor +"_"+ dataLOT +"_"+ dataDate + "_" + dataQTY+"_" + dataPrintDate +"_" +  dataCount
        encoded = encode(dataPrint.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        imagePrint = pathImage + dataPN+".png"
        img.save(imagePrint)
        # Send Data To Printer
        l = zpl.Label(10,50)
        image_width = 9
        l.origin(.5,.5)
        l.write_graphic(Image.open(imagePrint),image_width)
        l.endorigin()
        l.origin(12, 1.5)
        l.write_text(self.dataPrint,char_width = 1.5,char_height = 1.5,line_width=36,max_line=10,line_spaces = 10)
        l.endorigin()
        print(l.dumpZPL().encode())
        l.preview()
        # self.printerSocket.connect((self.host, int(self.port)))
        # self.printerSocket.send(l.dumpZPL().encode())
        # self.printerSocket.close()

    # Remove File Image when send to Printer
        # os.remove(imagePrint)

    def excuteSQL(self,query):
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
    pathImage = os.path.join(curDir, './Data/image/')
    print(dbDir)
    
    #######UI#######
  # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())