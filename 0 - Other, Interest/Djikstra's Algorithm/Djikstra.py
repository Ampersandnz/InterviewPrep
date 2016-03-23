import matplotlib.pyplot as plt
import networkx as nx

__author__ = 'Michael'
# Personal test to learn/test implement for reference Dijkstra's Algorithm
# Graph setup and plotting code from:
# https://networkx.github.io/documentation/latest/examples/drawing/weighted_graph.html

__INFINITY = 1000


def main():
    G = setup_graph()

    # Shortest path a -> d -> c -> f
    distance = dijkstra(G, 'a', 'f')
    print('Distance from a to f is ' + distance)
    draw_graph(G)

    G.remove_node('d')
    print('Removed node d')

    # New shortest path a -> c -> f
    distance = dijkstra(G, 'a', 'f')
    print('Distance from a to f is now ' + distance)

    draw_graph(G)


def dijkstra(G, start, end):
    distances = dict()
    unvisited = []

    # Initialise distances to all nodes as infinite, except start node = 0
    for n in G:
        if n == start:
            distances[n] = 0
        else:
            distances[n] = __INFINITY

        unvisited.append(n)

    current = start

    # Loop until destination node or all reachable nodes reached
    while end in unvisited or min(distances[x] for x in unvisited) == __INFINITY:
        # For each neighbour of current node
        for node in G[current]:
            # Get distance
            distance = G[current][node]['weight']

            # Calculate new tentative minimum distance from start
            tentative = distances[current] + distance

            # If less than current tentative distance, replace the old value
            if tentative < distances[node]:
                distances[node] = tentative

        # Once all neighbours have been calculated, mark node as visited
        unvisited.remove(current)

        # To avoid error on min() function
        if len(unvisited) == 0:
            break

        # Get subset of distances dict containing only unvisited nodes
        sub_dict = dict([(u, distances.get(u)) for u in unvisited])

        # Invert the dictionary (keys <-> values)
        inverse_distances = {v: k for k, v in sub_dict.items()}

        # Find the unvisited node with the smallest tentative distance
        current = inverse_distances[min(inverse_distances)]

    # Return the total distance to the destination node
    return str(distances[end])


def setup_graph():
    G = nx.Graph()

    G.add_edge('a', 'b', weight=6)
    G.add_edge('a', 'c', weight=8)
    G.add_edge('c', 'd', weight=1)
    G.add_edge('c', 'e', weight=7)
    G.add_edge('c', 'f', weight=9)
    G.add_edge('a', 'd', weight=3)

    G.add_node('g')

    return G


def draw_graph(G):
    e_large = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
    e_small = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=e_large, width=6)
    nx.draw_networkx_edges(G, pos, edgelist=e_small, width=6, alpha=0.5, edge_color='b', style='dashed')

    # labels
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
