from collections import deque

class TreeNode: def init(self, state, path_cost=0): self.state = state  # State of the node self.children = []  # List to hold child nodes self.path_cost = path_cost  # Path cost to reach this node

def add_child(self, child):
    self.children.append(child)

def goal_test(node, goal): return node.state == goal

def bfs(problem): node = problem['initial_state'] frontier = deque([(node, [node.state])])  # FIFO queue with path explored = set()

if goal_test(node, problem['goal']):
    return [node.state]  # Return path if initial state is the goal

while frontier:
    node, path = frontier.popleft()
    explored.add(node.state)
    
    for child in node.children:
        if child.state not in explored and child not in [n for n, _ in frontier]:
            new_path = path + [child.state]  # Update path
            if goal_test(child, problem['goal']):
                return new_path  # Return path to solution
            frontier.append((child, new_path))

return "Failure"  # Return failure if no solution found

Taking input from the user

nodes = {}  # Dictionary to store nodes n = int(input("Enter number of nodes: ")) for _ in range(n): state = int(input("Enter node state: ")) if state not in nodes: nodes[state] = TreeNode(state)

num_children = int(input(f"Enter number of children for node {state}: "))
for _ in range(num_children):
    child_state = int(input("Enter child state: "))
    if child_state not in nodes:
        nodes[child_state] = TreeNode(child_state)
    if nodes[child_state] not in nodes[state].children:  # Prevent duplicate edges
        nodes[state].add_child(nodes[child_state])

initial_state = int(input("Enter initial state: ")) goal_state = int(input("Enter goal state: "))

problem = {'initial_state': nodes[initial_state], 'goal': goal_state} print("BFS Solution Path:", bfs(problem))

