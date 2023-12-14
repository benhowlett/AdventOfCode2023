class Node:
    def __init__(self, symbol, loc, connections):
        self.symbol = symbol
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
    
def get_connections(symbol, loc):
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
        
def get_symbol(connections):
    match connections:
        case [True, False, True, False]:
            return '|'
        case [False, True, False, True]:
            return '-'
        case [True, True, False, False]:
            return 'L'
        case [True, False, False, True]:
            return 'J'
        case [False, False, True, True]:
            return '7'
        case [False, True, True, False]:
            return 'F'
        case _:
            return ''
        
def follow_paths(paths, map):
    reachedFurthestPoint = False
    while not reachedFurthestPoint:
        for i, path in enumerate(paths):
            


input = open('test.txt', 'r')

map = []

for line in input:
    map.append(list(line.strip()))

startLoc = ()

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S": startLoc = (i, j)
        map[i][j] = Node(map[i][j], (i, j), get_connections(map[i][j]))

startConnections = [map[startLoc[0] - 1][startLoc[1]].symbol, map[startLoc[0]][startLoc[1] + 1].symbol, map[startLoc[0] + 1][startLoc[1]].symbol, map[startLoc[0]][startLoc[1] - 1].symbol]

for i, connection in enumerate(startConnections):
    startConnections[i] = get_connections(connection)[i-2]

map[startLoc[0]][startLoc[1]].symbol = get_symbol(startConnections)
map[startLoc[0]][startLoc[1]].connections = startConnections

paths = []

for i, connection in enumerate(map[startLoc[0]][startLoc[1]].connections):
    print(connection)
    if connection == True:
        newPath = Path(startLoc)
        match i:
            case 0:
                nextLoc = (startLoc[0] - 1, startLoc[1])
            case 1:
                nextLoc = (startLoc[0], startLoc[1] + 1)
            case 2:
                nextLoc = (startLoc[0] + 1, startLoc[1])
            case 3:
                nextLoc = (startLoc[0], startLoc[1] - 1)
            case _:
                nextLoc = (0, 0)
        newPath.add_node_to_path(map[nextLoc[0]][nextLoc[1]])
        paths.append(newPath)

        