# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PyQt4 import QtCore
from PIL import Image
from imagehash import average_hash, phash, dhash
import os
import numpy as np


__all__ = ["FindImgThread", "DelFileThread"]


class Singleton(QtCore.QThread):
    """Singleton Class
    This is a class to make thread being a Singleton class.
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class FindImgThread(Singleton):
    progressBarSignal = QtCore.pyqtSignal(int)
    finishSignal = QtCore.pyqtSignal(dict)
    disabledSignal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super(FindImgThread, self).__init__(parent)
        self.bar_num = 2

    def set_params(self, userpath, hash_method, search_depth):
        self.userpath = userpath
        self.hash_method = hash_method
        self.search_depth = search_depth

    def get_filepaths(self, directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        return file_paths

    def is_image(self, filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") \
                or f.endswith(".bmp") or f.endswith(".gif")

    def run(self):
        self.disabledSignal.emit(True)
        self.progressBarSignal.emit(self.bar_num)
        # set up path searching depth
        searchfunc = None
        if self.search_depth == "current":
            searchfunc = os.listdir
        elif self.search_depth == "recursive":
            searchfunc = self.get_filepaths
        else:
            searchfunc = os.listdir
        image_filenames = [os.path.join(self.userpath, path).encode('utf-8')
                            for path in searchfunc(self.userpath.encode('utf-8'))
                            if self.is_image(path)]
        self.bar_num += 30
        self.progressBarSignal.emit(self.bar_num)
        # set up hash function
        hashfunc = None
        if self.hash_method == 'aHash':
            hashfunc = average_hash
        elif self.hash_method == "pHash":
            hashfunc = phash
        elif self.hash_method == 'dHash':
            hashfunc = dhash
        # get image hash value and store them in a dictionary
        images_hash = {}
        img_cnt = 0
        img_interval = int(np.ceil(len(image_filenames) / 50.0))
        for img in sorted(image_filenames):
            img_cnt += 1
            if img_cnt % img_interval == 0:
                self.bar_num += 1
                self.progressBarSignal.emit(self.bar_num)
            try:
                pil_img = Image.open(img)
            except IOError:
                continue
            hash_value = hashfunc(pil_img)
            images_hash[img] = [hash_value, 0]
        # classfy the images
        images_cls = {}
        while True:
            cnt = 0
            # find the image that hasn't been classified as the new class entrance
            for k, v in images_hash.iteritems():
                if v[1] != 0:
                    cnt += 1
                else:  # image is not classified
                    cur_cls = len(images_cls) + 1
                    entrance_img_hash = v[0]

                    images_cls[cur_cls] = []
                    images_cls[cur_cls].append([k, str(entrance_img_hash)])

                    images_hash[k][1] = cur_cls
                    break
            # if all the image are classified, break
            if cnt >= len(images_hash):
                break
            # find the similar image and append to the current class
            for k, v in images_hash.iteritems():
                if v[1] == 0 and v[0] - entrance_img_hash <= 8:
                    images_cls[cur_cls].append([k, str(v[0])])
                    # update class in the hash table
                    images_hash[k][1] = cur_cls

        self.progressBarSignal.emit(100)
        self.finishSignal.emit(images_cls)
        self.disabledSignal.emit(False)


class DelFileThread(Singleton):
    finishSignal = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(DelFileThread, self).__init__(parent)
        self.info = "Successfully removed all the images."

    def set_params(self, imgs_list):
        self.imgs_list = imgs_list

    def run(self):
        is_success = True
        imgs_list_len = len(self.imgs_list)
        for idx in xrange(imgs_list_len):
            img = self.imgs_list.pop(0)
            try:
                os.remove(img)
            except OSError, e:
                self.info = "Fialed to delete file due to:\n %s"
                # return False, info
                is_success = False
                break
        self.finishSignal.emit([is_success, self.info])
