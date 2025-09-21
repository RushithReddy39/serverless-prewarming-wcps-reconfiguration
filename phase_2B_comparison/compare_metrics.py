import json
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

def load_results(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def cold_start_rate(predicted, actual):
    cold_hits = sum(max(a - p, 0) for a, p in zip(actual, predicted))
    total = sum(actual)
    return round(cold_hits / total * 100, 2)

def utilization_rate(alive_containers):
    used = sum(1 for a in alive_containers if a > 0)
    return round((used / len(alive_containers)) * 100, 2)

def compare_metrics(file1, file2, label1, label2):
    r1 = load_results(file1)
    r2 = load_results(file2)

    metrics = {}

    # Cold start
    csr1 = cold_start_rate(r1["predicted"], r1["actual"])
    csr2 = cold_start_rate(r2["predicted"], r2["actual"])
    metrics["Cold Start Rate (%)"] = [csr1, csr2]

    # MAE
    mae1 = mean_absolute_error(r1["actual"], r1["predicted"])
    mae2 = mean_absolute_error(r2["actual"], r2["predicted"])
    metrics["Prediction Error (MAE)"] = [round(mae1, 2), round(mae2, 2)]

    # Utilization
    util1 = utilization_rate(r1["alive_containers"])
    util2 = utilization_rate(r2["alive_containers"])
    metrics["Container Utilization (%)"] = [util1, util2]

    print("\n=== Metric Comparison ===")
    for key in metrics:
        print(f"{key}: {label1} = {metrics[key][0]}, {label2} = {metrics[key][1]}")

    # Bar Plot
    fig, ax = plt.subplots()
    metric_names = list(metrics.keys())
    values1 = [v[0] for v in metrics.values()]
    values2 = [v[1] for v in metrics.values()]

    x = range(len(metric_names))
    ax.bar([i - 0.2 for i in x], values1, width=0.4, label=label1)
    ax.bar([i + 0.2 for i in x], values2, width=0.4, label=label2)
    ax.set_xticks(x)
    ax.set_xticklabels(metric_names, rotation=15)
    ax.set_ylabel("Metric Values")
    ax.set_title("Slope-Based vs ML-Based Optimization")
    ax.legend()
    plt.tight_layout()
    plt.savefig("comparison_plot.png")
    print("✅ Graph saved: comparison_plot.png")

if __name__ == "__main__":
    compare_metrics("results_slope.json", "results_ml.json", "Slope", "ML")
