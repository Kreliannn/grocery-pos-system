from PyQt6 import QtCore, QtGui, QtWidgets
from backend.product import Product
from backend.soldProduct import SoldProduct
from backend.transaction import  Transaction

class Ui_MainWindow(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(900, 600)
        Dashboard.setStyleSheet("font-family: 'Segoe UI'; font-size: 12px;")

        self.centralwidget = QtWidgets.QWidget(parent=Dashboard)
        self.centralwidget.setObjectName("centralwidget")

        # Main layout
        self.main_layout = QtWidgets.QHBoxLayout(self.centralwidget)

        # Sidebar (was top navbar)
        self.sidebar = QtWidgets.QFrame()
        self.sidebar.setStyleSheet("background-color: #2c3e50; color: white;")
        self.sidebar.setFixedWidth(180)
        self.sidebar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)

        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 10, 10, 10)
        self.sidebar_layout.setSpacing(10)

        button_names = ["Add Product", "Products", "AI Assistant", "Sales Tracker", "Notification", "Receipt History", "Logout"]
        self.nav_buttons = []
        for name in button_names:
            btn = QtWidgets.QPushButton(name)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: whitesmoke;       /* Default background */
                    color: gray;                        /* Default text */
                    border: 1px solid #38BDF8;          /* Border */
                    border-radius: 6px;
                    padding: 10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #1D4ED8;          /* Hover background */
                    color: white;                       /* Hover text */
                }
            """)

            self.sidebar_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        self.sidebar_layout.addStretch()
        self.main_layout.addWidget(self.sidebar)

        # Info content
        self.info_frame = QtWidgets.QFrame()
        self.info_frame.setObjectName("info_frame")

        self.info_layout = QtWidgets.QGridLayout(self.info_frame)

        self.box_today_sales = QtWidgets.QGroupBox("Today Sales")
        self.box_today_sales.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")
        self.label_today_sales = QtWidgets.QLabel()
        self.label_today_sales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_today_sales.setStyleSheet("font-size: 24px; color: #2c3e50;")
        vbox = QtWidgets.QVBoxLayout(self.box_today_sales)
        vbox.addWidget(self.label_today_sales)

        self.box_overall_sales = QtWidgets.QGroupBox("Overall Sales")
        self.box_overall_sales.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")
        self.label_overall_sales = QtWidgets.QLabel()
        self.label_overall_sales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_overall_sales.setStyleSheet("font-size: 24px; color: #2c3e50;")
        vbox2 = QtWidgets.QVBoxLayout(self.box_overall_sales)
        vbox2.addWidget(self.label_overall_sales)

        self.box_product_count = QtWidgets.QGroupBox("Product Count")
        self.box_product_count.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")
        self.label_product_count = QtWidgets.QLabel()
        self.label_product_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_product_count.setStyleSheet("font-size: 24px; color: #2c3e50;")
        vbox3 = QtWidgets.QVBoxLayout(self.box_product_count)
        vbox3.addWidget(self.label_product_count)

        self.box_item_sold = QtWidgets.QGroupBox("Item Sold")
        self.box_item_sold.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")
        self.label_item_sold = QtWidgets.QLabel()
        self.label_item_sold.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_item_sold.setStyleSheet("font-size: 24px; color: #2c3e50;")
        vbox4 = QtWidgets.QVBoxLayout(self.box_item_sold)
        vbox4.addWidget(self.label_item_sold)

        self.info_layout.addWidget(self.box_today_sales, 0, 0)
        self.info_layout.addWidget(self.box_overall_sales, 0, 1)
        self.info_layout.addWidget(self.box_product_count, 1, 0)
        self.info_layout.addWidget(self.box_item_sold, 1, 1)

        self.main_layout.addWidget(self.info_frame)

        myProduct = Product()
        mySoldProduct = SoldProduct()
        myTransaction = Transaction()

        soldProductCount = mySoldProduct.getSoldProductCount()["sum(qty)"]
        totalSales = myTransaction.getTotalSales()["sum(total)"]
        todaySales = myTransaction.getTodaySales()["sum(total)"]
        productCount = len(myProduct.getProducts())

        self.label_today_sales.setText("₱" + str(todaySales))
        self.label_overall_sales.setText("₱" +  str(totalSales))
        self.label_product_count.setText(str(productCount))
        self.label_item_sold.setText(str(soldProductCount))

        
        self.nav_buttons[0].clicked.connect(Dashboard.showAdminAddProduct)
        self.nav_buttons[1].clicked.connect(Dashboard.showAdminProducts)
        self.nav_buttons[2].clicked.connect(Dashboard.showAdminAssistant)
        self.nav_buttons[3].clicked.connect(Dashboard.showAdminSalesTracker)
        self.nav_buttons[4].clicked.connect(Dashboard.showAdminNotification)
        self.nav_buttons[5].clicked.connect(Dashboard.showRecieptHistory)
        self.nav_buttons[6].clicked.connect(Dashboard.showLoginPage)

        self.sidebar.setStyleSheet("background-color: #38BDF8; color: white;")  # Primary Blue
        btn.setStyleSheet("""
            QPushButton {
                background-color: whitesmoke;        /* Sky Blue */
                color: #64748B;                   /* Navy Blue text */
                border: 1px solid #38BDF8;        /* Slate Blue border */
                border-radius: 6px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1D4ED8;        /* Hover State: Darker Blue */
                color: white;
            }
        """)


        Dashboard.setCentralWidget(self.centralwidget)
        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)


    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Dashboard"))