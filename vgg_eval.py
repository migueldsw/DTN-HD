from dataset.dataset_loader import raw_img_X,y
from feature_extractor.vgg16 import create_vgg16, train_model, save_features
import numpy as np
import cv2
import datetime
if __name__ == "__main__":
    X = np.array([cv2.resize(im,(224,224)) for im in raw_img_X])
    y = y
    ct = datetime.datetime.now()
    print "Data loaded!\n training VGG..."
    net = create_vgg16()
    model = train_model(X,y,net,epoch=1)
    print "VGG16 trained!"
    print "Done 100 epochs in: "
    print(datetime.datetime.now())
    print "started in: "
    print ct
    save_features(X, model)
