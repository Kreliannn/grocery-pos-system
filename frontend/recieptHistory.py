from PyQt6 import QtCore, QtGui, QtWidgets
from backend.transaction import Transaction

class Ui_MainWindow(object):

    def __init__(self):
        self.myTransaction = Transaction()
        data = self.myTransaction.getTransactions()
        self.receipt = list(reversed(data))

    def setupUi(self, ReceiptPage):
        ReceiptPage.setObjectName("ReceiptPage")
        ReceiptPage.resize(380, 600)

        self.centralwidget = QtWidgets.QWidget(parent=ReceiptPage)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Top bar with Home button
        self.topBar = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton("Home")
        self.topBar.addWidget(self.homeButton)
        self.topBar.addStretch()
        self.verticalLayout.addLayout(self.topBar)

        # Scroll area container
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QtWidgets.QWidget()
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollContent)

        # Add 5 images
        for item in self.receipt:
            label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap("frontend/reciept_img/" + item["transaction_id"] + ".png")
            desired_height = 200

            # Ensure image fills full width and custom height
            scaled_pixmap = pixmap.scaled(
                ReceiptPage.width(),  # 100% width of main window
                desired_height,
                QtCore.Qt.AspectRatioMode.IgnoreAspectRatio,
                QtCore.Qt.TransformationMode.SmoothTransformation
            )
            label.setPixmap(pixmap)
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.scrollLayout.addWidget(label)

        self.scrollContent.setLayout(self.scrollLayout)
        self.scrollArea.setWidget(self.scrollContent)
        self.verticalLayout.addWidget(self.scrollArea)

        ReceiptPage.setCentralWidget(self.centralwidget)
        self.retranslateUi(ReceiptPage)
        QtCore.QMetaObject.connectSlotsByName(ReceiptPage)

    def retranslateUi(self, ReceiptPage):
        ReceiptPage.setWindowTitle("Receipt Viewer")
