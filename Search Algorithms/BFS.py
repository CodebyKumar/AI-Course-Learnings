from collections import deque

# Create a node with given state, parent, action, and path cost
def create_node(state, parent=None, action=None, path_cost=0):
    return {
        'state': state,
        'parent': parent,
        'action': action,
        'path_cost': path_cost,
        'children': []
    }

# Create a problem instance with initial state, goal state, and nodes dictionary
def create_problem(initial_state, goal_state, nodes_dict):
    return {
        'initial_state': initial_state,
        'goal_state': goal_state,
        'nodes_dict': nodes_dict
    }

# Test if the given state is the goal state
def goal_test(problem, state):
    return state == problem['goal_state']

# Get possible actions (children) for a given state
def get_actions(problem, state):
    if state in problem['nodes_dict']:
        return [child['state'] for child in problem['nodes_dict'][state]['children']]
    return []

# Create a child node from a parent node and an action
def child_node(parent, action):
    return create_node(
        state=action, 
        parent=parent, 
        action=action, 
        path_cost=parent['path_cost'] + 1
    )

# Generate the solution path from the goal node to the initial node
def solution(node):
    path = []
    current = node
    while current:
        path.append(current['state'])
        current = current['parent']
    path.reverse()
    
    print(f"Goal Found!")
    print(f"Path from source to destination:")
    for i, state in enumerate(path):
        if i < len(path)-1:
            print(f"{state}->", end="")
        else:
            print(f"{state}")
    return path

# Perform breadth-first search on the problem
def breadth_first_search(problem):
    node = create_node(state=problem['initial_state'])
    
    if goal_test(problem, node['state']):
        return solution(node)
    
    frontier = deque([node])
    frontier_states = {node['state']}
    explored = set()
    
    step = 1
    while frontier:
        print(f"\nStep {step}:")
        print(f"Frontier: {[n['state'] for n in frontier]}")
        print(f"Explored: {explored}")
        
        node = frontier.popleft()
        frontier_states.remove(node['state'])
        print(f"Goal Test on: {node['state']}")
        
        explored.add(node['state'])
        
        for action in get_actions(problem, node['state']):
            child = child_node(node, action)
            
            if child['state'] not in explored and child['state'] not in frontier_states:
                if goal_test(problem, child['state']):
                    return solution(child)
                
                frontier.append(child)
                frontier_states.add(child['state'])
        
        step += 1
    
    return None

# Create a tree structure from user input
def create_tree():
    nodes_dict = {}
    
    num_nodes = int(input("Enter the number of nodes: "))
    print("\nEnter the names of the nodes:")
    
    for i in range(num_nodes):
        name = input(f"Node {i+1}: ").strip()
        nodes_dict[name] = create_node(name)
    
    print("\nDefine the tree structure:")
    print("For each node, enter the children (comma-separated, or press Enter for none)")
    
    for name in list(nodes_dict.keys()):
        children_input = input(f"Children of {name}: ")
        if children_input.strip():
            for child in [c.strip() for c in children_input.split(',')]:
                if child in nodes_dict:
                    if child not in nodes_dict[name]['children']:
                        nodes_dict[name]['children'].append(nodes_dict[child])
                else:
                    print(f"Warning: Node '{child}' doesn't exist.")
    
    return nodes_dict

# Search for a path from start state to goal state
def search(nodes_dict, start_state, goal_state):
    if start_state not in nodes_dict or goal_state not in nodes_dict:
        print(f"Start or goal state not found in the tree.")
        return None
    
    print(f"\nSearching for path from '{start_state}' to '{goal_state}'...")
    problem = create_problem(start_state, goal_state, nodes_dict)
    
    result = breadth_first_search(problem)
    
    if not result:
        print(f"No Path Found from '{start_state}' to '{goal_state}'")
    
    return result

# Print the tree structure
def print_tree(nodes_dict):
    print("\nTree Structure:")
    for state, node in nodes_dict.items():
        children = [child['state'] for child in node['children']]
        print(f"{state} -> {', '.join(children) if children else 'No children'}")

# Main function to create tree, show structure, and perform search
def main():
    nodes_dict = create_tree()
    print_tree(nodes_dict)
    
    start = input("\nEnter the start node name: ").strip()
    goal = input("Enter the goal node name: ").strip()
    
    search(nodes_dict, start, goal)

if __name__ == "__main__":
    main()
