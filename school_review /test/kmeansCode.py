import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

##############################################################################
# Binarize image data

im = np.array(Image.open('/home/drjr/Desktop/1.png').convert("L"))
h, w = im.shape
X = [(h - x, y) for x in range(h) for y in range(w) if im[x][y]]
X = np.array(X)
n_clusters = 4

##############################################################################
# Compute clustering with KMeans

k_means = KMeans(init='k-means++', n_clusters=n_clusters)
k_means.fit(X)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels_unique = np.unique(k_means_labels)

##############################################################################
# Plot result

colors = ['#4EACC5', '#FF9C34', '#4E9A06', '#FF3300']
plt.figure()
plt.hold(True)
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    plt.plot(X[my_members, 1], X[my_members, 0], 'w',
            markerfacecolor=col, marker='.')
    plt.plot(cluster_center[1], cluster_center[0], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=6)
plt.title('KMeans')
plt.grid(True)
plt.show()