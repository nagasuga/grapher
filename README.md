Grapher
=======

lib to create graph/nodes to test graph algorithms


Install
=======

```
pip install -U git+https://github.com/nagasuga/grapher.git
```


Usage
=====

```
from grapher import Graph
graph = Graph()
graph.add_node('A')
graph.remove_node('A')

graph.add_node('A')
graph.add_node('B')
graph.add_edge('A', 'B', weight=2)
graph.remove_edge('A', 'B')
```
