# Form implementation generated from reading ui file '.\ScanVT2.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 649)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Data/Icon/Logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(40, 44, 52);\n"
"color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(90, 60, 971, 591))
        self.stackedWidget.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.lbLog = QtWidgets.QLabel(self.homePage)
        self.lbLog.setGeometry(QtCore.QRect(0, 360, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbLog.setFont(font)
        self.lbLog.setAutoFillBackground(False)
        self.lbLog.setStyleSheet("\n"
"color : #DA1818;\n"
"font-size:20px;\n"
"")
        self.lbLog.setText("")
        self.lbLog.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbLog.setObjectName("lbLog")
        self.textArea = QtWidgets.QPlainTextEdit(self.homePage)
        self.textArea.setGeometry(QtCore.QRect(40, 410, 271, 71))
        self.textArea.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"border-radius:10px;\n"
"color:#DDDDDD;\n"
"font-size:14px;")
        self.textArea.setReadOnly(True)
        self.textArea.setCenterOnScroll(False)
        self.textArea.setObjectName("textArea")
        self.frame = QtWidgets.QFrame(self.homePage)
        self.frame.setGeometry(QtCore.QRect(390, 30, 450, 450))
        self.frame.setStyleSheet("*{\n"
"background-color: #EBEBEB;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.image_label = QtWidgets.QLabel(self.frame)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 450, 450))
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap(".\\../../Pictures/pngtree-no-camera-png-image_8427391.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.btnPrint = QtWidgets.QPushButton(self.homePage)
        self.btnPrint.setGeometry(QtCore.QRect(120, 500, 111, 41))
        self.btnPrint.setStyleSheet("*{color:#DDDDDD;\n"
"background-color: rgb(52, 59, 72);\n"
"border:none;\n"
"font-size: 14px;\n"
"border-radius:10px;\n"
"}\n"
":hover{\n"
"border: solid red;\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.btnPrint.setObjectName("btnPrint")
        self.txtPN = QtWidgets.QLineEdit(self.homePage)
        self.txtPN.setGeometry(QtCore.QRect(121, 21, 203, 36))
        self.txtPN.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtPN.setObjectName("txtPN")
        self.txtVendor = QtWidgets.QLineEdit(self.homePage)
        self.txtVendor.setGeometry(QtCore.QRect(121, 69, 203, 36))
        self.txtVendor.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtVendor.setObjectName("txtVendor")
        self.txtLOT = QtWidgets.QLineEdit(self.homePage)
        self.txtLOT.setGeometry(QtCore.QRect(121, 117, 203, 36))
        self.txtLOT.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtLOT.setObjectName("txtLOT")
        self.txtDATE = QtWidgets.QLineEdit(self.homePage)
        self.txtDATE.setGeometry(QtCore.QRect(121, 165, 203, 36))
        self.txtDATE.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtDATE.setObjectName("txtDATE")
        self.txtQTY = QtWidgets.QLineEdit(self.homePage)
        self.txtQTY.setGeometry(QtCore.QRect(121, 213, 203, 36))
        self.txtQTY.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtQTY.setObjectName("txtQTY")
        self.txtPRINTDATE = QtWidgets.QLineEdit(self.homePage)
        self.txtPRINTDATE.setGeometry(QtCore.QRect(121, 261, 203, 36))
        self.txtPRINTDATE.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtPRINTDATE.setObjectName("txtPRINTDATE")
        self.txtCount = QtWidgets.QLineEdit(self.homePage)
        self.txtCount.setGeometry(QtCore.QRect(121, 309, 203, 36))
        self.txtCount.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtCount.setObjectName("txtCount")
        self.lb_PN = QtWidgets.QLabel(self.homePage)
        self.lb_PN.setGeometry(QtCore.QRect(-2, 30, 62, 21))
        self.lb_PN.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_PN.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_PN.setObjectName("lb_PN")
        self.lb_Vendor = QtWidgets.QLabel(self.homePage)
        self.lb_Vendor.setGeometry(QtCore.QRect(-2, 70, 52, 21))
        self.lb_Vendor.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_Vendor.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_Vendor.setObjectName("lb_Vendor")
        self.lbCount = QtWidgets.QLabel(self.homePage)
        self.lbCount.setGeometry(QtCore.QRect(-2, 320, 55, 21))
        self.lbCount.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lbCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbCount.setObjectName("lbCount")
        self.lb_QTY = QtWidgets.QLabel(self.homePage)
        self.lb_QTY.setGeometry(QtCore.QRect(-2, 220, 33, 21))
        self.lb_QTY.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_QTY.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_QTY.setObjectName("lb_QTY")
        self.lb_LOT = QtWidgets.QLabel(self.homePage)
        self.lb_LOT.setGeometry(QtCore.QRect(-2, 120, 32, 21))
        self.lb_LOT.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_LOT.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_LOT.setObjectName("lb_LOT")
        self.lb_DATE = QtWidgets.QLabel(self.homePage)
        self.lb_DATE.setGeometry(QtCore.QRect(-2, 170, 40, 21))
        self.lb_DATE.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_DATE.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_DATE.setObjectName("lb_DATE")
        self.lb_DatePrint = QtWidgets.QLabel(self.homePage)
        self.lb_DatePrint.setGeometry(QtCore.QRect(-2, 270, 81, 21))
        self.lb_DatePrint.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_DatePrint.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_DatePrint.setObjectName("lb_DatePrint")
        self.stackedWidget.addWidget(self.homePage)
        self.dataPage = QtWidgets.QWidget()
        self.dataPage.setObjectName("dataPage")
        self.dataTableWidget = QtWidgets.QTableWidget(self.dataPage)
        self.dataTableWidget.setGeometry(QtCore.QRect(1, 25, 491, 481))
        self.dataTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.dataTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dataTableWidget.setGridStyle(QtCore.Qt.PenStyle.DashDotDotLine)
        self.dataTableWidget.setRowCount(1)
        self.dataTableWidget.setObjectName("dataTableWidget")
        self.dataTableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.dataTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.dataTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.dataTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.dataTableWidget.setHorizontalHeaderItem(3, item)
        self.dataTableWidget.horizontalHeader().setVisible(False)
        self.dataTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.dataTableWidget.horizontalHeader().setStretchLastSection(False)
        self.dataTableWidget.verticalHeader().setVisible(False)
        self.lb_MaNCU = QtWidgets.QLabel(self.dataPage)
        self.lb_MaNCU.setGeometry(QtCore.QRect(531, 25, 55, 19))
        self.lb_MaNCU.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_MaNCU.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_MaNCU.setObjectName("lb_MaNCU")
        self.lb_nameNCU = QtWidgets.QLabel(self.dataPage)
        self.lb_nameNCU.setGeometry(QtCore.QRect(531, 133, 54, 19))
        self.lb_nameNCU.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_nameNCU.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_nameNCU.setObjectName("lb_nameNCU")
        self.lb_DATE_5 = QtWidgets.QLabel(self.dataPage)
        self.lb_DATE_5.setGeometry(QtCore.QRect(531, 187, 92, 38))
        self.lb_DATE_5.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_DATE_5.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.lb_DATE_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_DATE_5.setObjectName("lb_DATE_5")
        self.txtnameNCU = QtWidgets.QLineEdit(self.dataPage)
        self.txtnameNCU.setGeometry(QtCore.QRect(629, 133, 201, 34))
        self.txtnameNCU.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtnameNCU.setReadOnly(False)
        self.txtnameNCU.setObjectName("txtnameNCU")
        self.txt_PN = QtWidgets.QLineEdit(self.dataPage)
        self.txt_PN.setGeometry(QtCore.QRect(629, 79, 201, 34))
        self.txt_PN.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txt_PN.setReadOnly(False)
        self.txt_PN.setObjectName("txt_PN")
        self.lb_PN_ADD = QtWidgets.QLabel(self.dataPage)
        self.lb_PN_ADD.setGeometry(QtCore.QRect(531, 79, 18, 19))
        self.lb_PN_ADD.setStyleSheet("font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_PN_ADD.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_PN_ADD.setObjectName("lb_PN_ADD")
        self.txtformat = QtWidgets.QLineEdit(self.dataPage)
        self.txtformat.setGeometry(QtCore.QRect(629, 189, 201, 34))
        self.txtformat.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtformat.setReadOnly(False)
        self.txtformat.setObjectName("txtformat")
        self.txtMaNCU = QtWidgets.QLineEdit(self.dataPage)
        self.txtMaNCU.setGeometry(QtCore.QRect(629, 25, 201, 34))
        self.txtMaNCU.setStyleSheet("QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtMaNCU.setReadOnly(False)
        self.txtMaNCU.setObjectName("txtMaNCU")
        self.btnAdd = QtWidgets.QPushButton(self.dataPage)
        self.btnAdd.setGeometry(QtCore.QRect(592, 245, 80, 40))
        self.btnAdd.setStyleSheet("*{color:#DDDDDD;\n"
"background-color: rgb(52, 59, 72);\n"
"border:none;\n"
"font-size: 14px;\n"
"border-radius:10px;\n"
"}\n"
":hover{\n"
"border: solid red;\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.btnAdd.setObjectName("btnAdd")
        self.btnUpload = QtWidgets.QPushButton(self.dataPage)
        self.btnUpload.setGeometry(QtCore.QRect(733, 245, 80, 40))
        self.btnUpload.setStyleSheet("*{color:#DDDDDD;\n"
"background-color: rgb(52, 59, 72);\n"
"border:none;\n"
"font-size: 14px;\n"
"border-radius:10px;\n"
"}\n"
":hover{\n"
"border: solid red;\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.btnUpload.setObjectName("btnUpload")
        self.stackedWidget.addWidget(self.dataPage)
        self.pagePrinterConfig = QtWidgets.QWidget()
        self.pagePrinterConfig.setObjectName("pagePrinterConfig")
        self.btnConnectPrinter = QtWidgets.QPushButton(self.pagePrinterConfig)
        self.btnConnectPrinter.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.btnConnectPrinter.setObjectName("btnConnectPrinter")
        self.widget = QtWidgets.QWidget(self.pagePrinterConfig)
        self.widget.setGeometry(QtCore.QRect(60, 60, 174, 54))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtHost = QtWidgets.QLineEdit(self.widget)
        self.txtHost.setObjectName("txtHost")
        self.gridLayout.addWidget(self.txtHost, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtPort = QtWidgets.QLineEdit(self.widget)
        self.txtPort.setObjectName("txtPort")
        self.gridLayout.addWidget(self.txtPort, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.pagePrinterConfig)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 60, 80, 590))
        self.frame_2.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_Home = QtWidgets.QPushButton(self.frame_2)
        self.btn_Home.setEnabled(True)
        self.btn_Home.setGeometry(QtCore.QRect(0, 0, 80, 45))
        self.btn_Home.setStyleSheet("QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(40, 44, 52);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Data/Icon/icon_menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_Home.setIcon(icon1)
        self.btn_Home.setObjectName("btn_Home")
        self.btn_SQL = QtWidgets.QPushButton(self.frame_2)
        self.btn_SQL.setGeometry(QtCore.QRect(0, 40, 80, 45))
        self.btn_SQL.setStyleSheet("QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(40, 44, 52);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Data/Icon/icon_settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_SQL.setIcon(icon2)
        self.btn_SQL.setObjectName("btn_SQL")
        self.btnPrintConf = QtWidgets.QPushButton(self.frame_2)
        self.btnPrintConf.setGeometry(QtCore.QRect(0, 80, 80, 45))
        self.btnPrintConf.setStyleSheet("QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(40, 44, 52);\n"
"}")
        self.btnPrintConf.setIcon(icon2)
        self.btnPrintConf.setObjectName("btnPrintConf")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(80, 0, 920, 60))
        self.frame_3.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 80, 60))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btngoHome = QtWidgets.QPushButton(self.frame_4)
        self.btngoHome.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.btngoHome.setStyleSheet("QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(40, 44, 52);\n"
"}")
        self.btngoHome.setText("")
        self.btngoHome.setIcon(icon)
        self.btngoHome.setIconSize(QtCore.QSize(55, 55))
        self.btngoHome.setObjectName("btngoHome")
        self.frame_3.raise_()
        self.stackedWidget.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPrint.setText(_translate("MainWindow", "Print"))
        self.lb_PN.setText(_translate("MainWindow", "PN Code"))
        self.lb_Vendor.setText(_translate("MainWindow", "Vendor"))
        self.lbCount.setText(_translate("MainWindow", "COUNT"))
        self.lb_QTY.setText(_translate("MainWindow", "QTY"))
        self.lb_LOT.setText(_translate("MainWindow", "LOT"))
        self.lb_DATE.setText(_translate("MainWindow", "DATE"))
        self.lb_DatePrint.setText(_translate("MainWindow", "PRINT DATE"))
        item = self.dataTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã NCU"))
        item = self.dataTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PN"))
        item = self.dataTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tên NCU"))
        item = self.dataTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Format"))
        self.lb_MaNCU.setText(_translate("MainWindow", "MÃ NCU"))
        self.lb_nameNCU.setText(_translate("MainWindow", "Tên NCU"))
        self.lb_DATE_5.setText(_translate("MainWindow", "Format\n"
"(Ex: 1-1-5-4-2)"))
        self.lb_PN_ADD.setText(_translate("MainWindow", "PN"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnUpload.setText(_translate("MainWindow", "Upload"))
        self.btnConnectPrinter.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "HOST"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.btn_Home.setText(_translate("MainWindow", " HOME"))
        self.btn_SQL.setText(_translate("MainWindow", " DATA"))
        self.btnPrintConf.setText(_translate("MainWindow", "PRINT"))
