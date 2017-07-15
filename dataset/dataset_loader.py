"""
Loads all data set content
"""

import numpy as np
import pandas as pd
from data_reader import load_image, get_text_data
from utils import IMAGE_LIST_FILE, COMPLETE_TAGS_FILE, IMAGES_PATH, check_cache_path, save_cache, load_cache

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


def image_file_path(index):
    inst = FULL_DATA.iloc[index]
    file_path = IMAGES_PATH + '%s/%s_%s.jpg' % (inst.category, inst.prefix, inst.PID)
    return file_path


def desc_images(img_list):
    shape_list = [i.shape for i in img_list]
    shape_list = np.array(shape_list)
    y_list = shape_list[:, 0]
    x_list = shape_list[:, 1]
    print('x min/max: %d / %d\ny min/max: %d / %d' % (np.min(x_list), np.max(x_list), np.min(y_list), np.max(y_list)))


def raw_image_x():
    """
    Compose image img_X from DATA
    :return: list of image data: [np.array{shape: h,w,3}]
    """
    index_list = DATA.index.values
    return load_image([image_file_path(i) for i in index_list])


def raw_txt_x():
    return get_text_data(DATA.index.values)


def one_hot_category_encode(category):
    out = np.zeros(10)
    for i in range(len(CATEGORIES_LIST)):
        if category == CATEGORIES_LIST[i]:
            out[i] = 1
    if out.sum() == 0:
        raise ValueError('Unknown category!!!')
    return out


def raw_one_hot_y():
    return np.array([one_hot_category_encode(s) for s in DATA['category'].tolist()])


FULL_DATA = load_all_data()
DATA = pd.DataFrame()  # data of interest
for cat in CATEGORIES_LIST:
    DATA = DATA.append(get_category(cat))
if check_cache_path():
    raw_img_X = load_cache('img_x')
    raw_txt_X = load_cache('txt_x')
    y = load_cache('y')
else:
    raw_img_X = raw_image_x()
    raw_txt_X = raw_txt_x()
    y = raw_one_hot_y()
    save_cache('img_x', raw_img_X)
    save_cache('txt_x', raw_txt_X)
    save_cache('y', y)

if __name__ == "__main__":
    print ("All data: ")
    print (FULL_DATA.head())
    print ("Shape: %s" % str(FULL_DATA.shape))
    print ("Full data len.: %d" % len(FULL_DATA))
    print ("Data len.: %d" % len(DATA))
    print ("test image ...")
    ip = image_file_path(79233)
    print (ip)
    im = load_image(ip, show=False)
    print (im.shape)
    print ("Image X: shape:")
    print (raw_img_X.shape)
    desc_images(raw_img_X)
    print ("Text X: shape:")
    print (raw_txt_X.shape)
    print ("Y: shape:")
    print (y.shape)
