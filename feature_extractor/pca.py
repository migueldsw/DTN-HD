"""
Run PCA
"""
from sklearn.decomposition import PCA
from dataset.utils import save_cache


def get_pc(X, n):
    pca = PCA(n_components=n, svd_solver='arpack') #svd_solver='full'
    px = pca.fit_transform(X)
    # print(pca.explained_variance_ratio_)
    save_cache("pcx", px)
    return px
