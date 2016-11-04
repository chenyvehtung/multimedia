# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PIL import Image
from imagehash import average_hash, phash, dhash
import os


class FindImgThread(QtCore.QThread):
    progressBarSignal = QtCore.pyqtSignal(int)
    finishSignal = QtCore.pyqtSignal(dict)

    def __init__(self, userpath, hash_method, search_depth, parent=None):
        super(FindImgThread, self).__init__(parent)
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
        self.progressBarSignal.emit(10)
        # set up path searching depth
        searchfunc = None
        if self.search_depth == "current":
            searchfunc = os.listdir
        elif self.search_depth == "recursive":
            searchfunc = self.get_filepaths
        else:
            searchfunc = os.listdir
        image_filenames = [unicode(os.path.join(self.userpath, path), 'utf-8')
                           for path in searchfunc(self.userpath.encode('utf-8'))
                            if self.is_image(path)]
        self.progressBarSignal.emit(50)
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
        for img in sorted(image_filenames):
            #try:
            #    img = 
            #except IOError:
            #    continue
            hash_value = hashfunc(Image.open(img))
            images_hash[img] = [hash_value, 0]
        self.progressBarSignal.emit(70)
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
