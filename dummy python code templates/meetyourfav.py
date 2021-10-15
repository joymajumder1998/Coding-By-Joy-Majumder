import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G=nx.read_edgelist("input.txt")
N=list(G.nodes)
print(G.nodes)
nx.draw(G)
plt.show()
spll=[]
for u in N:
    for v in N:
        if(u!=v):
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between ",u," and ",v," is : ",l)
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll)
avg_spl=np.average(spll)
print(min_spl)
print(max_spl)
print(avg_spl)