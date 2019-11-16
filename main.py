import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_LoginWindow
from registration import Ui_RegisterWindow
from dialog import Ui_Dialog


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.btnSingUp.clicked.connect(self.openRegisterForm)

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

        self.btnOK.clicked.connect(self.onClickOK)

    def onClickOK(self):
        self.label.clear()
        self.hide()
        logWin.regWin.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logWin = LoginWindow()
    logWin.show()
    sys.exit(app.exec_())
