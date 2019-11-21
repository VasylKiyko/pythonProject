# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, Ui_Login):
        Ui_Login.setObjectName("Ui_Login")
        Ui_Login.resize(480, 380)
        Ui_Login.setMinimumSize(QtCore.QSize(480, 380))
        Ui_Login.setMaximumSize(QtCore.QSize(480, 380))
        Ui_Login.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.centralwidget = QtWidgets.QWidget(Ui_Login)
        self.centralwidget.setMaximumSize(QtCore.QSize(540, 540))
        self.centralwidget.setObjectName("centralwidget")
        self.btnSingIn = QtWidgets.QPushButton(self.centralwidget)
        self.btnSingIn.setGeometry(QtCore.QRect(190, 189, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(87)
        font.setStrikeOut(False)
        self.btnSingIn.setFont(font)
        self.btnSingIn.setStyleSheet("QPushButton {\n"
"  font-weight: 700;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  padding: .2em 1em calc(.2em + 3px);\n"
"  border-radius: .900em;\n"
"  background: rgb(64,199,129);\n"
"  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
"  transition: 0.2s;\n"
"} \n"
"QPushButton:hover { background: rgb(53, 167, 110); }\n"
"QPushButton:pressed {\n"
"  background: rgb(33,147,90);\n"
"  box-shadow: 0 3px rgb(33,147,90) inset;\n"
"}")
        self.btnSingIn.setObjectName("btnSingIn")
        self.btnSingUpLog = QtWidgets.QPushButton(self.centralwidget)
        self.btnSingUpLog.setGeometry(QtCore.QRect(190, 239, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(87)
        font.setStrikeOut(False)
        self.btnSingUpLog.setFont(font)
        self.btnSingUpLog.setStyleSheet("QPushButton {\n"
"  font-weight: 700;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  padding: .2em 1em calc(.2em + 3px);\n"
"  border-radius: .900em;\n"
" background: rgb(64,199,129);\n"
"  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
"  transition: 0.2s;\n"
"} \n"
"QPushButton:hover { background: rgb(53, 167, 110); }\n"
"QPushButton:pressed {\n"
"  background: rgb(33,147,90);\n"
"  box-shadow: 0 3px rgb(33,147,90) inset;\n"
"}")
        self.btnSingUpLog.setObjectName("btnSingUpLog")
        self.leLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leLogin.setGeometry(QtCore.QRect(140, 104, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leLogin.setFont(font)
        self.leLogin.setToolTip("")
        self.leLogin.setWhatsThis("")
        self.leLogin.setStyleSheet("QLineEdit {\n"
"background-color: rgb(238, 238, 238);\n"
"  outline: 0;\n"
"  border-bottom: 2px;\n"
"  border-top: 0;\n"
"  border-left: 0;\n"
"  border-right: 0;\n"
"  border-bottom-style: double;\n"
"  border-bottom-color: #34495e;\n"
"  height: 46px;\n"
"  width: 300px;\n"
"}")
        self.leLogin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leLogin.setText("")
        self.leLogin.setObjectName("leLogin")
        self.lePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(140, 140, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lePassword.setFont(font)
        self.lePassword.setToolTip("")
        self.lePassword.setWhatsThis("")
        self.lePassword.setStyleSheet("QLineEdit {\n"
"background-color: rgb(238, 238, 238);\n"
"  outline: 0;\n"
"  border-bottom: 2px;\n"
"  border-top: 0;\n"
"  border-left: 0;\n"
"  border-right: 0;\n"
"  border-bottom-style: double;\n"
"  border-bottom-color: #34495e;\n"
"  height: 46px;\n"
"  width: 300px;\n"
"}")
        self.lePassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lePassword.setText("")
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        Ui_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Login)
        QtCore.QMetaObject.connectSlotsByName(Ui_Login)

    def retranslateUi(self, Ui_Login):
        _translate = QtCore.QCoreApplication.translate
        Ui_Login.setWindowTitle(_translate("Ui_Login", "miniOSBB - Log in"))
        self.btnSingIn.setText(_translate("Ui_Login", "SIGN IN"))
        self.btnSingUpLog.setText(_translate("Ui_Login", "SIGN UP"))
        self.leLogin.setPlaceholderText(_translate("Ui_Login", "Login"))
        self.lePassword.setPlaceholderText(_translate("Ui_Login", "Password"))
