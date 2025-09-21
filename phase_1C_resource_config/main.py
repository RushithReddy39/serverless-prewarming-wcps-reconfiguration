# main.py

from config import WORKFLOW_DAG, MEMORY_STEP, MIN_MEMORY_MB, SLO_MS
from dag import get_critical_path
from utils import simulate_runtime, simulate_cost, get_priority
import heapq

def deep_copy_dag(dag):
    return {k: v.copy() for k, v in dag.items()}

def get_total_runtime(dag, path):
    return sum(simulate_runtime(dag[n][3]) for n in path if n != 'start' and n != 'end')

def get_total_cost(dag, path):
    return sum(simulate_cost(dag[n][3]) for n in path if n != 'start' and n != 'end')

def optimize_resource_allocation(dag, path):
    pq = []
    for n in path:
        if n in ('start', 'end'):
            continue
        old_m = dag[n][3]
        if old_m - MEMORY_STEP >= MIN_MEMORY_MB:
            new_m = old_m - MEMORY_STEP
            old_rt = simulate_runtime(old_m)
            new_rt = simulate_runtime(new_m)
            old_cost = simulate_cost(old_m)
            new_cost = simulate_cost(new_m)
            priority = get_priority(old_cost, new_cost, old_rt, new_rt)
            heapq.heappush(pq, (-priority, n))  # Max-heap

    while pq:
        _, n = heapq.heappop(pq)
        current_mem = dag[n][3]
        if current_mem - MEMORY_STEP >= MIN_MEMORY_MB:
            dag[n][3] -= MEMORY_STEP
            print(f"Reduced memory of {n} to {dag[n][3]} MB")

        total_rt = get_total_runtime(dag, path)
        if total_rt > SLO_MS:
            print(f"Runtime exceeded SLO ({total_rt} ms > {SLO_MS} ms) — stopping.")
            break

def print_results(dag, path):
    print("\nFinal Configuration:")
    for n in path:
        if n not in ('start', 'end'):
            print(f"{n}: {dag[n][3]} MB → {simulate_runtime(dag[n][3])} ms, ₹{simulate_cost(dag[n][3])}")
    print(f"\nTotal Runtime: {get_total_runtime(dag, path)} ms")
    print(f"Total Cost: ₹{get_total_cost(dag, path)}")

if __name__ == "__main__":
    dag = deep_copy_dag(WORKFLOW_DAG)
    path = get_critical_path(dag)

    print("Critical Path:", " → ".join(path))
    print(f"Initial Runtime: {get_total_runtime(dag, path)} ms")
    print(f"Initial Cost: ₹{get_total_cost(dag, path)}\n")

    optimize_resource_allocation(dag, path)
    print_results(dag, path)
