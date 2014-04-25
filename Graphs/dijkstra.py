# input: graph, node
# output: shortest path and the length
from collections import defaultdict as dt
from copy import deepcopy as dc


def get_path(path,node,node_path):
    tmp = path[node].pop()
    if tmp == -1:
        return
    else:
        node_path.append(tmp)
        return get_path(path,tmp,node_path)


def dijkstra(graph,node):
    known = [node]
    cost = {}
    inf = float('inf')
    path = dt(list)
    for k in graph.keys():
        cost[k] = inf
        path[k].append(-1)
    cost[node] = 0
    while len(known) != len(graph.keys()):
        cur = known[-1]
        for k,v in (graph[cur]).items():
            if (k not in known) and (v+cost[cur] < cost[k]):
                cost[k] = v + cost[cur]
                path[k].append(cur)
        min_node = min(filter(lambda x: x not in known,cost),key=lambda x: cost[x])
        known.append(min_node)
    shortest_path = {}
    for k in graph.keys():
        node_path = []
        tmp_path = dc(path)
        get_path(tmp_path,k,node_path)
        node_path.reverse()
        shortest_path[k] = node_path
    return shortest_path

graph = {
        0:{2:3, 3:4, 4:1},
        1:{2:4, 5:6, 6:4},
        2:{0:3, 1:4, 5:2},
        3:{0:4},
        4:{0:1, 7:9},
        5:{1:6, 2:2, 6:6, 7:4},
        6:{1:4, 5:6},
        7:{4:9, 5:4}
        }
graph1={ 
    0:{1:3, 2:8, 4:7},
    1:{0:3, 2:6, 5:8},
    2:{0:8, 1:6, 6:7},
    3:{7:3},
    4:{0:7, 7:9},
    5:{1:8, 6:9},
    6:{2:7, 5:9},
    7:{3:3, 4:9}
}

s_path = dijkstra(graph,2)

print s_path
