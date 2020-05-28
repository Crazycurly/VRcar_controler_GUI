# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\school\python\VRcar_controler_GUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_start = QtWidgets.QPushButton(self.centralwidget)
        self.but_start.setGeometry(QtCore.QRect(200, 570, 75, 23))
        self.but_start.setObjectName("but_start")
        self.mjpeg_label = QtWidgets.QLabel(self.centralwidget)
        self.mjpeg_label.setGeometry(QtCore.QRect(150, 40, 640, 480))
        self.mjpeg_label.setText("")
        self.mjpeg_label.setObjectName("mjpeg_label")
        self.but_stop = QtWidgets.QPushButton(self.centralwidget)
        self.but_stop.setGeometry(QtCore.QRect(500, 570, 75, 23))
        self.but_stop.setObjectName("but_stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 25))
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
        self.but_start.setText(_translate("MainWindow", "start"))
        self.but_stop.setText(_translate("MainWindow", "stop"))
