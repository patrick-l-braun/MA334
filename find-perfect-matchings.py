import networkx as nx


def perfect_matching(G: nx.Graph):
    # Basecheck for existence perfect matching
    if len(G.edges()) < len(G.nodes())/2:
        return []
    elif len(G.nodes()) == 2 and len(G.edges()) == 1:
        return [[list(G.edges)[0]]]

    # fix an edge
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
    """ identical function but uses max_weight_matching as base case"""

    # Base case check for existence perfect matching
    if len(nx.max_weight_matching(G)) != len(list(G.nodes))/2:
        return []
    elif len(G.nodes()) == 2 and len(G.edges()) > 0:
        return [[list(G.edges)[0]]]

    # fix an edge
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


# Example Usage
petersen = nx.read_graph6("./graph_examaple/10_snark.g6")
matching_petersen = perfect_matching(petersen)
print(
    f'For petersen, number of matchings: {len(matching_petersen)} \nMatchings: {matching_petersen}')


eighteen_node_snark = nx.read_graph6("./graph_examaple/20_snark.g6")[0]
matchings_in_snark = perfect_matching(eighteen_node_snark)
print(
    f'\n\nFor 18 node snark example, number of matchings: {len(matchings_in_snark)}')
