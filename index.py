import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from frontend.loginPage import Ui_MainWindow as loginPageUi
from frontend.cashierHome import Ui_MainWindow as cashierHomeUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showCashierHome()

    def showLoginPage(self):
        self.login = loginPageUi()
        self.login.setupUi(self)
    
    def showCashierHome(self):
        self.cashierHome = cashierHomeUi()
        self.cashierHome.setupUi(self)


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())