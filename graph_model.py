import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# ----------------------------
# FILE PATHS
# ----------------------------

nodes_path = "data/Nodes.csv"
edges_path = "data/Edges (Plant).csv"

# ----------------------------
# LOAD DATA
# ----------------------------

nodes = pd.read_csv(nodes_path)
edges = pd.read_csv(edges_path)

print("Nodes Loaded:", nodes.shape)
print("Edges Loaded:", edges.shape)

print("\nNodes Columns:", nodes.columns)
print("Edges Columns:", edges.columns)

# ----------------------------
# CREATE GRAPH
# ----------------------------

G = nx.DiGraph()

# ADD NODES
for node in nodes["Node"]:
    G.add_node(node)

# ADD EDGES
for _, row in edges.iterrows():
    source = row["node1"]
    target = row["node2"]
    G.add_edge(source, target)

# ----------------------------
# GRAPH SUMMARY
# ----------------------------

print("\nSupply Chain Graph Created")
print("Total Nodes:", G.number_of_nodes())
print("Total Edges:", G.number_of_edges())

# ----------------------------
# CLEAN VISUALIZATION
# ----------------------------

plt.figure(figsize=(14,10))

# spring layout (NO scipy needed)
pos = nx.spring_layout(G, k=1.5, iterations=50, seed=42)

# draw nodes
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=500,
    node_color="skyblue"
)

# draw edges lighter
nx.draw_networkx_edges(
    G,
    pos,
    width=0.4,
    alpha=0.4,
    arrows=False
)

# show only a few labels
important_nodes = list(G.nodes())[:10]

labels = {node: node for node in important_nodes}

nx.draw_networkx_labels(
    G,
    pos,
    labels=labels,
    font_size=8
)

plt.title("Supply Chain Network Graph (Clean View)")
plt.axis("off")
plt.show()