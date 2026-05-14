"""
Should be similar to point plotter but with vectors instead of points
"""

import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.widgets import Button, TextBox
import numpy as np

ani = None
def reset(event, fig, ax, boxes, plot_btn):
    global ani
    if ani and ani.event_source is not None:
        ani.event_source.stop()
    ani = None

    ax.clear()
    ax.axhline(0, color="black", linestyle="--")
    ax.axvline(0, color="black", linestyle="--")
    ax.grid(True)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    for box in boxes:
        box.eventson = False
        box.set_val("")
        box.eventson = True
        
    plot_btn.set_active(True)
    fig.canvas.draw_idle()

def start_animation(event, fig, ax, boxes, plot_btn):
    global ani
    if ani:
        return 
    try:
        x1 = int(boxes[0].text)
        y1 = int(boxes[1].text)
        x2 = int(boxes[2].text)
        y2 = int(boxes[3].text)
    except ValueError:
        print("Error: All fields must contain valid integers.")
        return
    plot_btn.set_active(False)

    max_val = max(abs(x1), abs(y1), abs(x1 + x2), abs(y1 + y2), 5)
    ax.set_xlim(-max_val - 1, max_val + 1)
    ax.set_ylim(-max_val - 1, max_val + 1)

    v1 = ax.quiver(0, 0, 0, 0, angles="xy", scale_units="xy", scale=1, color="red")
    v2 = ax.quiver(x1, y1, 0, 0, angles="xy", scale_units="xy", scale=1, color="green")
    v3 = ax.quiver(0, 0, 0, 0, angles="xy", scale_units="xy", scale=1, color="blue")

    frames_per_vector = 30
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
    ani = anim.FuncAnimation(fig, update, frames=total_frames, interval=40, blit=True, repeat=False)
    fig.canvas.draw_idle()

def main():
    fig = plt.figure(figsize=(5, 5))
    fig.canvas.manager.set_window_title("Vector Plotter")
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.78])
    ax.axhline(0, color="black", linestyle="--")
    ax.axvline(0, color="black", linestyle="--")
    ax.grid(True)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    box_positions = [
        [0.10, 0.90, 0.1, 0.05],  # x1
        [0.20, 0.90, 0.1, 0.05],  # y1
        [0.40, 0.90, 0.1, 0.05],  # x2
        [0.50, 0.90, 0.1, 0.05]   # y2
    ]
    labels = ["x1", "y1", "x2", "y2"]
    boxes = []
    for pos, label in zip(box_positions, labels):
        box_ax = fig.add_axes(pos)
        box_ax.set_title(label, y=.92, fontsize=10)
        box = TextBox(box_ax, "", initial="")
        boxes.append(box)

    plot_ax = fig.add_axes([0.70, 0.90, 0.10, 0.05])
    plot_btn = Button(plot_ax, "Plot", color="lightgreen")

    reset_ax = fig.add_axes([0.80, 0.90, 0.10, 0.05])
    reset_btn = Button(reset_ax, "Reset", color="lightcoral")

    plot_btn.on_clicked(lambda event: start_animation(event, fig, ax, boxes, plot_btn))
    reset_btn.on_clicked(lambda event: reset(event, fig, ax, boxes, plot_btn))

    plt.show()
    

if __name__ == "__main__":
    main()