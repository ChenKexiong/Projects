# input: a list of links
# output: a graph in form of dict
from collections import defaultdict as dt


def link_to_graph(links):
    graph = dt(list)
    for link in links:
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    print graph

links = [(1, 2), (1, 4), (2, 3), (3, 4)]
link_to_graph(links)
