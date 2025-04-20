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
from backend.notification import Notification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)  # Increased window size for better layout
        MainWindow.setStyleSheet("background-color: #f0f0f0;")
        
        # Create a central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # App title
        self.appTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(10, 10, 980, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        self.appTitle.setFont(font)
        self.appTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.appTitle.setText("POS System")
        self.appTitle.setStyleSheet("color: #2c3e50; background-color: #ecf0f1; border-radius: 10px; padding: 5px;")
        
        # Camera widget with rounded corners and shadow
        self.cameraWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.cameraWidget.setGeometry(QtCore.QRect(20, 80, 460, 400))
        self.cameraWidget.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 15px;
            border: 2px solid #bdc3c7;
        """)
        
        # Camera label with title
        self.cameraTitle = QtWidgets.QLabel(parent=self.cameraWidget)
        self.cameraTitle.setGeometry(QtCore.QRect(0, 5, 460, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.cameraTitle.setFont(font)
        self.cameraTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cameraTitle.setText("Barcode Scanner")
        self.cameraTitle.setStyleSheet("color: #2c3e50; background: transparent;")
        
        # Camera view
        self.camera = QtWidgets.QLabel(parent=self.cameraWidget)
        self.camera.setGeometry(QtCore.QRect(10, 40, 440, 350))
        self.camera.setStyleSheet("""
            background: #f5f5f5;
            font-size: 24px;
            color: #7f8c8d;
            qproperty-alignment: 'AlignCenter';
            border-radius: 10px;
        """)
        self.camera.setText("Loading camera...")
        self.camera.setObjectName("camera")
        
        # Cart table with better styling
        self.cartWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.cartWidget.setGeometry(QtCore.QRect(500, 80, 480, 400))
        self.cartWidget.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 15px;
            border: 2px solid #bdc3c7;
        """)
        
        # Cart title
        self.cartTitle = QtWidgets.QLabel(parent=self.cartWidget)
        self.cartTitle.setGeometry(QtCore.QRect(0, 5, 480, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.cartTitle.setFont(font)
        self.cartTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cartTitle.setText("Shopping Cart")
        self.cartTitle.setStyleSheet("color: #2c3e50; background: transparent;")
        
        # Product table
        self.tableWidget = QtWidgets.QTableWidget(parent=self.cartWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 460, 310))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                gridline-color: #d0d0d0;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                padding: 6px;
                border: none;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #cce5ff;
            }
        """)
        
        # Set column headers
        headers = ["Product", "Qty", "Price", "Total"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem(header)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        
        # Set column widths
        self.tableWidget.setColumnWidth(0, 180)  # Product name (wider)
        self.tableWidget.setColumnWidth(1, 60)   # Quantity
        self.tableWidget.setColumnWidth(2, 90)   # Price
        self.tableWidget.setColumnWidth(3, 110)  # Total
        
        # Delete last item button
        self.deleteLastBtn = QtWidgets.QPushButton(parent=self.cartWidget)
        self.deleteLastBtn.setGeometry(QtCore.QRect(10, 355, 460, 35))
        self.deleteLastBtn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        self.deleteLastBtn.setText("Delete Last Item")
        self.deleteLastBtn.clicked.connect(self.removeLastItem)
        
        # Total and payment panel
        self.checkoutPanel = QtWidgets.QWidget(parent=self.centralwidget)
        self.checkoutPanel.setGeometry(QtCore.QRect(20, 500, 960, 120))
        self.checkoutPanel.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 15px;
            border: 2px solid #bdc3c7;
        """)
        
        # Total label
        self.totalLabel = QtWidgets.QLabel(parent=self.checkoutPanel)
        self.totalLabel.setGeometry(QtCore.QRect(20, 20, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        self.totalLabel.setFont(font)
        self.totalLabel.setText("TOTAL:")
        self.totalLabel.setStyleSheet("color: #2c3e50;")
        
        # Total amount
        self.total = QtWidgets.QLabel(parent=self.checkoutPanel)
        self.total.setGeometry(QtCore.QRect(180, 20, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        self.total.setFont(font)
        self.total.setText("0")
        self.total.setStyleSheet("color: #16a085;")
        
        # Pay button
        self.payButton = QtWidgets.QPushButton(parent=self.checkoutPanel)
        self.payButton.setGeometry(QtCore.QRect(650, 20, 290, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        self.payButton.setFont(font)
        self.payButton.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #16a085;
            }
        """)
        self.payButton.setText("PAY")
        self.payButton.clicked.connect(self.proceedToPayment)
        
        # Home button (keeping only this button as requested)
        self.homeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(20, 640, 960, 40))
        self.homeButton.setText("Home")
        self.homeButton.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet("background-color: #ecf0f1; color: #34495e;")
        
        # Initialize receipts and cart
        self.recipt = {}
        self.myProduct = Product()
        self.mySoldProduct = SoldProduct()
        self.myTransaction = Transaction()
        self.cart = []
        
        # Start camera with delay
        utils.delayCameraLoad(self.startCamera, 100, MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addToTable(self, barcode):
        product = self.myProduct.getProductByBarCode(barcode)
     
        if product:
            if product['stocks'] <= 0:
                utils.alertError("Product Out Of Stock")
                return
        
            dialog = utils.askPopUp(self.mainWindow, "Product Quantity:", 1)
            ok = dialog.exec()
            qty = dialog.intValue() 

            if qty > product['stocks']:
                utils.alertError("Invalid quantity. The current stock of product is " + str(product['stocks']))
                return
            
            if ok:
                total = qty * product['price']
                row_position = self.tableWidget.rowCount() 
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(product['name']))
                self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(qty)))
                self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(product['price'])))   
                self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(total)))
                
                self.cart.append({
                    "product_id": product['product_id'],
                    "name": product['name'],
                    "qty": qty,
                    "total": total
                })
                self.updateTotal()
        else:
             utils.alertError("Product not found")

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
                "transaction_id": transactionId,
                "date": date.today(),
                "total": self.getTotal(),
                "payment": paymentVal,
                "customer_change": paymentVal - self.getTotal()
            }

            for cartItem in self.cart:
                item = {
                    "qty": cartItem['qty'],
                    "product_id": cartItem['product_id'],
                    "transaction_id": transactionId
                }
                self.mySoldProduct.addSoldProduct(item)
                if(self.myProduct.deductStocks(cartItem['product_id'], cartItem['qty'])):
                        product = self.myProduct.getProduct(cartItem['product_id'])
                        myNotification = Notification()
                        myNotification.addNotifications({
                            "header": "Out Of Stock",
                            "message": "Product: " + product['name'],
                            "icon": "warning"
                        })
            
            self.myTransaction.addTransaction(self.recipt)
            self.transaction_id = transactionId
        else:
            utils.alertError("Insufficient Payment")

    def removeLastItem(self):
        row_count = self.tableWidget.rowCount()
        if row_count > 0:
            row_position = row_count - 1
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

