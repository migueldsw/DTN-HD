import numpy as np
import cv2
from matplotlib.pyplot import imshow
from PIL import Image
from keras import backend as K
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import Flatten
from keras.layers import MaxPooling2D as MaxPool
from keras.models import Model
from dataset.utils import save_cache


def create_vgg16(num_classes=10):
    img_input = Input(shape=(224, 224, 3))
    # block 1
    net = Conv2D(64, (3, 3), activation='relu', padding='same', name='conv1_1')(img_input)
    net = Conv2D(64, (3, 3), activation='relu', padding='same', name='conv1_2')(net)
    net = MaxPool((2, 2), strides=(2, 2), name='maxpool1')(net)
    # block 2
    net = Conv2D(128, (3, 3), activation='relu', padding='same', name='conv2_1')(net)
    net = Conv2D(128, (3, 3), activation='relu', padding='same', name='conv2_2')(net)
    net = MaxPool((2, 2), strides=(2, 2), name='maxpool2')(net)
    # block 3
    net = Conv2D(256, (3, 3), activation='relu', padding='same', name='conv3_1')(net)
    net = Conv2D(256, (3, 3), activation='relu', padding='same', name='conv3_2')(net)
    net = Conv2D(256, (3, 3), activation='relu', padding='same', name='conv3_3')(net)
    net = MaxPool((2, 2), strides=(2, 2), name='maxpool3')(net)
    # block 4
    net = Conv2D(512, (3, 3), activation='relu', padding='same', name='conv4_1')(net)
    net = Conv2D(512, (3, 3), activation='relu', padding='same', name='conv4_2')(net)
    net = Conv2D(512, (3, 3), activation='relu', padding='same', name='conv4_3')(net)
    net = MaxPool((2, 2), strides=(2, 2), name='maxpool4')(net)
    # block 5
    net = Conv2D(512, (3, 3), activation='relu', padding='same', name='conv5_1')(net)
    net = Conv2D(512, (3, 3), activation='relu', padding='same', name='conv5_2')(net)
    net = Conv2D(512, (3, 3), activation='relu', padding='same', name='conv5_3')(net)
    net = MaxPool((2, 2), strides=(2, 2), name='maxpool5')(net)

    # classification block
    net = Flatten(name='flatten')(net)
    net = Dense(4096, activation='relu', name='fc1')(net)
    net = Dense(4096, activation='relu', name='fc2')(net)
    net = Dense(num_classes, activation='softmax', name='predictions')(net)

    model = Model(inputs=img_input, outputs=net)
    return model


def train_model(X, y, model, epoch=50):
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X, y, batch_size=8, epochs=epoch, verbose=1)
    return model


def extract_vgg_features(X, model):
    layer_index = 21
    features = []
    inpt = model.input
    output = model.layers[layer_index].output
    func = K.function([inpt]+[K.learning_phase()], [output])
    for x in X:
        features.append(func([np.array([x])]))
    features = np.array(features)
    features = features.reshape((features.shape[0], features.shape[-1]))
    return features


def save_features(data, model):
    features = extract_vgg_features(data, model)
    save_cache('xf', features)

if __name__ == "__main__":
    model = create_vgg16()