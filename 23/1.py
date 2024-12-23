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
count = 0
for clique in nx.enumerate_all_cliques(G):
    t = False
    if len(clique) == 3:
        for node in clique:
            if node[0] == "t":
                t = True
    if t:
        count += 1
print(count)
