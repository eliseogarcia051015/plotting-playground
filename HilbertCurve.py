"""
This program visualizes the Hilbert curve, a recursive
space-filling curve that visits every point in a grid
without crossing itself.
"""

import matplotlib.pyplot as plt
import math

# Current turtle position
x = 0
y = 0

# Direction vectors
dx = 1
dy = 0

# Lists of points for plotting
x_points = [0]
y_points = [0]


def forward(step):
    global x, y

    x += dx * step
    y += dy * step

    x_points.append(x)
    y_points.append(y)


def left():
    global dx, dy
    dx, dy = -dy, dx


def right():
    global dx, dy
    dx, dy = dy, -dx


def hilbert(level, angle, step):
    """
    Recursive Hilbert curve algorithm.
    """

    if level == 0:
        return

    if angle == 90:
        left()
    else:
        right()

    hilbert(level - 1, -angle, step)

    forward(step)

    if angle == 90:
        right()
    else:
        left()

    hilbert(level - 1, angle, step)

    forward(step)

    hilbert(level - 1, angle, step)

    if angle == 90:
        right()
    else:
        left()

    forward(step)

    hilbert(level - 1, -angle, step)

    if angle == 90:
        left()
    else:
        right()


def window(order):
    global x, y, dx, dy
    global x_points, y_points

    # Reset globals
    x = 0
    y = 0
    dx = 1
    dy = 0

    x_points = [0]
    y_points = [0]

    grid_size = 2 ** order
    step = 1

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.canvas.manager.set_window_title("Hilbert Curve Visualizer")

    hilbert(order, 90, step)

    ax.plot(x_points, y_points)

    ax.set_xlim(-1, grid_size)
    ax.set_ylim(-1, grid_size)

    ax.set_aspect('equal')

    plt.show()


def main():
    while True:
        try:
            order = int(input("Enter order: "))

            if order > 0:
                break

            print("Try a positive number")

        except ValueError:
            print("Not a number. Try again")

    window(order)


if __name__ == "__main__":
    main()