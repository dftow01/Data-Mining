
# 📊 Clustering Algorithms and Evaluation Metrics

## Introduction

Clustering is an unsupervised learning technique used to group similar data points together such that points in the same group (cluster) are more similar to each other than to those in other groups. It's widely used in various fields, including marketing segmentation, social network analysis, and bioinformatics.

---

## 🔹 Clustering Algorithms

### 1. K-Means Clustering

**Concept**:  
K-Means partitions data into **K** clusters by minimizing the within-cluster sum of squares (inertia). It aims to find cluster centers (centroids) such that the total distance between data points and their respective cluster centers is minimized.

**Algorithm Steps**:

1. **Initialization**: Select `K` initial centroids randomly or using methods like k-means++ for better convergence.
2. **Assignment Step**: Assign each data point to the nearest centroid based on a distance metric (typically Euclidean distance).
3. **Update Step**: Recompute the centroid of each cluster as the mean of all points assigned to it.
4. **Repeat**: Continue steps 2 and 3 until centroids no longer change significantly or a maximum number of iterations is reached.

**Characteristics**:

- Requires predefining the number of clusters `K`.
- Assumes clusters are spherical and of similar size.
- Sensitive to outliers and noise.

**Use Cases**:

- Market segmentation
- Document clustering
- Image compression

**References**:

- [Introduction to Data Science - Harvard University](https://rafalab.dfci.harvard.edu/dsbook/clustering.html)

---

### 2. Agglomerative Hierarchical Clustering

**Concept**:  
A bottom-up approach where each data point starts in its own cluster, and clusters are iteratively merged based on similarity until all points are in a single cluster or a stopping criterion is met.

**Algorithm Steps**:

1. Start with each data point as a single cluster.
2. At each iteration, merge the two most similar clusters based on a linkage criterion.
3. Repeat until the desired number of clusters is achieved or all points are merged into one cluster.

**Linkage Criteria**:

- **Single Linkage**: Minimum distance between points of two clusters.
- **Complete Linkage**: Maximum distance between points of two clusters.
- **Average Linkage**: Average distance between all pairs of points in two clusters.
- **Ward’s Method**: Minimizes the total within-cluster variance.

**Characteristics**:

- Does not require specifying the number of clusters in advance.
- Can capture complex cluster shapes.
- Computationally intensive for large datasets.

**Use Cases**:

- Gene expression data analysis
- Document clustering

**References**:

- [Introduction to Data Science - Harvard University](https://rafalab.dfci.harvard.edu/dsbook/clustering.html)

---

### 3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

**Concept**:  
Groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions.

**Algorithm Steps**:

1. For each point, retrieve its ε-neighborhood (all points within distance ε).
2. If the ε-neighborhood contains at least `minPts` points, create a cluster.
3. Expand the cluster by recursively adding all density-reachable points.
4. Repeat until all points are visited.

**Parameters**:

- `ε` (epsilon): Radius of the neighborhood.
- `minPts`: Minimum number of points required to form a dense region.

**Characteristics**:

- Does not require specifying the number of clusters.
- Can find arbitrarily shaped clusters.
- Robust to outliers.
- Struggles with varying densities and high-dimensional data.

**Use Cases**:

- Spatial data analysis
- Anomaly detection

**References**:

- [Density-based Clustering in Spatial Databases - Harvard University](https://lweb.cfa.harvard.edu/~kurtz/CSNA/1998/Density-based_Clustering_in_Spatial_Databases_-_the_Algorithm_Gd.html)

---

## 🧮 Cluster Quality Metrics

Evaluating the quality of clustering results is crucial. Metrics are categorized into:

- **Internal Metrics**: Evaluate the clustering structure using the data alone.
- **External Metrics**: Compare the clustering results to external ground truth labels.

### 1. Silhouette Score

**Concept**:  
Measures how similar an object is to its own cluster compared to other clusters.

**Formula**:

For a data point \( i \):

- ```math \( a(i) \) ```: Average distance between ```math \( i \)``` and all other points in the same cluster.
- ```math\( b(i) \) ```: Minimum average distance from ```math\( i \)``` to points in a different cluster.


```math
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
```

- ```math\( s(i) \)``` ranges from -1 to 1.
  - Close to 1: The data point is well matched to its own cluster.
  - Close to 0: The data point is on or very close to the decision boundary between two neighboring clusters.
  - Negative values: The data point might have been assigned to the wrong cluster.

**Use Cases**:

- Determining the optimal number of clusters.
- Comparing different clustering algorithms.

**References**:

- [Introduction to Data Science - Harvard University](https://rafalab.dfci.harvard.edu/dsbook/clustering.html)

---

### 2. Davies-Bouldin Index (DBI)

**Concept**:  
Evaluates the average similarity between each cluster and its most similar one, considering the ratio of within-cluster distances to between-cluster distances.

**Formula**:

```math
DBI = \frac{1}{k} \sum_{i=1}^{k} \max_{j \neq i} \left( \frac{\sigma_i + \sigma_j}{d_{ij}} \right)
```

- ```math\( \sigma_i \)```: Average distance of all points in cluster ```math\( i \)``` to its centroid.
- ```math\( d_{ij} \)```: Distance between centroids of clusters ```math\( i \)``` and ```math\( j \)```.

- Lower DBI values indicate better clustering.

**Use Cases**:

- Model selection.
- Comparing clustering algorithms.

**References**:

- [Introduction to Data Science - Harvard University](https://rafalab.dfci.harvard.edu/dsbook/clustering.html)

---

### 3. Normalized Mutual Information (NMI)

**Concept**:  
Measures the similarity between the clustering assignments and the ground truth labels.

**Formula**:

```math
NMI(U, V) = \frac{2 \cdot I(U; V)}{H(U) + H(V)}
```

- ```math\( I(U; V) \)```: Mutual information between the cluster assignments ```math\( U \)``` and the ground truth labels ```math\( V \)```.
- ```math\( H(U) \)``` and ```math\( H(V) \)```: Entropies of ```math\( U \)``` and ```math\( V \)```, respectively.

- NMI ranges from 0 (no mutual information) to 1 (perfect correlation).

**Use Cases**:

- Evaluating clustering performance when ground truth labels are available.

**References**:

- [Introduction to Data Science - Harvard University](https://rafalab.dfci.harvard.edu/dsbook/clustering.html)

---

## 📊 Summary Table

### Clustering Algorithms

| Algorithm                    | Requires Predefined `K` | Handles Noise | Cluster Shape Flexibility | Computational Complexity |
|------------------------------|-------------------------|---------------|---------------------------|--------------------------|
| K-Means                      | ✅ Yes                  | ❌ No         | ❌ Low (Spherical)         | O(nkdi)                  |
| Agglomerative Hierarchical   | ❌ No                   | ❌ No         | ✅ High                    | O(n² log n)              |
| DBSCAN                       | ❌ No                   | ✅ Yes        | ✅ High                    | O(n log n) (with indexing)|

### Cluster Quality Metrics

| Metric                 | Type     | Range   | Ideal Value | Requires Ground Truth |
|------------------------|----------|---------|-------------|-----------------------|
| Silhouette Score       | Internal | [-1, 1] | Close to 1  | ❌ No                 |
| Davies-Bouldin Index   | Internal | [0, ∞)  | Close to 0  | ❌ No                 |
| Normalized Mutual Info | External | [0, 1]  | Close to 1  | ✅ Yes                |

---

## 📚 References
