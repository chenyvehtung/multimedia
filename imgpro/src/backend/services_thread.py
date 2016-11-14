# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QPixmap
from PIL import Image
import os
import numpy as np


__all__ = ["ResizeImgThread", "BlurImgThread"]


class Singleton(QtCore.QThread):
    """Singleton Class
    This is a class to make thread being a Singleton class.
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class ResizeImgThread(Singleton):
    progressBarSignal = QtCore.pyqtSignal(int)
    finishSignal = QtCore.pyqtSignal(np.ndarray)
    disabledSignal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super(ResizeImgThread, self).__init__(parent)

    def set_params(self, imgpath, resize_h, resize_w):
        self.imgpath = imgpath
        self.resize_h = resize_h
        self.resize_w = resize_w

    def run(self):
        self.disabledSignal.emit(True)

        input_img = np.array(Image.open(self.imgpath))
        old_height, old_width, old_channels = input_img.shape
        x_scale = float(self.resize_h) / old_height
        y_scale = float(self.resize_w) / old_width

        output_img = np.zeros((self.resize_h, self.resize_w, old_channels), dtype=np.uint8)
        for xidx in xrange(self.resize_h):
            self.progressBarSignal.emit(int(float(xidx) / self.resize_h * 90.0))
            old_x = float(xidx) / x_scale
            for yidx in xrange(self.resize_w):
                old_y = float(yidx) / y_scale
                if old_x.is_integer() or old_y.is_integer():
                    output_img[xidx, yidx] = input_img[int(old_x), int(old_y)]
                else:  # use bilinear interpolation
                    x1 = int(np.floor(old_x))
                    x2 = int(np.ceil(old_x)) if int(np.ceil(old_x)) < old_height else old_height - 1
                    y1 = int(np.floor(old_y))
                    y2 = int(np.ceil(old_y)) if int(np.ceil(old_y)) < old_width else old_width - 1

                    q11 = input_img[x1, y1]
                    q12 = input_img[x1, y2]
                    q21 = input_img[x2, y1]
                    q22 = input_img[x2, y2]

                    output_img[xidx, yidx] = (q11 * (x2 - old_x) * (y2 - old_y)
                                            + q21 * (old_x - x1) * (y2 - old_y)
                                            + q12 * (x2 - old_x) * (old_y - y1)
                                            + q22 * (old_x - x1) * (old_y - y1)) \
                                            / ((x2 - x1) * (y2 - y1) + 1e-10)
        self.finishSignal.emit(output_img)
        self.disabledSignal.emit(False)


class BlurImgThread(Singleton):
    progressBarSignal = QtCore.pyqtSignal(int)
    finishSignal = QtCore.pyqtSignal(np.ndarray)
    disabledSignal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super(BlurImgThread, self).__init__(parent)

    def set_params(self, imgpath, filter_len):
        self.imgpath = imgpath
        self.avg_filter = self.gen_avg_filter(filter_len)

    def gen_avg_filter(self, filter_len):
        return 1.0 / (filter_len * filter_len) * np.ones((filter_len, filter_len))

    def run(self):
        self.disabledSignal.emit(True)

        input_img = np.array(Image.open(self.imgpath))
        height, width, channels = input_img.shape
        output_img = np.zeros_like(input_img)
        # rotate the filter by 180 degree
        filter_rt = np.rot90(self.avg_filter, 2)
        # add zero-padding
        filter_len =  filter_rt.shape[0]
        pad_len = filter_len / 2
        pad_h = np.zeros((pad_len, width, channels))
        pad_img = np.vstack((pad_h, input_img, pad_h))
        pad_v = np.zeros((height + 2 * pad_len, pad_len, channels))
        pad_img = np.hstack((pad_v, pad_img, pad_v))
        self.progressBarSignal.emit(10)
        # convolution on pad image
        for row in xrange(height):
            self.progressBarSignal.emit(int(float(row) / height * 80.0) + 10)
            for col in xrange(width):
                img_patch = pad_img[row:row + filter_len, col:col + filter_len]
                # transpose to make img_patch as in R G B plane, multiply by broadcasting
                conv = np.multiply(filter_rt, img_patch.transpose((2, 0, 1)))
                output_img[row][col] = np.sum(np.sum(conv, axis=1), axis=1)

        self.finishSignal.emit(output_img)
        self.disabledSignal.emit(False)
