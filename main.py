import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_LoginWindow
from registration import Ui_RegisterWindow
from dialog import Ui_Dialog
import Client as cl


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        #self.client = cl.Client()

        #self.btnSingInLog.clicked.connect(self.log_in)
        self.btnSingUpLog.clicked.connect(self.openRegisterForm)

    #def __del__(self):
        #self.client.__del__()

    #def log_in(self):
        #login = self.leLogin.text()
        #password = self.lePassword.text()
        #log_in_data = [login, password]
        #self.client.log_in(log_in_data)

    def openRegisterForm(self):
        self.regWin = RegisterWindow()
        logWin.hide()
        self.regWin.show()


class RegisterWindow(QMainWindow, Ui_RegisterWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.btnSingUpReg.clicked.connect(self.openDialog)

    def openDialog(self):
        self.dialWin = DialogWindow()
        self.dialWin.show()


class DialogWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.btnDialogOK.clicked.connect(self.onClickOK)

    def onClickOK(self):
        logWin.regWin.close()
        logWin.show()
        self.close()

    def closeEvent(self, QCloseEvent):
        logWin.regWin.close()
        logWin.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logWin = LoginWindow()
    logWin.show()
    sys.exit(app.exec_())