import sys
import cv2
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QInputDialog
from backend.utils.util import utils
from backend.product import Product
from backend.transaction import Transaction
from backend.soldProduct import SoldProduct
from datetime import date





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 576)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 361, 371))
        self.widget.setStyleSheet("background-color:  whitesmoke\n""")
        self.widget.setObjectName("widget")


        self.recipt = {}

        self.myProduct = Product()
        self.mySoldProduct = SoldProduct()
        self.myTransaction = Transaction()

        self.cart = []

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
        self.tableWidget.setGeometry(QtCore.QRect(380, 80, 411, 325))
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

        # Add "Delete Last Item" button below the table
        self.deleteLastBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteLastBtn.setGeometry(QtCore.QRect(380, 410, 411, 40))  # Adjust size/position as needed
        self.deleteLastBtn.setStyleSheet("background-color: red; color: white; font-size: 18px;")
        self.deleteLastBtn.setText("Delete Last Item")
        self.deleteLastBtn.clicked.connect(self.removeLastItem)


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

        self.pushButton_4.clicked.connect(self.proceedToPayment)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addToTable(self, barcode):
        product = self.myProduct.getProductByBarCode(barcode)
        if product:
            dialog = utils.askPopUp(self.mainWindow, "product quantity:", 1)
            ok = dialog.exec()
            qty = dialog.intValue() 

            if ok:
                total = qty * product['price']; 
                row_position = self.tableWidget.rowCount() 
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(product['name']))
                self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(qty)))
                self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(product['price'])))   
                self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(total)))
                
                self.cart.append({
                    "product_id" : product['product_id'],
                    "name" : product['name'],
                    "qty" : qty,
                    "total" : total
                })
                self.updateTotal()
        else:
             utils.alertError("not found")

  
    def updateTotal(self):
        total = self.getTotal()
        self.total.setText(str(total))

    def getTotal(self):
        total = 0
        for obj in self.cart:
            total = total + obj['total']
        return total

    def proceedToPayment(self):
        dialog = utils.askPopUp(self.mainWindow, "Enter Customer Payment: ")
        ok = dialog.exec()
        paymentVal = dialog.intValue() 

        if(paymentVal >= self.getTotal()):
            transactionId = utils.generateId()
            self.recipt = {
                "transaction_id" : transactionId,
                "date":  date.today(),
                "total": self.getTotal(),
                "payment": paymentVal,
                "customer_change": paymentVal - self.getTotal()
            }

            for cartItem in self.cart:
                item = {
                    "qty" : cartItem['qty'],
                    "product_id" : cartItem['product_id'],
                    "transaction_id" :  transactionId
                }
                self.mySoldProduct.addSoldProduct(item)

            self.myTransaction.addTransaction(self.recipt)
        else:
            utils.alertError("kulang")

    def removeLastItem(self):
        row_position = self.tableWidget.rowCount() - 1
        self.tableWidget.removeRow(row_position)
        self.cart.pop()
        self.updateTotal()

    
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


