import json
import matplotlib.pyplot as plt

def load_json(file):
    with open(file) as f:
        return json.load(f)

def compare_configs(file1, file2, label1, label2):
    d1 = load_json(file1)
    d2 = load_json(file2)

    print(f"\n--- Resource Configuration Comparison ---")
    print(f"{label1} Runtime: {d1['runtime']} ms | Cost: ₹{d1['cost']}")
    print(f"{label2} Runtime: {d2['runtime']} ms | Cost: ₹{d2['cost']}")

    funcs = list(d1["memory_alloc"].keys())
    mem1 = [d1["memory_alloc"][f] for f in funcs]
    mem2 = [d2["memory_alloc"][f] for f in funcs]

    # Memory comparison plot
    x = range(len(funcs))
    plt.figure()
    plt.bar([i - 0.2 for i in x], mem1, width=0.4, label=label1)
    plt.bar([i + 0.2 for i in x], mem2, width=0.4, label=label2)
    plt.xticks(x, funcs)
    plt.ylabel("Memory (MB)")
    plt.title("Memory Allocation Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("resourceconfig_memory.png")

    # Cost/Runtime bar plot
    plt.figure()
    metrics = ["Runtime (ms)", "Total Cost (₹)"]
    vals1 = [d1["runtime"], d1["cost"]]
    vals2 = [d2["runtime"], d2["cost"]]
    plt.bar([0, 1], vals1, width=0.4, label=label1)
    plt.bar([0.4, 1.4], vals2, width=0.4, label=label2)
    plt.xticks([0.2, 1.2], metrics)
    plt.title("Runtime & Cost Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("resourceconfig_summary.png")

    print("✅ Plots saved: resourceconfig_memory.png & resourceconfig_summary.png")

if __name__ == "__main__":
    compare_configs("original_config.json", "lookahead_config.json", "Greedy", "Lookahead")
