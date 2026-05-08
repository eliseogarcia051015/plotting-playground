"""
Should be similar to point plotter but with vectors instead of pointa
"""

import matplotlib.pyplot as plt

def main():
    fig = plt.figure(figsize=(5,5))
    fig.canvas.manager.set_window_title("Vector Plotter")
    ax = fig.add_subplot(111)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.axhline(0, color="black", linestyle="--")
    ax.axvline(0, color="black", linestyle="--")
    ax.grid(True)

    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    ax.quiver(0,0,x1,y1, angles="xy", scale_units="xy", scale=1, color="red")

    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    ax.quiver(x1,y1,x2,y2, angles="xy", scale_units="xy", scale=1, color="green")

    print(f"<{x1},{y2} + <{x2},{y2}> = <{x1+x2},{y1+y2}>")
    ax.quiver(0,0,x1+x2,y1+y2, angles="xy", scale_units="xy", scale=1, color="blue")
    plt.show()

if __name__ == "__main__":
    main()