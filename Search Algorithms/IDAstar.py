class TreeNode:
    def __init__(self, state, heuristic=0):
        self.state = state
        self.heuristic = heuristic
        self.children = []  # Each child is a tuple (child_node, cost)

    def add_child(self, child, cost):
        self.children.append((child, cost))


def goal_test(node, goal):
    return node.state == goal


def ida_star(root, goal):
    def dfs(node, g, threshold, path, visited):
        f = g + node.heuristic
        if f > threshold:
            return f
        if goal_test(node, goal):
            return path
        min_threshold = float('inf')
        visited.add(node.state)
        for child, cost in node.children:
            if child.state not in visited:
                result = dfs(child, g + cost, threshold, path + [child.state], visited.copy())
                if isinstance(result, list):  # Found path
                    return result
                min_threshold = min(min_threshold, result)
        return min_threshold

    threshold = root.heuristic
    while True:
        result = dfs(root, 0, threshold, [root.state], set())
        if isinstance(result, list):
            return result
        if result == float('inf'):
            return "Failure"
        threshold = result


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
        cost = int(input(f"Enter cost from {state} to {child_state}: "))
        if child_state not in nodes:
            child_heuristic = int(input(f"Enter heuristic for child node {child_state}: "))
            nodes[child_state] = TreeNode(child_state, child_heuristic)
        nodes[state].add_child(nodes[child_state], cost)

initial_state = int(input("Enter initial state: "))
goal_state = int(input("Enter goal state: "))

solution = ida_star(nodes[initial_state], goal_state)
print("IDA* Search Solution Path:", solution)