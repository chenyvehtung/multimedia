# -*- coding:utf-8 -*-

from ui.rm_dlg_ui import Ui_viewDialog
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMessageBox
import sys
# from backend.services import del_images
from backend.services_thread import DelFileThread


class RemoveDlg(QtGui.QDialog):
    def __init__(self, img_list, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_viewDialog()
        self.ui.setupUi(self)
        self.img_list = img_list

        model = QtGui.QStandardItemModel()
        for idx in xrange(len(img_list)):
            item = QtGui.QStandardItem(unicode(img_list[idx][0]))
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
        cur_img = unicode(self.img_list[idx][0])
        scene = QtGui.QGraphicsScene()
        pixmap = QtGui.QPixmap(cur_img)
        img_width = self.ui.graphicsView.size().width()
        pixmap = pixmap.scaledToWidth(int(img_width) - 5)
        scene.addPixmap(pixmap)
        self.ui.graphicsView.setScene(scene)

    def rm_imgs(self):
        self.rm_imgs_id = []
        model = self.ui.listView.model()
        for idx in xrange(model.rowCount()):
            item = model.item(idx)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                self.rm_imgs_id.append(idx)

        if len(self.rm_imgs_id) > 0:
            msg_text = "Do you really want to remove the selected %d images?" % len(self.rm_imgs_id)
            ans = QMessageBox.question(None, "Remove Images", msg_text,
                                    QMessageBox.Yes or QMessageBox.No, QMessageBox.No)
            if ans == QMessageBox.Yes:
                self.del_img_thread = DelFileThread()
                self.del_img_thread.set_params([unicode(self.img_list[idx][0]) for idx in self.rm_imgs_id])
                self.del_img_thread.finishSignal.connect(self.show_results)
                self.del_img_thread.start()
        else:
            QMessageBox.information(None, "Remove Images",
                                    "You haven't selected any images yet, please check some.",
                                    QMessageBox.Ok)

    def show_results(self, info_list):
        status, info = info_list
        if status:
            QMessageBox.information(None, "Remove Succeed", info, QMessageBox.Ok)
            # remove the delete images from img_list
            offset = 0
            for idx in self.rm_imgs_id:
                del self.img_list[idx - offset]
                offset += 1
        else:
            QMessageBox.warning(None, "Remove Failed", info)
        self.close()

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
