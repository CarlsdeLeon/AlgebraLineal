import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
W = nx.Graph()
D = nx.Graph()


fig, axes = plt.subplots(1,3)

fig.set_size_inches(9,3)

nx.draw(G,ax=axes[0],with_labels=True, node_color='#22bbbb',node_size=500)
axes[0].set_title("Gráfica G")

layout=nx.spring_layout(W)
labels2 = nx.get_edge_attributes(W,'weight')
nx.draw(W,layout,ax=axes[1],with_labels=True, node_color='#bb22bb',node_size=500)
nx.draw_networkx_edge_labels(W,layout,ax=axes[1],edge_labels=labels2)
axes[1].set_title("Gráfica ponderada G")

nx.draw(D,ax=axes[2],with_labels=True, node_color='#bbbb22',node_size=500)
axes[2].set_title("Gráfica dirigida D")



plt.show()