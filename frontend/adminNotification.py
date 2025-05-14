from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from backend.notification import Notification

class Ui_MainWindow(object):
    def setupUi(self, NotificationPage):
        NotificationPage.setObjectName("NotificationPage")
        NotificationPage.resize(450, 600)
        
        # Set application-wide font and styling
        NotificationPage.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 14px;
                background-color: #F8FAFC;
            }
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 5px;
                padding: 8px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #F1F5F9;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #CBD5E1;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #64748B;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=NotificationPage)
        self.centralwidget.setObjectName("centralwidget")

        # Header section with title and home button
        self.header_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.header_widget.setGeometry(QtCore.QRect(0, 0, 450, 60))
        self.header_widget.setStyleSheet("""
            background-color: #FFFFFF;
            border-bottom: 1px solid #CBD5E1;
        """)
        
        self.header_layout = QtWidgets.QHBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(20, 15, 20, 15)
        
        # Home button
        self.home_button = QtWidgets.QPushButton(parent=self.header_widget)
        self.home_button.setText("Home")
        self.home_button.setFixedSize(100, 30)

        self.home_button.setStyleSheet("""
            QPushButton {
                background-color: #2563EB;      /* Primary Blue */
                color: #FFFFFF;                 /* White text */
                border: 1px solid #1E3A8A;      /* Navy Blue border */
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1D4ED8;      /* Darker Blue on hover */
            }
            QPushButton:pressed {
                background-color: #1E3A8A;      /* Navy Blue when pressed */
            }
        """)

        
        # Page title
        self.page_title = QtWidgets.QLabel("Notifications")
        self.page_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        
        self.header_layout.addWidget(self.home_button)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.page_title)
        self.header_layout.addStretch()
        
        # Scrollable notification container
        self.scroll_area = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(20, 70, 410, 510))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        self.scroll_content = QtWidgets.QWidget()
        self.scroll_content.setStyleSheet("background-color: transparent;")
        self.scroll_area.setWidget(self.scroll_content)

        self.notification_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.notification_layout.setSpacing(12)
        self.notification_layout.setContentsMargins(5, 5, 5, 5)

        myNotification = Notification()
        notifications = myNotification.getNotifications()

        for notif in notifications:
            # Card/Frame for each notification
            frame = QtWidgets.QFrame()
            frame.setStyleSheet("""
                background-color: #FFFFFF;
                border-radius: 8px;
                padding: 0px;
                
            """)
            frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            frame.setMinimumHeight(100)

            main_layout = QtWidgets.QHBoxLayout(frame)
            main_layout.setContentsMargins(15, 15, 15, 15)

            # Icon on the left with color indicator
            icon_container = QtWidgets.QWidget()
            icon_container.setFixedSize(55, 55)
            icon_layout = QtWidgets.QVBoxLayout(icon_container)
            icon_layout.setContentsMargins(0, 0, 0, 0)
            
            icon_label = QtWidgets.QLabel()
            icon_label.setFixedSize(55, 55)
            icon_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
            # Color the icon based on notification type
            if notif["icon"] == "warning":
                icon = NotificationPage.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxWarning)
                icon_label.setStyleSheet("""
                    background-color: #FEF2F2;
                    border-radius: 27px;
                    padding: 5px;
                """)
            else:
                icon = NotificationPage.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation)
                icon_label.setStyleSheet("""
                    background-color: #E0F2FE;
                    border-radius: 27px;
                    padding: 5px;
                """)
            
            icon_label.setPixmap(icon.pixmap(30, 30))
            icon_layout.addWidget(icon_label)

            # Texts on the right
            text_layout = QtWidgets.QVBoxLayout()
            text_layout.setSpacing(5)
            
            header_container = QtWidgets.QWidget()
            header_layout = QtWidgets.QHBoxLayout(header_container)
            header_layout.setContentsMargins(0, 0, 0, 0)
            
            header = QtWidgets.QLabel(notif['header'])
            header.setStyleSheet("""
                font-size: 15px;
                font-weight: bold;
                color: #1E3A8A;
            """)
            
            header_layout.addWidget(header)
            header_layout.addStretch()
            
            timestamp_label = QtWidgets.QLabel(notif['datetime'])
            timestamp_label.setStyleSheet("""
                font-size: 12px;
                color: #64748B;
            """)
            header_layout.addWidget(timestamp_label)

            message = QtWidgets.QLabel(notif['message'])
            message.setStyleSheet("""
                font-size: 14px;
                color: #64748B;
                margin-top: 3px;
            """)
            message.setWordWrap(True)
            
            text_layout.addWidget(header_container)
            text_layout.addWidget(message)

            main_layout.addWidget(icon_container)
            main_layout.addLayout(text_layout, 1)
            self.notification_layout.addWidget(frame)

        # Add some space at the end
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.notification_layout.addItem(spacer)

        NotificationPage.setCentralWidget(self.centralwidget)
        self.retranslateUi(NotificationPage)
        QtCore.QMetaObject.connectSlotsByName(NotificationPage)

    def retranslateUi(self, NotificationPage):
        _translate = QtCore.QCoreApplication.translate
        NotificationPage.setWindowTitle(_translate("NotificationPage", "Notification Page"))
