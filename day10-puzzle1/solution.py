class Node:
    def __init__(self, loc, connections):
        self.loc = loc
        self.connections = connections

class Path:
    def __init__(self, start):
        self.nodes = [start]
    
    def get_path_len(self) -> int:
        return len(self.nodes - 1)
    
    def add_node_to_path(self, node):
        self.nodes.append(node)

    def get_current_node(self) -> Node:
        return self.nodes[-1]

    def get_node_before(self, node):
        for i in range(len(self.nodes)):
            if self.nodes[i] == node: return self.nodes[i - 1]
        return 0
    
def get_connections(symbol):
    match symbol:
        case '|':
            return [True, False, True, False]
        case '-':
            return [False, True, False, True]
        case 'L':
            return [True, True, False, False]
        case 'J':
            return [True, False, False, True]
        case '7':
            return [False, False, True, True]
        case 'F':
            return [False, True, True, False]
        case _:
            return [False, False, False, False]

input = open('test.txt', 'r')

map = []

for line in input:
    map.append(list(line.strip()))

for i in range(len(map)):
    for j in range(len(map[i])):
        map[i][j] = Node((i, j), get_connections(map[i][j]))

for node in map[0]:
    print(node.loc, node.connections)