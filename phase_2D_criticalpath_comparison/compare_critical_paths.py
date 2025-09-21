import json
import matplotlib.pyplot as plt

def load_json(path):
    with open(path) as f:
        return json.load(f)

def compare_and_plot(file1, file2, label1, label2):
    d1 = load_json(file1)
    d2 = load_json(file2)

    print(f"\n--- Critical Path Comparison ---")
    print(f"{label1} Path: {' → '.join(d1['path'])}")
    print(f"{label2} Path: {' → '.join(d2['path'])}")

    print(f"\nRuntime: {label1} = {d1['runtime']} ms | {label2} = {d2['runtime']} ms")
    print(f"Cost   : {label1} = ₹{d1['cost']}     | {label2} = ₹{d2['cost']}")

    # Bar plot
    x = range(2)
    plt.figure()
    plt.bar(x, [d1["runtime"], d2["runtime"]], width=0.4, label="Runtime")
    plt.xticks(x, [label1, label2])
    plt.ylabel("Runtime (ms)")
    plt.title("Critical Path Runtime Comparison")
    plt.grid(True)
    plt.savefig("critical_path_runtime.png")

    plt.figure()
    plt.bar(x, [d1["cost"], d2["cost"]], width=0.4, color='orange', label="Cost")
    plt.xticks(x, [label1, label2])
    plt.ylabel("Cost (₹)")
    plt.title("Critical Path Cost Comparison")
    plt.grid(True)
    plt.savefig("critical_path_cost.png")

    print("✅ Plots saved: critical_path_runtime.png & critical_path_cost.png")

if __name__ == "__main__":
    compare_and_plot("original_path.json", "weighted_path.json", "Original", "Weighted")
