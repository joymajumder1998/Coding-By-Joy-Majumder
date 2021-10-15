import networkx as nx
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(10,0.2) #create a graph of 10 nodes and edge prob.0.2
print(G.nodes) #print the name of edges
nx.draw(G)
nx.write_gexf(G,"mygraph.gexf")
plt.show()