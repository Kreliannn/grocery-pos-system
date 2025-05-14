from PyQt6 import QtCore, QtGui, QtWidgets
from backend.aiAssistant import Ai
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(parent=ChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # === Top layout with Home button ===
        self.topLayout = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setText("Home")
        self.homeButton.setMinimumHeight(40)
        self.topLayout.addWidget(self.homeButton)
        self.verticalLayout.addLayout(self.topLayout)

        # === Chat area ===
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.chatContainer = QtWidgets.QWidget()
        self.chatContainer.setObjectName("chatContainer")
        self.chatLayout = QtWidgets.QVBoxLayout(self.chatContainer)
        self.chatLayout.setObjectName("chatLayout")
        self.chatContainer.setStyleSheet("background:#fffdd0")

     

        # Spacer to push messages up
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.chatLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.chatContainer)
        self.verticalLayout.addWidget(self.scrollArea)

        # === Input area ===
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.messageInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.messageInput.setObjectName("messageInput")
        self.messageInput.setMinimumHeight(40)
        self.hboxlayout.addWidget(self.messageInput)
        self.sendButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setMinimumHeight(40)
        self.hboxlayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.hboxlayout)

        
        self.myAi = Ai()

        messages = self.myAi.getConvoMessages()

        for item in messages:
            self.add_message(item)


        self.sendButton.clicked.connect(self.sendPrompt)


        self.homeButton.clicked.connect(ChatWindow.showAdminDashboard)

        ChatWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def sendPrompt(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prompt = self.messageInput.text()
        response = self.myAi.generateAnswer(prompt)
        adminMessage = {
            "sender" : "admin",
            "message" : prompt,
            "datetime" : date
        }
        aiMessage = {
            "sender" : "ai",
            "message" : response,
            "datetime" : date
        }
        self.myAi.addMessage(adminMessage)
        self.myAi.addMessage(aiMessage)
        self.add_message(adminMessage)
        self.add_message(aiMessage)
        self.messageInput.setText("")

        


    def add_message(self,message ):
        # Create a container widget for each message
        message_widget = QtWidgets.QWidget()
        message_layout = QtWidgets.QVBoxLayout(message_widget)
        message_layout.setContentsMargins(10, 5, 10, 5)

        # Label for message text
        msg_label = QtWidgets.QLabel(message['message'])
        msg_label.setWordWrap(True)

        # Apply different background colors based on sender
        if message['sender'] == "admin":
            msg_label.setStyleSheet("""
                background-color: whitesmoke;
                padding: 8px;
                border-radius: 10px;
            """)
        else:  # sender == "ai"
            msg_label.setStyleSheet("""
                background-color: lightblue;
                padding: 8px;
                border-radius: 10px;
            """)

        msg_label.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)

        # Label for timestamp
        time_label = QtWidgets.QLabel(message['datetime'])
        time_label.setStyleSheet("font-size: 10px; color: gray;")
        time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        message_layout.addWidget(msg_label)
        message_layout.addWidget(time_label)

        # Horizontal layout to position the message left/right
        container = QtWidgets.QHBoxLayout()
        spacer_left = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        spacer_right = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        if message["sender"] == "admin":
            container.addItem(spacer_left)
            container.addWidget(message_widget)
        else:
            container.addWidget(message_widget)
            container.addItem(spacer_right)

        self.chatLayout.insertLayout(self.chatLayout.count() - 1, container)



    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "Chat"))
        self.sendButton.setText(_translate("ChatWindow", "Send"))
        self.homeButton.setText(_translate("ChatWindow", "Home"))
    
