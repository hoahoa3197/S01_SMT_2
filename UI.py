# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScanVT2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFormLayout,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 649)
        icon = QIcon()
        icon.addFile(u"Data/Icon/Logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(90, 60, 971, 591))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.textArea = QPlainTextEdit(self.homePage)
        self.textArea.setObjectName(u"textArea")
        self.textArea.setGeometry(QRect(40, 410, 271, 71))
        self.textArea.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius:10px;\n"
"color:#DDDDDD;\n"
"font-size:14px;")
        self.textArea.setReadOnly(True)
        self.textArea.setCenterOnScroll(False)
        self.frame = QFrame(self.homePage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(390, 30, 450, 450))
        self.frame.setStyleSheet(u"*{\n"
"background-color: #EBEBEB;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.image_label = QLabel(self.frame)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(0, 0, 450, 450))
        self.image_label.setPixmap(QPixmap(u"../../Pictures/pngtree-no-camera-png-image_8427391.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.btnPrint = QPushButton(self.homePage)
        self.btnPrint.setObjectName(u"btnPrint")
        self.btnPrint.setGeometry(QRect(120, 500, 111, 41))
        self.btnPrint.setStyleSheet(u"*{color:#DDDDDD;\n"
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
        self.txtPN = QLineEdit(self.homePage)
        self.txtPN.setObjectName(u"txtPN")
        self.txtPN.setGeometry(QRect(121, 21, 203, 36))
        self.txtPN.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtVendor = QLineEdit(self.homePage)
        self.txtVendor.setObjectName(u"txtVendor")
        self.txtVendor.setGeometry(QRect(121, 69, 203, 36))
        self.txtVendor.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtLOT = QLineEdit(self.homePage)
        self.txtLOT.setObjectName(u"txtLOT")
        self.txtLOT.setGeometry(QRect(121, 117, 203, 36))
        self.txtLOT.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtDATE = QLineEdit(self.homePage)
        self.txtDATE.setObjectName(u"txtDATE")
        self.txtDATE.setGeometry(QRect(121, 165, 203, 36))
        self.txtDATE.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtQTY = QLineEdit(self.homePage)
        self.txtQTY.setObjectName(u"txtQTY")
        self.txtQTY.setGeometry(QRect(121, 213, 203, 36))
        self.txtQTY.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtPRINTDATE = QLineEdit(self.homePage)
        self.txtPRINTDATE.setObjectName(u"txtPRINTDATE")
        self.txtPRINTDATE.setGeometry(QRect(121, 261, 203, 36))
        self.txtPRINTDATE.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtCount = QLineEdit(self.homePage)
        self.txtCount.setObjectName(u"txtCount")
        self.txtCount.setGeometry(QRect(121, 309, 203, 36))
        self.txtCount.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lb_PN = QLabel(self.homePage)
        self.lb_PN.setObjectName(u"lb_PN")
        self.lb_PN.setGeometry(QRect(-2, 30, 62, 21))
        self.lb_PN.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_PN.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_Vendor = QLabel(self.homePage)
        self.lb_Vendor.setObjectName(u"lb_Vendor")
        self.lb_Vendor.setGeometry(QRect(-2, 70, 52, 21))
        self.lb_Vendor.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_Vendor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbCount = QLabel(self.homePage)
        self.lbCount.setObjectName(u"lbCount")
        self.lbCount.setGeometry(QRect(-2, 320, 55, 21))
        self.lbCount.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lbCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_QTY = QLabel(self.homePage)
        self.lb_QTY.setObjectName(u"lb_QTY")
        self.lb_QTY.setGeometry(QRect(-2, 220, 33, 21))
        self.lb_QTY.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_QTY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_LOT = QLabel(self.homePage)
        self.lb_LOT.setObjectName(u"lb_LOT")
        self.lb_LOT.setGeometry(QRect(-2, 120, 32, 21))
        self.lb_LOT.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_LOT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_DATE = QLabel(self.homePage)
        self.lb_DATE.setObjectName(u"lb_DATE")
        self.lb_DATE.setGeometry(QRect(-2, 170, 40, 21))
        self.lb_DATE.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_DATE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_DatePrint = QLabel(self.homePage)
        self.lb_DatePrint.setObjectName(u"lb_DatePrint")
        self.lb_DatePrint.setGeometry(QRect(-2, 270, 81, 21))
        self.lb_DatePrint.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_DatePrint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnCapture = QPushButton(self.homePage)
        self.btnCapture.setObjectName(u"btnCapture")
        self.btnCapture.setGeometry(QRect(560, 500, 111, 41))
        self.btnCapture.setStyleSheet(u"*{color:#DDDDDD;\n"
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
        self.stackedWidget.addWidget(self.homePage)
        self.dataPage = QWidget()
        self.dataPage.setObjectName(u"dataPage")
        self.txtnameNCU = QLineEdit(self.dataPage)
        self.txtnameNCU.setObjectName(u"txtnameNCU")
        self.txtnameNCU.setGeometry(QRect(629, 133, 201, 34))
        self.txtnameNCU.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtnameNCU.setReadOnly(False)
        self.txt_PN = QLineEdit(self.dataPage)
        self.txt_PN.setObjectName(u"txt_PN")
        self.txt_PN.setGeometry(QRect(629, 79, 201, 34))
        self.txt_PN.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txt_PN.setReadOnly(False)
        self.txtformat = QLineEdit(self.dataPage)
        self.txtformat.setObjectName(u"txtformat")
        self.txtformat.setGeometry(QRect(629, 189, 201, 34))
        self.txtformat.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtformat.setReadOnly(False)
        self.txtMaNCU = QLineEdit(self.dataPage)
        self.txtMaNCU.setObjectName(u"txtMaNCU")
        self.txtMaNCU.setGeometry(QRect(629, 25, 201, 34))
        self.txtMaNCU.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtMaNCU.setReadOnly(False)
        self.btnAdd = QPushButton(self.dataPage)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(592, 245, 80, 40))
        self.btnAdd.setStyleSheet(u"*{color:#DDDDDD;\n"
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
        self.btnUpload = QPushButton(self.dataPage)
        self.btnUpload.setObjectName(u"btnUpload")
        self.btnUpload.setGeometry(QRect(733, 245, 80, 40))
        self.btnUpload.setStyleSheet(u"*{color:#DDDDDD;\n"
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
        self.layoutWidget = QWidget(self.dataPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(531, 25, 88, 202))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(35)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_MaNCU = QLabel(self.layoutWidget)
        self.lb_MaNCU.setObjectName(u"lb_MaNCU")
        self.lb_MaNCU.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_MaNCU.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_MaNCU)

        self.lb_PN_ADD = QLabel(self.layoutWidget)
        self.lb_PN_ADD.setObjectName(u"lb_PN_ADD")
        self.lb_PN_ADD.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_PN_ADD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_PN_ADD)

        self.lb_nameNCU = QLabel(self.layoutWidget)
        self.lb_nameNCU.setObjectName(u"lb_nameNCU")
        self.lb_nameNCU.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_nameNCU.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_nameNCU)

        self.lb_DATE_5 = QLabel(self.layoutWidget)
        self.lb_DATE_5.setObjectName(u"lb_DATE_5")
        self.lb_DATE_5.setStyleSheet(u"font-size:14px;\n"
"color:#DDDDDD;")
        self.lb_DATE_5.setTextFormat(Qt.PlainText)
        self.lb_DATE_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_DATE_5)

        self.dataTableWidget = QTableWidget(self.dataPage)
        if (self.dataTableWidget.columnCount() < 4):
            self.dataTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.dataTableWidget.rowCount() < 1):
            self.dataTableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dataTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dataTableWidget.setItem(0, 0, __qtablewidgetitem5)
        self.dataTableWidget.setObjectName(u"dataTableWidget")
        self.dataTableWidget.setGeometry(QRect(10, 30, 500, 500))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTableWidget.sizePolicy().hasHeightForWidth())
        self.dataTableWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.dataTableWidget.setPalette(palette)
        self.dataTableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"     background-color: transparent;\n"
"     padding: 10px;\n"
"     border-radius: 5px;\n"
"     gridline-color: rgb(44, 49, 58);\n"
"     border-bottom: 1px solid rgb(44, 49, 60);\n"
"    \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"     border-color: rgb(44, 49, 60);\n"
"     padding-left: 5px;\n"
"     padding-right: 5px;\n"
"     gridline-color: rgb(44, 49, 60);\n"
"    \n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"     background-color: rgb(189, 147, 249);\n"
"    \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: rgb(33, 37, 43);\n"
"     max-width: 30px;\n"
"     border: 1px solid rgb(44, 49, 58);\n"
"     border-style: none;\n"
"     border-bottom: 1px solid rgb(44, 49, 60);\n"
"     border-right: 1px solid rgb(44, 49, 60);\n"
"    \n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"     background-color: rgb(33, 37, 43);\n"
"    \n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"     border: 1px solid rgb(33, 37, 43);\n"
"     background-color: rgb(33, 37, 4"
                        "3);\n"
"     padding: 3px;\n"
"     border-top-left-radius: 7px;\n"
"     border-top-right-radius: 7px;\n"
"    \n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"     border: 1px solid rgb(44, 49, 60);\n"
"    \n"
"}\n"
"\n"
"")
        self.dataTableWidget.setFrameShape(QFrame.NoFrame)
        self.dataTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dataTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.dataTableWidget.setAutoScrollMargin(16)
        self.dataTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dataTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dataTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dataTableWidget.setShowGrid(True)
        self.dataTableWidget.setGridStyle(Qt.DashLine)
        self.dataTableWidget.setSortingEnabled(False)
        self.dataTableWidget.horizontalHeader().setVisible(True)
        self.dataTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.dataTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.dataTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.dataTableWidget.horizontalHeader().setStretchLastSection(True)
        self.dataTableWidget.verticalHeader().setVisible(False)
        self.dataTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.dataTableWidget.verticalHeader().setMinimumSectionSize(30)
        self.dataTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.dataTableWidget.verticalHeader().setHighlightSections(False)
        self.dataTableWidget.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.dataPage)
        self.pagePrinterConfig = QWidget()
        self.pagePrinterConfig.setObjectName(u"pagePrinterConfig")
        self.txtHost = QLineEdit(self.pagePrinterConfig)
        self.txtHost.setObjectName(u"txtHost")
        self.txtHost.setGeometry(QRect(110, 10, 201, 34))
        self.txtHost.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtHost.setReadOnly(False)
        self.txtPort = QLineEdit(self.pagePrinterConfig)
        self.txtPort.setObjectName(u"txtPort")
        self.txtPort.setGeometry(QRect(110, 60, 201, 34))
        self.txtPort.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:15px;\n"
"color:#DDDDDD;\n"
"font-size: 24px;\n"
"text-align:center;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.txtPort.setReadOnly(False)
        self.btnConnectPrinter = QPushButton(self.pagePrinterConfig)
        self.btnConnectPrinter.setObjectName(u"btnConnectPrinter")
        self.btnConnectPrinter.setGeometry(QRect(150, 120, 111, 41))
        self.btnConnectPrinter.setStyleSheet(u"*{color:#DDDDDD;\n"
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
        self.label = QLabel(self.pagePrinterConfig)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 51, 31))
        self.label_2 = QLabel(self.pagePrinterConfig)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 51, 21))
        self.stackedWidget.addWidget(self.pagePrinterConfig)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 60, 80, 590))
        self.frame_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_Home = QPushButton(self.frame_2)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setEnabled(True)
        self.btn_Home.setGeometry(QRect(0, 0, 80, 45))
        self.btn_Home.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Data/Icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Home.setIcon(icon1)
        self.btn_Home.setIconSize(QSize(24, 24))
        self.btn_SQL = QPushButton(self.frame_2)
        self.btn_SQL.setObjectName(u"btn_SQL")
        self.btn_SQL.setGeometry(QRect(0, 45, 80, 45))
        self.btn_SQL.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Data/Icon/data.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_SQL.setIcon(icon2)
        self.btn_SQL.setIconSize(QSize(24, 24))
        self.btnPrintConf = QPushButton(self.frame_2)
        self.btnPrintConf.setObjectName(u"btnPrintConf")
        self.btnPrintConf.setGeometry(QRect(0, 90, 80, 45))
        self.btnPrintConf.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Data/image/printer-fill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPrintConf.setIcon(icon3)
        self.btnPrintConf.setIconSize(QSize(20, 20))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(80, 0, 920, 60))
        self.frame_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lbLog = QLabel(self.frame_3)
        self.lbLog.setObjectName(u"lbLog")
        self.lbLog.setGeometry(QRect(240, 0, 341, 60))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setItalic(False)
        self.lbLog.setFont(font)
        self.lbLog.setAutoFillBackground(False)
        self.lbLog.setStyleSheet(u"\n"
"color : #00FF1A;\n"
"font-size:40px;\n"
"")
        self.lbLog.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 80, 60))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btngoHome = QPushButton(self.frame_4)
        self.btngoHome.setObjectName(u"btngoHome")
        self.btngoHome.setGeometry(QRect(0, 0, 60, 60))
        self.btngoHome.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
        self.btngoHome.setIcon(icon)
        self.btngoHome.setIconSize(QSize(55, 55))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_3.raise_()
        self.stackedWidget.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_label.setText("")
        self.btnPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.lb_PN.setText(QCoreApplication.translate("MainWindow", u"PN Code", None))
        self.lb_Vendor.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.lbCount.setText(QCoreApplication.translate("MainWindow", u"COUNT", None))
        self.lb_QTY.setText(QCoreApplication.translate("MainWindow", u"QTY", None))
        self.lb_LOT.setText(QCoreApplication.translate("MainWindow", u"LOT", None))
        self.lb_DATE.setText(QCoreApplication.translate("MainWindow", u"DATE", None))
        self.lb_DatePrint.setText(QCoreApplication.translate("MainWindow", u"PRINT DATE", None))
        self.btnCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnUpload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.lb_MaNCU.setText(QCoreApplication.translate("MainWindow", u"NCU Code", None))
        self.lb_PN_ADD.setText(QCoreApplication.translate("MainWindow", u"PN Code", None))
        self.lb_nameNCU.setText(QCoreApplication.translate("MainWindow", u"Name NCU", None))
        self.lb_DATE_5.setText(QCoreApplication.translate("MainWindow", u"Format\n"
"(Ex: 1-5-4-2)", None))
        ___qtablewidgetitem = self.dataTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Supplier Code", None));
        ___qtablewidgetitem1 = self.dataTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"P/N", None));
        ___qtablewidgetitem2 = self.dataTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Supplier Name", None));
        ___qtablewidgetitem3 = self.dataTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Format", None));
        ___qtablewidgetitem4 = self.dataTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.dataTableWidget.isSortingEnabled()
        self.dataTableWidget.setSortingEnabled(False)
        self.dataTableWidget.setSortingEnabled(__sortingEnabled)

        self.txtHost.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.txtPort.setText(QCoreApplication.translate("MainWindow", u"12345", None))
        self.btnConnectPrinter.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HOST", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u" HOME", None))
        self.btn_SQL.setText(QCoreApplication.translate("MainWindow", u" DATA", None))
        self.btnPrintConf.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.lbLog.setText(QCoreApplication.translate("MainWindow", u"STATUS : OK", None))
        self.btngoHome.setText("")
    # retranslateUi

