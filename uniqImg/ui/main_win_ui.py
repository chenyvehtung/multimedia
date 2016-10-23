# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_uniqimg(object):
    def setupUi(self, uniqimg):
        uniqimg.setObjectName(_fromUtf8("uniqimg"))
        uniqimg.resize(800, 600)
        self.centralwidget = QtGui.QWidget(uniqimg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.editPath = QtGui.QLineEdit(self.centralwidget)
        self.editPath.setObjectName(_fromUtf8("editPath"))
        self.gridLayout_2.addWidget(self.editPath, 0, 0, 1, 1)
        self.buttonOpen = QtGui.QPushButton(self.centralwidget)
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.gridLayout_2.addWidget(self.buttonOpen, 0, 3, 1, 1)
        self.buttonSearch = QtGui.QPushButton(self.centralwidget)
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.gridLayout_2.addWidget(self.buttonSearch, 0, 5, 1, 1)
        self.comboAlg = QtGui.QComboBox(self.centralwidget)
        self.comboAlg.setObjectName(_fromUtf8("comboAlg"))
        self.comboAlg.addItem(_fromUtf8(""))
        self.comboAlg.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboAlg, 0, 4, 1, 1)
        self.gridShow = QtGui.QGridLayout()
        self.gridShow.setObjectName(_fromUtf8("gridShow"))
        self.labelWait = QtGui.QLabel(self.centralwidget)
        self.labelWait.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWait.setObjectName(_fromUtf8("labelWait"))
        self.gridShow.addWidget(self.labelWait, 0, 0, 1, 1)
        self.labelWel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("HVD Bodedo"))
        font.setPointSize(25)
        self.labelWel.setFont(font)
        self.labelWel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWel.setObjectName(_fromUtf8("labelWel"))
        self.gridShow.addWidget(self.labelWel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridShow, 1, 0, 1, 6)
        uniqimg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(uniqimg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        uniqimg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(uniqimg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        uniqimg.setStatusBar(self.statusbar)
        self.actionUser_Guide = QtGui.QAction(uniqimg)
        self.actionUser_Guide.setObjectName(_fromUtf8("actionUser_Guide"))
        self.actionAbout = QtGui.QAction(uniqimg)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(uniqimg)
        QtCore.QMetaObject.connectSlotsByName(uniqimg)

    def retranslateUi(self, uniqimg):
        uniqimg.setWindowTitle(_translate("uniqimg", "UniqImg", None))
        self.buttonOpen.setText(_translate("uniqimg", "Open Folder", None))
        self.buttonSearch.setText(_translate("uniqimg", "Search", None))
        self.comboAlg.setItemText(0, _translate("uniqimg", "AHash", None))
        self.comboAlg.setItemText(1, _translate("uniqimg", "PHash", None))
        self.labelWait.setText(_translate("uniqimg", "Searching for the similar image", None))
        self.labelWel.setText(_translate("uniqimg", "Welcome to Unique Image", None))
        self.menuHelp.setTitle(_translate("uniqimg", "Help", None))
        self.actionUser_Guide.setText(_translate("uniqimg", "User Guide", None))
        self.actionAbout.setText(_translate("uniqimg", "About", None))

