from PyQt4 import QtCore, QtGui, QtDesigner
from mainwindow import Ui_uniqimg

def dump_ui(widget, path):
    builder = QtDesigner.QFormBuilder()
    stream = QtCore.QFile(path)
    stream.open(QtCore.QIODevice.WriteOnly)
    builder.save(stream, widget)
    stream.close()

app = QtGui.QApplication([''])

dialog = QtGui.QMainWindow()
Ui_uniqimg().setupUi(dialog)

dialog.show()

dump_ui(dialog, 'myui.ui')
