"""
Loads all data set content
"""

import numpy as np
import pandas as pd
from utils import DATASET_ROOT_PATH, IMAGE_LIST_FILE, COMPLETE_TAGS_FILE

CATEGORIES_LIST = ['birds',
                   'building',
                   'cars',
                   'cat',
                   'dog',
                   'fish',
                   'flowers',
                   'horses',
                   'mountain',
                   'plane']


def read_text_file(path):
    """
    Read each line of a given (path) file
    :param path: file path
    :return: list of lines(text)
    """
    f = open(path, 'r')
    return [x.strip('\n') for x in f.readlines()]


def load_image_list():
    lines = read_text_file(DATASET_ROOT_PATH + IMAGE_LIST_FILE)
    nlines = []
    for l in lines:
        a = l.split("\\")
        category = a[0]
        file_name = a[1].split("_")
        prefix = file_name[0]
        img_id = file_name[1].split(".")[0]
        nlines.append([category, prefix, img_id])
    nlines = np.array(nlines)
    imagelist = pd.DataFrame(nlines)
    imagelist.columns = ['category', 'prefix', 'PID']
    # imagelist['words_data_index'] = pd.DataFrame(np.array(xrange(imagelist.shape[0])))
    # imagelist.set_index('PID', inplace=True)
    return imagelist


def load_all_tags():
    lines = read_text_file(DATASET_ROOT_PATH + COMPLETE_TAGS_FILE)
    nlines = []
    for l in lines:
        a = l.split("      ")
        if len(a) == 2:
            a[1] = a[1].split(" ")
            a[0] = int(a[0])
        elif len(a) == 1:
            a = [a[0], []]
        nlines.append(a)
    all_tags = pd.DataFrame(nlines)
    all_tags.columns = ['PID', 'all_tags']
    # all_tags.set_index('PID', inplace=True)
    return all_tags['all_tags']


def load_all_data():
    imagelist = load_image_list()
    all_tags = load_all_tags()
    all_data = pd.concat([imagelist, all_tags], axis=1)
    print all_data.shape
    return all_data


if __name__ == "__main__":
    all_data = load_all_data()
    print("All data len.: %d" % len(all_data))
