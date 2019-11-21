# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, Ui_Registration):
        Ui_Registration.setObjectName("Ui_Registration")
        Ui_Registration.resize(500, 440)
        Ui_Registration.setMinimumSize(QtCore.QSize(500, 440))
        Ui_Registration.setMaximumSize(QtCore.QSize(500, 440))
        Ui_Registration.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.centralwidget = QtWidgets.QWidget(Ui_Registration)
        self.centralwidget.setMaximumSize(QtCore.QSize(540, 540))
        self.centralwidget.setObjectName("centralwidget")
        self.btnSingUpReg = QtWidgets.QPushButton(self.centralwidget)
        self.btnSingUpReg.setGeometry(QtCore.QRect(150, 340, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(87)
        font.setStrikeOut(False)
        self.btnSingUpReg.setFont(font)
        self.btnSingUpReg.setStyleSheet("QPushButton {\n"
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
        self.btnSingUpReg.setObjectName("btnSingUpReg")
        self.leName = QtWidgets.QLineEdit(self.centralwidget)
        self.leName.setGeometry(QtCore.QRect(110, 91, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leName.setFont(font)
        self.leName.setToolTip("")
        self.leName.setWhatsThis("")
        self.leName.setStyleSheet("QLineEdit {\n"
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
        self.leName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leName.setText("")
        self.leName.setObjectName("leName")
        self.leSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.leSurname.setGeometry(QtCore.QRect(260, 91, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leSurname.setFont(font)
        self.leSurname.setToolTip("")
        self.leSurname.setWhatsThis("")
        self.leSurname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leSurname.setStyleSheet("QLineEdit {\n"
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
        self.leSurname.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leSurname.setText("")
        self.leSurname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leSurname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.leSurname.setObjectName("leSurname")
        self.lePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(110, 171, 281, 31))
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
        self.leConPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.leConPassword.setGeometry(QtCore.QRect(110, 211, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leConPassword.setFont(font)
        self.leConPassword.setToolTip("")
        self.leConPassword.setWhatsThis("")
        self.leConPassword.setStyleSheet("QLineEdit {\n"
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
        self.leConPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.leConPassword.setText("")
        self.leConPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leConPassword.setObjectName("leConPassword")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 60, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(74, 74, 74)")
        self.label_6.setObjectName("label_6")
        self.leAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.leAddress.setGeometry(QtCore.QRect(110, 251, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leAddress.setFont(font)
        self.leAddress.setToolTip("")
        self.leAddress.setWhatsThis("")
        self.leAddress.setStyleSheet("QLineEdit {\n"
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
        self.leAddress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leAddress.setText("")
        self.leAddress.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leAddress.setObjectName("leAddress")
        self.leApartNum = QtWidgets.QLineEdit(self.centralwidget)
        self.leApartNum.setGeometry(QtCore.QRect(110, 291, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leApartNum.setFont(font)
        self.leApartNum.setToolTip("")
        self.leApartNum.setWhatsThis("")
        self.leApartNum.setStyleSheet("QLineEdit {\n"
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
        self.leApartNum.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leApartNum.setText("")
        self.leApartNum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leApartNum.setObjectName("leApartNum")
        self.leLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leLogin.setGeometry(QtCore.QRect(110, 131, 281, 31))
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
        self.leLogin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leLogin.setObjectName("leLogin")
        Ui_Registration.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Registration)
        QtCore.QMetaObject.connectSlotsByName(Ui_Registration)

    def retranslateUi(self, Ui_Registration):
        _translate = QtCore.QCoreApplication.translate
        Ui_Registration.setWindowTitle(_translate("Ui_Registration", "miniOSBB - Registration"))
        self.btnSingUpReg.setText(_translate("Ui_Registration", "SIGN UP"))
        self.leName.setPlaceholderText(_translate("Ui_Registration", "Name"))
        self.leSurname.setPlaceholderText(_translate("Ui_Registration", "Surname"))
        self.lePassword.setPlaceholderText(_translate("Ui_Registration", "Password"))
        self.leConPassword.setPlaceholderText(_translate("Ui_Registration", "Confirm password"))
        self.label_6.setText(_translate("Ui_Registration", "Registration"))
        self.leAddress.setPlaceholderText(_translate("Ui_Registration", "Street"))
        self.leApartNum.setPlaceholderText(_translate("Ui_Registration", "Apartment number"))
        self.leLogin.setPlaceholderText(_translate("Ui_Registration", "Login"))
