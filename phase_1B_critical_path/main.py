# main.py

from config import WORKFLOW_DAG
from dag import find_critical_path

def display_critical_path(path, dag):
    print("Critical Path:")
    total_runtime = 0
    for node in path:
        runtime = dag[node][0]
        total_runtime += runtime
        print(f" → {node} (Runtime: {runtime} ms)")
    print(f"\nTotal Estimated Runtime (Critical Path): {total_runtime} ms")

if __name__ == "__main__":
    path = find_critical_path(WORKFLOW_DAG)
    display_critical_path(path, WORKFLOW_DAG)
