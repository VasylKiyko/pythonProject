# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(230, 80)
        Dialog.setMinimumSize(QtCore.QSize(230, 80))
        Dialog.setMaximumSize(QtCore.QSize(230, 80))
        Dialog.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.btnDialogOK = QtWidgets.QPushButton(Dialog)
        self.btnDialogOK.setGeometry(QtCore.QRect(80, 40, 70, 21))
        self.btnDialogOK.setStyleSheet("QPushButton {\n"
                                       "  font-weight: 700;\n"
                                       "  color: white;\n"
                                       "  text-decoration: none;\n"
                                       "  padding: .2em 1em calc(.2em + 3px);\n"
                                       "  border-radius: 10px;\n"
                                       "  background: rgb(64,199,129);\n"
                                       "} \n"
                                       "QPushButton:hover { background: rgb(53, 167, 110); }\n"
                                       "QPushButton:pressed {\n"
                                       "  background: rgb(33,147,90);\n"
                                       "}")
        self.btnDialogOK.setObjectName("btnDialogOK")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(74, 74, 74)")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.btnDialogOK.setText(_translate("Dialog", "ОК"))
        self.label.setText(_translate("Dialog", "Registration successful"))
