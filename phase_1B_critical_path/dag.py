# dag.py

def get_runtime(node, dag):
    return dag[node][0]

def get_successors(node, dag):
    return dag[node][1]

def get_probabilities(node, dag):
    return dag[node][2]

def is_parallel(probabilities):
    return all(p == 1.0 for p in probabilities)

def select_branch_by_probability(successors, probabilities):
    max_index = probabilities.index(max(probabilities))
    return successors[max_index]

def select_parallel_by_runtime(successors, dag):
    return max(successors, key=lambda s: get_runtime(s, dag))

def find_critical_path(dag):
    cpath = []
    node = 'start'
    while node != 'end':
        cpath.append(node)
        successors = get_successors(node, dag)
        probs = get_probabilities(node, dag)

        if not successors:
            break
        elif len(successors) == 1:
            node = successors[0]
        elif is_parallel(probs):
            node = select_parallel_by_runtime(successors, dag)
        else:
            node = select_branch_by_probability(successors, probs)

    cpath.append('end')
    return cpath
