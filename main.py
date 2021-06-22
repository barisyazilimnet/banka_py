# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1252, 673)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.period_text_label = QtWidgets.QLabel(self.centralwidget)
        self.period_text_label.setGeometry(QtCore.QRect(896, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.period_text_label.setFont(font)
        self.period_text_label.setLineWidth(1)
        self.period_text_label.setObjectName("period_text_label")
        self.cb_period = QtWidgets.QComboBox(self.centralwidget)
        self.cb_period.setGeometry(QtCore.QRect(976, 70, 251, 31))
        self.cb_period.setObjectName("cb_period")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1, 160, 1241, 471))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.btn_filter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_filter.setGeometry(QtCore.QRect(896, 110, 331, 41))
        self.btn_filter.setObjectName("btn_filter")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(10, 90, 211, 61))
        self.btn_save.setObjectName("btn_save")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(230, 90, 211, 61))
        self.btn_edit.setObjectName("btn_edit")
        self.cb_bank = QtWidgets.QComboBox(self.centralwidget)
        self.cb_bank.setGeometry(QtCore.QRect(976, 20, 251, 31))
        self.cb_bank.setObjectName("cb_bank")
        self.cb_bank.addItem("")
        self.cb_bank.addItem("")
        self.cb_bank.addItem("")
        self.bank_text_label = QtWidgets.QLabel(self.centralwidget)
        self.bank_text_label.setGeometry(QtCore.QRect(896, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bank_text_label.setFont(font)
        self.bank_text_label.setObjectName("bank_text_label")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(450, 90, 211, 61))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_payment = QtWidgets.QPushButton(self.centralwidget)
        self.btn_payment.setGeometry(QtCore.QRect(670, 90, 211, 61))
        self.btn_payment.setObjectName("btn_payment")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1252, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.period_text_label.setText(_translate("MainWindow", "Dönem"))
        self.tableWidget.setSortingEnabled(False)
        self.btn_filter.setText(_translate("MainWindow", "Filtrele"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet"))
        self.btn_edit.setText(_translate("MainWindow", "Düzenle"))
        self.cb_bank.setItemText(0, _translate("MainWindow", "Enpara.com"))
        self.cb_bank.setItemText(1, _translate("MainWindow", "Garanti BBVA"))
        self.cb_bank.setItemText(2, _translate("MainWindow", "Özel"))
        self.bank_text_label.setText(_translate("MainWindow", "Banka"))
        self.btn_delete.setText(_translate("MainWindow", "Sil"))
        self.btn_payment.setText(_translate("MainWindow", "Ödeme"))
