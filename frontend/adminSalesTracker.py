from PyQt6 import QtCore, QtGui, QtWidgets
from backend.transaction import Transaction
from backend.notification import Notification
from backend.utils.util import utils

class Ui_MainWindow(object):
    def setupUi(self, SalesReportPage):
        SalesReportPage.setObjectName("SalesReportPage")
        SalesReportPage.resize(1000, 700)
        
        # Global stylesheet
        SalesReportPage.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                background-color: #F8FAFC;
                color: #1E3A8A;
            }
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QLabel {
                color: #1E3A8A;
            }
            QCalendarWidget {
                background-color: #FFFFFF;
                border-radius: 8px;
            }
            QCalendarWidget QWidget {
                alternate-background-color: #F1F5F9;
            }
            QCalendarWidget QToolButton {
                color: #1E3A8A;
                background-color: #E0F2FE;
                border-radius: 4px;
            }
            QCalendarWidget QMenu {
                background-color: #FFFFFF;
                color: #1E3A8A;
            }
            QCalendarWidget QSpinBox {
                background-color: #FFFFFF;
                color: #1E3A8A;
                border: 1px solid #CBD5E1;
                border-radius: 4px;
            }
            QTableWidget {
                background-color: #FFFFFF;
                border-radius: 8px;
                border: none;
                gridline-color: #CBD5E1;
            }
            QTableWidget::item {
                padding: 6px;
                border-bottom: 1px solid #F1F5F9;
            }
            QTableWidget::item:selected {
                background-color: #E0F2FE;
                color: #1E3A8A;
            }
            QHeaderView::section {
                background-color: #F1F5F9;
                color: #64748B;
                font-weight: bold;
                padding: 8px;
                border: none;
                border-bottom: 1px solid #CBD5E1;
            }
            QScrollBar:vertical {
                background-color: #F1F5F9;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #CBD5E1;
                border-radius: 6px;
            }
            QFrame.Card {
                background-color: #FFFFFF;
                border-radius: 8px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=SalesReportPage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)

        # Header with title
        self.headerFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.headerFrame.setMaximumHeight(70)
        self.headerFrame.setStyleSheet("""
            background-color: #2563EB;
            border-radius: 10px;
            padding: 10px;
        """)
        self.headerLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        
        self.titleLabel = QtWidgets.QLabel("Sales Report Dashboard")
        self.titleLabel.setFixedHeight(50)  # Adjust value as needed

        self.titleLabel.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
            padding-left: 10px;
            margin-top: -50px
        """)
        self.headerLayout.addWidget(self.titleLabel)
        
        # Top navigation bar
        self.topBar = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton("Home")
        self.homeButton.setMinimumHeight(36)
        self.homeButton.setStyleSheet("""
            background-color: #FFFFFF;
            color: #1E3A8A;
            border-radius: 6px;
            font-weight: bold;
        """)
        self.headerLayout.addStretch()
        self.headerLayout.addWidget(self.homeButton)
        
        self.verticalLayout.addWidget(self.headerFrame)

        # Middle section: calendar and table in a card
        self.contentFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.contentFrame.setProperty("class", "Card")
        self.contentFrame.setStyleSheet("""
            QFrame.Card {
                background-color: #FFFFFF;
                border-radius: 12px;
                padding: 10px;
            }
        """)
        
        self.contentLayout = QtWidgets.QVBoxLayout(self.contentFrame)
        self.contentLayout.setContentsMargins(20, 20, 20, 20)
        self.contentLayout.setSpacing(20)
        
        # Subheader
        self.subheaderLabel = QtWidgets.QLabel("Daily Sales Tracking")
        self.subheaderLabel.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        self.contentLayout.addWidget(self.subheaderLabel)
        
        # Add separator line
        self.separator = QtWidgets.QFrame()
        self.separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator.setStyleSheet("background-color: #CBD5E1;")
        self.contentLayout.addWidget(self.separator)
        
        # Calendar and table section
        self.middleLayout = QtWidgets.QHBoxLayout()
        self.middleLayout.setSpacing(20)

        # Left panel with calendar
        self.leftPanel = QtWidgets.QFrame()
        self.leftPanel.setProperty("class", "Card")
        self.leftPanel.setMinimumWidth(350)
        self.leftPanel.setMaximumWidth(350)
        self.leftPanel.setStyleSheet("""
            background-color: #F1F5F9;
            border-radius: 8px;
            padding: 10px;
        """)
        
        self.calendarLayout = QtWidgets.QVBoxLayout(self.leftPanel)
        self.calendarLayout.setContentsMargins(10, 10, 10, 10)
        self.calendarLayout.setSpacing(15)
        
        # Calendar title
        self.calendarTitle = QtWidgets.QLabel("Select Date")
        self.calendarTitle.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #1E3A8A;
        """)
        self.calendarLayout.addWidget(self.calendarTitle)
        
        # Calendar widget with styled look
        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 6px;
        """)
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarLayout.addWidget(self.calendar)

        self.calendar.setFixedHeight(200)  # Adjust the number as needed

        
        # Track button with custom styling
        self.trackButton = QtWidgets.QPushButton("Track Sales")
        self.trackButton.setStyleSheet("""
            background-color: #38BDF8;
            color: white;
            font-size: 14px;
            font-weight: bold;
            border-radius: 6px;
            padding: 12px;
        """)
        font_btn = QtGui.QFont()
        font_btn.setPointSize(14)
        font_btn.setBold(True)
        self.trackButton.setFont(font_btn)
        self.trackButton.setFixedHeight(50)
        self.calendarLayout.addWidget(self.trackButton)
        
        # Sales info panel
        self.infoPanel = QtWidgets.QFrame()
        self.infoPanel.setStyleSheet("""
            background-color: #E0F2FE;
            border-radius: 6px;
            padding: 10px;
        """)
        self.infoPanelLayout = QtWidgets.QVBoxLayout(self.infoPanel)
        
        # Sales and Date labels
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)

        # Date display
        self.dateLabelLayout = QtWidgets.QHBoxLayout()
        self.dateLabelText = QtWidgets.QLabel("Date:")
        self.dateLabelText.setFont(font_label)
        self.dateLabelText.setStyleSheet("color: #64748B;")
        self.dateLabel = QtWidgets.QLabel("Not selected")
        self.dateLabel.setFont(font_label)
        self.dateLabel.setStyleSheet("color: #1E3A8A;")
        self.dateLabelLayout.addWidget(self.dateLabelText)
        self.dateLabelLayout.addWidget(self.dateLabel)
        self.dateLabelLayout.addStretch()
        self.infoPanelLayout.addLayout(self.dateLabelLayout)
        
        # Sales display
        self.salesLabelLayout = QtWidgets.QHBoxLayout()
        self.salesLabelText = QtWidgets.QLabel("Total Sales:")
        self.salesLabelText.setFont(font_label)
        self.salesLabelText.setStyleSheet("color: #64748B;")
        self.salesLabel = QtWidgets.QLabel("₱ 0")
        self.salesLabel.setFont(font_label)
        self.salesLabel.setStyleSheet("color: #1E3A8A;")
        self.salesLabelLayout.addWidget(self.salesLabelText)
        self.salesLabelLayout.addWidget(self.salesLabel)
        self.salesLabelLayout.addStretch()
        self.infoPanelLayout.addLayout(self.salesLabelLayout)
        
        self.calendarLayout.addWidget(self.infoPanel)
        self.calendarLayout.addStretch()
        
        # Right panel with table
        self.rightPanel = QtWidgets.QFrame()
        self.rightPanel.setProperty("class", "Card")
        self.tableLayout = QtWidgets.QVBoxLayout(self.rightPanel)
        self.tableLayout.setContentsMargins(0, 0, 0, 0)

        # Table header
        self.tableHeader = QtWidgets.QLabel("Transaction Details")
        self.tableHeader.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #1E3A8A;
            padding: 10px;
        """)
        self.tableLayout.addWidget(self.tableHeader)
        
        # Table widget with better styling
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Transaction ID", "Date", "Total"])
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableLayout.addWidget(self.table)
        
        # Add panels to middle layout
        self.middleLayout.addWidget(self.leftPanel)
        self.middleLayout.addWidget(self.rightPanel, 1)
        
        self.contentLayout.addLayout(self.middleLayout)
        self.verticalLayout.addWidget(self.contentFrame)
        
        # Add status bar at the bottom
        self.statusBar = QtWidgets.QLabel("Ready to track sales data. Select a date and click Track.")
        self.statusBar.setStyleSheet("""
            background-color: #F1F5F9;
            color: #64748B;
            padding: 8px;
            border-radius: 6px;
        """)
        self.verticalLayout.addWidget(self.statusBar)

        SalesReportPage.setCentralWidget(self.centralwidget)


        self.homeButton.clicked.connect(SalesReportPage.showAdminDashboard)


        # Connect signals
        self.trackButton.clicked.connect(self.track)

        self.retranslateUi(SalesReportPage)
        QtCore.QMetaObject.connectSlotsByName(SalesReportPage)

    def track(self):
        self.table.setRowCount(0)
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        self.statusBar.setText(f"Tracking sales for {selected_date}...")
        
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
        
        # Update status bar with results
        transaction_count = self.table.rowCount()
        self.statusBar.setText(f"Found {transaction_count} transactions on {selected_date}. Total sales: ₱ {total_sales}")
        
   

    def retranslateUi(self, SalesReportPage):
        SalesReportPage.setWindowTitle("Sales Report Dashboard")
