from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        def setupUi(self, Dashboard):
            Dashboard.setObjectName("Dashboard")
            Dashboard.resize(900, 600)
            Dashboard.setStyleSheet("font-family: 'Segoe UI'; font-size: 12px;")

            self.centralwidget = QtWidgets.QWidget(parent=Dashboard)
            self.centralwidget.setObjectName("centralwidget")

            # Top navbar
            self.navbar = QtWidgets.QFrame(parent=self.centralwidget)
            self.navbar.setGeometry(QtCore.QRect(0, 0, 900, 60))
            self.navbar.setStyleSheet("background-color: #2c3e50; color: white;")
            self.navbar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.navbar.setObjectName("navbar")

            # Navbar buttons
            button_names = ["Add Product", "Receipt History", "AI Assistant", "Sales Tracker", "Notification"]
            self.nav_buttons = []
            for i, name in enumerate(button_names):
                btn = QtWidgets.QPushButton(parent=self.navbar)
                btn.setGeometry(QtCore.QRect(20 + i*170, 15, 150, 30))
                btn.setText(name)
                btn.setStyleSheet("background-color: #34495e; color: white; border-radius: 5px;")
                self.nav_buttons.append(btn)

            # Dashboard info boxes (hardcoded)
            self.info_frame = QtWidgets.QFrame(parent=self.centralwidget)
            self.info_frame.setGeometry(QtCore.QRect(0, 70, 900, 300))
            self.info_frame.setObjectName("info_frame")

            self.box_today_sales = QtWidgets.QGroupBox(parent=self.info_frame)
            self.box_today_sales.setTitle("Today Sales")
            self.box_today_sales.setGeometry(QtCore.QRect(20, 10, 400, 130))
            self.box_today_sales.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")

            self.label_today_sales = QtWidgets.QLabel(parent=self.box_today_sales)
            self.label_today_sales.setGeometry(QtCore.QRect(0, 40, 400, 50))
            self.label_today_sales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.label_today_sales.setStyleSheet("font-size: 24px; color: #2c3e50;")
            self.label_today_sales.setText("0")

            self.box_overall_sales = QtWidgets.QGroupBox(parent=self.info_frame)
            self.box_overall_sales.setTitle("Overall Sales")
            self.box_overall_sales.setGeometry(QtCore.QRect(460, 10, 400, 130))
            self.box_overall_sales.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")

            self.label_overall_sales = QtWidgets.QLabel(parent=self.box_overall_sales)
            self.label_overall_sales.setGeometry(QtCore.QRect(0, 40, 400, 50))
            self.label_overall_sales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.label_overall_sales.setStyleSheet("font-size: 24px; color: #2c3e50;")
            self.label_overall_sales.setText("0")

            self.box_product_count = QtWidgets.QGroupBox(parent=self.info_frame)
            self.box_product_count.setTitle("Product Count")
            self.box_product_count.setGeometry(QtCore.QRect(20, 160, 400, 130))
            self.box_product_count.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")

            self.label_product_count = QtWidgets.QLabel(parent=self.box_product_count)
            self.label_product_count.setGeometry(QtCore.QRect(0, 40, 400, 50))
            self.label_product_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.label_product_count.setStyleSheet("font-size: 24px; color: #2c3e50;")
            self.label_product_count.setText("0")

            self.box_item_sold = QtWidgets.QGroupBox(parent=self.info_frame)
            self.box_item_sold.setTitle("Item Sold")
            self.box_item_sold.setGeometry(QtCore.QRect(460, 160, 400, 130))
            self.box_item_sold.setStyleSheet("QGroupBox { background-color: #ecf0f1; border: 1px solid #bdc3c7; border-radius: 10px; font-weight: bold; }")

            self.label_item_sold = QtWidgets.QLabel(parent=self.box_item_sold)
            self.label_item_sold.setGeometry(QtCore.QRect(0, 40, 400, 50))
            self.label_item_sold.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.label_item_sold.setStyleSheet("font-size: 24px; color: #2c3e50;")
            self.label_item_sold.setText("0")

            Dashboard.setCentralWidget(self.centralwidget)
            self.retranslateUi(Dashboard)
            QtCore.QMetaObject.connectSlotsByName(Dashboard)

        def retranslateUi(self, Dashboard):
            _translate = QtCore.QCoreApplication.translate
            Dashboard.setWindowTitle(_translate("Dashboard", "Dashboard"))