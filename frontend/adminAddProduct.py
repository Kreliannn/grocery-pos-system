import sys
import cv2
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from backend.utils.util import utils
from PyQt6.QtWidgets import QFileDialog
import shutil
import os
from backend.utils.util import utils
from backend.product import Product
from backend.notification import Notification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 750)  # Increased size for better layout
        MainWindow.setStyleSheet("background-color: #f5f5f5;")
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Header area with app title
        self.headerFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.headerFrame.setStyleSheet("background-color: #3498db;")
        
        # Home button with improved styling
        self.pushButton = QtWidgets.QPushButton(parent=self.headerFrame)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2c3e50;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #ecf0f1;
            }
            QPushButton:pressed {
                background-color: #bdc3c7;
            }
        """)
        self.pushButton.setObjectName("pushButton")
        
        # Page title with better positioning and styling
        self.label = QtWidgets.QLabel(parent=self.headerFrame)
        self.label.setGeometry(QtCore.QRect(300, 15, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        
        # Main content container
        self.contentFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.contentFrame.setGeometry(QtCore.QRect(25, 85, 750, 650))
        self.contentFrame.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
        """)
        
        # Camera section with better styling
        self.cameraSection = QtWidgets.QFrame(parent=self.contentFrame)
        self.cameraSection.setGeometry(QtCore.QRect(20, 20, 710, 200))
        self.cameraSection.setStyleSheet("""
            background-color: #f9f9f9;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
        """)
        
        # Camera label
        self.label_5 = QtWidgets.QLabel(parent=self.cameraSection)
        self.label_5.setGeometry(QtCore.QRect(15, 10, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #2c3e50; border: none; background: transparent;")
        self.label_5.setObjectName("label_5")
        
        # Camera feed
        self.camera = QtWidgets.QLabel(parent=self.cameraSection)
        self.camera.setGeometry(QtCore.QRect(15, 45, 680, 140))
        self.camera.setStyleSheet("""
            background: #f0f0f0;
            font-size: 24px;
            color: #7f8c8d;
            qproperty-alignment: 'AlignCenter';
            border-radius: 5px;
            border: 1px solid #dcdde1;
        """)
        self.camera.setText("Loading camera...")
        self.camera.setObjectName("camera")
        
        # Barcode result section
        self.label_6 = QtWidgets.QLabel(parent=self.contentFrame)
        self.label_6.setGeometry(QtCore.QRect(35, 230, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #2c3e50; background: transparent;")
        self.label_6.setObjectName("label_6")
        
        self.barcodeName = QtWidgets.QLabel(parent=self.contentFrame)
        self.barcodeName.setGeometry(QtCore.QRect(135, 230, 595, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.barcodeName.setFont(font)
        self.barcodeName.setObjectName("barcodeName")
        self.barcodeName.setStyleSheet("color: #e74c3c; padding-left: 5px;")




        # Define smaller font for labels
        small_font = QtGui.QFont()
        small_font.setPointSize(10)


        self.formSection = QtWidgets.QFrame(parent=self.contentFrame)
        self.formSection.setGeometry(QtCore.QRect(20, 270, 710, 370))  # increased height
        self.formSection.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)

        # Form layout using vertical layout
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.formSection)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 710, 370))
        self.formLayout = QtWidgets.QVBoxLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(8)

        input_style = """
            QLineEdit {
                border: none;
                padding: 3px;
                background-color: #fff;
                border-bottom: 1px solid #ccc;
            }
        """

        # Product Name
        self.label_2 = QtWidgets.QLabel("Product Name")
        self.label_2.setFont(small_font)
        self.label_2.setStyleSheet("color: #2c3e50;")
        self.name = QtWidgets.QLineEdit()
        self.name.setFont(small_font)
        self.name.setPlaceholderText("Enter product name")
        self.name.setStyleSheet(input_style)
        self.formLayout.addWidget(self.label_2)
        self.formLayout.addWidget(self.name)

        # Price
        self.label_3 = QtWidgets.QLabel("Price")
        self.label_3.setFont(small_font)
        self.label_3.setStyleSheet("color: #2c3e50;")
        self.price = QtWidgets.QLineEdit()
        self.price.setFont(small_font)
        self.price.setPlaceholderText("Enter price")
        self.price.setStyleSheet(input_style)
        self.formLayout.addWidget(self.label_3)
        self.formLayout.addWidget(self.price)

        # Stocks
        self.label_7 = QtWidgets.QLabel("Stocks")
        self.label_7.setFont(small_font)
        self.label_7.setStyleSheet("color: #2c3e50;")
        self.stocks = QtWidgets.QLineEdit()
        self.stocks.setFont(small_font)
        self.stocks.setPlaceholderText("Enter stock quantity")
        self.stocks.setStyleSheet(input_style)
        self.formLayout.addWidget(self.label_7)
        self.formLayout.addWidget(self.stocks)

        # File label and filename
        self.label_8 = QtWidgets.QLabel("Image")
        self.label_8.setFont(small_font)
        self.label_8.setStyleSheet("color: #2c3e50;")
        self.formLayout.addWidget(self.label_8)

        self.fileName = QtWidgets.QLabel("No file chosen")
        self.fileName.setFont(QtGui.QFont("Arial", 10))
        self.fileName.setStyleSheet("color: #e74c3c; padding-left: 5px;")
        self.formLayout.addWidget(self.fileName)

        # File Button
        self.fileButton = QtWidgets.QPushButton("Upload Image")
        self.fileButton.setFont(small_font)
        self.fileButton.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.formLayout.addWidget(self.fileButton)

        # Add product button (inside the form now)
        self.addProductButton = QtWidgets.QPushButton("Add Product")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.addProductButton.setFont(font)
        self.addProductButton.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 6px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        self.addProductButton.setObjectName("addProductButton")
        self.addProductButton.clicked.connect(self.addProduct)
        self.formLayout.addWidget(self.addProductButton)

                
        # Add product button
        self.addProductButton = QtWidgets.QPushButton(parent=self.contentFrame)
        self.addProductButton.setGeometry(QtCore.QRect(20, 630, 710, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.addProductButton.setFont(font)
        self.addProductButton.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #219653;
            }
        """)
        self.addProductButton.setObjectName("addProductButton")
        self.addProductButton.clicked.connect(self.addProduct)

        self.fileButton.clicked.connect(lambda: self.open_file_dialog(MainWindow))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setStyleSheet("background-color: #ecf0f1;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.stopCamera)
        self.pushButton.clicked.connect(MainWindow.showAdminDashboard)
        
        self.newFileName = ""
        utils.delayCameraLoad(self.startCamera, 100, MainWindow)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addProduct(self):
        name = self.name.text()
        price = self.price.text()
        barcode = self.barcodeName.text()
        stocks = self.stocks.text()
        image = self.newFileName

        if not name or not price or barcode == "NO SELECTED BARCODE" or not stocks or not image:
            utils.alertError("Please fill in all fields.")
            return
        
        myProduct = Product()

        myProduct.addProduct({
            "name": name,
            "barcode": barcode,
            "price": price,
            "image": image,
            "stocks": stocks
        })

        myNotification = Notification()
        myNotification.addNotifications({
            "header": "Add Product",
            "message": "Product: " + name,
            "icon": "success"
        })
        
        utils.alertSuccess("Product added successfully.")
        self.reset()
     
    def saveBarcode(self, barcode_data):
        utils.alertSuccess("Barcode detected")
        self.barcodeName.setText(barcode_data)
        self.barcodeName.setStyleSheet("color: #27ae60; font-weight: bold; padding-left: 5px;")
    
    def open_file_dialog(self, MainWindow):
        file_path, _ = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            upload_folder = os.path.join(os.getcwd(), 'frontend/product_img')
            os.makedirs(upload_folder, exist_ok=True) 

            file_name = os.path.basename(file_path)
            ext = os.path.splitext(file_path)[1] 
            new_file_name = utils.generateId() + ext
            destination = os.path.join(upload_folder, new_file_name)

            shutil.copy(file_path, destination)
            print(f"File saved to: {destination}")

            self.newFileName = new_file_name

            self.fileName.setText(file_name)
            self.fileName.setStyleSheet("color: #27ae60; font-weight: bold; padding-left: 5px;")

    def reset(self):
        self.name.setText("")
        self.price.setText("")
        self.barcodeName.setText("NO SELECTED BARCODE")
        self.barcodeName.setStyleSheet("color: #e74c3c; padding-left: 5px;")
        self.stocks.setText("")
        self.fileName.setText("NO SELECTED IMAGE")
        self.fileName.setStyleSheet("color: #e74c3c; padding-left: 5px;")

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

    def stopCamera(self):
        self.cap.release() 

    def startCamera(self, MainWindow):
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(lambda: utils.scanBarCodeAndUpdateFrame(self.cap, self.camera, self.saveBarcode))
        self.timer.start(30)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Product Management"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "ADD PRODUCT"))
        self.label_2.setText(_translate("MainWindow", "PRODUCT NAME:"))
        self.label_3.setText(_translate("MainWindow", "PRODUCT PRICE:"))
        self.label_5.setText(_translate("MainWindow", "SCAN PRODUCT BARCODE:"))
        self.label_6.setText(_translate("MainWindow", "BARCODE:"))
        self.label_7.setText(_translate("MainWindow", "PRODUCT INITIAL STOCKS:"))
        self.fileButton.setText(_translate("MainWindow", "SELECT PRODUCT IMAGE"))
        self.label_8.setText(_translate("MainWindow", "IMAGE:"))
        self.fileName.setText(_translate("MainWindow", "NO SELECTED IMAGE"))
        self.barcodeName.setText(_translate("MainWindow", "NO SELECTED BARCODE"))
        self.addProductButton.setText(_translate("MainWindow", "ADD PRODUCT"))