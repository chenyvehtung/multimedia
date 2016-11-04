# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_uniqimg
from ui.gd_dlg_ui import Ui_Dialog
# from backend.services import find_simialr_imgs
from rm_dlg import RemoveDlg
from backend.services_thread import FindImgThread


__all__ = ["MainWin"]


class GdDlg(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class QScene(QtGui.QGraphicsScene):
    clicked = QtCore.pyqtSignal(int)

    def __init__(self, obj_cls):
        QtGui.QGraphicsScene.__init__(self)
        self.obj_cls = obj_cls

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(self.obj_cls)


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_uniqimg()
        self.ui.setupUi(self)

        self.progressBar = QtGui.QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        self.ui.statusbar.addPermanentWidget(self.progressBar)

        self.init_toolbar()
        self.label_show("labelWel")

        QtCore.QObject.connect(self.ui.buttonOpen, QtCore.SIGNAL("clicked()"),
                               self.file_dialog)
        QtCore.QObject.connect(self.ui.buttonSearch, QtCore.SIGNAL("clicked()"),
                               self.image_search)
        self.ui.buttonSearch.setAutoDefault(True)
        self.ui.editPath.returnPressed.connect(self.ui.buttonSearch.click)

    def init_toolbar(self):
        self.ui.toolBar.setStyleSheet("spacing:8px; padding:2px;")
        self.comboAlg = QtGui.QComboBox()
        self.comboAlg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.toolBar.addWidget(self.comboAlg)
        self.comboAlg.insertItems(1, ["aHash", "pHash", "dHash"])
        self.comboAlg.setToolTip("Hash Algorithm")

        self.comboMethod = QtGui.QComboBox()
        self.comboMethod.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.toolBar.addWidget(self.comboMethod)
        self.comboMethod.insertItems(1, ["recursive", "current"])
        self.comboMethod.setToolTip("Search Depth")

    # setting up the actions
    @QtCore.pyqtSlot()
    def on_actionHomepage_triggered(self):
        self.clr_imgs()
        self.label_show("labelWel")

    @QtCore.pyqtSlot()
    def on_actionOpen_Folder_triggered(self):
        self.file_dialog()

    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        QtGui.QMessageBox.about(None, "About UniqImg",
            "<p align='center' style='font-size:16pt'><b>Uniq</b>ue <b>Im</b>a<b>g</b>e"
            "is simple application that helps you to remove some duplicate images</p>"
            "<p align='center' style='font-size:12pt'>Developed by <b>Donald</b>.</p>"
            "<p align='center' style='font-size:12pt'>Oct. 2016</p>")

    @QtCore.pyqtSlot()
    def on_actionUser_Guide_triggered(self):
        gd_dlg = GdDlg()
        gd_dlg.exec_()

    def file_dialog(self):
        from os.path import expanduser
        fd = QtGui.QFileDialog(self)
        self.pathname = fd.getExistingDirectory(caption="Open Folder",
                                                directory=expanduser("~"))
        self.ui.editPath.setText(self.pathname)
        self.ui.editPath.setFocus(True)

    def image_search(self):
        self.clr_imgs()
        self.label_show("labelWait")

        userpath = unicode(self.ui.editPath.text())
        hash_method = self.comboAlg.currentText()
        search_depth = self.comboMethod.currentText()
        self.find_img_thread = FindImgThread(userpath, hash_method, search_depth)
        self.find_img_thread.finishSignal.connect(self.image_show)
        self.find_img_thread.progressBarSignal.connect(self.progressBar.setValue)
        self.find_img_thread.start()

    def image_show(self, images):
        self.images = images

        # clear the images shown before
        self.clr_imgs()
        self.label_show()

        self.ui.gridShow.setSpacing(10)
        self.grviews = []

        row, col = 0, 0
        no_duplicate = True
        for k, img_list in images.iteritems():
            if len(img_list) > 1:
                no_duplicate = False
                grview = QtGui.QGraphicsView()
                scene = QScene(obj_cls=int(k))
                pixmap = QtGui.QPixmap(unicode(img_list[0][0]))
                pixmap = pixmap.scaled(grview.size().height() / 2,
                                       grview.size().width() / 2,
                                       QtCore.Qt.KeepAspectRatio)
                scene.addPixmap(pixmap)
                scene.clicked.connect(self.open_rm_dlg)
                grview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                grview.setScene(scene)
                grview.setToolTip("Click to show detail")
                self.ui.gridShow.addWidget(grview, row, col, 1, 1)

                col = (col + 1) % 4
                if col == 0:
                    row += 1
        if no_duplicate:
            self.label_show("labelCon")

    def open_rm_dlg(self, img_cls):
        rmdlg = RemoveDlg(self.images[int(img_cls)])
        rmdlg.exec_()
        # reshow gridShow for update
        self.image_show(self.images)

    def label_show(self, label_name="labelHide"):
        self.ui.labelWel.setVisible(False)
        self.ui.labelWait.setVisible(False)
        self.ui.labelCon.setVisible(False)
        self.progressBar.hide()
        if label_name == "labelWait":
            self.ui.labelWait.setVisible(True)
            self.progressBar.show()
            self.ui.statusbar.showMessage("  Searching...")
            # print "Searching....."
        elif label_name == "labelWel":
            self.ui.labelWel.setVisible(True)
            self.ui.statusbar.showMessage("  Welcome")
            self.ui.editPath.setText("")
        elif label_name == "labelCon":
            self.ui.labelCon.setVisible(True)
            self.ui.statusbar.showMessage("  No duplicate")
        else:
            self.ui.statusbar.showMessage("  All done")

    def clr_imgs(self):
        import sip
        while self.ui.gridShow.count() > 0:
            item = self.ui.gridShow.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if isinstance(w, QtGui.QGraphicsView):
                w.deleteLater()
