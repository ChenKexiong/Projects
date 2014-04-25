# input: a graph in form of dict
# output: true stands for connected and vice versa


def is_connected(graph):
    visited = set()
    start = (graph.keys())[0]
    s = [start]
    while len(s):
        node = s.pop()
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                s.append(n)
    if len(visited) == len(graph.keys()):
        return True
    else:
        return False

graph1 = {1:[2, 3], 2:[1], 3:[1], 4:5, 5:4}
graph2 = {1:[2, 4], 2:[1, 3], 3:[2, 4], 4:[1, 3]}
if is_connected(graph2):
    print "Connected!"
else:
    print "Not connected!"
