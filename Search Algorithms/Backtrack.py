import operator

# Map string operator to actual Python functions
ops = {
    '!=': operator.ne,
    '==': operator.eq,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge
}

def backtracking_search(csp):
    return backtrack({}, csp)

def backtrack(assignment, csp):
    if is_complete(assignment, csp):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    for value in csp['domains']:
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            inferences = inference(csp, var, value)
            if inferences is not None:
                assignment.update(inferences)
                result = backtrack(assignment, csp)
                if result is not None:
                    return result
                for key in inferences:
                    del assignment[key]
            del assignment[var]
    return None

# Helper functions
def is_complete(assignment, csp):
    return len(assignment) == len(csp['variables'])

def select_unassigned_variable(assignment, csp):
    for var in csp['variables']:
        if var not in assignment:
            return var

def is_consistent(var, value, assignment, csp):
    for neighbor in csp['constraints'].get(var, []):
        if neighbor in assignment:
            constraint = csp['constraints'][(var, neighbor)]
            if not constraint(value, assignment[neighbor]):
                return False
    return True

def inference(csp, var, value):
    return {}

# Input section
def get_input():
    variables = input("Enter variables (comma-separated): ").split(",")
    variables = [v.strip() for v in variables]

    domain = input("Enter fixed domain values (comma-separated): ").split(",")
    domain = [val.strip() for val in domain]

    constraints = {}
    print("\nEnter constraints in the form: A != B or X == Y")
    while True:
        expr = input("Enter constraint or 'done' to finish: ")
        if expr.lower() == 'done':
            break
        parts = expr.strip().split()
        if len(parts) != 3:
            print("Invalid format. Use: A != B")
            continue
        var1, op_str, var2 = parts
        if op_str not in ops:
            print("Unsupported operator. Use one of:", list(ops.keys()))
            continue
        func = ops[op_str]
        constraints[(var1, var2)] = func
        if var1 not in constraints:
            constraints[var1] = []
        constraints[var1].append(var2)

    return {
        'variables': variables,
        'domains': domain,
        'constraints': constraints
    }

# Run the program
if __name__ == "__main__":
    csp = get_input()
    result = backtracking_search(csp)
    print("\nSolution:", result)