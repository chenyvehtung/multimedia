# -*- coding:utf-8 -*-

from ui.rm_dlg_ui import Ui_viewDialog
from PyQt4 import QtGui, QtCore
import sys
from backend.services import del_images


class RemoveDlg(QtGui.QDialog):
    def __init__(self, img_list, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_viewDialog()
        self.ui.setupUi(self)
        self.img_list = img_list

        model = QtGui.QStandardItemModel()
        for idx in xrange(len(img_list)):
            item = QtGui.QStandardItem(str(img_list[idx]))
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setCheckable(True)
            model.appendRow(item)
        self.ui.listView.setModel(model)

        QtCore.QObject.connect(self.ui.buttonRemove, QtCore.SIGNAL("clicked()"),
                               self.rm_imgs)
        QtCore.QObject.connect(self.ui.buttonCancel, QtCore.SIGNAL("clicked()"),
                               self.close)
        self.ui.checkBoxAll.stateChanged.connect(self.check_all)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_listView_clicked(self, index):
        self.image_show(int(index.row()))

    def image_show(self, idx):
        # print idx
        cur_img = self.img_list[idx]
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(cur_img))
        self.ui.graphicsView.setScene(scene)

    def rm_imgs(self):
        rm_imgs_id = []
        model = self.ui.listView.model()
        for idx in xrange(model.rowCount()):
            item = model.item(idx)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                rm_imgs_id.append(idx)

        from PyQt4.QtGui import QMessageBox
        if len(rm_imgs_id) > 0:
            msg_text = "Do you really want to remove the selected %d images?" % len(rm_imgs_id)
            ans = QMessageBox.question(None, "Remove Images", msg_text,
                                    QMessageBox.Yes or QMessageBox.No, QMessageBox.No)
            if ans == QMessageBox.Yes:
                status, info = del_images([self.img_list[idx] for idx in rm_imgs_id])
                if status:
                    QMessageBox.information(None, "Remove Succeed", info, QMessageBox.Ok)
                    # remove the delete images from img_list
                    offset = 0
                    for idx in rm_imgs_id:
                        del self.img_list[idx - offset]
                        offset += 1
                else:
                    QMessageBox.warning(None, "Remove Failed", info)
                self.close()
        else:
            QMessageBox.information(None, "Remove Images",
                                    "You haven't selected any images yet, please check some.",
                                    QMessageBox.Ok)

    def check_all(self):
        model = self.ui.listView.model()
        if self.ui.checkBoxAll.isChecked():
            for idx in xrange(model.rowCount()):
                item = model.item(idx)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                    item.setCheckState(QtCore.Qt.Checked)
        else:
            for idx in xrange(model.rowCount()):
                item = model.item(idx)
                if item.isCheckable():
                    item.setCheckState(QtCore.Qt.Unchecked)
