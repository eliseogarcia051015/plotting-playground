# Beverton-Holt Model (Stochastic Growth Rate Simulation)

#This comes from my math modeling class (lab 3). I think I want to 
#implement more of those assignments on here becasue they look cool
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.style.use("dark_background")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
    fig.canvas.manager.set_window_title(
        "Stochastic Beverton-Holt Model"
    )

    # Model parameters
    K = 1000  # carrying capacity
    x0 = 200  # initial population
    N = 250  # number of simulations
    t_max = 100  # time horizon (0..100)

    r_min, r_max = 0.2, 3.0  # uniform distribution bounds for r

    x = np.zeros((N, t_max + 1))
    x[:, 0] = x0

    # Run simulations
    for i in range(N):
        for t in range(t_max):
            r = np.random.uniform(r_min, r_max)

            x[i, t+1] = (r * x[i, t]) / (1 + ((r - 1) / K) * x[i, t])

    time = np.arange(t_max + 1)
    x_mean = np.mean(x, axis=0)
    x_std = np.std(x, axis=0)

    # Subplot 1: Trajectories and Mean
    for i in range(N):
        ax1.plot(
            time, x[i], color="#ff4d4d", alpha=0.15, linewidth=0.8
        )

    ax1.plot(
        time,
        x_mean,
        color="white",
        linewidth=2.5,
        label="Mean Trajectory",
    )
    ax1.set_title(
        "Beverton-Holt Population Trajectories (N=250)", fontsize=12
    )
    ax1.set_ylabel("Population Size")
    ax1.set_ylim(0, K * 1.1)
    ax1.grid(True, linestyle="--", alpha=0.3)
    ax1.legend(loc="lower right")

    # Subplot 2: Standard Deviation
    ax2.plot(
        time,
        x_std,
        color="#00bfff",
        linewidth=2,
        label="Std Deviation",
    )
    ax2.set_title("Standard Deviation Over Time", fontsize=12)
    ax2.set_xlabel("Time Step (t)")
    ax2.set_ylabel("Standard Deviation")
    ax2.grid(True, linestyle="--", alpha=0.3)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()