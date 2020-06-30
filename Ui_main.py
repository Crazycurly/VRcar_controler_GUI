# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\school\python\VRcar_controler_GUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_gamepad = QtWidgets.QPushButton(Dialog)
        self.btn_gamepad.setObjectName("btn_gamepad")
        self.horizontalLayout_2.addWidget(self.btn_gamepad)
        self.btn_stop = QtWidgets.QPushButton(Dialog)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_2.addWidget(self.btn_stop)
        self.btn_start = QtWidgets.QPushButton(Dialog)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mjpeg_label = QtWidgets.QLabel(Dialog)
        self.mjpeg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mjpeg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mjpeg_label.setObjectName("mjpeg_label")
        self.horizontalLayout.addWidget(self.mjpeg_label)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_gamepad.setText(_translate("Dialog", "gamepad"))
        self.btn_stop.setText(_translate("Dialog", "stop"))
        self.btn_start.setText(_translate("Dialog", "start"))
        self.mjpeg_label.setText(_translate("Dialog", "TextLabel"))
