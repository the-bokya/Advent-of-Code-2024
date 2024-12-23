import networkx as nx
node_pairs = []
while True:
    try:
        node_pair = input().split("-")
        node_pairs.append(node_pair)
    except:
        break

G = nx.Graph()
G.add_edges_from(node_pairs)
clique_largest = 0
out = ""
for clique in nx.enumerate_all_cliques(G):
    if len(clique) > clique_largest:
        out = ",".join(sorted(clique))
        clique_largest = len(clique)
print(out)
