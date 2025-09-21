# main.py

from predictor import MLForecaster
from simulator import ContainerManager
from config import WINDOW_SIZE, MAX_CONTAINERS, PREWARM_THRESHOLD, TERMINATE_THRESHOLD
import matplotlib.pyplot as plt

def run_simulation(invocations, title):
    forecaster = MLForecaster(WINDOW_SIZE)
    manager = ContainerManager(MAX_CONTAINERS)

    predictions = []
    alive_containers = []

    print(f"\n--- {title} ---")

    for i in range(WINDOW_SIZE, len(invocations)):
        window = invocations[i - WINDOW_SIZE:i]
        actual = invocations[i]
        predicted = forecaster.predict_next(window)
        predictions.append(predicted)

        print(f"Window: {window} → Predicted: {predicted}, Actual: {actual}")

        diff = predicted - actual
        if diff >= PREWARM_THRESHOLD:
            print("Action: Pre-warming")
            manager.prewarm(2)
        elif diff <= TERMINATE_THRESHOLD:
            print("Action: Termination")
            manager.terminate_idle(2)
        else:
            print("Action: No change")

        alive = manager.get_alive_count()
        alive_containers.append(alive)
        print(f"Alive containers: {alive}\n")

    # Plotting
    plt.figure()
    plt.plot(range(WINDOW_SIZE, len(invocations)), predictions, label="Predicted")
    plt.plot(range(WINDOW_SIZE, len(invocations)), invocations[WINDOW_SIZE:], label="Actual")
    plt.title(f"ML Prediction vs Actual - {title}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{title.lower().replace(' ', '_')}_prediction.png")

    plt.figure()
    plt.plot(alive_containers, label="Alive Containers", color="green")
    plt.title(f"Alive Containers Over Time - {title}")
    plt.xlabel("Time Window")
    plt.ylabel("Containers")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"{title.lower().replace(' ', '_')}_containers.png")

if __name__ == "__main__":
    traces = {
        "Rising Pattern": [5, 10, 15, 20, 25, 30, 35],
        "Falling Pattern": [35, 30, 25, 20, 15, 10, 5],
        "Mixed Pattern":   [10, 20, 10, 25, 15, 30, 10]
    }

    for label, inv in traces.items():
        run_simulation(inv, label)
