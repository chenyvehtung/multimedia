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

class Ui_imgpro(object):
    def setupUi(self, imgpro):
        imgpro.setObjectName(_fromUtf8("imgpro"))
        imgpro.resize(935, 678)
        self.centralwidget = QtGui.QWidget(imgpro)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 9, 1, 1)
        self.labelWel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("HVD Bodedo"))
        font.setPointSize(24)
        self.labelWel.setFont(font)
        self.labelWel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWel.setObjectName(_fromUtf8("labelWel"))
        self.gridLayout_2.addWidget(self.labelWel, 1, 1, 1, 13)
        self.buttonDefault = QtGui.QPushButton(self.centralwidget)
        self.buttonDefault.setObjectName(_fromUtf8("buttonDefault"))
        self.gridLayout_2.addWidget(self.buttonDefault, 0, 2, 1, 1)
        self.buttonBlur = QtGui.QPushButton(self.centralwidget)
        self.buttonBlur.setObjectName(_fromUtf8("buttonBlur"))
        self.gridLayout_2.addWidget(self.buttonBlur, 0, 11, 1, 1)
        self.buttonOpen = QtGui.QPushButton(self.centralwidget)
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.gridLayout_2.addWidget(self.buttonOpen, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 6, 1, 1)
        self.gridShow = QtGui.QGridLayout()
        self.gridShow.setObjectName(_fromUtf8("gridShow"))
        self.gridLayout_2.addLayout(self.gridShow, 1, 1, 1, 13)
        self.editH = QtGui.QLineEdit(self.centralwidget)
        self.editH.setObjectName(_fromUtf8("editH"))
        self.gridLayout_2.addWidget(self.editH, 0, 5, 1, 1)
        self.labelWait = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("HVD Bodedo"))
        font.setPointSize(24)
        self.labelWait.setFont(font)
        self.labelWait.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWait.setObjectName(_fromUtf8("labelWait"))
        self.gridLayout_2.addWidget(self.labelWait, 1, 1, 1, 13)
        self.editW = QtGui.QLineEdit(self.centralwidget)
        self.editW.setObjectName(_fromUtf8("editW"))
        self.gridLayout_2.addWidget(self.editW, 0, 7, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 4, 1, 1)
        self.buttonResize = QtGui.QPushButton(self.centralwidget)
        self.buttonResize.setObjectName(_fromUtf8("buttonResize"))
        self.gridLayout_2.addWidget(self.buttonResize, 0, 8, 1, 1)
        self.editS = QtGui.QLineEdit(self.centralwidget)
        self.editS.setObjectName(_fromUtf8("editS"))
        self.gridLayout_2.addWidget(self.editS, 0, 10, 1, 1)
        self.buttonSave = QtGui.QPushButton(self.centralwidget)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.gridLayout_2.addWidget(self.buttonSave, 0, 3, 1, 1)
        imgpro.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(imgpro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        imgpro.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(imgpro)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        imgpro.setStatusBar(self.statusbar)
        self.actionUser_Guide = QtGui.QAction(imgpro)
        self.actionUser_Guide.setObjectName(_fromUtf8("actionUser_Guide"))
        self.actionAbout = QtGui.QAction(imgpro)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHomepage = QtGui.QAction(imgpro)
        self.actionHomepage.setObjectName(_fromUtf8("actionHomepage"))
        self.actionOpen_Image = QtGui.QAction(imgpro)
        self.actionOpen_Image.setObjectName(_fromUtf8("actionOpen_Image"))
        self.actionExit = QtGui.QAction(imgpro)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionHomepage)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(imgpro)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), imgpro.close)
        QtCore.QMetaObject.connectSlotsByName(imgpro)

    def retranslateUi(self, imgpro):
        imgpro.setWindowTitle(_translate("imgpro", "ImgPro", None))
        self.label_3.setText(_translate("imgpro", "Size : ", None))
        self.labelWel.setText(_translate("imgpro", "Welcome to Image Pro", None))
        self.buttonDefault.setText(_translate("imgpro", "Default", None))
        self.buttonBlur.setText(_translate("imgpro", "Blur", None))
        self.buttonOpen.setText(_translate("imgpro", "Open Image", None))
        self.label_2.setText(_translate("imgpro", "Width :", None))
        self.labelWait.setText(_translate("imgpro", "Processing Image", None))
        self.label.setText(_translate("imgpro", "Height :", None))
        self.buttonResize.setText(_translate("imgpro", "Resize", None))
        self.buttonSave.setText(_translate("imgpro", "Save", None))
        self.menuHelp.setTitle(_translate("imgpro", "Help", None))
        self.menuFile.setTitle(_translate("imgpro", "File", None))
        self.actionUser_Guide.setText(_translate("imgpro", "User Guide", None))
        self.actionAbout.setText(_translate("imgpro", "About", None))
        self.actionHomepage.setText(_translate("imgpro", "Homepage", None))
        self.actionHomepage.setShortcut(_translate("imgpro", "Ctrl+H", None))
        self.actionOpen_Image.setText(_translate("imgpro", "Open Image", None))
        self.actionOpen_Image.setShortcut(_translate("imgpro", "Ctrl+O", None))
        self.actionExit.setText(_translate("imgpro", "Exit", None))
        self.actionExit.setShortcut(_translate("imgpro", "Ctrl+Q", None))

