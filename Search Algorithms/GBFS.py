import heapq

class TreeNode:
    def __init__(self, state, heuristic=0):
        self.state = state
        self.heuristic = heuristic
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def goal_test(node, goal):
    return node.state == goal


def greedy_best_first_search(start_node, goal):
    visited = set()
    priority_queue = [(start_node.heuristic, start_node, [start_node.state])]

    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)

        if current_node.state in visited:
            continue

        visited.add(current_node.state)

        if goal_test(current_node, goal):
            return path

        for child in current_node.children:
            if child.state not in visited:
                heapq.heappush(priority_queue, (child.heuristic, child, path + [child.state]))

    return "Failure"


# Taking input
nodes = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    state = int(input("Enter node state: "))
    heuristic = int(input(f"Enter heuristic for node {state}: "))
    if state not in nodes:
        nodes[state] = TreeNode(state, heuristic)

    num_children = int(input(f"Enter number of children for node {state}: "))
    for _ in range(num_children):
        child_state = int(input("Enter child state: "))
        if child_state not in nodes:
            child_heuristic = int(input(f"Enter heuristic for child node {child_state}: "))
            nodes[child_state] = TreeNode(child_state, child_heuristic)
        nodes[state].add_child(nodes[child_state])

initial_state = int(input("Enter initial state: "))
goal_state = int(input("Enter goal state: "))

solution = greedy_best_first_search(nodes[initial_state], goal_state)
print("Greedy Best-First Search Solution Path:", solution)