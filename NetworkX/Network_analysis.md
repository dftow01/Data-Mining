# Network Analysis Techniques
Friendly reminder: Take a deep breath before reading the documentation and finish it in one shot 🙃

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

**Use case:** If 80% of user pairs are within 3 hops, it demonstrates the "small world" phenomenon where everyone is closely connected despite the large network size.

---

### 8. Calculate graph density, number of connected components, degree of centrality and plot the distribution

```python
# Calculate basic network metrics
density = nx.density(G1)
num_components = nx.number_connected_components(G1)

print(f"Graph density: {density:.3f}")
print(f"Number of connected components: {num_components}")

# Analyze degree distribution
degrees = [d for n, d in G1.degree()]
degree_counts = Counter(degrees)

# Plot degree centrality distribution
plt.figure(figsize=(15, 8))
plt.hist(deg_centrality.values(), bins=25, color="skyblue")
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2]) 
plt.title("Degree Centrality Histogram", fontdict={"size": 35}, loc="center")
plt.xlabel("Degree Centrality", fontdict={"size": 20})
plt.ylabel("Counts", fontdict={"size": 20})
plt.show()

# Print degree statistics
print(f"Average degree: {np.mean(degrees):.2f}")
print(f"Degree standard deviation: {np.std(degrees):.2f}")
print(f"Maximum degree: {max(degrees)}")
print(f"Minimum degree: {min(degrees)}")
```

**How the code works:**

1. **Calculate Network Metrics**:
   - `nx.density(G1)` calculates how many edges exist compared to maximum possible edges
   - `nx.number_connected_components(G1)` counts separate network clusters

2. **Extract Degree Data**:
   - `G1.degree()` returns pairs of (node, degree) for each node
   - List comprehension `[d for n, d in G1.degree()]` extracts only the degree values
   - `Counter(degrees)` counts frequency of each degree value

3. **Create Histogram**:
   - `plt.hist(deg_centrality.values(), bins=25)` creates histogram with 25 bins
   - `deg_centrality.values()` gets all degree centrality scores (0 to 1 range)
   - Custom x-axis ticks show specific centrality values for better readability

4. **Calculate Statistics**:
   - `np.mean(degrees)`, `np.std(degrees)` calculate average and spread
   - `max(degrees)`, `min(degrees)` find most and least connected users

**What this analysis reveals:**
- **Graph Density**: How interconnected the network is (ranges from 0 to 1)
- **Connected Components**: Number of separate network clusters
- **Degree Distribution**: Shows how friendship connections are distributed across users
- **Degree Statistics**: Reveals network characteristics like popular vs. average users

**Use case**: A low density with high degree variation suggests some users are extremely popular while most have few connections.

---

### 9. Plot the users with highest degree centralities from the size of their nodes

```python
plt.figure(figsize=(12, 8))

# Identify top 10 users by degree centrality
top_degree_nodes = [node for node, _ in sorted(deg_centrality.items(),
                                              key=lambda x: x[1], reverse=True)[:10]]

# Size nodes proportional to their degree centrality
node_sizes = [3000 * deg_centrality[node] for node in G1.nodes()]
node_colors = ['red' if node in top_degree_nodes else 'lightblue' for node in G1.nodes()]

# Create consistent layout
pos = nx.spring_layout(G1, k=1, iterations=50, seed=42)
nx.draw(G1, pos,
        node_color=node_colors,
        node_size=node_sizes,
        with_labels=True,
        font_size=8,
        font_weight='bold',
        edge_color='gray',
        alpha=0.7)

plt.title("Network with Node Sizes Proportional to Degree Centrality\n(Red nodes = Top 10 highest degree centrality)",
          fontsize=14, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()

# Display top 10 users with their metrics
print("Top 10 nodes by degree centrality:")
for i, (node, centrality) in enumerate(sorted(deg_centrality.items(),
                                             key=lambda x: x[1], reverse=True)[:10], 1):
    print(f"{i}. Node {node}: {centrality:.3f} (degree: {G1.degree(node)})")
```

**How the code works:**

1. **Find Top Nodes**:
   - `sorted(deg_centrality.items(), key=lambda x: x[1], reverse=True)` sorts nodes by centrality value
   - `[:10]` takes the top 10 highest centrality nodes
   - List comprehension extracts just the node IDs

2. **Calculate Visual Properties**:
   - `node_sizes = [3000 * deg_centrality[node] for node in G1.nodes()]` makes node size proportional to centrality
   - Multiplier `3000` scales sizes for visibility
   - `node_colors` list assigns red to top nodes, light blue to others

3. **Create Network Layout**:
   - `nx.spring_layout()` positions nodes using force-directed algorithm
   - `k=1` controls node spacing, `iterations=50` improves layout quality
   - `seed=42` ensures reproducible layout positions

4. **Draw Network**:
   - `nx.draw()` creates the visualization with all specified properties
   - `with_labels=True` shows node IDs on the graph
   - `alpha=0.7` makes nodes slightly transparent

5. **Display Rankings**:
   - Loop through sorted centrality values to show top 10 with their actual degree counts

**Visualization benefits:**
- **Node Size**: Larger nodes = more connections (higher degree centrality)
- **Color Coding**: Red nodes highlight the most connected users
- **Network Position**: Shows where popular users are located in the network structure

**Facebook Ego Network context**: Popular users (large red nodes) often serve as information hubs and community connectors.

---

### 10. Calculate the betweenness centralities for the 8 highest degree centralities nodes and show their centrality values

```python
# Get top 8 nodes by degree centrality
top_8_degree_nodes = [node for node, _ in sorted(deg_centrality.items(),
                                                 key=lambda x: x[1], reverse=True)[:8]]

print("Betweenness centralities for the 8 highest degree centrality nodes:")
betweenness_for_top_degree = []
for i, node in enumerate(top_8_degree_nodes, 1):
    bet_cent = betweenness_centrality[node]
    deg_cent = deg_centrality[node]
    betweenness_for_top_degree.append((node, bet_cent, deg_cent))
    print(f"{i}. Node {node}:")
    print(f"   Degree Centrality: {deg_cent:.3f}")
    print(f"   Betweenness Centrality: {bet_cent:.3f}")

# Create comparison bar chart
plt.figure(figsize=(10, 6))
nodes = [item[0] for item in betweenness_for_top_degree]
bet_values = [item[1] for item in betweenness_for_top_degree]
deg_values = [item[2] for item in betweenness_for_top_degree]

x = np.arange(len(nodes))
width = 0.35

plt.bar(x - width/2, deg_values, width, label='Degree Centrality', alpha=0.7, color='skyblue')
plt.bar(x + width/2, bet_values, width, label='Betweenness Centrality', alpha=0.7, color='orange')

plt.xlabel('Node')
plt.ylabel('Centrality Value')
plt.title('Comparison of Degree and Betweenness Centralities\nfor Top 8 Degree Centrality Nodes')
plt.xticks(x, [f'Node {node}' for node in nodes], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**How the code works:**

1. **Get Top Degree Nodes**:
   - Same sorting logic as before, but takes only top 8 nodes
   - `[:8]` slices the list to get first 8 highest degree centrality nodes

2. **Extract Both Centrality Values**:
   - Loop through each top degree node with `enumerate(top_8_degree_nodes, 1)`
   - `enumerate(..., 1)` provides index starting from 1 for numbering
   - Look up both centrality values: `betweenness_centrality[node]` and `deg_centrality[node]`
   - Store as tuples: `(node_id, betweenness_value, degree_value)`

3. **Prepare Data for Plotting**:
   - `nodes = [item[0] for item in betweenness_for_top_degree]` extracts node IDs
   - `bet_values = [item[1] for item in ...]` extracts betweenness centrality values
   - `deg_values = [item[2] for item in ...]` extracts degree centrality values

4. **Create Side-by-Side Bar Chart**:
   - `x = np.arange(len(nodes))` creates x-axis positions (0, 1, 2, ...)
   - `width = 0.35` sets bar width
   - `x - width/2` and `x + width/2` positions bars side by side
   - Two `plt.bar()` calls create bars for each centrality type

5. **Format Chart**:
   - `plt.xticks(x, [f'Node {node}' for node in nodes], rotation=45)` labels x-axis with node names
   - `rotation=45` tilts labels to prevent overlap
   - `plt.legend()` shows which color represents which centrality type

**Insights from comparison:**
- **High Degree ≠ High Betweenness**: Popular users aren't always bridges between communities
- **Different Roles**: Some users are popular within their group, others connect different groups
- **Strategic Importance**: High betweenness nodes are critical for information flow across the network

---

### 11. Plot nodes with highest betweenness centralities and where they are located in the network

```python
# Find top 8 users by betweenness centrality
top_betweenness_nodes = [node for node, _ in sorted(betweenness_centrality.items(),
                                                   key=lambda x: x[1], reverse=True)[:8]]

plt.figure(figsize=(12, 8))

# Normalize node sizes by betweenness centrality
max_betweenness = max(betweenness_centrality.values())
node_sizes = [3000 * (betweenness_centrality[node] / max_betweenness) for node in G1.nodes()]
node_colors = ['red' if node in top_betweenness_nodes else 'white' for node in G1.nodes()]

nx.draw(G1, pos,
        node_color=node_colors,
        node_size=node_sizes,
        with_labels=True,
        font_size=8,
        font_weight='bold',
        edge_color='gray',
        alpha=0.7)

plt.title("Network with Node Sizes Proportional to Betweenness Centrality\n(Red nodes = Top 8 highest betweenness centrality)",
          fontsize=14, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()

print("Top 8 nodes by betweenness centrality:")
for i, (node, centrality) in enumerate(sorted(betweenness_centrality.items(),
                                             key=lambda x: x[1], reverse=True)[:8], 1):
    print(f"{i}. Node {node}: {centrality:.3f}")
```

**How the code works:**

1. **Find Top Betweenness Nodes**:
   - `sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)` sorts by betweenness centrality
   - `[:8]` takes top 8 nodes with highest betweenness centrality values

2. **Normalize Node Sizes**:
   - `max_betweenness = max(betweenness_centrality.values())` finds the highest betweenness centrality value
   - `betweenness_centrality[node] / max_betweenness` normalizes each value to 0-1 range
   - Multiply by `3000` to scale for visibility in the graph
   - This ensures the highest betweenness node gets maximum size

3. **Color Coding**:
   - `node_colors` list assigns red to top 8 betweenness nodes, white to all others
   - Red nodes will stand out as the key "bridge" users in the network

4. **Use Previous Layout**:
   - `pos` variable from previous visualization ensures consistent node positioning
   - This allows easy comparison between degree and betweenness centrality visualizations

5. **Display Rankings**:
   - Print top 8 nodes with their exact betweenness centrality scores
   - Shows which users act as the most important bridges in the network

**Strategic importance of bridge users:**
- **Information Brokers**: Control flow of information between different groups
- **Network Vulnerability**: Removing these users could fragment the network
- **Influence Potential**: Can introduce people from different communities to each other

---

### 12. Calculate the nodes with highest closeness centralities

```python
# Identify users with highest closeness centrality
top_closeness_nodes = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)

print("Top 10 nodes by closeness centrality:")
for i, (node, centrality) in enumerate(top_closeness_nodes[:10], 1):
    print(f"{i}. Node {node}: {centrality:.3f}")
```

**How the code works:**

1. **Sort by Closeness Centrality**:
   - `closeness_centrality.items()` returns pairs of (node, centrality_value)
   - `sorted(..., key=lambda x: x[1], reverse=True)` sorts by centrality value (x[1])
   - `reverse=True` puts highest values first

2. **Display Top 10**:
   - `[:10]` slices to get top 10 nodes
   - `enumerate(..., 1)` provides numbering starting from 1
   - Loop prints each node with its closeness centrality score

**What closeness centrality tells us:**
- Higher values mean shorter average distances to all other nodes
- These users can spread information most efficiently across the network

**What closeness centrality reveals:**
- **Information Spreaders**: Users who can quickly reach everyone in the network
- **Central Position**: Users located at the "heart" of the network
- **Communication Efficiency**: Shortest average path to all other users

---

### 13. Calculate the average distance of any particular node (user_number) to any other node. Plot the distribution of the closeness centralities

```python
# Calculate distances from a specific user (e.g., user 0)
user_number = 0
distances_from_user = dict(nx.shortest_path_length(G1, source=user_number))
avg_distance_from_user = np.mean(list(distances_from_user.values()))

print(f"Average distance from node {user_number} to all other nodes: {avg_distance_from_user:.3f}")

# Plot closeness centrality distribution
plt.figure(figsize=(15, 12))
closeness_values = list(closeness_centrality.values())

plt.hist(closeness_values, bins=20, alpha=0.7, color='green', edgecolor='black')
plt.xlabel('Closeness Centrality')
plt.ylabel('Frequency')
plt.title('Distribution of Closeness Centralities')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Mean closeness centrality: {np.mean(closeness_values):.3f}")
print(f"Standard deviation: {np.std(closeness_values):.3f}")
```

**How the code works:**

1. **Calculate Distances from Specific User**:
   - `nx.shortest_path_length(G1, source=user_number)` calculates shortest paths from user 0 to all others
   - Returns a dictionary: `{target_node: distance}` for all reachable nodes
   - `dict()` converts the result to a regular dictionary
   - `np.mean(list(distances_from_user.values()))` calculates average distance

2. **Extract All Closeness Values**:
   - `closeness_centrality.values()` gets all centrality scores
   - `list()` converts to list for easier manipulation

3. **Create Distribution Histogram**:
   - `bins=20` divides the range of closeness values into 20 intervals
   - `alpha=0.7` makes bars slightly transparent
   - `edgecolor='black'` adds black borders to bars for clarity

4. **Calculate Summary Statistics**:
   - `np.mean(closeness_values)` shows average closeness centrality
   - `np.std(closeness_values)` shows how spread out the values are

**What this analysis reveals:**
- **Individual Perspective**: How well-positioned user 0 is in the network
- **Overall Distribution**: Shows variation in how "central" different users are
- **Network Compactness**: Lower average distances indicate a more connected network

**Analysis benefits:**
- **Individual Perspective**: Shows how well-positioned a specific user is
- **Network Efficiency**: Average distance reveals overall network compactness
- **Distribution Pattern**: Shows variation in user positions within the network

---

### 14. Calculate the nodes with the highest eigenvector centrality. Identify the nodes

```python
# Find users with highest eigenvector centrality
top_eigen_nodes = sorted(eigen_vector.items(), key=lambda x: x[1], reverse=True)

print("Top 10 nodes by eigenvector centrality:")
for i, (node, centrality) in enumerate(top_eigen_nodes[:10], 1):
    print(f"{i}. Node {node}: {centrality:.3f}")

print(f"\nThe node with highest eigenvector centrality is Node {top_eigen_nodes[0][0]} with value {top_eigen_nodes[0][1]:.3f}")
```

**How the code works:**

1. **Sort by Eigenvector Centrality**:
   - `eigen_vector.items()` returns (node, centrality_value) pairs
   - `sorted(..., key=lambda x: x[1], reverse=True)` sorts by centrality value in descending order
   - Result is a list of tuples ordered from highest to lowest centrality

2. **Display Top 10 Users**:
   - `[:10]` gets first 10 items (highest centrality values)
   - `enumerate(..., 1)` provides ranking numbers starting from 1
   - Loop prints each node with its eigenvector centrality score

3. **Identify Top User**:
   - `top_eigen_nodes[0][0]` gets the node ID of the highest-ranking user
   - `top_eigen_nodes[0][1]` gets the centrality value of that user
   - This identifies the single most influential user in the network

**What eigenvector centrality reveals:**
- Users connected to other highly-connected users score higher
- It's not just about quantity of connections, but quality of connections
- The top user has the most influence through their network position

**Eigenvector centrality significance:**
- **Quality over Quantity**: Not just about having many friends, but having influential friends
- **Recursive Influence**: Users connected to other highly-connected users score higher
- **Elite Networks**: Identifies users in the "inner circle" of influential people

---

### 15. Plot the distribution of eigenvector centralities. Identify the eigenvector centralities of nodes based on their size

```python
plt.figure(figsize=(15, 12))
eigen_values = list(eigen_vector.values())

plt.hist(eigen_values, bins=20, alpha=0.7, color='purple', edgecolor='black')
plt.xlabel('Eigenvector Centrality')
plt.ylabel('Frequency')
plt.title('Distribution of Eigenvector Centralities')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**How the code works:**

1. **Extract Eigenvector Values**:
   - `eigen_vector.values()` gets all eigenvector centrality scores from the dictionary
   - `list()` converts to a list for plotting and analysis

2. **Create Distribution Histogram**:
   - `plt.hist(eigen_values, bins=20)` creates histogram with 20 bins
   - `bins=20` divides the range of values into 20 equal intervals
   - `alpha=0.7` makes bars semi-transparent for better visual appeal
   - `color='purple'` sets the bar color to distinguish from other centrality plots
   - `edgecolor='black'` adds black borders around bars for clarity

3. **Format the Plot**:
   - X-axis shows eigenvector centrality values (typically 0 to 1)
   - Y-axis shows frequency (how many users have each centrality range)
   - Grid helps read exact values from the plot

**What the distribution shows:**
- Most users typically have low eigenvector centrality (left side of histogram)
- Few users have high eigenvector centrality (right side of histogram)
- This reveals the network's influence hierarchy - most users are regular, few are highly influential
- A right-skewed distribution is common, showing power-law-like influence distribution

**Distribution insights:**
- **Power Law Pattern**: Usually shows few highly influential users and many with low influence
- **Elite vs. Regular Users**: Clear distinction between influential and regular users
- **Network Hierarchy**: Reveals the hierarchical structure of influence in the network

---

## Conclusion: 
- **Identify influential users** (high centrality scores)
- **Understand information flow** (shortest paths and network structure)
- **Assess network resilience** (connectivity and critical bridges)
- **Optimize content distribution** (leverage central nodes for maximum reach)
- **Detect community structures** (through betweenness centrality patterns)
- **Measure network efficiency** (via average path lengths and closeness centrality)
