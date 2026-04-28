# Try to simulate a ball being dropping 
import matplotlib.pyplot as plt

def main():
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(4,5))
    fig.canvas.manager.set_window_title("Gravity Simulator")
    ax = fig.add_subplot(111)
    ax.set_xlim(0,1), ax.set_xticks([])
    ax.set_ylim(0,1.2), ax.set_yticks([])
    plt.pause(1)

    ax.scatter(0.5, 1, color="white", linewidth=10)
    fig.canvas.draw()

    plt.show()

if __name__ == "__main__":
    main()