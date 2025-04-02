from collections import deque

class TreeNode:
    def __init__(self, state, path_cost=0):
        self.state = state  # State of the node
        self.children = []  # List to hold child nodes
        self.path_cost = path_cost  # Path cost to reach this node

    def add_child(self, child):
        self.children.append(child)

def goal_test(node, goal):
    return node.state == goal

def bfs(problem):
    node = problem['initial_state']
    frontier = deque([(node, [node.state])])  # FIFO queue with paths
    visited = set()  # Set to keep track of visited nodes

    if goal_test(node, problem['goal']):
        return [node.state]  # Return path if initial state is the goal

    while frontier:
        node, path = frontier.popleft()

        if node.state in visited:  # Skip if node is already visited
            continue
        visited.add(node.state)

        for child in node.children:
            if child.state not in visited:  # Prevent revisiting
                new_path = path + [child.state]
                if goal_test(child, problem['goal']):
                    return new_path
                frontier.append((child, new_path))

    return "Failure"  # No solution found

# Taking input from the user
nodes = {}  # Dictionary to store nodes
n = int(input("Enter number of nodes: "))  
for _ in range(n):
    state = int(input("Enter node state: "))  
    if state not in nodes:
        nodes[state] = TreeNode(state)

    num_children = int(input(f"Enter number of children for node {state}: "))
    for _ in range(num_children):
        child_state = int(input("Enter child state: "))
        if child_state not in nodes:
            nodes[child_state] = TreeNode(child_state)
        nodes[state].add_child(nodes[child_state])  # Allow cyclic edges

initial_state = int(input("Enter initial state: "))  
goal_state = int(input("Enter goal state: "))  

problem = {'initial_state': nodes[initial_state], 'goal': goal_state}  
print("BFS Solution Path:", bfs(problem))