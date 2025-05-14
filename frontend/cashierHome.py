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
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("""
            background-color: #F8FAFC;
            font-family: 'Segoe UI', Arial, sans-serif;
        """)
        
        # Create a central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # App title with enhanced styling
        self.appTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(10, 10, 980, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        self.appTitle.setFont(font)
        self.appTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.appTitle.setText("POS System")
        self.appTitle.setStyleSheet("""
            color: #1E3A8A; 
            background-color: #FFFFFF; 
            border-radius: 10px; 
            padding: 5px;
            border: 1px solid #CBD5E1;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
        """)
        
        # Camera widget with enhanced styling
        self.cameraWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.cameraWidget.setGeometry(QtCore.QRect(20, 80, 460, 400))
        self.cameraWidget.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 12px;
            border: 1px solid #CBD5E1;
        """)
        
        # Camera label with title
        self.cameraTitle = QtWidgets.QLabel(parent=self.cameraWidget)
        self.cameraTitle.setGeometry(QtCore.QRect(0, 10, 460, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.cameraTitle.setFont(font)
        self.cameraTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cameraTitle.setText("Barcode Scanner")
        self.cameraTitle.setStyleSheet("color: #1E3A8A; background: transparent;")
        
        # Camera view with better styling
        self.camera = QtWidgets.QLabel(parent=self.cameraWidget)
        self.camera.setGeometry(QtCore.QRect(15, 45, 430, 340))
        self.camera.setStyleSheet("""
            background: #F1F5F9;
            font-size: 18px;
            color: #64748B;
            qproperty-alignment: 'AlignCenter';
            border-radius: 8px;
            border: 1px dashed #CBD5E1;
        """)
        self.camera.setText("Loading camera...")
        self.camera.setObjectName("camera")
        
        # Cart widget with enhanced styling
        self.cartWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.cartWidget.setGeometry(QtCore.QRect(500, 80, 480, 400))
        self.cartWidget.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 12px;
            border: 1px solid #CBD5E1;
        """)
        
        # Cart title with better font
        self.cartTitle = QtWidgets.QLabel(parent=self.cartWidget)
        self.cartTitle.setGeometry(QtCore.QRect(0, 10, 480, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.cartTitle.setFont(font)
        self.cartTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cartTitle.setText("Grocery Cart")
        self.cartTitle.setStyleSheet("color: #1E3A8A; background: transparent;")
        
        # Product table with theme-based styling
        self.tableWidget = QtWidgets.QTableWidget(parent=self.cartWidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 45, 450, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                gridline-color: #CBD5E1;
                border-radius: 8px;
                border: 1px solid #CBD5E1;
            }
            QHeaderView::section {
                background-color: #2563EB;
                color: white;
                font-weight: bold;
                padding: 8px;
                border: none;
            }
            QTableWidget::item {
                padding: 6px;
                color: #1E3A8A;
            }
            QTableWidget::item:selected {
                background-color: #E0F2FE;
                color: #1E3A8A;
            }
            QScrollBar:vertical {
                border: none;
                background: #F1F5F9;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #CBD5E1;
                border-radius: 5px;
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
        self.tableWidget.setColumnWidth(3, 100)  # Total
        
        # Delete last item button with theme styling
        self.deleteLastBtn = QtWidgets.QPushButton(parent=self.cartWidget)
        self.deleteLastBtn.setGeometry(QtCore.QRect(15, 355, 450, 35))
        self.deleteLastBtn.setStyleSheet("""
            QPushButton {
                background-color: #F1F5F9;
                color: #1E3A8A;
                font-size: 13px;
                font-weight: bold;
                border-radius: 6px;
                padding: 5px;
                border: 1px solid #CBD5E1;
            }
            QPushButton:hover {
                background-color: #E0F2FE;
            }
            QPushButton:pressed {
                background-color: #CBD5E1;
            }
        """)
        self.deleteLastBtn.setText("Delete Last Item")
        self.deleteLastBtn.clicked.connect(self.removeLastItem)
        
        # Total and payment panel with enhanced styling
        self.checkoutPanel = QtWidgets.QWidget(parent=self.centralwidget)
        self.checkoutPanel.setGeometry(QtCore.QRect(20, 500, 960, 120))
        self.checkoutPanel.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 12px;
       
        """)
        
        # Total label with theme-based styling
        self.totalLabel = QtWidgets.QLabel(parent=self.checkoutPanel)
        self.totalLabel.setGeometry(QtCore.QRect(20, 20, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        self.totalLabel.setFont(font)
        self.totalLabel.setText("TOTAL:")
        self.totalLabel.setStyleSheet("color: #1E3A8A;")
        
        # Total amount with theme color
        self.total = QtWidgets.QLabel(parent=self.checkoutPanel)
        self.total.setGeometry(QtCore.QRect(180, 20, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        self.total.setFont(font)
        self.total.setText("0")
        self.total.setStyleSheet("color: #2563EB;")
        
        # Total currency label (new component)
        self.currencyLabel = QtWidgets.QLabel(parent=self.checkoutPanel)
        self.currencyLabel.setGeometry(QtCore.QRect(150, 20, 30, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        self.currencyLabel.setFont(font)
        self.currencyLabel.setText("₱")
        self.currencyLabel.setStyleSheet("color: #64748B;")
        
        # Pay button with theme colors
        self.payButton = QtWidgets.QPushButton(parent=self.checkoutPanel)
        self.payButton.setGeometry(QtCore.QRect(650, 20, 290, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        self.payButton.setFont(font)
        self.payButton.setStyleSheet("""
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QPushButton:pressed {
                background-color: #1E3A8A;
            }
        """)
        self.payButton.setText("PAY")
        self.payButton.clicked.connect(self.proceedToPayment)
        
        # Home button with theme styling
        self.homeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(20, 640, 960, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.homeButton.setFont(font)
        self.homeButton.setText("Home")
        self.homeButton.setStyleSheet("""
            QPushButton {
                background-color: #38BDF8;
                color: white;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #0EA5E9;
            }
            QPushButton:pressed {
                background-color: #0284C7;
            }
        """)
        
        # Cart count badge (new component)
        self.cartCountBadge = QtWidgets.QLabel(parent=self.cartWidget)
        self.cartCountBadge.setGeometry(QtCore.QRect(430, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.cartCountBadge.setFont(font)
        self.cartCountBadge.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cartCountBadge.setText("0")
        self.cartCountBadge.setStyleSheet("""
            background-color: #2563EB;
            color: white;
            border-radius: 15px;
        """)
        
        # Add status bar with better styling
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet("background-color: #F1F5F9; color: #64748B;")
        self.statusbar.showMessage("Ready")
        
        # Initialize receipts and cart
        self.recipt = {}
        self.myProduct = Product()
        self.mySoldProduct = SoldProduct()
        self.myTransaction = Transaction()
        self.cart = []

        self.homeButton.clicked.connect(self.stopCamera)
        self.homeButton.clicked.connect(MainWindow.showCashier)
        self.payButton.clicked.connect(self.stopCamera)
       
        
        self.tableWidget.verticalHeader().setVisible(False)


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
                self.updateCartCount()  # Update the cart count badge
                self.statusbar.showMessage(f"Added {product['name']} to cart")
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
        
    def updateCartCount(self):
        # Update the cart count badge
        self.cartCountBadge.setText(str(len(self.cart)))

    def proceedToPayment(self):
        if len(self.cart) == 0:
            utils.alertError("Cart is empty")
            return
            
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
            self.statusbar.showMessage(f"Payment successful. Transaction ID: {transactionId}")
            self.mainWindow.showCashierReciept(transactionId)    
            utils.alertError("Insufficient Payment")

    def removeLastItem(self):
        row_count = self.tableWidget.rowCount()
        if row_count > 0:
            row_position = row_count - 1
            removed_item = self.cart[row_position]["name"]
            self.tableWidget.removeRow(row_position)
            self.cart.pop()
            self.updateTotal()
            self.updateCartCount()  # Update the cart count
            self.statusbar.showMessage(f"Removed {removed_item} from cart")
    
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
        self.statusbar.showMessage("Camera activated. Ready to scan barcodes.")