
# 📊 Clustering Algorithms and Evaluation Metrics

## Introduction

Clustering is an unsupervised learning technique used to group similar data points together such that points in the same group (cluster) are more similar to each other than to those in other groups. It's widely used in various fields, including marketing segmentation, social network analysis, and bioinformatics.

---

## 🔹 Clustering Algorithms

### 1. K-Means Clustering

**Concept**:  
K-Means partitions data into **K** clusters by minimizing the within-cluster sum of squares (inertia).

**Algorithm Steps**:

1. Select `K` initial centroids.
2. Assign each data point to the nearest centroid.
3. Update centroids by averaging points in each cluster.
4. Repeat steps 2–3 until convergence.

---

### 2. Agglomerative Hierarchical Clustering

**Concept**:  
A bottom-up approach where each data point starts in its own cluster and pairs of clusters are merged as one moves up the hierarchy.

**Linkage Criteria**:

- **Single Linkage**: Minimum distance
- **Complete Linkage**: Maximum distance
- **Average Linkage**: Average pairwise distance
- **Ward's Method**: Minimizes variance

---

### 3. DBSCAN

**Concept**:  
Groups dense regions of data and identifies noise/outliers.

**Parameters**:

- `ε` (epsilon): Neighborhood radius
- `minPts`: Minimum points required to form a dense region

**Steps**:

1. For each unvisited point, find its `ε`-neighborhood.
2. If the neighborhood has `minPts` or more, start a new cluster.
3. Expand cluster recursively with density-connected points.

---

## 🧮 Cluster Quality Metrics

### 1. Silhouette Score

Measures how similar a point is to its own cluster vs others.

**Formula**:

```math
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
```

Where:

- `a(i)`: average intra-cluster distance of point `i`
- `b(i)`: average nearest-cluster distance for point `i`

Range: `[-1, 1]`, where higher is better.

---

### 2. Davies-Bouldin Index (DBI)

Evaluates average similarity of each cluster with its most similar one.

**Formula**:

```math
DBI = \frac{1}{k} \sum_{i=1}^{k} \max_{j \neq i} \left( \frac{\sigma_i + \sigma_j}{d_{ij}} \right)
```

Where:

- `σᵢ`: average distance within cluster `i`
- `dᵢⱼ`: distance between centroids of clusters `i` and `j`

Lower is better.

---

### 3. Normalized Mutual Information (NMI)

Compares clustering results with ground truth.

**Formula**:

```math
NMI(U, V) = \frac{2 \cdot I(U; V)}{H(U) + H(V)}
```

Where:

- `I(U; V)`: Mutual Information
- `H(U)`, `H(V)`: Entropies

Range: `[0, 1]`, higher is better.

---

## 📊 Summary Table

| Algorithm | Needs `K`? | Handles Noise | Flexible Shapes | Complexity |
|-----------|------------|----------------|------------------|-------------|
| K-Means   | ✅          | ❌              | ❌ (Spherical)    | O(nkdi)     |
| Agglo HC  | ❌          | ❌              | ✅                | O(n² log n) |
| DBSCAN    | ❌          | ✅              | ✅                | O(n log n)  |

| Metric     | Type     | Range     | Best Value | Needs Ground Truth? |
|------------|----------|-----------|------------|----------------------|
| Silhouette | Internal | [-1, 1]   | Close to 1 | ❌                   |
| DBI        | Internal | [0, ∞)    | Close to 0 | ❌                   |
| NMI        | External | [0, 1]    | Close to 1 | ✅                   |

---

## 📚 References

- [Harvard Data Science Book](https://rafalab.dfci.harvard.edu/dsbook/clustering.html)
- [CSNA - Harvard](https://lweb.cfa.harvard.edu/~kurtz/CSNA/1998/Density-based_Clustering_in_Spatial_Databases_-_the_Algorithm_Gd.html)
