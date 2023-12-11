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
    
def get_move_count(start, end, nodes, instructions):
    moveCount = 0
    instructionIndex = 0
    currentNode = start
    while currentNode != end:
        if instructionIndex == len(instructions): instructionIndex = 0
        currentNode = get_next_node(nodes[currentNode], instructions[instructionIndex])
        moveCount += 1
    return moveCount

input = open('input.txt', 'r')

instructions = ""

nodes = {}

for index, line in enumerate(input):
    if index == 0:
        instructions = line.strip()
    elif index > 1:
        name = line.strip()