import pandas as pd
import networkx as nx

# -----------------------------
# LOAD DATA
# -----------------------------

nodes = pd.read_csv("data/Nodes.csv")
edges = pd.read_csv("data/Edges (Plant).csv")

# -----------------------------
# CREATE GRAPH
# -----------------------------

G = nx.DiGraph()

# add nodes
for node in nodes["Node"]:
    G.add_node(node)

# add edges with cost
for _, row in edges.iterrows():
    
    source = row["node1"]
    target = row["node2"]

    # assign default transport cost
    cost = 1

    G.add_edge(source, target, weight=cost)

print("Graph Created")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())


# -----------------------------
# OPERATIONS RESEARCH PART
# -----------------------------

def find_optimal_route(graph, source, destination):

    try:
        path = nx.shortest_path(graph, source, destination, weight="weight")
        cost = nx.shortest_path_length(graph, source, destination, weight="weight")

        return path, cost

    except nx.NetworkXNoPath:
        return None, None


# -----------------------------
# TEST OPTIMIZATION
# -----------------------------

source = list(G.nodes())[0]
destination = list(G.nodes())[10]

route, cost = find_optimal_route(G, source, destination)

print("\nOptimal Route:")
print(route)

print("\nTotal Cost:", cost)