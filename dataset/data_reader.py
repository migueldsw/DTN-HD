"""
Reads data set data files (images and texts)
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from dataset.utils import TEXT_DATA_FILE, TAG_LIST_FILE


def show_image(im):
    plt.imshow(im)
    plt.show()


def load_image(image_path, show=False):
    im = cv2.imread(image_path)
    if show:
        show_image(im)
    return im


def crop_image(img, x, y, w, h):
    return img[y: y + h, x: x + w]


def desc_image_list(img_list):
    shape_list = [i.shape for i in img_list]
    shape_list = np.array(shape_list)
    y_list = shape_list[:, 0]
    x_list = shape_list[:, 1]
    print('x min/max: %d / %d\ny min/max: %d / %d' % (np.min(x_list), np.max(x_list), np.min(y_list), np.max(y_list)))


def load_tags1k():
    # f = open(DATA_PATH, 'r')
    # lines =  [x.strip('\n') for x in f.readlines()]
    # TEMP STUB
    with open(TEXT_DATA_FILE) as myfile:
        head = [next(myfile) for x in xrange(500)]
    lines = head
    #
    nlines = []
    for l in lines:
        a = l.split("\t")
        nlines.append([int(i) for i in a[0:-1]])
    return np.array(nlines)


words_data = load_tags1k()


def load_tags(index_list):
    return np.array([words_data[i] for i in index_list])


def get_tags_list():
    print("Tag List")
    f = open(TAG_LIST_FILE, 'r')
    lines = [x.strip('\n') for x in f.readlines()]
    return np.array(lines)


def tags1k_words(occurrences):
    out = []
    for i in range(len(occurrences)):
        if occurrences[i] > 0:
            out.append(tag_list[i])
    return out


tag_list = get_tags_list()
tag_list = [i.split('\r')[0] for i in tag_list]
