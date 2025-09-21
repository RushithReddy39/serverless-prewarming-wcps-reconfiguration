import json
import matplotlib.pyplot as plt

with open("data.json", "r") as f:
    data = json.load(f)

nodes = list(data["before"].keys())

def extract(field):
    return [data["before"][n][field] for n in nodes], [data["after"][n][field] for n in nodes]

mem_before, mem_after = extract("memory")
rt_before, rt_after = extract("runtime")
cost_before, cost_after = extract("cost")

x = range(len(nodes))

plt.figure()
plt.bar(x, mem_before, width=0.4, label='Before', align='center')
plt.bar([i + 0.4 for i in x], mem_after, width=0.4, label='After', align='center')
plt.xticks([i + 0.2 for i in x], nodes)
plt.title("Memory Allocation per Function")
plt.ylabel("Memory (MB)")
plt.legend()
plt.grid(True)
plt.savefig("memory_comparison.png")

plt.figure()
plt.bar(x, rt_before, width=0.4, label='Before', align='center')
plt.bar([i + 0.4 for i in x], rt_after, width=0.4, label='After', align='center')
plt.xticks([i + 0.2 for i in x], nodes)
plt.title("Runtime per Function")
plt.ylabel("Runtime (ms)")
plt.legend()
plt.grid(True)
plt.savefig("runtime_comparison.png")

plt.figure()
plt.bar(x, cost_before, width=0.4, label='Before', align='center')
plt.bar([i + 0.4 for i in x], cost_after, width=0.4, label='After', align='center')
plt.xticks([i + 0.2 for i in x], nodes)
plt.title("Cost per Function")
plt.ylabel("Cost (₹)")
plt.legend()
plt.grid(True)
plt.savefig("cost_comparison.png")

print("✅ Plots saved: memory_comparison.png, runtime_comparison.png, cost_comparison.png")
