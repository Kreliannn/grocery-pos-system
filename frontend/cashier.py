from PyQt6 import QtCore, QtWidgets, QtGui

class Ui_MainWindow(object):
    def setupUi(self, CashierPage):
        CashierPage.setObjectName("CashierPage")
        CashierPage.resize(800, 600)
        
        # Apply global stylesheet
        CashierPage.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 12px;
                background-color: #F8FAFC;
                color: #1E3A8A;
            }
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 6px;
                padding: 12px;
                font-weight: bold;
                min-height: 20px;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QPushButton:pressed {
                background-color: #1E40AF;
            }
            QLabel {
                color: #1E3A8A;
            }
            QFrame {
                background-color: #FFFFFF;
                border-radius: 8px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=CashierPage)
        self.centralwidget.setObjectName("centralwidget")

        # Create a header
        self.header_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 800, 80))
        self.header_frame.setStyleSheet("""
            QFrame {
                background-color: #2563EB;
                border-radius: 0px;
            }
        """)
        
        # Header title
        self.header_label = QtWidgets.QLabel(parent=self.header_frame)
        self.header_label.setGeometry(QtCore.QRect(30, 20, 300, 40))
        self.header_label.setText("Cashier Dashboard")
        self.header_label.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: white;
        """)
        
     
        
        # Main content card
        self.main_card = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_card.setGeometry(QtCore.QRect(50, 110, 700, 440))
        self.main_card.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
        """)
        
        # Card title
        self.card_title = QtWidgets.QLabel(parent=self.main_card)
        self.card_title.setGeometry(QtCore.QRect(30, 25, 200, 30))
        self.card_title.setText("Quick Actions")
        self.card_title.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        
        # Horizontal line separator
        self.separator = QtWidgets.QFrame(parent=self.main_card)
        self.separator.setGeometry(QtCore.QRect(30, 60, 640, 1))
        self.separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator.setStyleSheet("""
            background-color: #CBD5E1;
        """)

        # Create vertical layout widget for buttons
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.main_card)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 100, 300, 280))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)

        # Scan button with improved styling
        self.btn_scan = QtWidgets.QPushButton("Scan Products", parent=self.verticalLayoutWidget)
        self.btn_scan.setStyleSheet("""
            background-color: #38BDF8;
            color: white;
            border-radius: 6px;
            padding: 16px;
            font-size: 14px;
            font-weight: bold;
        """)
        self.verticalLayout.addWidget(self.btn_scan)

        # History button
        self.btn_history = QtWidgets.QPushButton("Receipt History", parent=self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.btn_history)

        # Logout button with custom color
        self.btn_logout = QtWidgets.QPushButton("Logout", parent=self.verticalLayoutWidget)
        self.btn_logout.setStyleSheet("""
            background-color: #F1F5F9;
            color: #64748B;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            padding: 16px;
            font-size: 14px;
            font-weight: bold;
        """)
        self.verticalLayout.addWidget(self.btn_logout)

        # Status bar at the bottom
        self.status_bar = QtWidgets.QLabel(parent=self.centralwidget)
        self.status_bar.setGeometry(QtCore.QRect(0, 570, 800, 30))
        self.status_bar.setText("  System Status: Online")
        self.status_bar.setStyleSheet("""
            background-color: #F1F5F9;
            color: #64748B;
            padding-left: 10px;
            border-top: 1px solid #CBD5E1;
        """)

        CashierPage.setCentralWidget(self.centralwidget)
        
        # Connect buttons to functions
        self.btn_scan.clicked.connect(CashierPage.showCashierHome)
        self.btn_history.clicked.connect(CashierPage.showCashierRecieptHistory)
        self.btn_logout.clicked.connect(CashierPage.showLoginPage)

        self.retranslateUi(CashierPage)
        QtCore.QMetaObject.connectSlotsByName(CashierPage)

    def retranslateUi(self, CashierPage):
        _translate = QtCore.QCoreApplication.translate
        CashierPage.setWindowTitle(_translate("CashierPage", "Cashier Dashboard"))