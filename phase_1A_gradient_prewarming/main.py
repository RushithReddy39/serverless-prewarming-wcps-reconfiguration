# main.py

import matplotlib.pyplot as plt
from simulator import ContainerManager
from config import WINDOW_SIZE, MAX_CONTAINERS, PREWARM_COUNT, TERMINATE_COUNT

def calculate_slope(invocations):
    x = list(range(len(invocations)))
    y = invocations
    n = len(x)
    x_mean = sum(x)/n
    y_mean = sum(y)/n
    numerator = sum((x[i] - x_mean)*(y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean)**2 for i in range(n))
    return numerator / denominator if denominator != 0 else 0

def run_simulation(invocations, title):
    print(f"\n---- {title} ----")
    manager = ContainerManager(MAX_CONTAINERS)
    slopes = []
    alive_containers = []

    for i in range(len(invocations) - WINDOW_SIZE + 1):
        window = invocations[i:i+WINDOW_SIZE]
        slope = calculate_slope(window)
        slopes.append(slope)

        print(f"Window: {window}, Slope: {slope:.2f}")

        if slope > 0:
            print("Action: Pre-warming")
            manager.prewarm(PREWARM_COUNT)
        elif slope < 0:
            print("Action: Terminating")
            manager.terminate_idle(TERMINATE_COUNT)
        else:
            print("Action: No change")

        alive_containers.append(manager.get_alive_count())
        print(f"Alive containers: {manager.get_alive_count()}\n")

    # Plotting slope vs time
    plt.figure()
    plt.plot(slopes, label='Slope')
    plt.title(f"Slope Trend - {title}")
    plt.xlabel("Time Window")
    plt.ylabel("Slope Value")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"plots/{title.lower().replace(' ', '_')}_slope.png")

    # Plotting alive containers
    plt.figure()
    plt.plot(alive_containers, label='Alive Containers', color='green')
    plt.title(f"Container Count Over Time - {title}")
    plt.xlabel("Time Window")
    plt.ylabel("Alive Containers")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"plots/{title.lower().replace(' ', '_')}_containers.png")

if __name__ == "__main__":
    traces = {
        "Rising Invocation Pattern": [5, 10, 15, 20, 25, 30],
        "Falling Invocation Pattern": [30, 25, 20, 15, 10, 5]
    }

    for label, trace in traces.items():
        run_simulation(trace, label)
