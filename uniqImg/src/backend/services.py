# -*- coding:utf-8 -*-
""" unique image backend

This module deal with some operation on images
including finding similar images, remove image files

"""

__all__ = ["find_simialr_imgs", "del_images"]

from PIL import Image
from imagehash import average_hash, phash, dhash
import os


def _get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def find_simialr_imgs(userpath, hash_method, search_depth):
    import os
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") \
                or f.endswith(".bmp") or f.endswith(".gif")
    # set up path searching depth
    searchfunc = None
    if search_depth == "current":
        searchfunc = os.listdir
    elif search_depth == "recursive":
        searchfunc = _get_filepaths
    else:
        searchfunc = os.listdir
    image_filenames = [unicode(os.path.join(userpath, path), 'utf-8')
                       for path in searchfunc(userpath.encode('utf-8'))
                        if is_image(path)]
    # set up hash function
    hashfunc = None
    if hash_method == 'aHash':
        hashfunc = average_hash
    elif hash_method == "pHash":
        hashfunc = phash
    elif hash_method == 'dHash':
        hashfunc = dhash
    # get image hash value and store them in a dictionary
    images_hash = {}
    for img in sorted(image_filenames):
        hash_value = hashfunc(Image.open(img))
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

    return images_cls


def del_images(imgs_list):
    info = "Successfully removed all the images."
    imgs_list_len = len(imgs_list)
    for idx in xrange(imgs_list_len):
        img = imgs_list.pop(0)
        try:
            os.remove(img)
        except OSError, e:
            info = "Fialed to delete file due to:\n %s"
            return False, info
    return True, info
