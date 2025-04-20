from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, NotificationPage):
        NotificationPage.setObjectName("NotificationPage")
        NotificationPage.resize(450, 600)
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
        self.scroll_area.setGeometry(QtCore.QRect(20, 70, 410, 500))
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        self.notification_layout = QtWidgets.QVBoxLayout(self.scroll_content)

        # Mockup notifications with datetime
        mock_data = [
            {"header": "System Error", "message": "An error occurred during processing.", "icon": "warning", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"header": "Upload Complete", "message": "Your product list has been updated.", "icon": "success", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"header": "Low Inventory", "message": "Stock for item #234 is running low.", "icon": "warning", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"header": "Sales Update", "message": "You've made 10 sales today!", "icon": "success", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        ]

        for data in mock_data:
            frame = QtWidgets.QFrame()
            frame.setStyleSheet("background-color: #f5f5f5; border-radius: 10px; padding: 10px;")
            frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            frame.setMinimumHeight(100)

            main_layout = QtWidgets.QHBoxLayout(frame)

            # Icon on the left
            icon_label = QtWidgets.QLabel()
            icon_label.setFixedSize(55, 55)
            if data["icon"] == "warning":
                icon = NotificationPage.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxWarning)
            else:
                icon = NotificationPage.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation)
            icon_label.setPixmap(icon.pixmap(55, 55))

            # Texts on the right
            text_layout = QtWidgets.QVBoxLayout()
            header = QtWidgets.QLabel(f"<b>{data['header']}</b>")
            header.setStyleSheet("font-size: 13px;")

            message = QtWidgets.QLabel(data['message'])
            message.setStyleSheet("font-size: 14px;")
            message.setWordWrap(True)

            timestamp_label = QtWidgets.QLabel(data['datetime'])
            timestamp_label.setStyleSheet("font-size: 11px; color: gray;")

            text_layout.addWidget(header)
            text_layout.addWidget(message)
            text_layout.addWidget(timestamp_label)

            main_layout.addWidget(icon_label)
            main_layout.addLayout(text_layout)
            self.notification_layout.addWidget(frame)


        NotificationPage.setCentralWidget(self.centralwidget)
        self.retranslateUi(NotificationPage)
        QtCore.QMetaObject.connectSlotsByName(NotificationPage)

    def retranslateUi(self, NotificationPage):
        _translate = QtCore.QCoreApplication.translate
        NotificationPage.setWindowTitle(_translate("NotificationPage", "Notification Page"))
