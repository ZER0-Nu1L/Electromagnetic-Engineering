# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 615)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/Figure_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 621, 491))
        self.label_3.setStyleSheet("image:url(:/新前缀/Ideas/Figure_1.png)")
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setPixmap(QtGui.QPixmap(":/image/Triangle.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 530, 621, 21))
        self.label_4.setObjectName("label_4")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(680, 140, 151, 261))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
    
#Picture change Part
    #change 3
        self.pBt_3 = QtWidgets.QPushButton(self.widget)
        self.pBt_3.setObjectName("pBt_3")
        self.verticalLayout.addWidget(self.pBt_3)

        self.pBt_3.toggle()
        self.pBt_3.clicked.connect(self.change_3)
    #change 4
        self.pBt_4 = QtWidgets.QPushButton(self.widget)
        self.pBt_4.setObjectName("pBt_4")
        self.verticalLayout.addWidget(self.pBt_4)

        self.pBt_4.toggle()
        self.pBt_4.clicked.connect(self.change_4)
    #change 5
        self.pBt_5 = QtWidgets.QPushButton(self.widget)
        self.pBt_5.setObjectName("pBt_5")
        self.verticalLayout.addWidget(self.pBt_5)

        self.pBt_5.toggle()
        self.pBt_5.clicked.connect(self.change_5)
    #change 6
        self.pBt_6 = QtWidgets.QPushButton(self.widget)
        self.pBt_6.setObjectName("pBt_6")
        self.verticalLayout.addWidget(self.pBt_6)

        self.pBt_6.toggle()
        self.pBt_6.clicked.connect(self.change_6)
    #change 7
        self.pBt_7 = QtWidgets.QPushButton(self.widget)
        self.pBt_7.setObjectName("pBt_7")
        self.verticalLayout.addWidget(self.pBt_7)
    
        self.pBt_7.toggle()
        self.pBt_7.clicked.connect(self.change_7)
    

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 30))
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
        self.label_4.setText(_translate("MainWindow", "注：一些无关常量参数的都设定为简单值，对本例没有本质上的影响"))
        self.pBt_3.setText(_translate("MainWindow", "正三角形"))
        self.pBt_4.setText(_translate("MainWindow", "正四边形"))
        self.pBt_5.setText(_translate("MainWindow", "正五边形"))
        self.pBt_6.setText(_translate("MainWindow", "正六边形"))
        self.pBt_7.setText(_translate("MainWindow", "正七边形"))
    
    def change_3(self):   
        self.label_3.setPixmap(QtGui.QPixmap(":/image/Hexagon.png"))
    def change_4(self):
        self.label_3.setPixmap(QtGui.QPixmap(":/image/Hexagon.png"))
    def change_5(self):
        self.label_3.setPixmap(QtGui.QPixmap(":/image/Hexagon.png"))
    def change_6(self):
        self.label_3.setPixmap(QtGui.QPixmap(":/image/Hexagon.png"))
    def change_7(self):
        self.label_3.setPixmap(QtGui.QPixmap(":/image/Hexagon.png"))

import source_rc
