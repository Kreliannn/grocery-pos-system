
from PyQt6 import QtCore, QtGui, QtWidgets
from backend.utils.util import utils




class Ui_MainWindow(object):

    def __init__(self):
        self.loginCashier = False
        self.loginAdmin = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 576)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(20, 220, 341, 41))
        self.loginButton.setObjectName("loginButton")


        self.loginButton.clicked.connect(self.checkCredencials)


        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setGeometry(QtCore.QRect(22, 110, 341, 41))
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(20, 170, 341, 41))
        self.password.setText("")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 70, 161, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

      

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def checkCredencials(self):
        usernameVal = self.username.text()
        passwordVal = self.password.text()

        if usernameVal == "admin" and passwordVal == "123":
            self.loginAdmin = True
            print("Login successful welcome admin")
  
        elif usernameVal == "cashier" and passwordVal == "123":
            self.loginCashier = True
            print("Login successful welcome cashier")
        else:
            print("Invalid credentials")
            utils.alertError("Invalid credentials")
            self.password.setText("")

         
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "LOGIN PAGE"))
