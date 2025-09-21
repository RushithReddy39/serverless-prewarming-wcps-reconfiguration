# config.py

# Node format: runtime, successors, transition_probabilities, memory (MB), cost per invocation
WORKFLOW_DAG = {
    'start': [0, ['f1'], [1.0], 0, 0],

    'f1': [100, ['f2', 'f3'], [0.8, 0.2], 768, 0.30],
    'f2': [150, ['f4'], [1.0], 768, 0.50],
    'f3': [120, ['f4'], [1.0], 768, 0.40],

    'f4': [90, ['f5', 'f6'], [1.0, 1.0], 768, 0.20],
    'f5': [200, ['end'], [1.0], 768, 0.70],
    'f6': [50, ['end'], [1.0], 768, 0.10],

    'end': [0, [], [], 0, 0]
}

MIN_MEMORY_MB = 128  # Minimum allowed memory
MEMORY_STEP = 128     # Reduce memory in 128MB steps
SLO_MS = 600          # Max allowed runtime (Service Level Objective)
