# main.py

from config import WORKFLOW_DAG
from weighted_dag import find_critical_path_weighted

def print_path(dag, path):
    total_runtime = 0
    total_cost = 0
    print("Weighted Critical Path:")
    for node in path:
        runtime = dag[node][0]
        cost = dag[node][4]
        total_runtime += runtime
        total_cost += cost
        print(f" → {node} (Runtime: {runtime} ms, Cost: ₹{cost})")
    print(f"\nTotal Runtime: {total_runtime} ms")
    print(f"Total Cost: ₹{round(total_cost, 3)}")

if __name__ == "__main__":
    path = find_critical_path_weighted(WORKFLOW_DAG)
    print_path(WORKFLOW_DAG, path)
