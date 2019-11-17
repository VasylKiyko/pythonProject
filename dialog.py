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
        self.btnDialogOK = QtWidgets.QPushButton(Dialog)
        self.btnDialogOK.setGeometry(QtCore.QRect(80, 40, 70, 20))
        self.btnDialogOK.setObjectName("btnDialogOK")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 111, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnDialogOK.setText(_translate("Dialog", "ОК"))
        self.label.setText(_translate("Dialog", "Registration successful"))
