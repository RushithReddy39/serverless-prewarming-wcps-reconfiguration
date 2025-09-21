# config.py

# DAG node format: runtime, successors, transition_probabilities, memory (MB), cost
WORKFLOW_DAG = {
    'start': [0, ['f1'], [1.0], 0, 0],

    'f1': [100, ['f2', 'f3'], [0.8, 0.2], 768, 0.3],
    'f2': [150, ['f4'], [1.0], 768, 0.5],
    'f3': [120, ['f4'], [1.0], 768, 0.4],

    'f4': [90, ['f5', 'f6'], [1.0, 1.0], 768, 0.2],
    'f5': [200, ['end'], [1.0], 768, 0.7],
    'f6': [50, ['end'], [1.0], 768, 0.1],

    'end': [0, [], [], 0, 0]
}

# Weights for weighted priority: α * cost + β * runtime
ALPHA = 0.7
BETA = 0.3
