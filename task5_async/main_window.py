# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 168)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.url1 = QtWidgets.QLineEdit(self.groupBox)
        self.url1.setObjectName("url1")
        self.gridLayout.addWidget(self.url1, 0, 0, 1, 1)
        self.url2 = QtWidgets.QLineEdit(self.groupBox)
        self.url2.setObjectName("url2")
        self.gridLayout.addWidget(self.url2, 0, 1, 1, 1)
        self.url3 = QtWidgets.QLineEdit(self.groupBox)
        self.url3.setObjectName("url3")
        self.gridLayout.addWidget(self.url3, 0, 2, 1, 1)
        self.progress1 = QtWidgets.QProgressBar(self.groupBox)
        self.progress1.setEnabled(False)
        self.progress1.setProperty("value", 0)
        self.progress1.setObjectName("progress1")
        self.gridLayout.addWidget(self.progress1, 1, 0, 1, 1)
        self.progress2 = QtWidgets.QProgressBar(self.groupBox)
        self.progress2.setEnabled(False)
        self.progress2.setProperty("value", 0)
        self.progress2.setObjectName("progress2")
        self.gridLayout.addWidget(self.progress2, 1, 1, 1, 1)
        self.progress3 = QtWidgets.QProgressBar(self.groupBox)
        self.progress3.setEnabled(False)
        self.progress3.setProperty("value", 0)
        self.progress3.setObjectName("progress3")
        self.gridLayout.addWidget(self.progress3, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.start_downloading)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "URL файлов"))
        self.pushButton.setText(_translate("MainWindow", "Start downloading!"))

