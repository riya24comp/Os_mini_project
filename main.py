import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create directed graph
G = nx.DiGraph()

# Input number of processes and resources
p = int(input("Enter number of processes: "))
r = int(input("Enter number of resources: "))

processes = [f"P{i+1}" for i in range(p)]
resources = [f"R{i+1}" for i in range(r)]

G.add_nodes_from(processes)
G.add_nodes_from(resources)

edges = []

# Input allocation edges (Resource -> Process)
alloc_edges = int(input("Enter number of allocation edges (Resource -> Process): "))
print("Enter allocation edges (R P):")
for _ in range(alloc_edges):
    res, proc = input().split()
    edges.append((res, proc))

# Input request edges (Process -> Resource)
req_edges = int(input("Enter number of request edges (Process -> Resource): "))
print("Enter request edges (P R):")
for _ in range(req_edges):
    proc, res = input().split()
    edges.append((proc, res))

# Prepare plot
fig, ax = plt.subplots()
pos = nx.circular_layout(G)

def update(frame):
    ax.clear()
    G.clear_edges()
    G.add_edges_from(edges[:frame+1])

    colors = ["lightblue" if node.startswith("P") else "lightgreen" for node in G.nodes()]

    nx.draw(G, pos,
            with_labels=True,
            node_color=colors,
            node_size=2000,
            font_size=12,
            arrows=True,
            ax=ax)

ani = FuncAnimation(fig, update, frames=len(edges), interval=1000, repeat=False)

plt.show()

# Deadlock detection after animation
try:
    nx.find_cycle(G, orientation='original')
    print("Deadlock detected in the Resource Allocation Graph!")
except:
    print("No Deadlock detected.")
