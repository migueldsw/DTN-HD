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

if __name__ == "__main__":
    for var in [("DATASET_ROOT_PATH: %s" % DATASET_ROOT_PATH),
                ("IMAGE_LIST_FILE: %s" % IMAGE_LIST_FILE),
                ("COMPLETE_TAGS_FILE: %s" % COMPLETE_TAGS_FILE),
                ("IMAGES_PATH: %s" % IMAGES_PATH),
                ("TEXT_DATA_FILE: %s" % TEXT_DATA_FILE),
                ("TAG_LIST_FILE: %s" % TAG_LIST_FILE)]:
        print (var)
