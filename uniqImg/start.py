# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_uniqimg
from PIL import Image
from imagehash import average_hash, phash
from rm_dlg import RemoveDlg


class QScene(QtGui.QGraphicsScene):
    def __init__(self, *args, **kwds):
        QtGui.QGraphicsScene.__init__(self, *args, **kwds)

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            rmdlg = RemoveDlg([1, 2])
            rmdlg.exec_()



class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_uniqimg()
        self.ui.setupUi(self)

        # hide to searching label
        self.ui.labelWait.setVisible(False)

        QtCore.QObject.connect(self.ui.buttonOpen, QtCore.SIGNAL("clicked()"),
                               self.file_dialog)
        QtCore.QObject.connect(self.ui.buttonSearch, QtCore.SIGNAL("clicked()"),
                               self.image_search)


    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.pathname = fd.getExistingDirectory(caption="Open Folder",
                                                directory="/home/donald/Pictures/Temp")
        self.ui.editPath.setText(self.pathname)

    def image_search(self):
        import os
        def is_image(filename):
            f = filename.lower()
            return f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") \
                    or f.endswith(".bmp") or f.endswith(".gif")

        self.ui.labelWel.setVisible(False)
        self.ui.labelWait.setVisible(True)

        userpath = str(self.ui.editPath.text())
        image_filenames = [os.path.join(userpath, path) for path in os.listdir(userpath)
                           if is_image(path)]

        hashfunc = None
        hash_method = self.ui.comboAlg.currentText()
        if hash_method == 'AHash':
            hashfunc = average_hash
        elif hash_method == "PHash":
            hashfunc = phash

        self.images = {}
        for img in sorted(image_filenames):
            hash_value = hashfunc(Image.open(img))
            self.images[hash_value] = self.images.get(hash_value, []) + [img]

        self.image_show()

    def image_show(self):

        self.ui.labelWait.setVisible(False)
        self.ui.gridShow.setSpacing(10)
        self.grviews = []

        row, col = 0, 0
        for k, img_list in self.images.iteritems():
            if len(img_list) > 1:
                grview = QtGui.QGraphicsView()
                scene = QScene()
                pixmap = QtGui.QPixmap(img_list[0])
                scene.addPixmap(pixmap)
                grview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                grview.setScene(scene)
                self.ui.gridShow.addWidget(grview, row, col, 1, 1)
                col = (col + 1) % 4
                if col == 0:
                    row += 1

    def open_rm_dlg(self):
        rmdlg = RemoveDlg([1, 2])
        rmdlg.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mywin = MainWin()
    mywin.show()
    sys.exit(app.exec_())
