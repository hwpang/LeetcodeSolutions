from typing import List
import numpy as np
import matplotlib.pyplot as plt

class KMeans(object):
    
    def __init__(self, data: np.ndarray, k: int=3):
        assert isinstance(data, np.ndarray)
        assert isinstance(k, int)
        assert len(data.shape) == 2
        
        self.data = data
        self.k = k
        self.centroids = self.data[np.random.choice(len(self.data), self.k, replace=False)]
        self.cluster_assignment = np.array([0 for _ in range(len(self.data))])

    def fit(self):

        while True:
            
            updated = False
            for data_ind, data_point in enumerate(self.data):
                min_distance = np.inf
                min_distance_index = None
                for centroid_index, centroid in enumerate(self.centroids):
                    distance = np.linalg.norm(data_point - centroid)
                    if distance < min_distance:
                        min_distance = distance
                        min_distance_index = centroid_index

                if min_distance_index != self.cluster_assignment[data_ind]:
                    self.cluster_assignment[data_ind] = min_distance_index
                    updated = True
            
            if not updated:
                break

            for centroid_index, _ in enumerate(self.centroids):
                self.centroids[centroid_index] = self.data[self.cluster_assignment == centroid_index].mean(axis=0)

N = 100
num_features = 2
data  = np.random.rand(N, num_features)
data[:N//3, :] += 1
model = KMeans(data, k=3)
model.data
model.fit()

plt.figure()
plt.scatter([c[0] for c in model.centroids], [c[1] for c in model.centroids], c='r', marker='x')
plt.scatter([d[0] for d in data], [d[1] for d in data], c=model.cluster_assignment)
plt.savefig('k_means_clustering.pdf')