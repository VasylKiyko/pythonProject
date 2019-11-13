# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from registration import Ui_RegisterWindow


class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 380)
        MainWindow.setMinimumSize(QtCore.QSize(480, 380))
        MainWindow.setMaximumSize(QtCore.QSize(480, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(540, 540))
        self.centralwidget.setObjectName("centralwidget")
        self.btnSingIn = QtWidgets.QPushButton(self.centralwidget)
        self.btnSingIn.setGeometry(QtCore.QRect(190, 210, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSingIn.setFont(font)
        self.btnSingIn.setObjectName("btnSingIn")
        self.btnSingUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnSingUp.setGeometry(QtCore.QRect(190, 260, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSingUp.setFont(font)
        self.btnSingUp.setObjectName("btnSingUp")

        self.btnSingUp.clicked.connect(self.openRegisterForm)

        self.leLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leLogin.setGeometry(QtCore.QRect(140, 125, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leLogin.setFont(font)
        self.leLogin.setToolTip("")
        self.leLogin.setWhatsThis("")
        self.leLogin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leLogin.setText("")
        self.leLogin.setObjectName("leLogin")
        self.lePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(140, 170, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lePassword.setFont(font)
        self.lePassword.setToolTip("")
        self.lePassword.setWhatsThis("")
        self.lePassword.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lePassword.setText("")
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 105, 45, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 155, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openRegisterForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        main.hide()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log in"))
        self.btnSingIn.setText(_translate("MainWindow", "SING IN"))
        self.btnSingUp.setText(_translate("MainWindow", "SING UP"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
