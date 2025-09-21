# main.py

from config import WORKFLOW_DAG, MIN_MEMORY_MB, MEMORY_STEP, SLO_MS, LOOKAHEAD_STEPS
from dag import get_critical_path
from utils import simulate_cost, simulate_runtime, get_priority
import copy

def get_total_runtime(dag, path):
    return sum(simulate_runtime(dag[n][3]) for n in path if n not in ('start', 'end'))

def get_total_cost(dag, path):
    return sum(simulate_cost(dag[n][3]) for n in path if n not in ('start', 'end'))

def lookahead_best_config(dag, node):
    best_priority = float("-inf")
    best_config = dag[node][3]

    current_mem = dag[node][3]
    for steps in range(1, LOOKAHEAD_STEPS + 1):
        mem_try = current_mem - steps * MEMORY_STEP
        if mem_try < MIN_MEMORY_MB:
            break
        old_cost = simulate_cost(current_mem)
        new_cost = simulate_cost(mem_try)
        old_rt = simulate_runtime(current_mem)
        new_rt = simulate_runtime(mem_try)
        pr = get_priority(old_cost, new_cost, old_rt, new_rt)
        if pr > best_priority:
            best_priority = pr
            best_config = mem_try

    return best_config

def optimize_with_lookahead(dag, path):
    for node in path:
        if node in ('start', 'end'):
            continue
        original = dag[node][3]
        new_mem = lookahead_best_config(dag, node)
        if new_mem != original:
            dag[node][3] = new_mem
            print(f"Optimized {node}: {original}MB → {new_mem}MB")

        total_rt = get_total_runtime(dag, path)
        if total_rt > SLO_MS:
            print(f"SLO violated ({total_rt} ms > {SLO_MS} ms). Stopping.")
            break

def print_results(dag, path):
    print("\nFinal Configuration:")
    for node in path:
        if node not in ('start', 'end'):
            mem = dag[node][3]
            print(f"{node}: {mem}MB → {simulate_runtime(mem)} ms, ₹{simulate_cost(mem)}")
    print(f"Total Runtime: {get_total_runtime(dag, path)} ms")
    print(f"Total Cost: ₹{get_total_cost(dag, path)}")

if __name__ == "__main__":
    dag = copy.deepcopy(WORKFLOW_DAG)
    path = get_critical_path(dag)

    print("Critical Path:", " → ".join(path))
    print(f"Initial Runtime: {get_total_runtime(dag, path)} ms")
    print(f"Initial Cost: ₹{get_total_cost(dag, path)}\n")

    optimize_with_lookahead(dag, path)
    print_results(dag, path)
