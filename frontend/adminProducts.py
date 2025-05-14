from PyQt6 import QtCore, QtWidgets
from backend.product import Product
from PyQt6.QtGui import QPixmap
from backend.utils.util import utils
from backend.product import Product
from backend.notification import Notification

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.mainWindow = MainWindow
        # Apply global styles
        MainWindow.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 14px;
                background-color: #F8FAFC;
                color: #1E3A8A;
            }
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 5px;
                padding: 8px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #F1F5F9;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #CBD5E1;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #64748B;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar:horizontal {
                border: none;
                background-color: #F1F5F9;
                height: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:horizontal {
                background-color: #CBD5E1;
                border-radius: 5px;
            }
            QScrollBar::handle:horizontal:hover {
                background-color: #64748B;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
        """)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Vertical layout for the central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)

        # Header container
        self.headerContainer = QtWidgets.QWidget(parent=self.centralwidget)
        self.headerContainer.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 8px;
        """)
        self.headerLayout = QtWidgets.QHBoxLayout(self.headerContainer)
        self.headerLayout.setContentsMargins(15, 15, 15, 15)
        
        # Page title
        self.pageTitle = QtWidgets.QLabel("Products", parent=self.headerContainer)
        self.pageTitle.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        
        # Home button
        self.homeButton = QtWidgets.QPushButton("Home", parent=self.headerContainer)
        self.homeButton.setFixedSize(100, 40)
        self.homeButton.setStyleSheet("""
            background-color: #2563EB;
            color: white;
            border-radius: 5px;
            font-weight: bold;
        """)
        
        self.headerLayout.addWidget(self.pageTitle)
        self.headerLayout.addStretch()
        self.headerLayout.addWidget(self.homeButton)
        
        self.verticalLayout.addWidget(self.headerContainer)

        # Scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background: transparent; border: none;")
        self.verticalLayout.addWidget(self.scrollArea)

        self.scrollAreaContent = QtWidgets.QWidget()
        self.scrollAreaContent.setStyleSheet("background: transparent;")
        self.scrollArea.setWidget(self.scrollAreaContent)

        # Grid layout for cards
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaContent)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)

        self.homeButton.clicked.connect(MainWindow.showAdminDashboard)

        self.myProduct = Product()
        products = self.myProduct.getProducts()

        # Add product cards to grid layout
        for i, product in enumerate(products):
            card = self.createProductCard(
                product['product_id'],
                product['name'],
                product['price'],
                product['stocks'],
                product['image']
            )
            row = i // 3  # 3 cards per row
            col = i % 3
            self.gridLayout.addWidget(card, row, col)

    def createProductCard(self, id, name, price, stocks, image):
        # Product information to store for button clicks
        product_info = {
            'id': id,
            'name': name,
            'price': price,
            'stocks': stocks
        }
        
        card = QtWidgets.QWidget()
        card.setFixedSize(230, 280)
        card.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 12px;
        """)

        # Product name label (visible at top of card)
        name_label = QtWidgets.QLabel(name, parent=card)
        name_label.setGeometry(QtCore.QRect(15, 15, 200, 20))
        name_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        # Image container with styling
        image_container = QtWidgets.QWidget(parent=card)
        image_container.setGeometry(QtCore.QRect(15, 45, 200, 150))
        image_container.setStyleSheet("""
            background-color: #F1F5F9;
            border-radius: 8px;
        """)
        
        # Image
        image_label = QtWidgets.QLabel(parent=image_container)
        image_label.setGeometry(QtCore.QRect(0, 0, 200, 150))
        image_label.setStyleSheet("border-radius: 8px;")

        # Load image from path
        pixmap = QPixmap("frontend/product_img/" + image)
        scaled_pixmap = pixmap.scaled(200, 150, QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
                                     QtCore.Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setScaledContents(True)
        
        # Price and stocks info
        info_label = QtWidgets.QLabel(f"₱{price} \t\t {stocks} in stock", parent=card)
        info_label.setGeometry(QtCore.QRect(15, 205, 200, 20))
        info_label.setStyleSheet("""
            color: #64748B;
            font-size: 14px;
        """)
        
        # Buttons container
        button_container = QtWidgets.QWidget(parent=card)
        button_container.setGeometry(QtCore.QRect(15, 230, 200, 40))
        
        # Button layout
        button_layout = QtWidgets.QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)
        
        # Edit button
        edit_button = QtWidgets.QPushButton("Edit", parent=button_container)
        edit_button.setStyleSheet("""
            background-color: #38BDF8;
            color: white;
            border-radius: 5px;
            font-weight: bold;
            padding: 5px;
        """)
        
        # Delete button
        delete_button = QtWidgets.QPushButton("Delete", parent=button_container)
        delete_button.setStyleSheet("""
            background-color: #EF4444;
            color: white;
            border-radius: 5px;
            font-weight: bold;
            padding: 5px;
        """)
        
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        
        # Connect buttons to functions
        edit_button.clicked.connect(lambda: self.editProduct(product_info))
        delete_button.clicked.connect(lambda: self.deleteProduct(product_info))

        return card
        
    def editProduct(self, product):
        print(f"Edit product: {product}")
        self.mainWindow.showAdminEditProducts(product)
        
    def deleteProduct(self, product):
        print(f"Delete product: {product}")
    
   


