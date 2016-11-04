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
        uniqimg.resize(740, 520)
        self.centralwidget = QtGui.QWidget(uniqimg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.editPath = QtGui.QLineEdit(self.centralwidget)
        self.editPath.setObjectName(_fromUtf8("editPath"))
        self.gridLayout_2.addWidget(self.editPath, 0, 0, 1, 1)
        self.buttonSearch = QtGui.QPushButton(self.centralwidget)
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.gridLayout_2.addWidget(self.buttonSearch, 0, 2, 1, 1)
        self.gridShow = QtGui.QGridLayout()
        self.gridShow.setObjectName(_fromUtf8("gridShow"))
        self.gridLayout_2.addLayout(self.gridShow, 1, 0, 1, 3)
        self.buttonOpen = QtGui.QPushButton(self.centralwidget)
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.gridLayout_2.addWidget(self.buttonOpen, 0, 1, 1, 1)
        self.labelCon = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("HVD Bodedo"))
        font.setPointSize(16)
        self.labelCon.setFont(font)
        self.labelCon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCon.setObjectName(_fromUtf8("labelCon"))
        self.gridLayout_2.addWidget(self.labelCon, 1, 0, 1, 3)
        self.labelWel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("HVD Bodedo"))
        font.setPointSize(24)
        self.labelWel.setFont(font)
        self.labelWel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWel.setObjectName(_fromUtf8("labelWel"))
        self.gridLayout_2.addWidget(self.labelWel, 1, 0, 1, 3)
        self.labelWait = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("HVD Bodedo"))
        font.setPointSize(24)
        self.labelWait.setFont(font)
        self.labelWait.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWait.setObjectName(_fromUtf8("labelWait"))
        self.gridLayout_2.addWidget(self.labelWait, 1, 0, 1, 3)
        uniqimg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(uniqimg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        uniqimg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(uniqimg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        uniqimg.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(uniqimg)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        uniqimg.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUser_Guide = QtGui.QAction(uniqimg)
        self.actionUser_Guide.setObjectName(_fromUtf8("actionUser_Guide"))
        self.actionAbout = QtGui.QAction(uniqimg)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHomepage = QtGui.QAction(uniqimg)
        self.actionHomepage.setObjectName(_fromUtf8("actionHomepage"))
        self.actionOpen_Folder = QtGui.QAction(uniqimg)
        self.actionOpen_Folder.setObjectName(_fromUtf8("actionOpen_Folder"))
        self.actionExit = QtGui.QAction(uniqimg)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionHomepage)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(uniqimg)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), uniqimg.close)
        QtCore.QMetaObject.connectSlotsByName(uniqimg)

    def retranslateUi(self, uniqimg):
        uniqimg.setWindowTitle(_translate("uniqimg", "UniqImg", None))
        self.buttonSearch.setText(_translate("uniqimg", "Search", None))
        self.buttonOpen.setText(_translate("uniqimg", "Open Folder", None))
        self.labelCon.setText(_translate("uniqimg", "Congratulation!\n"
"The directory doesn\'t contain any duplicate images", None))
        self.labelWel.setText(_translate("uniqimg", "Welcome to Unique Image", None))
        self.labelWait.setText(_translate("uniqimg", "Searching for the similar image", None))
        self.menuHelp.setTitle(_translate("uniqimg", "Help", None))
        self.menuFile.setTitle(_translate("uniqimg", "File", None))
        self.toolBar.setWindowTitle(_translate("uniqimg", "toolBar", None))
        self.actionUser_Guide.setText(_translate("uniqimg", "User Guide", None))
        self.actionAbout.setText(_translate("uniqimg", "About", None))
        self.actionHomepage.setText(_translate("uniqimg", "Homepage", None))
        self.actionHomepage.setShortcut(_translate("uniqimg", "Ctrl+H", None))
        self.actionOpen_Folder.setText(_translate("uniqimg", "Open Folder", None))
        self.actionOpen_Folder.setShortcut(_translate("uniqimg", "Ctrl+O", None))
        self.actionExit.setText(_translate("uniqimg", "Exit", None))
        self.actionExit.setShortcut(_translate("uniqimg", "Ctrl+Q", None))

