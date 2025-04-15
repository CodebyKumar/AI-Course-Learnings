class TreeNode:
    def __init__(self, state, heuristic=0):
        self.state = state
        self.heuristic = heuristic
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def goal_test(node, goal):
    return node.state == goal


def best_first_recursive(node, goal, path, visited):
    if goal_test(node, goal):
        return path

    visited.add(node.state)

    # Sort children by heuristic
    sorted_children = sorted(
        [child for child in node.children if child.state not in visited],
        key=lambda x: x.heuristic
    )

    for child in sorted_children:
        result = best_first_recursive(child, goal, path + [child.state], visited)
        if result:
            return result

    return None


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

solution = best_first_recursive(nodes[initial_state], goal_state, [initial_state], set())
print("Recursive Best-First Search Path:", solution if solution else "Failure")