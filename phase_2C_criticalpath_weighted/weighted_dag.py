# weighted_dag.py

from config import ALPHA, BETA

def get_runtime(node, dag):
    return dag[node][0]

def get_successors(node, dag):
    return dag[node][1]

def get_probabilities(node, dag):
    return dag[node][2]

def get_cost(node, dag):
    return dag[node][4]

def is_parallel(probs):
    return all(p == 1.0 for p in probs)

def weighted_score(node, dag):
    cost = get_cost(node, dag)
    runtime = get_runtime(node, dag)
    return (ALPHA * cost) + (BETA * runtime / 1000)  # normalized

def find_critical_path_weighted(dag):
    path = []
    node = 'start'
    while node != 'end':
        path.append(node)
        succs = get_successors(node, dag)
        probs = get_probabilities(node, dag)

        if not succs:
            break
        elif len(succs) == 1:
            node = succs[0]
        elif is_parallel(probs):
            node = max(succs, key=lambda s: weighted_score(s, dag))
        else:
            node = max(succs, key=lambda s: weighted_score(s, dag))
    path.append('end')
    return path
