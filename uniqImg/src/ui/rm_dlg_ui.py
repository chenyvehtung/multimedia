# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rmdialog.ui'
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

class Ui_viewDialog(object):
    def setupUi(self, viewDialog):
        viewDialog.setObjectName(_fromUtf8("viewDialog"))
        viewDialog.resize(727, 430)
        self.gridLayout = QtGui.QGridLayout(viewDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(viewDialog)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 2)
        self.checkBoxAll = QtGui.QCheckBox(viewDialog)
        self.checkBoxAll.setObjectName(_fromUtf8("checkBoxAll"))
        self.gridLayout.addWidget(self.checkBoxAll, 1, 0, 1, 1)
        self.buttonCancel = QtGui.QPushButton(viewDialog)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.gridLayout.addWidget(self.buttonCancel, 1, 1, 1, 1)
        self.buttonRemove = QtGui.QPushButton(viewDialog)
        self.buttonRemove.setObjectName(_fromUtf8("buttonRemove"))
        self.gridLayout.addWidget(self.buttonRemove, 1, 2, 1, 1)
        self.listView = QtGui.QListView(viewDialog)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)

        self.retranslateUi(viewDialog)
        QtCore.QMetaObject.connectSlotsByName(viewDialog)

    def retranslateUi(self, viewDialog):
        viewDialog.setWindowTitle(_translate("viewDialog", "Similar Image", None))
        self.checkBoxAll.setText(_translate("viewDialog", "Select All", None))
        self.buttonCancel.setText(_translate("viewDialog", "Cancel", None))
        self.buttonRemove.setText(_translate("viewDialog", "Remove", None))

