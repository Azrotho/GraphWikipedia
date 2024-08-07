import networkx as nx
import pickle
import matplotlib.pyplot as plt

graph = pickle.load(open('wikipedia-final.pickle', 'rb'))
print("Graphe chargé avec succès.")

print(f"Nombre de nœuds : {graph.number_of_nodes()}")
print(f"Nombre d'arêtes : {graph.number_of_edges()}")


nx.draw_random(graph, with_labels=True, node_size=0.1)
# Save the graph in a file
print("Sauvegarde du graphe...")
fig = plt.gcf()
fig.set_size_inches(4000, 2000)
fig.savefig("wikipedia.png", dpi=100)