from PyQt6 import QtCore, QtGui, QtWidgets
from backend.transaction import Transaction
from backend.notification  import Notification
from backend.utils.util import utils

class Ui_MainWindow(object):
    def setupUi(self, SalesReportPage):
        SalesReportPage.setObjectName("SalesReportPage")
        SalesReportPage.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(parent=SalesReportPage)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Top Bar
        self.topBar = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton("Home")
        self.topBar.addWidget(self.homeButton)
        self.topBar.addStretch()
        self.verticalLayout.addLayout(self.topBar)

        # Middle section: calendar and table
        self.middleLayout = QtWidgets.QHBoxLayout()

        self.calendarLayout = QtWidgets.QVBoxLayout()
        self.calendar = QtWidgets.QCalendarWidget()
        self.trackButton = QtWidgets.QPushButton("Track")

        # Make Track button bigger
        font_btn = QtGui.QFont()
        font_btn.setPointSize(14)
        font_btn.setBold(True)
        self.trackButton.setFont(font_btn)
        self.trackButton.setFixedHeight(50)

        self.calendarLayout.addWidget(self.calendar)
        self.calendarLayout.addWidget(self.trackButton)

        # Sales and Date labels (moved under Track button)
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)

        self.salesLabelText = QtWidgets.QLabel("Sales:")
        self.salesLabel = QtWidgets.QLabel("₱ 0")
        self.dateLabelText = QtWidgets.QLabel("Date:")
        self.dateLabel = QtWidgets.QLabel("00-00-00")

        for label in [self.salesLabelText, self.salesLabel, self.dateLabelText, self.dateLabel]:
            label.setFont(font_label)
            self.calendarLayout.addWidget(label)

        self.calendarLayout.addStretch()
        self.middleLayout.addLayout(self.calendarLayout)

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Transaction ID", "Date", "Total"])
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.middleLayout.addWidget(self.table)

        self.verticalLayout.addLayout(self.middleLayout)

        SalesReportPage.setCentralWidget(self.centralwidget)

        self.trackButton.clicked.connect(self.track)

        self.retranslateUi(SalesReportPage)
        QtCore.QMetaObject.connectSlotsByName(SalesReportPage)

    
    def track(self):
        self.table.setRowCount(0)
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        myTransaction = Transaction()
        data = myTransaction.getTransactions()
        total_sales = 0

        for entry in data:
            if entry["date"] == selected_date:
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(entry["transaction_id"]))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(entry["date"]))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(f"₱ {entry['total']}"))
                total_sales += entry["total"]

        self.sales = total_sales
        self.salesLabel.setText(f"₱ {self.sales}")
        self.dateLabel.setText(str(selected_date))
        
        myNotification = Notification()
        myNotification.addNotifications({
            "header" : "Track Sales" ,
            "message" : str(selected_date) + " sales is " + str(total_sales),
            "icon" : "success"
        })
       

    def retranslateUi(self, SalesReportPage):
        SalesReportPage.setWindowTitle("Sales Report")
