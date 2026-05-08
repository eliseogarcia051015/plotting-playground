"""
Should be similar to point plotter but with vectors instead of pointa
"""

import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

def main():
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    print(f"<{x1},{y1}> + <{x2},{y2}> = <{x1+x2},{y1+y2}>")

    fig = plt.figure(figsize=(5,5))
    fig.canvas.manager.set_window_title("Vector Plotter")
    ax = fig.add_subplot(111)

    ax.axhline(0, color="black", linestyle="--")
    ax.axvline(0, color="black", linestyle="--")
    ax.grid(True)

    max_val = max(abs(x1), abs(y1), abs(x1 + x2), abs(y1 + y2), 5)
    ax.set_xlim(-max_val - 1, max_val + 1)
    ax.set_ylim(-max_val - 1, max_val + 1)

    v1 = ax.quiver(0,0,0,0, angles="xy", scale_units="xy", scale=1, color="red")
    v2 = ax.quiver(x1,y1,0,0, angles="xy", scale_units="xy", scale=1, color="green")
    v3 = ax.quiver(0,0,0,0, angles="xy", scale_units="xy", scale=1, color="blue")

    frames_per_vector = 20
    steps_v1_x = np.linspace(0, x1, frames_per_vector)
    steps_v1_y = np.linspace(0, y1, frames_per_vector)

    steps_v2_x = np.linspace(0, x2, frames_per_vector)
    steps_v2_y = np.linspace(0, y2, frames_per_vector)

    steps_v3_x = np.linspace(0, x1 + x2, frames_per_vector)
    steps_v3_y = np.linspace(0, y1 + y2, frames_per_vector)

    def update(frame):
        if frame < frames_per_vector:
            v1.set_UVC(steps_v1_x[frame], steps_v1_y[frame])

        elif frame < 2 * frames_per_vector:
            idx = frame - frames_per_vector
            v2.set_UVC(steps_v2_x[idx], steps_v2_y[idx])

        else:
            idx = frame - (2 * frames_per_vector)
            v3.set_UVC(steps_v3_x[idx], steps_v3_y[idx])

        return v1, v2, v3
    total_frames = frames_per_vector * 3
    ani = anim.FuncAnimation(fig, update, frames=total_frames, interval=40,blit=True, repeat=False)
    #ax.scatter(x1+x2,y1+y2, color="blue")

    plt.show()

if __name__ == "__main__":
    main()