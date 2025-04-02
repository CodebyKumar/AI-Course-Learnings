class TreeNode:
    def __init__(self, state, path_cost=0):
        self.state = state  # State of the node
        self.children = []  # List to hold child nodes
        self.path_cost = path_cost  # Path cost to reach this node

    def add_child(self, child):
        self.children.append(child)

def goal_test(node, goal):
    return node.state == goal

def dls(node, goal, depth_limit, path, visited):
    if goal_test(node, goal):  # Goal check
        return path

    if depth_limit == 0:  # If depth limit reached, return failure
        return None

    visited.add(node.state)  # Mark node as visited

    for child in node.children:
        if child.state not in visited:  # Avoid revisiting nodes
            result = dls(child, goal, depth_limit - 1, path + [child.state], visited.copy())
            if result is not None:
                return result

    return None

def iddfs(problem, max_depth):
    for depth in range(max_depth + 1):  # Incrementally increase depth limit
        print(f"Searching with depth limit {depth}...")
        visited = set()
        result = dls(problem['initial_state'], problem['goal'], depth, [problem['initial_state'].state], visited)
        if result:
            return result  # Return path if solution is found
    return "Failure"

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
max_depth = int(input("Enter maximum depth limit: "))  

problem = {'initial_state': nodes[initial_state], 'goal': goal_state}  
print("IDDFS Solution Path:", iddfs(problem, max_depth))