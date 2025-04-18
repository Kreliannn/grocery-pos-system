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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 663)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 270, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 350, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(80, 290, 351, 41))
        self.name.setObjectName("name")
        self.price = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(80, 370, 351, 41))
        self.price.setObjectName("price")
        self.camera = QtWidgets.QLabel(parent=self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(80, 90, 351, 131))
        self.camera.setStyleSheet("""
            background: whitesmoke;
            font-size: 24px;
            color: black;
            qproperty-alignment: 'AlignCenter';
        """)
        self.camera.setText("loading......")
        self.camera.setObjectName("camera")


        utils.delayCameraLoad(self.startCamera, 100, MainWindow)

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 70, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 230, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stocks = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.stocks.setGeometry(QtCore.QRect(80, 530, 351, 41))
        self.stocks.setObjectName("stocks")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 510, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.fileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(80, 450, 351, 41))
        self.fileButton.setObjectName("fileButton")

        self.fileButton.clicked.connect(lambda: self.open_file_dialog(MainWindow))

        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 430, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.fileName = QtWidgets.QLabel(parent=self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(140, 430, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.fileName.setFont(font)
        self.fileName.setObjectName("fileName")
        self.barcodeName = QtWidgets.QLabel(parent=self.centralwidget)
        self.barcodeName.setGeometry(QtCore.QRect(170, 230, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.barcodeName.setFont(font)
        self.barcodeName.setObjectName("barcodeName")
        self.addProductButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addProductButton.setGeometry(QtCore.QRect(80, 590, 351, 51))

        self.addProductButton.clicked.connect(self.addProduct)

        self.fileName.setStyleSheet("color: red; font-weight: normal;")
        self.barcodeName.setStyleSheet("color: red; font-weight: normal;")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.addProductButton.setFont(font)
        self.addProductButton.setStyleSheet("BACKGROUND: GREEN; COLOR :WHITE")
        self.addProductButton.setObjectName("addProductButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addProduct(self):
        name = self.name.text()
        price = self.price.text()
        barcode = self.barcodeName.text()
        stocks = self.stocks.text()
        image = self.fileName.text()

        if not name or not price or barcode == "NO SELECTED BARCODE" or not stocks or image == "NO SELECTED IMAGE":
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
        
        utils.alertSuccess("Product added successfully.")
        self.reset()
     
    def saveBarcode(self, barcode_data):
        self.barcodeName.setText(barcode_data)
        self.barcodeName.setStyleSheet("color: green; font-weight: bold;")

    
    def open_file_dialog(self, MainWindow):
          file_path, _ = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
          if file_path:
            upload_folder = os.path.join(os.getcwd(), 'frontend/img')
            os.makedirs(upload_folder, exist_ok=True) 

            file_name = os.path.basename(file_path)
            destination = os.path.join(upload_folder, file_name)

            shutil.copy(file_path, destination)
            print(f"File saved to: {destination}")

            self.fileName.setText(file_name)
            self.fileName.setStyleSheet("color: green; font-weight: bold;")

    def reset(self):
        self.name.setText("")
        self.price.setText("")
        self.barcodeName.setText("NO SELECTED BARCODE")
        self.barcodeName.setStyleSheet("color: black; font-weight: normal;")
        self.stocks.setText("")
        self.fileName.setText("NO SELECTED IMAGE")
        self.fileName.setStyleSheet("color: black; font-weight: normal;")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "ADD PRODUCT"))
        self.label_2.setText(_translate("MainWindow", "PRODUCT NAME:"))
        self.label_3.setText(_translate("MainWindow", "PRODUCT PRICE:"))
        self.label_5.setText(_translate("MainWindow", "SCAN PRODUCT BARCODE:"))
        self.label_6.setText(_translate("MainWindow", "BARCODE: "))
        self.label_7.setText(_translate("MainWindow", "PRODUCT INITIAL STOCKS:"))
        self.fileButton.setText(_translate("MainWindow", "OPEN FILE"))
        self.label_8.setText(_translate("MainWindow", "IMAGE: "))
        self.fileName.setText(_translate("MainWindow", "NO SELECTED IMAGE"))
        self.barcodeName.setText(_translate("MainWindow", "NO SELECTED BARCODE"))
        self.addProductButton.setText(_translate("MainWindow", "ADD PRODUCT"))

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

