from math import lcm

class Node:

    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

def get_next_node(node, direction) -> str:
    if direction == "L":
        return node.left
    else:
        return node.right
    
def get_move_count(starts, nodes, instructions):
    moveCount = 0
    instructionIndex = 0
    allEndWithZ = False
    currentNodes = starts
    while not allEndWithZ:
        if instructionIndex == len(instructions): instructionIndex = 0
        allEndWithZ = True
        for i, node in enumerate(currentNodes):
            # print(node)
            currentNodes[i] = get_next_node(nodes[node], instructions[instructionIndex])
            # print(node, node[2], node[2] != 'Z')
            if currentNodes[i][2] != 'Z': allEndWithZ = False 
            # else:
            #     print(currentNodes, moveCount, 'node index:', i, 'char:', currentNodes[i][2])
                # input("Press enter to continue...")
        moveCount += 1
        instructionIndex += 1

    return moveCount

file = open('input.txt', 'r')

instructions = ""

nodes = {}

for index, line in enumerate(file):
    if index == 0:
        instructions = line.strip()
    elif index > 1:
        name = line.strip().split()[0]
        left = line.strip().split()[2][1:-1]
        right = line.strip().split()[3][:-1]
        nodes[name] = Node(name, left, right)

starts = []

for node in nodes:
    if node[2] == 'A': starts.append(node)

firstHits = []

for start in starts:
    firstHits.append(get_move_count([start], nodes, instructions))

print(lcm(firstHits[0], firstHits[1], firstHits[2], firstHits[3], firstHits[4], firstHits[5]))