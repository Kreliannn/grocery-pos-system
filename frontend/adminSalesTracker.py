from PyQt6 import QtCore, QtGui, QtWidgets

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
        self.calendarLayout.addWidget(self.calendar)
        self.calendarLayout.addWidget(self.trackButton)
        self.calendarLayout.addStretch()

        self.middleLayout.addLayout(self.calendarLayout)

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Transaction ID", "Date", "Total"])
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.middleLayout.addWidget(self.table)

        self.verticalLayout.addLayout(self.middleLayout)

        # Bottom summary
        self.summaryLayout = QtWidgets.QHBoxLayout()
        self.salesLabelText = QtWidgets.QLabel("Sales:")
        self.salesLabel = QtWidgets.QLabel("₱ 0")
        self.dateLabelText = QtWidgets.QLabel("Date:")
        self.dateLabel = QtWidgets.QLabel("00-00-00")

        for w in [self.salesLabelText, self.salesLabel, self.dateLabelText, self.dateLabel]:
            self.summaryLayout.addWidget(w)

        self.summaryLayout.addStretch()
        self.verticalLayout.addLayout(self.summaryLayout)

        SalesReportPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(SalesReportPage)
        QtCore.QMetaObject.connectSlotsByName(SalesReportPage)

    def retranslateUi(self, SalesReportPage):
        SalesReportPage.setWindowTitle("Sales Report")
