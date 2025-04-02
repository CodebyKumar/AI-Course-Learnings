import heapq

class TreeNode:
    def __init__(self, state):
        self.state = state
        self.children = []  # Stores (child, cost) tuples

    def add_child(self, child, cost):
        self.children.append((child, cost))

def goal_test(node, goal):
    return node.state == goal

def ucs(problem):
    initial_node = problem['initial_state']
    goal_state = problem['goal']

    priority_queue = [(0, initial_node, [initial_node.state])]  # (Cost, Node, Path)
    visited = {}  # Dictionary to store the minimum cost to reach each node

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)  # Get node with least cost

        if node.state in visited and visited[node.state] <= cost:
            continue  # Ignore if we already found a cheaper way

        visited[node.state] = cost  # Update cost for this node

        if goal_test(node, goal_state):  # Goal check
            return path, cost  # Return path and cost

        for child, child_cost in node.children:
            new_cost = cost + child_cost
            heapq.heappush(priority_queue, (new_cost, child, path + [child.state]))

    return "Failure"  # No path found

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
        cost = int(input(f"Enter cost from {state} to {child_state}: "))

        if child_state not in nodes:
            nodes[child_state] = TreeNode(child_state)

        nodes[state].add_child(nodes[child_state], cost)

initial_state = int(input("Enter initial state: "))  
goal_state = int(input("Enter goal state: "))  

problem = {'initial_state': nodes[initial_state], 'goal': goal_state}  
solution = ucs(problem)

if solution != "Failure":
    print("UCS Solution Path:", solution[0])
    print("Total Cost:", solution[1])
else:
    print("UCS: No solution found")