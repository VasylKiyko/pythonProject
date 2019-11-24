import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from loginUi import Ui_LoginWindow
from registrationUi import Ui_RegisterWindow
from dialogUi import Ui_Dialog
from client import Client


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.client = Client()

        self.btnSingIn.clicked.connect(self.log_in)
        self.btnSingUpLog.clicked.connect(self.openRegisterForm)

    def __del__(self):
        self.client.__del__()

    def log_in(self):
        login = self.leLogin.text()
        password = self.lePassword.text()
        log_in_data = [login, password]

        self.client.log_in(log_in_data)

    def openRegisterForm(self):
        self.regWin = RegisterWindow()
        logWin.hide()
        self.regWin.show()


class RegisterWindow(QMainWindow, Ui_RegisterWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.btnSingUpReg.clicked.connect(self.registration)

    def registration(self):
        name = self.leName.text()
        surname = self.leSurname.text()
        login = self.leLogin.text()
        password = self.lePassword.text()
        confirmPassword = self.leConPassword.text()
        street = self.leAddress.text()
        apartNum = self.leApartNum.text()

        if name == '' or surname == '' or login == '' or password == '' \
                or confirmPassword == '' or street == '' or apartNum == '':
            self.lMessage.setText('*Fill in all fields')
        elif confirmPassword != password:
            self.lMessage.setText('*Passwords don`t match')
        else:
            registration_data = [login, password, name, surname, street, apartNum]
            clientExist = logWin.client.sign_up(registration_data)

            if clientExist:
                sleep(0.4)
                logWin.show()
                self.close()
                self.dialogWin = DialogWindow()
                self.dialogWin.show()
                self.dialogWin.label.setText('Registration successful')
            else:
                self.lMessage.setText('*Client is already exist')

    def closeEvent(self, QCloseEvent):
        logWin.show()


class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.btnDialogOK.clicked.connect(self.onClickOK)

    def onClickOK(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logWin = LoginWindow()
    logWin.show()
    sys.exit(app.exec_())
