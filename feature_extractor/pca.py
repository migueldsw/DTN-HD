"""
Run PCA

TEST TEST TEST ....
"""
import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

pca = PCA(n_components=2)

pca.fit(X)

# print(pca.explained_variance_ratio_)


pca = PCA(n_components=2, svd_solver='full')
x1 = pca.fit_transform(X)

# print(pca.explained_variance_ratio_)

pca = PCA(n_components=1, svd_solver='arpack')
x2 = pca.fit_transform(X)


# print(pca.explained_variance_ratio_)

# print('PCA...')
# print(X)
# print(x1)
# print(x2)

def get_pc(X, n):
    pca = PCA(n_components=n, svd_solver='arpack')
    x2 = pca.fit_transform(X)
    return x2
