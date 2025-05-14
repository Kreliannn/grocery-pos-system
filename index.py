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
from frontend.adminEditProduct import Ui_MainWindow as editproduct

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

    def showAdminAssistant(self ):
        self.adminAI = adminAssistant()
        self.adminAI.setupUi(self)

    def showCashierReciept(self, transaction_id):
        self.cashierReceipt = cashierReciptUi(transaction_id)
        self.cashierReceipt.setupUi(self)
     

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

    
    def showAdminDashboard(self):
        self.adminDashboard = adminDashboardUi()
        self.adminDashboard.setupUi(self)

     
    def showAdminProducts(self):
        self.adminProducts = adminProductsUi()
        self.adminProducts.setupUi(self)
     
    def showAdminEditProducts(self, product):
        self.adminEditProducts = editproduct()
        self.adminEditProducts.setupUi(self, product)

    def showAdminSalesTracker(self):
        self.adminSalesTracker = adminSalesTrackerUi()
        self.adminSalesTracker.setupUi(self)
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
