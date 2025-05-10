# Unsupervised Learning

## Unsupervised ML Algorithms
1. K-Means
2. Agglomerative Hierarchical Clustering
3. DBSCAN

## Dataset
- The dataset consists of 440 instances and 8 features.
- Channel means customers such as Horeca (Hotel, Restaurant, Cafe) or Retail Channel.
- Regions mean customer regions such as Lisbon, Oporto or others.
- Both of these features represent the background information of the customers.
- But if we are just analysing purchase values or spending, we should drop these two columns during the analysis.
- Clustering should be based on the natural structure of the dataset
- Including Channel as a feature would leak label information into unsupervised algorithms, which breaks the principle of discovering patterns without supervision.

## Clustering Methods
There are two common methods for clustering, which are Row-Based Clustering and Item-Based Clustering.

### Row-Based CLustering
**Data representation**: Each row is treated as a data point in an n-dimensional space, where n is the number of features (columns).
**Similarity**: Points that are close to each other in this feature space are grouped.
**Applications**: Customer segmentation, document clustering, image segmentation.
**Examples**: K-means, DBSCAN, hierarchical clustering.

### Column-based Clustering
**Data representation**: Each column represents a variable to be grouped with similar variables.
**Similarity**: Features showing similar patterns across observations are grouped.
**Applications**: Gene expression analysis, recommender systems, market basket analysis.
**Examples**: Spectral biclustering, Cheng and Church's algorithm.

--- 
## Algorithms
## K-Means Clustering (Centroid-Based Clustering)
- Organised data into groups based on their similarity. 
- The basic idea was to group data points using the centroid method.
- The algorithm will randomly picks some central points and assign data points into a cluster based on the closest distance to the centroid.
- After all the points are assigned to a cluster, the centroids are updated by finding the average position of the points in each cluster.
- This process repeats until the centroids stop changing, forming clusters. The goal of clustering is to divide the data points into clusters so that similar data points belong to the same group.

### Steps
1. First, we randomly initialise k points, called means or cluster centroids.
2. We categorise each item to its closest mean, and we update the mean’s coordinates, which are the averages of the items categorised in that cluster so far.
3. We repeat the process for a given number of iterations, and at the end, we have our clusters.

--- 

## Agglomerative Hierarchical Clustering (Connectivity-Based Clustering)
- A bottom-up approach that starts by treating each individual data point as its own cluster.
- At each iteration, the two closest clusters are merged based on a defined similarity (distance) measure.
- This process continues until all data points are merged into a single cluster, forming a hierarchical structure (usually visualized as a dendrogram).
- Summary: It successively merges smaller clusters into larger ones based on decreasing distance (increasing similarity).

### Distance Function (Metric)
- A distance function (also called a similarity or dissimilarity metric) is used to calculate how far apart two individual data points are.
- This forms the foundation of clustering, as it determines what “closeness” means.
- Common distance functions:
- Euclidean Distance: Straight-line distance between two points.
- Manhattan Distance: Sum of the absolute differences.
- Cosine Distance, Minkowski Distance, etc.

### Proximity Matrix
- The proximity matrix (or distance matrix) is a square matrix containing the pairwise distances between all data points.
- These distances are calculated using the chosen distance function (e.g., Euclidean).
- This matrix is the initial input used by the clustering algorithm to decide which points or clusters to merge.

### Linkage
- Once the distances between individual data points are computed, linkage determines how to calculate the distance between clusters (which may consist of multiple points).
- In other words, linkage is a strategy for combining point-to-point distances to define cluster-to-cluster proximity.
- This step decides which clusters to merge at each iteration of the algorithm.

### Think of the process like this:

1. **You have a distance function** (e.g., Euclidean)  
   → This is fixed and always used to compute distances between individual points.

2. **You have clusters made of multiple points**  
   → You now want to measure how far apart two clusters are.

3. **The linkage method decides which points between the clusters to use**  
   → It determines how to **combine the point-to-point distances** to compute the **cluster-to-cluster distance**.

### Example:

Suppose you have:

- **Cluster A** = {A1, A2}  
- **Cluster B** = {B1, B2, B3}

You use **Euclidean distance** to compute all pairwise distances between points in A and B:

|        | B1 | B2 | B3 |
|--------|----|----|----|
| A1     | 2  | 3  | 6  |
| A2     | 4  | 1  | 5  |

Now apply different **linkage methods**:

- **Single Linkage**:  
  - Distance = **min(2, 3, 6, 4, 1, 5) = 1**  
  - → Uses the **closest pair** of points between the clusters (A2 and B2)

- **Complete Linkage**:  
  - Distance = **max(2, 3, 6, 4, 1, 5) = 6**  
  - → Uses the **farthest pair** of points
  - In Complete Linkage clustering, the algorithm compares all pairs of clusters by calculating the maximum distance between any two points, one from each cluster. This method ensures that clusters are only merged when even their most distant points are relatively close, promoting more compact and evenly shaped clusters. Among all possible cluster pairs, the algorithm identifies the pair with the smallest maximum distance—in other words, it finds the two clusters whose worst-case (farthest) connection is still the best compared to others—and merges them. This approach prevents loosely connected or stretched clusters from forming too early, ensuring tighter and more well-separated groupings throughout the clustering process.

- **Average Linkage**:  
  - Distance = **(2 + 3 + 6 + 4 + 1 + 5) / 6 = 21 / 6 ≈ 3.5**

This demonstrates how linkage controls **which distances are used** and **how they are aggregated**, while the **Euclidean distance remains constant** as the underlying point-to-point metric.

#### Common Linkage Methods:
1. Single Linkage:
   - Cluster distance = minimum distance between any pair of points from the two clusters.
   - Tends to form elongated, chain-like clusters.
2. Complete Linkage:
   - Cluster distance = maximum distance between any pair of points from the two clusters.
   - Leads to more compact and spherical clusters.
3. Average Linkage:
   - Cluster distance = average of all pairwise distances between points in the two clusters.
   - Offers a balance between single and complete linkage.
4. Centroid Linkage:
   - Cluster distance = distance between the centroids (mean vectors) of the two clusters.
   - Sensitive to cluster shapes and can produce inversions (where merging reduces distance).
5. Ward’s Method:
   - Minimizes the increase in total within-cluster variance.
   - Often results in clusters of similar size and shape.
   - Uses squared Euclidean distance by default.

#### Steps of Agglomerative Hierarchical Clustering
1. Compute the proximity matrix using a selected distance function (e.g., Euclidean).
2. Use a linkage method to define distances between clusters based on the proximity matrix.
3. Merge the two clusters (or points) with the smallest cluster-to-cluster distance.
4. Update the proximity matrix to reflect the new cluster structure.
5. Repeat steps 2–4 until only a single cluster remains.

---

## DBSCAN Clustering (Density-Based Clustering)
- It groups data points that are closely packed together and marks outliers as noise based on their density in the feature space.
- It identifies clusters as dense regions in the data space, separated by areas of lower density.
- Unlike other clustering algorithms, which assume clusters should be compact and spherical, DBSCAN excels in handling real-world data irregularities such as
  - Arbitary-Shaped Clusters, where clusters can take any shape, not just circular or convex
  - Noise and Outliers: It effectively identifies and handles noise points without assigning them to any cluster

![Screenshot 2025-05-10 at 17 01 49](https://github.com/user-attachments/assets/626a3f95-f246-4f33-ae0a-b6530423751f)

### Key Parameters in DBSCAN
1. eps
   - This defines the radius of the neighbourhood around a data point.
   - If the distance between two points is less than or equal to eps, they are considered neighbours.
   - If eps is too small, most points will be classified as noise
   - If eps is too large, clusters may merge and the  algorithms might fail to distinguish between them
2. MinPts
   - This is the minimum number of points required within the eps radius to form a dense region or cluster.
   - A general rule of thumb is to set MinPts >= D+1, where D is the number of dimensions in the dataset. For most cases, a minimum value of MinPts = 3 is recommended.

#### Steps in the DBSCAN Algorithm
1. **Identify Core Points**: For each point in the dataset, count the number of points within its eps neighbourhood. If the count meets or exceeds MinPts, mark the point as a core point.
2. **Form Clusters**: For each core point that is not already assigned to a cluster, create a new cluster. Recursively find all density-connected points (points within the eps radius of the core point) and add them to the cluster.
3. **Density Connectivity**: Two points, a and b, are density-connected if there exists a chain of points where each point is within the eps radius of the next, and at least one point in the chain is a core point. This chaining process ensures that all points in a cluster are connected through a series of dense regions.
4. **Label Noise Points**: After processing all points, any point that does not belong to a cluster is labelled as noise.

---

## Steps
1. Load & inspect your data (done).
2. Preprocess: drop/encode categoricals, scale numerics.
3. K-Means: elbow, silhouette → fit → profile.
4. Hierarchical: dendrogram → fit → profile.
5. DBSCAN: k-distance plot → fit → profile.
6. Visualise and validate all clusterings to decide which best segments your customers.

