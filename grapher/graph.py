from .exceptions import NodeNotFound, DuplicateNodeError, EdgeNotFound


class Graph(object):
    def __init__(self):
        self._graph = {}
        self.connected_from = {}

    def add_node(self, name):
        if name in self._graph:
            raise DuplicateNodeError('Node-{} already in graph'.format(name))
        self._graph[name] = {}
        self.connected_from[name] = []

    def remove_node(self, name):
        if name not in self._graph:
            raise NodeNotFound('Node-{} not found'.format(name))
        del self._graph[name]
        for connected_node in self.connected_from[name]:
            del self._graph[connected_node][name]

    def add_edge(self, from_node, to_node, weight):
        self._graph[from_node][to_node] = weight
        self.connected_from[to_node].append(from_node)

    def remove_edge(self, from_node, to_node):
        if from_node not in self._graph:
            raise NodeNotFound('Node-{} not found'.format(from_node))

        if to_node not in self._graph[from_node]:
            err_msg = 'Edge {}=>{} not found'.format(from_node, to_node)
            raise EdgeNotFound(err_msg)

        del self._graph[from_node][to_node]

    def from_dict(self, data):
        self._graph = data
