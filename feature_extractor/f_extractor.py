from vgg16 import create_vgg16, train_model, extract_vgg_features, save_features
from pca import get_pc


def features_extract(X,y):
    net = create_vgg16(10)
    model = train_model(X, y, net, epoch=100)
    fx = extract_vgg_features(X,model)
    px = get_pc(fx, 1226)
    return px