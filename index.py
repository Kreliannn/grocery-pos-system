import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from frontend.loginPage import Ui_MainWindow as loginPageUi
from frontend.cashierHome import Ui_MainWindow as cashierHomeUi
from frontend.adminAddProduct import Ui_MainWindow as adminAddProductUi
from frontend.adminDashboard import Ui_MainWindow as adminDashboardUi
from frontend.adminProducts  import Ui_MainWindow as adminProductsUi
from frontend.cashierReciept  import Ui_MainWindow as cashierReciptUi
from frontend.adminSalesTracker import Ui_MainWindow as adminSalesTrackerUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showAdminSalesTracker()
        #self.showCashierReciept()

    def showLoginPage(self):
        self.login = loginPageUi()
        self.login.setupUi(self)
        self.login.loginButton.clicked.connect(lambda: self.showCashierHome() if self.login.loginCashier else print("wrong"))
        self.login.loginButton.clicked.connect(lambda: self.showAdminDashboard() if self.login.loginAdmin else print("wrong"))
    
    def showCashierHome(self):
        self.cashierHome = cashierHomeUi()
        self.cashierHome.setupUi(self)
        self.cashierHome.pushButton_3.clicked.connect(lambda: self.cashierHome.stopCamera())
        self.cashierHome.pushButton_3.clicked.connect(self.showAdminDashboard)
        self.cashierHome.pushButton_4.clicked.connect(lambda: self.cashierHome.stopCamera() if self.cashierHome.recipt else print("kulang"))
        self.cashierHome.pushButton_4.clicked.connect(lambda: self.showCashierReciept(self.cashierHome.transaction_id) if self.cashierHome.recipt else print("kulang"))

    def showCashierReciept(self, transaction_id):
        self.cashierHome = cashierReciptUi(transaction_id)
        self.cashierHome.setupUi(self)
        self.cashierHome.home.clicked.connect(self.showAdminDashboard)
      

    def showAdminAddProduct(self):
        self.adminAddProduct = adminAddProductUi()
        self.adminAddProduct.setupUi(self)
        self.adminAddProduct.pushButton.clicked.connect(lambda: self.adminAddProduct.stopCamera())
        self.adminAddProduct.pushButton.clicked.connect(self.showAdminDashboard)
    
    def showAdminDashboard(self):
        self.adminDashboard = adminDashboardUi()
        self.adminDashboard.setupUi(self)

        self.adminDashboard.pushButton_1.clicked.connect(self.showAdminAddProduct)
        self.adminDashboard.pushButton_2.clicked.connect(self.showAdminProducts)
        self.adminDashboard.pushButton_3.clicked.connect(self.showCashierHome)

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
