# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RestoreInstructionsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_Instructions = QtWidgets.QTableWidget(Form)
        self.tableWidget_Instructions.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Instructions.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_Instructions.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_Instructions.setObjectName("tableWidget_Instructions")
        self.tableWidget_Instructions.setColumnCount(2)
        self.tableWidget_Instructions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Instructions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Instructions.setHorizontalHeaderItem(1, item)
        self.tableWidget_Instructions.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Instructions.verticalHeader().setVisible(False)
        self.tableWidget_Instructions.verticalHeader().setDefaultSectionSize(16)
        self.tableWidget_Instructions.verticalHeader().setMinimumSectionSize(16)
        self.gridLayout.addWidget(self.tableWidget_Instructions, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Restore Instructions"))
        self.tableWidget_Instructions.setSortingEnabled(True)
        item = self.tableWidget_Instructions.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Address"))
        item = self.tableWidget_Instructions.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Original Instruction"))
