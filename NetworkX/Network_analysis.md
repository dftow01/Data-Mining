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
  Social networks often have surprisingly short average shortest paths, known as “six degrees of separation,” meaning most people are connected by just a few steps.

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

If needed, shortest path analysis can provide deep insights into the connectivity, information flow, and resilience of social and other complex networks.


## **Centrality in NetworkX**
1. Degree Centrality - Nodes with many direct connections	nx.degree_centrality(G)
2. Betweenness - Centrality	Nodes that lie on many shortest paths — act as "bridges"	nx.betweenness_centrality(G)
3. Closeness Centrality - Nodes that are close to all others (short average path)	nx.closeness_centrality(G)
4. Eigenvector Centrality	- Nodes connected to other well-connected nodes (influence)	nx.eigenvector_centrality(G)
5. PageRank	- A variant of eigenvector centrality (popular in web analysis)	nx.pagerank(G)
6. Katz Centrality - Like eigenvector, but considers longer paths with decay	nx.katz_centrality(G)

Use Cases (Facebook Ego Network Context)
1. Degree Centrality: Find users with the most friends.
2. Betweenness Centrality: Identify users who connect different communities.
3. Closeness Centrality: Spot users who can quickly spread information.
4. Eigenvector/PageRank: Discover "influential" users beyond direct connections.

