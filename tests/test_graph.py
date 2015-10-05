from unittest import TestCase


from grapher import Graph, NodeNotFound, DuplicateNodeError, EdgeNotFound


class GraphTest(TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_adding_nodes(self):
        self.assertEqual(self.graph._graph, {})
        self.graph.add_node('1')
        self.assertEqual(self.graph._graph, {'1': {}})
        self.graph.add_node('2')
        self.assertEqual(self.graph._graph, {'1': {}, '2': {}})

    def test_add_duplicate_node(self):
        self.graph.add_node('1')
        self.assertRaises(DuplicateNodeError, self.graph.add_node, '1')

    def test_remove_node(self):
        self.graph.add_node('1')
        self.graph.remove_node('1')
        self.assertEqual(self.graph._graph, {})

    def test_remove_non_existing_node(self):
        self.assertRaises(NodeNotFound, self.graph.remove_node, '1')

    def test_add_edges(self):
        self.graph.add_node('1')
        self.graph.add_node('2')
        self.graph.add_edge(from_node='1', to_node='2', weight=1)
        self.assertEqual(self.graph._graph, {'1': {'2': 1}, '2': {}})

        self.graph.add_edge(from_node='2', to_node='1', weight=5)
        self.assertEqual(self.graph._graph, {'1': {'2': 1}, '2': {'1': 5}})

    def test_add_edge_overwrite_existing(self):
        self.graph.add_node('1')
        self.graph.add_node('2')
        self.graph.add_edge(from_node='1', to_node='2', weight=1)
        self.graph.add_edge(from_node='1', to_node='2', weight=5)
        self.assertEqual(self.graph._graph, {'1': {'2': 5}, '2': {}})

    def test_remove_node_with_edge(self):
        self.graph.add_node('1')
        self.graph.add_node('2')
        self.graph.add_edge(from_node='1', to_node='2', weight=1)
        self.graph.remove_node('2')
        self.assertEqual(self.graph._graph, {'1': {}})

    def test_remove_edges(self):
        self.graph.add_node('1')
        self.graph.add_node('2')
        self.graph.add_edge(from_node='1', to_node='2', weight=1)
        self.graph.remove_edge(from_node='1', to_node='2')
        self.assertEqual(self.graph._graph, {'1': {}, '2': {}})

    def test_remove_non_existing_edges(self):
        self.graph.add_node('1')
        self.graph.add_node('2')
        self.assertRaises(EdgeNotFound, self.graph.remove_edge,
                          from_node='1', to_node='2')

    def test_remove_edges_without_node(self):
        self.assertRaises(NodeNotFound, self.graph.remove_edge,
                          from_node='1', to_node='2')

    def test_complex_graph(self):
        exp_graph = {'A': {'C':2,
                           'D':6},
                     'B': {'D':8,
                           'A':3},
                     'C': {'D':7,
                           'E':5},
                     'D': {'E':-2},
                     'E': {}}

        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_node('D')
        self.graph.add_node('E')
        self.graph.add_edge(from_node='A', to_node='C', weight=2)
        self.graph.add_edge(from_node='A', to_node='D', weight=6)
        self.graph.add_edge(from_node='B', to_node='A', weight=3)
        self.graph.add_edge(from_node='B', to_node='D', weight=8)
        self.graph.add_edge(from_node='C', to_node='D', weight=7)
        self.graph.add_edge(from_node='C', to_node='E', weight=5)
        self.graph.add_edge(from_node='D', to_node='E', weight=-2)
        self.assertEqual(self.graph._graph, exp_graph)

    def test_from_dict(self):
        data = {'A': {'C':2,
                      'D':6},
                'B': {'D':8,
                      'A':3},
                'C': {'D':7,
                      'E':5},
                'D': {'E':-2},
                'E': {}}
        self.graph.from_dict(data)
        self.assertEqual(self.graph._graph, data)
