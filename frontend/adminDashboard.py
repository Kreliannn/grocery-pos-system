from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 200, 250))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton_1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_1.setText("Button 1")
        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setText("Button 2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setText("Button 3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setText("Button 4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_5.setText("Button 5")
        self.verticalLayout.addWidget(self.pushButton_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Five Buttons Page")
