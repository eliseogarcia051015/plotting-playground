#Simple vector 
import matplotlib.pyplot as plt

def main():
    fig = plt.figure(figsize=(5,5))
    fig.canvas.manager.set_window_title("Vectorfield")
    ax = fig.add_subplot(111)
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)

    plt.show()

if __name__ == "__main__":
    main()