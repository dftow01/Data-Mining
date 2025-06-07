# Network Analysis Techniques

## Shortest Path in Network Analysis
### What is Shortest Path in a Network?

The **shortest path** between two nodes is the **minimum number of edges (or minimum total weight)** required to travel from one node to another.

- In an **unweighted** graph (like a Facebook friendship network), it represents the **fewest friend hops** between two users.
- In a **weighted** graph, it refers to the path with the **lowest total cost or distance**.

### What Does Shortest Path Indicate?

1. **Social Distance or Proximity**  
   In social networks, the shortest path represents how closely connected two people are. A shorter path means fewer intermediaries between them.

2. **Information or Influence Flow**  
   Shorter paths imply faster or easier transmission of information, ideas, or influence between nodes.

3. **Network Efficiency**  
   The average shortest path length across the entire network measures how efficiently information or resources can spread globally.

4. **Network Structure Insight**  
   Shortest paths help identify important nodes or edges that act as hubs or bottlenecks by being part of many shortest paths.

### Why Is It Important?

- **Small-World Phenomenon**  
  Social networks often have surprisingly short average shortest paths, known as "six degrees of separation," meaning most people are connected by just a few steps.

- **Routing & Navigation**  
  In communication or transportation networks, shortest paths optimize routing for efficiency.

- **Vulnerability & Resilience**  
  Nodes or edges that lie on many shortest paths (high betweenness) are critical for maintaining network connectivity and robustness.

### Relation to Centrality Measures

- **Betweenness Centrality** relies on shortest paths by counting how many shortest paths pass through a given node or edge.
- **Closeness Centrality** is based on the average shortest path length from a node to all others; nodes with shorter average distances are more central.

### Summary

| Concept                      | Meaning                                      | Example in Facebook Network                  |
|------------------------------|----------------------------------------------|----------------------------------------------|
| **Shortest Path**            | Minimum steps to connect two users           | Number of friend hops between Alice and Bob |
| **Average Shortest Path**    | Overall closeness of the network              | Average steps to reach any user in the network|
| **Shortest Path Length Distribution** | Variation of path lengths among user pairs | Most users are within 3-4 hops of each other |

---

## Centrality in NetworkX

| Centrality Type | Description | NetworkX Function | Use Case |
|----------------|-------------|-------------------|----------|
| **Degree Centrality** | Nodes with many direct connections | `nx.degree_centrality(G)` | Find users with the most friends |
| **Betweenness Centrality** | Nodes that lie on many shortest paths — act as "bridges" | `nx.betweenness_centrality(G)` | Identify users who connect different communities |
| **Closeness Centrality** | Nodes that are close to all others (short average path) | `nx.closeness_centrality(G)` | Spot users who can quickly spread information |
| **Eigenvector Centrality** | Nodes connected to other well-connected nodes (influence) | `nx.eigenvector_centrality(G)` | Discover "influential" users beyond direct connections |
| **PageRank** | A variant of eigenvector centrality (popular in web analysis) | `nx.pagerank(G)` | Rank nodes by importance (like Google's algorithm) |
| **Katz Centrality** | Like eigenvector, but considers longer paths with decay | `nx.katz_centrality(G)` | Measure influence with distance decay |

---

## Code Explanation

### 1. Creating the Network Graph

```python
G1 = nx.from_pandas_edgelist(facebook, 'start_node', 'end_node')
plt.figure(figsize=(10, 8))
nx.draw(G1, with_labels=True, node_size=300, font_size=8)
plt.title("Facebook Ego Network")
plt.show()
```

**What it does:**
- `nx.from_pandas_edgelist()` creates a NetworkX graph from a pandas DataFrame
- The DataFrame should have columns for source nodes (`start_node`) and target nodes (`end_node`)
- Each row represents one connection (edge) between two users
- The visualization shows the network structure with labeled nodes

**Why it's useful:** This gives us a visual representation of how users are connected in the Facebook network.

---

### 2. Basic Network Analysis

```python
print("Number of nodes (users): ", G1.number_of_nodes())
print("Number of edges (connections): ", G1.number_of_edges())
print("Network Density:", nx.density(G1))

degrees = dict(G1.degree)
avg_degree = sum(degrees.values()) / G1.number_of_nodes()
print("Average Degree:", avg_degree)

is_connected = nx.is_connected(G1)
print("Is the network connected?", is_connected)
```

**What each metric tells us:**
- **Nodes**: Total number of users in the network
- **Edges**: Total number of friendships/connections
- **Density**: How interconnected the network is (0 = no connections, 1 = everyone connected to everyone)
- **Average Degree**: Average number of friends per user
- **Connectivity**: Whether you can reach any user from any other user through connections

---

### 3. Shortest Path Analysis

```python
all_shortest_paths = dict(nx.all_pairs_shortest_path_length(G1))
# Example: Check shortest path between node 0 and node 42
print(all_shortest_paths[0][42])
```

**How it works:**
- `all_pairs_shortest_path_length()` calculates the shortest path between every pair of nodes
- Returns a nested dictionary structure: `{source_node: {target_node: path_length}}`
- Example structure:
  ```python
  {
    0: {0: 0, 1: 1, 2: 2, 42: 3},  # From node 0 to all others
    1: {0: 1, 1: 0, 2: 1, 42: 2},  # From node 1 to all others
    # ... and so on
  }
  ```

**Real-world meaning:** If `all_shortest_paths[0][42] = 3`, it means you need exactly 3 "friend hops" to connect user 0 and user 42.

---

### 4. Centrality Measurements

```python
deg_centrality = nx.degree_centrality(G1)
betweenness_centrality = nx.betweenness_centrality(G1)
closeness_centrality = nx.closeness_centrality(G1)
eigen_vector = nx.eigenvector_centrality(G1)
```

**What each centrality measures:**

#### Degree Centrality
- **Measures**: How many direct friends a user has
- **High score means**: Popular user with many connections
- **Facebook context**: Users who accept/send many friend requests

#### Betweenness Centrality
- **Measures**: How often a user lies on the shortest path between other users
- **High score means**: User acts as a "bridge" connecting different groups
- **Facebook context**: Users who connect different social circles (work, school, family)

#### Closeness Centrality
- **Measures**: How close a user is to all other users (average distance)
- **High score means**: User can reach everyone quickly through few connections
- **Facebook context**: Users who can spread information rapidly across the network

#### Eigenvector Centrality
- **Measures**: How well-connected a user's friends are
- **High score means**: User is connected to other influential/popular users
- **Facebook context**: Users in the "inner circle" of popular people

---

### 5. Network Distance Metrics

```python
print(f"Average shortest path length: ", nx.average_shortest_path_length(G1))
print(f"Network diameter: ", nx.diameter(G1))
```

**Metrics explained:**
- **Average Shortest Path Length**: Average number of steps needed to connect any two users
- **Network Diameter**: Maximum shortest path in the network (longest possible shortest route)

**Example interpretation:** If diameter = 5, it means the two most distant users are still only 5 friend-hops apart.

---

### 6. Visualizing Path Length Distribution

```python
# Step 1: Extract all path lengths from the nested dictionary
all_path_lengths = []
for source_node in all_shortest_paths:
    for target_node in all_shortest_paths[source_node]:
        if source_node != target_node:  # Exclude self-loops (distance 0)
            all_path_lengths.append(all_shortest_paths[source_node][target_node])

# Step 2: Count frequency of each path length
path_length_counts = Counter(all_path_lengths)
total_pairs = sum(path_length_counts.values())

# Step 3: Convert to percentages
path_length_percentages = {
    length: (count / total_pairs) * 100
    for length, count in path_length_counts.items()
}

# Step 4: Create histogram
plt.figure(figsize=(10, 6))
plt.hist(all_path_lengths, bins=range(1, max(all_path_lengths)+2),
         alpha=0.7, weights=[100 / total_pairs] * len(all_path_lengths),
         color='skyblue', edgecolor='black')
plt.xlabel('Shortest Path Length')
plt.ylabel('Frequency (%)')
plt.title('Distribution of Shortest Path Lengths in Facebook Ego Network')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Step-by-step breakdown:**

1. **Data Extraction**: Loop through the nested dictionary to collect all shortest path lengths
   - Outer loop: iterate through each source node
   - Inner loop: iterate through each target node and its distance
   - Skip when source = target (distance would be 0)

2. **Frequency Counting**: Use `Counter` to count how many node pairs have each path length
   - Result: `{1: 5000, 2: 8000, 3: 3000}` (example)
   - Meaning: 5000 pairs are 1 hop apart, 8000 pairs are 2 hops apart, etc.

3. **Percentage Calculation**: Convert raw counts to percentages for better interpretation

4. **Visualization**: Create a histogram showing the distribution
   - X-axis: Path length (1, 2, 3, 4, etc. hops)
   - Y-axis: Percentage of all node pairs
   - Shows the "small world" effect if most pairs have short paths

**Real-world insight:** If 80% of user pairs are within 3 hops, it demonstrates the "small world" phenomenon where everyone is closely connected despite the large network size.

---

## Key Takeaways

Understanding these metrics helps you:
- **Identify influential users** (high centrality scores)
- **Understand information flow** (shortest paths and network structure)
- **Assess network resilience** (connectivity and critical bridges)
- **Optimize content distribution** (leverage central nodes for maximum reach)
