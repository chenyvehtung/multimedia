#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_imgpro
from ui.gd_dlg_ui import Ui_Dialog
from backend.services_thread import ResizeImgThread, BlurImgThread


__all__ = ["MainWin"]


class GdDlg(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_imgpro()
        self.ui.setupUi(self)

        self.progressBar = QtGui.QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        self.ui.statusbar.addPermanentWidget(self.progressBar)

        self.label_show("labelWel")

        QtCore.QObject.connect(self.ui.buttonOpen, QtCore.SIGNAL("clicked()"),
                               self.file_dialog)
        QtCore.QObject.connect(self.ui.buttonDefault, QtCore.SIGNAL("clicked()"),
                               self.image_default)
        QtCore.QObject.connect(self.ui.buttonSave, QtCore.SIGNAL("clicked()"),
                               self.image_save)
        QtCore.QObject.connect(self.ui.buttonResize, QtCore.SIGNAL("clicked()"),
                               self.image_resize)
        QtCore.QObject.connect(self.ui.buttonBlur, QtCore.SIGNAL("clicked()"),
                               self.image_blur)

        self.ui.buttonOpen.setAutoDefault(True)
        self.ui.editH.returnPressed.connect(self.ui.buttonResize.click)
        self.ui.editW.returnPressed.connect(self.ui.buttonResize.click)
        self.ui.editS.returnPressed.connect(self.ui.buttonBlur.click)

    # setting up the actions
    @QtCore.pyqtSlot()
    def on_actionHomepage_triggered(self):
        self.clr_imgs()
        self.label_show("labelWel")

    @QtCore.pyqtSlot()
    def on_actionOpen_Image_triggered(self):
        self.file_dialog()

    @QtCore.pyqtSlot()
    def on_actionSave_Image_triggered(self):
        self.image_save()

    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        QtGui.QMessageBox.about(None, "About ImgPro",
            "<p align='center' style='font-size:16pt'><b>Im</b>a<b>g</b>e <b>Pro</b>cess "
            "is a simple application that helps you to process image</p>"
            "<p align='center' style='font-size:12pt'>Developed by <b>Lisa</b>.</p>"
            "<p align='center' style='font-size:12pt'>Nov. 2016</p>")

    @QtCore.pyqtSlot()
    def on_actionUser_Guide_triggered(self):
        gd_dlg = GdDlg()
        gd_dlg.exec_()

    def file_dialog(self):
        from os.path import expanduser
        fd = QtGui.QFileDialog(self)
        self.img_name = fd.getOpenFileName(caption="Open Image",
                                            directory=expanduser("~"),
                                            filter="Images (*.png *.gif *.jpg *.bmp *.jpeg)")
        self.image_default()

    def image_default(self):
        pix = QtGui.QPixmap(self.img_name)
        self.ui.editH.setText(str(pix.height()))
        self.ui.editW.setText(str(pix.width()))
        self.ui.editS.setText("0")
        self.image_show(pix)

    def image_save(self):
        fd = QtGui.QFileDialog(self)
        cur_dir = '/'.join(str(self.img_name).split('/')[:-1])
        save_name = fd.getSaveFileName(caption="Save Image",
                                       directory=cur_dir,
                                       filter="Images (*.png *.gif *.jpg *.bmp *.jpeg)")
        self.pix.save(save_name)

    def image_resize(self):
        self.clr_imgs()
        self.label_show("labelWait")

        resize_h = int(self.ui.editH.text())
        resize_w = int(self.ui.editW.text())
        self.resize_img_thread = ResizeImgThread()
        self.resize_img_thread.set_params(str(self.img_name), resize_h, resize_w)
        self.resize_img_thread.finishSignal.connect(self.ndarr2pix)
        self.resize_img_thread.progressBarSignal.connect(self.progressBar.setValue)
        self.resize_img_thread.disabledSignal.connect(self.set_rel_widget_disabled)
        self.resize_img_thread.start()

    def image_blur(self):
        self.clr_imgs()
        self.label_show("labelWait")

        filter_len = int(self.ui.editS.text())
        self.blur_img_thread = BlurImgThread()
        self.blur_img_thread.set_params(str(self.img_name), filter_len)
        self.blur_img_thread.finishSignal.connect(self.ndarr2pix)
        self.blur_img_thread.progressBarSignal.connect(self.progressBar.setValue)
        self.blur_img_thread.disabledSignal.connect(self.set_rel_widget_disabled)
        self.blur_img_thread.start()

    def ndarr2pix(self, ndarr):
        height, width, channels = ndarr.shape
        img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
        for x in xrange(width):
            self.progressBar.setValue(int(float(x) / width * 10.0) + 90)
            for y in xrange(height):
                img.setPixel(x, y, QtGui.QColor(*ndarr[y][x]).rgb())

        pix = QtGui.QPixmap.fromImage(img)
        self.progressBar.setValue(100)
        self.image_show(pix)

    def image_show(self, image):
        self.pix = image

        # clear the image shown before
        self.clr_imgs()
        self.label_show()

        grview = QtGui.QGraphicsView()
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(image)
        grview.setScene(scene)
        self.ui.gridShow.addWidget(grview)

    def label_show(self, label_name="labelHide"):
        self.ui.labelWel.setVisible(False)
        self.ui.labelWait.setVisible(False)
        self.progressBar.hide()
        if label_name == "labelWait":
            self.ui.labelWait.setVisible(True)
            self.progressBar.show()
            self.ui.statusbar.showMessage("  Processing...")
        elif label_name == "labelWel":
            self.ui.labelWel.setVisible(True)
            self.ui.statusbar.showMessage("  Welcome")
            self.ui.editH.setText("")
            self.ui.editW.setText("")
            self.ui.editS.setText("")
        else:
            self.ui.statusbar.showMessage("  All done")

    def clr_imgs(self):
        while self.ui.gridShow.count() > 0:
            item = self.ui.gridShow.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if isinstance(w, QtGui.QGraphicsView):
                w.deleteLater()

    def set_rel_widget_disabled(self, b):
        self.ui.buttonOpen.setDisabled(b)
        self.ui.buttonDefault.setDisabled(b)
        self.ui.buttonSave.setDisabled(b)
        self.ui.editH.setDisabled(b)
        self.ui.editW.setDisabled(b)
        self.ui.buttonResize.setDisabled(b)
        self.ui.editS.setDisabled(b)
        self.ui.buttonBlur.setDisabled(b)

        self.ui.actionOpen_Image.setDisabled(b)
        self.ui.actionHomepage.setDisabled(b)
        self.ui.actionSave_Image.setDisabled(b)
