import networkx as nx
import matplotlib.pyplot as plt
import time


# G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4, 5, 6])
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
# print(G)


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


def perfect_matching2(G: nx.Graph):
    # Base
    # check for existence perfect matching

    if len(nx.max_weight_matching(G)) != len(list(G.nodes))/2:
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


snarks = nx.read_graph6(
    r'C:\Users\patri\OneDrive\Documents\LSE\Third_year\MA334\graph_examaple\22_snark.g6')
print("snarks")


for i, g in enumerate(snarks):
    print(f'On interation {i}/{len(snarks)-1}')
    t0 = time.time()
    print(f'# of perfect matchings {len(perfect_matching(g))}')
    t1 = time.time()
    print(f'Time for perfect_matching {t1-t0}')
    print(f'# of perfect matchings {len(perfect_matching2(g))}')
    t2 = time.time()
    print(f'Time for perfect_matching2 {t2-t1}')
    print()
