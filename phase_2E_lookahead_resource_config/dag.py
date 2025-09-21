# dag.py

def get_critical_path(dag):
    path = []
    node = 'start'
    while node != 'end':
        path.append(node)
        succs = dag[node][1]
        if len(succs) == 1:
            node = succs[0]
        else:
            node = max(succs, key=lambda s: dag[s][0])  # default to runtime
    path.append('end')
    return path
