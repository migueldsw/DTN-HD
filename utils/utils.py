"""
General project utils
"""

import os.path

DATASET_ROOT_PATH = ''
IMAGE_LIST_FILE = ''
COMPLETE_TAGS_FILE = ''
IMAGES_PATH = ''
TEXT_DATA_FILE = ''
TAG_LIST_FILE = ''


with open(os.path.dirname(__file__) + '/../config.info') as f:
    content = f.readlines()
lines = [x.strip() for x in content]

DATASET_ROOT_PATH = lines[0]
IMAGE_LIST_FILE = DATASET_ROOT_PATH + lines[1]
COMPLETE_TAGS_FILE = DATASET_ROOT_PATH + lines[2]
IMAGES_PATH = DATASET_ROOT_PATH + lines[3]
TEXT_DATA_FILE = DATASET_ROOT_PATH + lines[4]
TAG_LIST_FILE = DATASET_ROOT_PATH + lines[5]
