from PyQt6 import QtCore, QtWidgets
from backend.product import Product

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
        self.scrollArea.setGeometry(QtCore.QRect(50, 60, 00, 450))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaContent = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollAreaContent)

        # Grid layout for cards
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaContent)

        myProduct = Product()

        products = myProduct.getProducts()

        # Add multiple mock product cards
        for product in products:
            card = self.createProductCard(product['name'], product['price'], product['price'], product['stocks'], product['image'] )
       

    def createProductCard(self, name, category, price, stocks, image):
        card = QtWidgets.QWidget()
        card.setFixedSize(200, 400)
        card.setStyleSheet("background: whitesmoke; border-radius: 8px;")

        # Image
        image = QtWidgets.QLabel(parent=card)
        image.setGeometry(QtCore.QRect(0, 0, 200, 150))
        image.setStyleSheet("background: gray; border-top-left-radius: 8px; border-top-right-radius: 8px;")

        # Name
        label_name = QtWidgets.QLabel("name", parent=card)
        label_name.setGeometry(QtCore.QRect(10, 160, 49, 16))
        input_name = QtWidgets.QLineEdit(name, parent=card)
        input_name.setGeometry(QtCore.QRect(10, 180, 180, 22))
        input_name.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")  # Added border

      
        # Price
        label_price = QtWidgets.QLabel("price", parent=card)
        label_price.setGeometry(QtCore.QRect(10, 260, 60, 16))
        input_price = QtWidgets.QLineEdit(price, parent=card)
        input_price.setGeometry(QtCore.QRect(10, 280, 180, 22))
        input_price.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")  # Added border

        # Stocks
        label_stocks = QtWidgets.QLabel("stocks", parent=card)
        label_stocks.setGeometry(QtCore.QRect(10, 310, 60, 16))
        input_stocks = QtWidgets.QLineEdit(stocks, parent=card)
        input_stocks.setGeometry(QtCore.QRect(10, 330, 180, 22))
        input_stocks.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")  # Added border

        # Button
        button = QtWidgets.QPushButton("save changes", parent=card)
        button.setGeometry(QtCore.QRect(10, 360, 180, 30))
        button.setStyleSheet("background: green; color: white; border-radius: 5px;")

        return card
