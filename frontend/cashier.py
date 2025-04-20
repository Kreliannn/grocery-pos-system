from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, CashierPage):
        CashierPage.setObjectName("CashierPage")
        CashierPage.resize(400, 300)
        CashierPage.setStyleSheet("font-family: 'Segoe UI'; font-size: 12px;")

        self.centralwidget = QtWidgets.QWidget(parent=CashierPage)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 60, 200, 180))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.btn_scan = QtWidgets.QPushButton("Scan", parent=self.verticalLayoutWidget)
        self.btn_scan.setStyleSheet("padding: 10px; background-color: #2ecc71; color: white; border-radius: 5px;")
        self.verticalLayout.addWidget(self.btn_scan)

        self.btn_history = QtWidgets.QPushButton("Receipt History", parent=self.verticalLayoutWidget)
        self.btn_history.setStyleSheet("padding: 10px; background-color: #3498db; color: white; border-radius: 5px;")
        self.verticalLayout.addWidget(self.btn_history)

        self.btn_logout = QtWidgets.QPushButton("Logout", parent=self.verticalLayoutWidget)
        self.btn_logout.setStyleSheet("padding: 10px; background-color: #e74c3c; color: white; border-radius: 5px;")
        self.verticalLayout.addWidget(self.btn_logout)

        CashierPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(CashierPage)
        QtCore.QMetaObject.connectSlotsByName(CashierPage)

    def retranslateUi(self, CashierPage):
        _translate = QtCore.QCoreApplication.translate
        CashierPage.setWindowTitle(_translate("CashierPage", "Cashier Page"))
