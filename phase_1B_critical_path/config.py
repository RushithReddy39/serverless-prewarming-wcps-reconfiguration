# config.py

# DAG node structure: node_id -> [runtime, successors (list of ids), transition probabilities]
WORKFLOW_DAG = {
    'start': [0, ['f1'], [1.0]],

    'f1': [100, ['f2', 'f3'], [0.8, 0.2]],  # branch: 80% f2, 20% f3

    'f2': [150, ['f4'], [1.0]],
    'f3': [120, ['f4'], [1.0]],

    'f4': [90, ['f5', 'f6'], [1.0, 1.0]],  # parallel execution of f5 & f6

    'f5': [200, ['end'], [1.0]],
    'f6': [50, ['end'], [1.0]],

    'end': [0, [], []]
}
