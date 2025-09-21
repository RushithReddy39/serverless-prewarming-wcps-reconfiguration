# config.py

# [runtime, successors, probs, memory (MB), cost]
WORKFLOW_DAG = {
    'start': [0, ['f1'], [1.0], 0, 0],

    'f1': [100, ['f2'], [1.0], 768, 0.3],
    'f2': [150, ['f4'], [1.0], 768, 0.5],

    'f4': [90, ['f5', 'f6'], [1.0, 1.0], 768, 0.2],
    'f5': [200, ['end'], [1.0], 768, 0.7],
    'f6': [50, ['end'], [1.0], 768, 0.1],

    'end': [0, [], [], 0, 0]
}

MIN_MEMORY_MB = 128
MEMORY_STEP = 128
SLO_MS = 600
LOOKAHEAD_STEPS = 2  # Try up to 2 memory reductions per function
