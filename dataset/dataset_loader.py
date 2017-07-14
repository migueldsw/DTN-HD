"""
Loads all data set content
"""

import numpy as np
import pandas as pd
from utils import IMAGE_LIST_FILE, COMPLETE_TAGS_FILE

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
    lines = read_text_file(IMAGE_LIST_FILE)
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
    lines = read_text_file(COMPLETE_TAGS_FILE)
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
    return pd.concat([imagelist, all_tags], axis=1)


def get_category(category):
    """
    get all instances from the same category
    :param category: category label string
    :return: data frame with category instances
    """
    return FULL_DATA.loc[FULL_DATA['category'] == category]


FULL_DATA = load_all_data()
DATA = pd.DataFrame()
for cat in CATEGORIES_LIST:
    DATA = DATA.append(get_category(cat))

if __name__ == "__main__":
    print ("All data: ")
    print (FULL_DATA.head())
    print ("Shape: %s" % str(FULL_DATA.shape))
    print("Full data len.: %d" % len(FULL_DATA))
    print("Data len.: %d" % len(DATA))
