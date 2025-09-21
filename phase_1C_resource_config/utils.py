# utils.py

def get_priority(old_cost, new_cost, old_rt, new_rt):
    delta_cost = old_cost - new_cost
    delta_rt = new_rt - old_rt
    return delta_cost / (delta_rt + 1)  # +1 to avoid division by zero

def simulate_runtime(memory_mb):
    # Runtime increases as memory decreases (inverse linear)
    base = 768
    return int(300 * (base / memory_mb))

def simulate_cost(memory_mb):
    # Cost per invocation decreases with memory
    return round(0.00025 * (memory_mb / 128), 5)
