from PyQt6 import QtCore, QtWidgets
from backend.product import Product
from PyQt6.QtGui import QPixmap
from backend.utils.util import utils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Scroll area
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 60, 700, 450))  # Fixed width
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaContent = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollAreaContent)

        # Grid layout for cards
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaContent)

        myProduct = Product()
        products = myProduct.getProducts()

        # Add product cards to grid layout
        for i, product in enumerate(products):
            card = self.createProductCard(
                product['name'],
                product['price'],
                product['stocks'],
                product['image']
            )
            row = i // 3  # 3 cards per row
            col = i % 3
            self.gridLayout.addWidget(card, row, col)

    def createProductCard(self, name, price, stocks, image):
        card = QtWidgets.QWidget()
        card.setFixedSize(200, 350)
        card.setStyleSheet("background: whitesmoke; border-radius: 8px; ")

        # Image
        image_label = QtWidgets.QLabel(parent=card)
        image_label.setGeometry(QtCore.QRect(0, 0, 200, 150))
        image_label.setStyleSheet("border-top-left-radius: 8px; border-top-right-radius: 8px;")

        # Load image from path
        pixmap = QPixmap("frontend/img/" + image)
        scaled_pixmap = pixmap.scaled(200, 150, QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding, QtCore.Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setScaledContents(True)

        # Name
        label_name = QtWidgets.QLabel("name", parent=card)
        label_name.setGeometry(QtCore.QRect(10, 160, 49, 16))
        input_name = QtWidgets.QLineEdit(name, parent=card)
        input_name.setGeometry(QtCore.QRect(10, 180, 180, 22))
        input_name.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")

        # Price
        label_price = QtWidgets.QLabel("price", parent=card)
        label_price.setGeometry(QtCore.QRect(10, 220, 60, 16))
        input_price = QtWidgets.QLineEdit(str(price), parent=card)
        input_price.setGeometry(QtCore.QRect(10, 240, 180, 22))
        input_price.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")

        # Stocks
        label_stocks = QtWidgets.QLabel("stocks", parent=card)
        label_stocks.setGeometry(QtCore.QRect(10, 270, 60, 16))
        input_stocks = QtWidgets.QLineEdit(str(stocks), parent=card)
        input_stocks.setGeometry(QtCore.QRect(10, 290, 180, 22))
        input_stocks.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")

        # Button
        button = QtWidgets.QPushButton("save changes", parent=card)
        button.setGeometry(QtCore.QRect(10, 330, 180, 30))
        button.setStyleSheet("background: green; color: white; border-radius: 5px;")

        button.clicked.connect(lambda : utils.alertSuccess(name))

        return card
    
    #def updateProduct(self, product):


