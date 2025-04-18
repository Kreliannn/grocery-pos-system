import sys
import cv2
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from backend.utils.util import utils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 576)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 361, 371))
        self.widget.setStyleSheet("background-color:  whitesmoke\n""")
        self.widget.setObjectName("widget")

        
        utils.delayCameraLoad(self.startCamera, 100, MainWindow)


        self.camera = QtWidgets.QLabel(parent=self.widget)
        self.camera.setGeometry(QtCore.QRect(0, 0, 361, 371))
        self.camera.setStyleSheet("""
            background: whitesmoke;
            font-size: 24px;
            color: black;
            qproperty-alignment: 'AlignCenter';
        """)
        self.camera.setText("loading......")
        self.camera.setObjectName("camera")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 460, 781, 101))
        self.widget_2.setStyleSheet("background-color:  whitesmoke")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.total = QtWidgets.QLabel(parent=self.widget_2)
        self.total.setGeometry(QtCore.QRect(210, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 20, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("BACKGROUND : GREEN; COLOR :WHITE")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(380, 80, 411, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addToTable(self, barcode_data):
        print("addToTable")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TOTAL:"))
        self.total.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "PAY"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "qty"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "total"))
        self.pushButton_3.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "Receipt History"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))

    
    
    def closeEvent(self, event):
        self.cap.release()
        event.accept()

    
    def stopCamera(self):
        self.cap.release() 

    
    def startCamera(self, MainWindow):
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(lambda: utils.scanBarCodeAndUpdateFrame(self.cap, self.camera, self.addToTable))
        self.timer.start(30)


