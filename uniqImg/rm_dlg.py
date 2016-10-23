# -*- coding:utf-8 -*-

from ui.rm_dlg_ui import Ui_viewDialog
from PyQt4 import QtGui, QtCore
import sys


class RemoveDlg(QtGui.QDialog):
    def __init__(self, img_list, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_viewDialog()
        self.ui.setupUi(self)

        self.img_list = img_list


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mywin = RemoveDlg([1, 2])
    mywin.show()
    sys.exit(app.exec_())
