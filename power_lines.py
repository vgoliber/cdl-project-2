import networkx as nx
import matplotlib.pyplot as plt

# Build the graph using networkx
M = 6
N = 6
G = nx.grid_2d_graph(M,N)

# Store an image of the graph
pos = {(x,y):(y,-x) for x,y in G.nodes()}
nx.draw(G, pos)
plt.savefig('plot.png', bbox_inches='tight')

# Define our sampler
from dwave.system import LeapHybridSampler
sampler = LeapHybridSampler()

# Solve our problem
import dwave_networkx as dnx
answer = dnx.min_vertex_cover(G, sampler)
print("Found cover of size", len(answer))
print("\nCover:\n", answer)

# Visualize solution
plt.clf()
pos = {(x,y):(y,-x) for x,y in G.nodes()}
nx.draw_networkx_nodes(G, pos, nodelist=answer, node_color='r')
nx.draw_networkx_nodes(G, pos, nodelist=G.nodes()-answer, node_color='c')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), style='solid', width=3)

plt.savefig('answer_plot.png', bbox_inches='tight')