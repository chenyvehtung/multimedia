# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
import main_win


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mywin = main_win.MainWin()
    mywin.show()
    sys.exit(app.exec_())
