# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python34\Lib\site-packages\PyQt4\MyQts\git\MainApp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(459, 275)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(90, 100, 101, 23))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(260, 100, 91, 23))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton1.setText(_translate("MainWindow", "Open Dialog 1", None))
        self.pushButton2.setText(_translate("MainWindow", "Open Dialog 2", None))

