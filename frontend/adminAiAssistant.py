from PyQt6 import QtCore, QtGui, QtWidgets
from backend.aiAssistant import Ai
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(400, 600)
        
        # Apply global styles
        ChatWindow.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 14px;
                background-color: #F8FAFC;
                color: #1E3A8A;
            }
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #CBD5E1;
                border-radius: 5px;
                padding: 5px 10px;
                color: #1E3A8A;
            }
            QLineEdit:focus {
                border: 1px solid #38BDF8;
            }
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #F1F5F9;
                width: 8px;
                border-radius: 4px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #CBD5E1;
                border-radius: 4px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #64748B;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(parent=ChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        # === Top layout with title and Home button ===
        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        
        # Chat title
        self.chatTitle = QtWidgets.QLabel("AI Assistant", parent=self.centralwidget)
        self.chatTitle.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        
        # Home button
        self.homeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setText("Home")
        self.homeButton.setFixedSize(100, 40)
        
        self.topLayout.addWidget(self.chatTitle)
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.homeButton)
        self.verticalLayout.addLayout(self.topLayout)

        # === Chat area ===
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)
        
        self.chatContainer = QtWidgets.QWidget()
        self.chatContainer.setObjectName("chatContainer")
        self.chatContainer.setStyleSheet("""
            background-color: #F1F5F9;
            border-radius: 10px;
        """)
        
        self.chatLayout = QtWidgets.QVBoxLayout(self.chatContainer)
        self.chatLayout.setObjectName("chatLayout")
        self.chatLayout.setContentsMargins(15, 15, 15, 15)
        self.chatLayout.setSpacing(12)

        # Spacer to push messages up
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.chatLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.chatContainer)
        self.verticalLayout.addWidget(self.scrollArea)

        # === Input area ===
        self.inputContainer = QtWidgets.QWidget(parent=self.centralwidget)
        self.inputContainer.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 5px;
        """)
        
        self.hboxlayout = QtWidgets.QHBoxLayout(self.inputContainer)
        self.hboxlayout.setContentsMargins(10, 10, 10, 10)
        self.hboxlayout.setSpacing(10)
        self.hboxlayout.setObjectName("hboxlayout")
        
        self.messageInput = QtWidgets.QLineEdit(parent=self.inputContainer)
        self.messageInput.setObjectName("messageInput")
        self.messageInput.setMinimumHeight(40)
        self.messageInput.setPlaceholderText("Type your message here...")
        self.hboxlayout.addWidget(self.messageInput)
        
        self.sendButton = QtWidgets.QPushButton(parent=self.inputContainer)
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setFixedSize(80, 40)
        self.sendButton.setText("Send")
        # Explicitly set the button style to ensure it's blue
        self.sendButton.setStyleSheet("""
            background-color: #2563EB;
            color: white;
            border-radius: 5px;
            font-weight: bold;
        """)
        self.hboxlayout.addWidget(self.sendButton)
        
        self.verticalLayout.addWidget(self.inputContainer)
        
        # Initialize AI and load messages
        self.myAi = Ai()
        messages = self.myAi.getConvoMessages()
        for item in messages:
            self.add_message(item)

        # Connect signals
        self.sendButton.clicked.connect(self.sendPrompt)
        self.messageInput.returnPressed.connect(self.sendPrompt)
        self.homeButton.clicked.connect(ChatWindow.showAdminDashboard)

        ChatWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def sendPrompt(self):
        prompt = self.messageInput.text().strip()
        if not prompt:  # Don't send empty messages
            return
            
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = self.myAi.generateAnswer(prompt)
        
        adminMessage = {
            "sender": "admin",
            "message": prompt,
            "datetime": date
        }
        
        aiMessage = {
            "sender": "ai",
            "message": response,
            "datetime": date
        }
        
        self.myAi.addMessage(adminMessage)
        self.myAi.addMessage(aiMessage)
        
        self.add_message(adminMessage)
        self.add_message(aiMessage)
        
        self.messageInput.clear()

        # Automatically scroll to the bottom after sending a message
        QTimer = QtCore.QTimer()
        QTimer.singleShot(100, self.scrollToBottom)

    def scrollToBottom(self):
        self.scrollArea.verticalScrollBar().setValue(
            self.scrollArea.verticalScrollBar().maximum()
        )

    def add_message(self, message):
        # Create a container widget for each message
        message_widget = QtWidgets.QWidget()
        message_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        
        message_layout = QtWidgets.QVBoxLayout(message_widget)
        message_layout.setContentsMargins(0, 0, 0, 2)
        message_layout.setSpacing(4)

        # Label for message text
        msg_label = QtWidgets.QLabel(message['message'])
        msg_label.setWordWrap(True)
        msg_label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        
        # Apply different styles based on sender
        if message['sender'] == "admin":
            msg_label.setStyleSheet("""
                background-color: #E0F2FE;
                padding: 12px;
                border-radius: 10px;
                border-top-right-radius: 2px;
                color: #1E3A8A;
            """)
            msg_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:  # sender == "ai"
            msg_label.setStyleSheet("""
                background-color: #FFFFFF;
                padding: 12px;
                border-radius: 10px;
                border-top-left-radius: 2px;
                color: #1E3A8A;
            """)
            msg_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)

        # Label for timestamp
        time_label = QtWidgets.QLabel(message['datetime'])
        time_label.setStyleSheet("""
            font-size: 10px;
            color: #64748B;
            padding-left: 5px;
            padding-right: 5px;
        """)
        
        if message['sender'] == "admin":
            time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        else:
            time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        message_layout.addWidget(msg_label)
        message_layout.addWidget(time_label)

        # Horizontal layout to position the message left/right
        container = QtWidgets.QHBoxLayout()
        container.setContentsMargins(0, 0, 0, 0)
        container.setSpacing(0)
        
        spacer_left = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        spacer_right = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        if message["sender"] == "admin":
            container.addItem(spacer_left)
            container.addWidget(message_widget, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            message_widget.setMaximumWidth(280)
        else:
            container.addWidget(message_widget, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
            container.addItem(spacer_right)
            message_widget.setMaximumWidth(280)

        self.chatLayout.insertLayout(self.chatLayout.count() - 1, container)
        
        # Scroll to the bottom after adding a message
        QTimer = QtCore.QTimer()
        QTimer.singleShot(100, self.scrollToBottom)

    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "AI Chat"))
        self.sendButton.setText(_translate("ChatWindow", "Send"))
        self.homeButton.setText(_translate("ChatWindow", "Home"))