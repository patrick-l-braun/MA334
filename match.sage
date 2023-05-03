import networkx as nx

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

def create_incidence_matrix(G: nx.Graph, perfect_matchings):
    # want to create matrix of len(E) * len(matchings) matrix

    # first create dictionary to convert edge to id
    edge_id = {edge: i for i, edge in enumerate(list(G.edges))}
    print(edge_id, G.edges)
    num_edges = len(list(G.edges))
    num_matchings = len(perfect_matchings)

    # create matrix
    M = [[0] * num_matchings for _ in range(num_edges)]
    for i, matching in enumerate(perfect_matchings):
        for edge in matching:
            M[edge_id[edge]][i]= 1

    return M

def set_up_polyhedron(M):
    #The construction of a polyhedron object via its
    # H-representation, requires a precise format. Each inequality
    # must be written as [b_i,a_i1, ..., a_id]. for (a_i1,...a_id)x + bi >= 0
    num_matchings = len(M[0])
    ieqs = []
    # x >= 0 and x <= 1
    for i in range(num_matchings):
        x = [0] * num_matchings
        x[i] = 1
        ieqs.append([0] + x) # says that xi + 0 >= 0
        x[i] = -1
        ieqs.append([1] + x) # says that -xi + 1 >= 0 i.e. 1 >= xi
    eqns = [[1] + row for row in M] # this gives us Mx = 1
    print(eqns, ieqs)
    P = Polyhedron(ieqs=ieqs, eqns = eqns)
    return P

G = nx.petersen_graph()
g_match = perfect_matching(G)
print(g_match)
m = create_incidence_matrix(G, g_match)
print(m)
p = set_up_polyhedron(m)
print(p)
print(p.volume(measure='induced'))
