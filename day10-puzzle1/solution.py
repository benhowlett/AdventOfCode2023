class Node:
    def __init__(self, symbol, loc, connections):
        self.symbol = symbol
        self.loc = loc
        self.connections = connections

class Path:
    def __init__(self, start):
        self.nodes = [start]
    
    def get_path_len(self) -> int:
        return len(self.nodes) - 1
    
    def add_node_to_path(self, node):
        self.nodes.append(node)

    def get_current_node(self) -> Node:
        return self.nodes[-1]

    def get_previous_node_loc(self):
        return self.nodes[-2].loc
    
    def get_next_node_loc(self):
        # print("Next node location info\n", self.nodes[-1].connections)
        for connection in self.nodes[-1].connections:
            # for node in self.nodes:
            #     print(node.loc)
            # print("current node loc:", self.nodes[-1].loc)
            # print("connection in current node:", connection)
            # print("previous node loc:", self.nodes[-2].loc)
            if connection != self.nodes[-2].loc: 
                return connection
        return ()

def get_connections(symbol, loc):
    match symbol:
        case '|':
            return [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1])]
        case '-':
            return [(loc[0], loc[1] + 1), (loc[0], loc[1] - 1)]
        case 'L':
            return [(loc[0] - 1, loc[1]), (loc[0], loc[1] + 1)]
        case 'J':
            return [(loc[0] - 1, loc[1]), (loc[0], loc[1] - 1)]
        case '7':
            return [(loc[0] + 1, loc[1]), (loc[0], loc[1] - 1)]
        case 'F':
            return [(loc[0], loc[1] + 1), (loc[0] + 1, loc[1])]
        case _:
            return []

input = open('test.txt', 'r')

map = []

for line in input:
    map.append(list(line.strip()))

startLoc = ()

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S": startLoc = (i, j)
        map[i][j] = Node(map[i][j], (i, j), get_connections(map[i][j], (i, j)))

startConnections = []

for i in range(len(map)):
    for j in range(len(map[i])):
        for connection in map[i][j].connections:
            if connection == startLoc: startConnections.append(map[i][j].loc)
map[startLoc[0]][startLoc[1]].connections = startConnections

paths = [Path(map[startLoc[0]][startLoc[1]]), Path(map[startLoc[0]][startLoc[1]].connections)]

maxPathFound = False

while not maxPathFound:
    for i, path in enumerate(paths):
        if path.get_path_len() == 0:
            currentNode = path.nodes[-1]
            print(currentNode)
            nextLoc = currentNode.connections[i]
            path.add_node_to_path(map[nextLoc[0]][nextLoc[1]])
    maxPathFound = True

print(paths[0].get_current_node().loc, paths[0].get_next_node_loc())
print(paths[0].get_current_node().loc, paths[0].get_next_node_loc())


