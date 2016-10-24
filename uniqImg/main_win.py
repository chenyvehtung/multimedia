# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_uniqimg
from backend.services import find_simialr_imgs
from rm_dlg import RemoveDlg

__all__ = ["MainWin"]


class QScene(QtGui.QGraphicsScene):
    clicked = QtCore.pyqtSignal(str)

    def __init__(self, obj_hash):
        QtGui.QGraphicsScene.__init__(self)
        self.obj_hash = obj_hash

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(self.obj_hash)


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_uniqimg()
        self.ui.setupUi(self)

        self.label_show("labelWel")

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
        self.label_show("labelWait")
        userpath = str(self.ui.editPath.text())
        hash_method = self.ui.comboAlg.currentText()
        self.images = find_simialr_imgs(userpath, hash_method)
        self.image_show()

    def image_show(self):
        self.label_show()
        self.ui.gridShow.setSpacing(10)
        self.grviews = []

        row, col = 0, 0
        for k, img_list in self.images.iteritems():
            if len(img_list) > 1:
                grview = QtGui.QGraphicsView()
                scene = QScene(obj_hash=str(k))
                pixmap = QtGui.QPixmap(img_list[0])
                scene.addPixmap(pixmap)
                scene.clicked.connect(self.open_rm_dlg)
                grview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                grview.setScene(scene)
                self.ui.gridShow.addWidget(grview, row, col, 1, 1)
                col = (col + 1) % 4
                if col == 0:
                    row += 1

    def open_rm_dlg(self, hash_value):
        rmdlg = RemoveDlg(self.images[str(hash_value)])
        rmdlg.exec_()
        # clear all the image in gridShow
        while self.ui.gridShow.count() > 0:
            item = self.ui.gridShow.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if isinstance(w, QtGui.QGraphicsView):
                w.deleteLater()
        # reshow gridShow for update
        self.image_show()

    def label_show(self, label_name="labelHide"):
        self.ui.labelWel.setVisible(False)
        self.ui.labelWait.setVisible(False)
        if label_name == "labelWait":
            self.ui.labelWait.setVisible(True)
        elif label_name == "labelWel":
            self.ui.labelWel.setVisible(True)
        else:
            pass  # hide all of the label
