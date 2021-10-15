import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
v=[1,2,3]
G.add_nodes_from(v)#add vertex from vertex set v
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
print(list(G.neighbors(1)))
print(G.nodes) #print the name of edges
nx.draw(G)
plt.show()