
from PyQt6 import QtCore, QtGui, QtWidgets
from backend.utils.util import utils


class Ui_MainWindow(object):

    def __init__(self):
        self.loginCashier = False
        self.loginAdmin = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)  # Adjusted size for better proportions
        MainWindow.setStyleSheet("background-color: #f5f5f5;")
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
     
        
        # Login container with shadow effect
        self.loginContainer = QtWidgets.QFrame(parent=self.centralwidget)
        self.loginContainer.setGeometry(QtCore.QRect(75, 90, 350, 350))
        self.loginContainer.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
         
        """)
        
        # Login header
        self.label = QtWidgets.QLabel(parent=self.loginContainer)
        self.label.setGeometry(QtCore.QRect(0, 30, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: #2c3e50;")
        self.label.setObjectName("label")
        
        # Username label
        self.usernameLabel = QtWidgets.QLabel(parent=self.loginContainer)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 80, 270, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setText("Username")
        self.usernameLabel.setStyleSheet("color: #7f8c8d;")
        
        # Username input field
        self.username = QtWidgets.QLineEdit(parent=self.loginContainer)
        self.username.setGeometry(QtCore.QRect(40, 105, 270, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("""
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                background-color: #f9f9f9;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
                background-color: white;
            }
        """)
        self.username.setPlaceholderText("Enter username")
        self.username.setText("")
        self.username.setObjectName("username")
        
        # Password label
        self.passwordLabel = QtWidgets.QLabel(parent=self.loginContainer)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 170, 270, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setText("Password")
        self.passwordLabel.setStyleSheet("color: #7f8c8d;")
        
        # Password input field
        self.password = QtWidgets.QLineEdit(parent=self.loginContainer)
        self.password.setGeometry(QtCore.QRect(40, 195, 270, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("""
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                background-color: #f9f9f9;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
                background-color: white;
            }
        """)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Setting password mode
        self.password.setPlaceholderText("Enter password")
        self.password.setText("")
        self.password.setObjectName("password")
        
        # Login button with modern styling
        self.loginButton = QtWidgets.QPushButton(parent=self.loginContainer)
        self.loginButton.setGeometry(QtCore.QRect(40, 270, 270, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6ea4;
            }
        """)
        self.loginButton.setObjectName("loginButton")
        
        # Connect login button to authentication function
        self.loginButton.clicked.connect(self.checkCredencials)
        
        # Footer text
        self.footerText = QtWidgets.QLabel(parent=self.centralwidget)
        self.footerText.setGeometry(QtCore.QRect(75, 520, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.footerText.setFont(font)
        self.footerText.setText("Group 8 - POS System")
        self.footerText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.footerText.setStyleSheet("color: #95a5a6;")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setStyleSheet("background-color: #ecf0f1;")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "POS System Login"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "LOGIN PAGE"))
