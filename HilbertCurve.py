"""
This program visualizes the Hilbert curve, a type of space-filling curve
that maps a one-dimensional line into a two-dimensional area. The curve is
generated recursively, with each iteration increasing its complexity and
level of detail. Despite being a continuous line, the Hilbert curve passes
through every point in a grid without crossing itself.
"""
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

def window(order: int):
    fig,ax = plt.subplots(figsize=(6,6))
    fig.canvas.manager.set_window_title("Hilbert Curve Visualizer")

    N = int(math.pow(2,order))
    ax.set_xlim(-0.5,N-0.5)
    ax.set_ylim(-0.5,N-0.5)

    x_coords, y_coords = plotPoints(order)
    line, =ax.plot([],[], color="blue", linewidth=2) #connecting line
    point, = ax.plot([], [], "ro", markersize=6) #corner points

    def update(frame):
        line.set_data(
            x_coords[:frame + 1],
            y_coords[:frame + 1]
        )

        point.set_data(
            [x_coords[frame]],
            [y_coords[frame]]
        )

        return line, point

    duration = 5000  # milliseconds
    interval = duration / len(x_coords)
    animation = FuncAnimation(
        fig,
        update,
        frames=len(x_coords),
        interval=interval,
        blit=True,
        repeat=False
    )

    plt.show()

def plotPoints(order: int):
    grid_size = int(math.pow(2, order))
    total_points = grid_size * grid_size
    
    x_coords = []
    y_coords = []

    for i in range(total_points):
        x, y = hilbert(i, order)
        x_coords.append(x)
        y_coords.append(y)
    return x_coords, y_coords

#  -----------
#  |_Q1_|_Q2_|
#  |_Q0_|_Q3_|
#  -----------
def hilbert(i, order):
    points = [ #base case
        (0,0),
        (0,1),
        (1,1),
        (1,0)
    ]
    if (order == 1):
        return points[i]
    quadrant_size = int(math.pow(4, order-1))
    quadrant = i // quadrant_size
    offset = i % quadrant_size

    x,y = hilbert(offset, order-1)
    half = 2 ** (order - 1)

    if quadrant == 0:
        return y, x
    elif quadrant == 1:
        return x, y + half
    elif quadrant == 2:
        return x + half, y + half
    else:  # quadrant == 3
        return (2 * half - 1 - y), (half - 1 - x)

def main():
    while(True):
        try:
            order = int(input("Enter order: "))
            if order > 0:
                break
            print("Try a positive number")
        except ValueError:
            print(f"Not a number. Try again")
    print(f"order = {order}")

    window(order)
    print("Everything successful")

if __name__ == "__main__":
    main()