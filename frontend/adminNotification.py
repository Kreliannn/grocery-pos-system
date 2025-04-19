from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, NotificationPage):
        NotificationPage.setObjectName("NotificationPage")
        NotificationPage.resize(420, 600)  # Adjusted window width to 500px
        NotificationPage.setStyleSheet("font-family: 'Segoe UI'; font-size: 14px;")

        self.centralwidget = QtWidgets.QWidget(parent=NotificationPage)
        self.centralwidget.setObjectName("centralwidget")

        # Home button at the top
        self.home_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(20, 20, 100, 30))
        self.home_button.setText("Home")
        self.home_button.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px;")

        # Scrollable notification container
        self.scroll_area = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(20, 70, 380, 500))  # Adjusted width for scroll area
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        self.notification_layout = QtWidgets.QVBoxLayout(self.scroll_content)

        # Mockup notifications
        mock_data = [
            {"header": "System Error", "message": "An error occurred during processing.", "icon": "error"},
            {"header": "Upload Complete", "message": "Your product list has been updated.", "icon": "success"},
            {"header": "Low Inventory", "message": "Stock for item #234 is running low.", "icon": "error"},
            {"header": "Sales Update", "message": "You've made 10 sales today!", "icon": "success"}
        ]

        for data in mock_data:
            frame = QtWidgets.QFrame()
            frame.setStyleSheet("background-color: #f5f5f5; border-radius: 10px; padding: 10px;")  # White smoke background
            frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            frame.setMinimumHeight(100)

            layout = QtWidgets.QHBoxLayout(frame)
            icon_label = QtWidgets.QLabel()
            if data["icon"] == "error":
                icon = NotificationPage.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
            else:
                icon = NotificationPage.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation)
            icon_label.setPixmap(icon.pixmap(32, 32))

            text_layout = QtWidgets.QVBoxLayout()
            header = QtWidgets.QLabel(f"<b style='font-size: 12px;'>{data['header']}</b>")  # Increased font size
            message = QtWidgets.QLabel(data['message'])
            message.setStyleSheet("font-size: 14px;")  # Increased font size for message

            text_layout.addWidget(header)
            text_layout.addWidget(message)

            layout.addWidget(icon_label)
            layout.addLayout(text_layout)
            self.notification_layout.addWidget(frame)

        NotificationPage.setCentralWidget(self.centralwidget)
        self.retranslateUi(NotificationPage)
        QtCore.QMetaObject.connectSlotsByName(NotificationPage)

    def retranslateUi(self, NotificationPage):
        _translate = QtCore.QCoreApplication.translate
        NotificationPage.setWindowTitle(_translate("NotificationPage", "Notification Page"))