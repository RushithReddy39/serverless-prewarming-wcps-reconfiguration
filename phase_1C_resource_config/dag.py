# dag.py

def get_critical_path(dag):
    def get_runtime(n): return dag[n][0]
    def get_succ(n): return dag[n][1]
    def get_probs(n): return dag[n][2]
    def is_parallel(p): return all(x == 1.0 for x in p)
    def pick_branch(succs, probs): return succs[probs.index(max(probs))]
    def pick_parallel(succs): return max(succs, key=lambda s: dag[s][0])

    path, node = [], 'start'
    while node != 'end':
        path.append(node)
        succs = get_succ(node)
        probs = get_probs(node)
        if not succs:
            break
        elif len(succs) == 1:
            node = succs[0]
        elif is_parallel(probs):
            node = pick_parallel(succs)
        else:
            node = pick_branch(succs, probs)
    path.append('end')
    return path

