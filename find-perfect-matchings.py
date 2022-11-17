import networkx as nx
import matplotlib.pyplot as plt
import time


# AMPL solver for mixed integr programming.
# normaliz, polymake, sagemath
# first

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
print(G)


# H = nx.Graph()
# H.add_nodes_from([1, 2, 3, 4, 5])
# H.add_edges_from([(1, 2), (2, 3), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# subax1 = plt.subplot(121)
# nx.draw(G)


# # newH = H.subgraph(list(set(H.nodes()) - set([3])))
# subax2 = plt.subplot(122)
# c = G.copy()
# c.remove_edge(3, 4)
# nx.draw(c)
# plt.show()


def perfect_matching(G: nx.Graph):
    # Base
    # check for existence perfect matching
    if len(G.edges()) < len(G.nodes())/2:
        # if not nx.is_perfect_matching(G, nx.maximal_matching(G)):
        return []
    elif len(G.nodes()) == 2 and len(G.edges()) > 0:
        return [[list(G.edges)[0]]]

    current_edge = list(G.edges)[0]
    node1 = current_edge[0]
    node2 = current_edge[1]

    # find all perfect matchings including edge 1
    # induced subgraph of removing start and end node
    G_induced = G.subgraph(list(set(G.nodes) - set([node1, node2])))
    matchings_in_induced = perfect_matching(G_induced)
    matchings_including_edge = [m + [current_edge]
                                for m in matchings_in_induced]

    # find all matchings without edge 1
    copy = G.copy()
    copy.remove_edge(node1, node2)
    matchings_without_edge = perfect_matching(copy)
    # return their union
    return matchings_including_edge + matchings_without_edge


# print(nx.maximal_matching(G))
# print(perfect_matching(G))
# print(len(perfect_matching(nx.complete_graph(8))))
# print(perfect_matching(nx.petersen_graph()))

t0 = time.time()

snarks = nx.read_graph6(
    r'C:\Users\patri\OneDrive\Documents\LSE\Third_year\MA334\graph_examaple\22_snark.g6')
print("\n snarks")
for i, g in enumerate(snarks):
    print(f'On interation {i}/{len(snarks)}')
    print(len(perfect_matching(g)))
    print()


# print(f'Time taken for {len(snarks)} interations was {t}')
# print(f'Average seconds per iteration is {t/len(snarks)}')
# 22 nodes took 257 seconds for 31 graphs
# avreging 8.3 seconds per

print(len(perfect_matching(nx.complete_graph(12))))

t1 = time.time()
t = t1 - t0
print(t)
