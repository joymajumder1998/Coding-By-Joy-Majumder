import networkx as nx
import matplotlib.pyplot as plt

G=nx.complete_graph(3) #create complete graphs of 3 nodes
print(G.nodes) #print the name of edges
nx.draw(G)
plt.show()