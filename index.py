import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from frontend.loginPage import Ui_MainWindow as loginPageUi
from frontend.cashierHome import Ui_MainWindow as cashierHomeUi
from frontend.adminAddProduct import Ui_MainWindow as adminAddProductUi
from frontend.adminDashboard import Ui_MainWindow as adminDashboardUi
from frontend.adminProducts  import Ui_MainWindow as adminProductsUi
from frontend.cashierReciept  import Ui_MainWindow as cashierReciptUi
from frontend.adminSalesTracker import Ui_MainWindow as adminSalesTrackerUi
from frontend.recieptHistory import Ui_MainWindow as recieptHistoryUi
from frontend.adminNotification import Ui_MainWindow as adminNotificationUi
from frontend.cashier import Ui_MainWindow as cashierUi
from frontend.cashierReceiptHistory import Ui_MainWindow as cashierHistoryUi
from frontend.adminAiAssistant import Ui_MainWindow as adminAssistant

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showLoginPage()


    def showLoginPage(self):
        self.login = loginPageUi()
        self.login.setupUi(self)
       
    
    def showCashierHome(self):
        self.cashierHome = cashierHomeUi()
        self.cashierHome.setupUi(self)          
    

    def showCashier(self ):
        self.cashier = cashierUi()
        self.cashier.setupUi(self)
        self.cashier.btn_scan.clicked.connect(self.showCashierHome)
        self.cashier.btn_history.clicked.connect(self.showCashierRecieptHistory)
        self.cashier.btn_logout.clicked.connect(self.showLoginPage)

    
    def showAdminAssistant(self ):
        self.adminAI = adminAssistant()
        self.adminAI.setupUi(self)
        self.adminAI.homeButton.clicked.connect(self.showAdminDashboard)
    
       

    def showCashierReciept(self, transaction_id):
        self.cashierReceipt = cashierReciptUi(transaction_id)
        self.cashierReceipt.setupUi(self)
        self.cashierReceipt.home.clicked.connect(self.showCashier)

    def showAdminNotification(self):
        self.adminNotif = adminNotificationUi()
        self.adminNotif.setupUi(self)
        self.adminNotif.home_button.clicked.connect(self.showAdminDashboard)
    
    def showRecieptHistory(self):
        self.recieptHistory = recieptHistoryUi()
        self.recieptHistory.setupUi(self)
        self.recieptHistory.homeButton.clicked.connect(self.showAdminDashboard)

    def showCashierRecieptHistory(self):
        self.recieptHistory = cashierHistoryUi()
        self.recieptHistory.setupUi(self)
        self.recieptHistory.homeButton.clicked.connect(self.showCashier)

    def showAdminAddProduct(self):
        self.adminAddProduct = adminAddProductUi()
        self.adminAddProduct.setupUi(self)
        self.adminAddProduct.pushButton.clicked.connect(lambda: self.adminAddProduct.stopCamera())
        self.adminAddProduct.pushButton.clicked.connect(self.showAdminDashboard)
    
    def showAdminDashboard(self):
        self.adminDashboard = adminDashboardUi()
        self.adminDashboard.setupUi(self)

     

    def showAdminProducts(self):
        self.adminProducts = adminProductsUi()
        self.adminProducts.setupUi(self)
        self.adminProducts.homeButton.clicked.connect(self.showAdminDashboard)

    def showAdminSalesTracker(self):
        self.adminSalesTracker = adminSalesTrackerUi()
        self.adminSalesTracker.setupUi(self)
        self.adminSalesTracker.homeButton.clicked.connect(self.showAdminDashboard)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
