"""
This program uses random points inside a square to estimate the value of pi (Monte Carlo Method).
Points that fall inside the inscribed circle are counted, and the ratio of
inside points to total points is used to approximate pi. 
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import TextBox
import numpy as np

def main():
    ncircles = None

    fig0 = plt.figure(figsize=(6, 3))
    fig0.canvas.manager.set_window_title("User input")

    fig0.text(0.025, 0.9, "Choose how many circles you would like to use for the visualization", fontsize=12, color='Black')
    ax = fig0.add_axes([0, 0, 1, 1])
    #ax.axvline(0.5, color="black", linestyle="--", linewidth=1)#center the porimpt box. maybe lower it as well
    ax_prompt = plt.axes([0.35, 0.5, 0.30, 0.2])
    prompt_box = TextBox(ax_prompt, "")

    ax.set_xticks([])
    ax.set_yticks([])

    def submit(text):
        nonlocal ncircles
        try:    
            value = int(text)
            if value <= 0:
                raise ValueError
            ncircles = value
            plt.close(fig0)
        except ValueError:
            print("Not valid input")
            prompt_box.set_val("")
            return
    prompt_box.on_submit(submit)
    plt.show()

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(7,7))
    fig.canvas.manager.set_window_title("Monte Carlo Method")
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_ylim(-1, 1)
    ax.set_xlim(-1, 1)
    ax.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    pi_text = fig.text(
    0.5, 0.93,
        r"$\pi \quad \approx \quad 4 * \frac{\mathrm{inside}}{\mathrm{inside}+\mathrm{outside}}$",
        ha="center", fontsize = 20\
    )
    fig.text(0.5, 0.04, f"Sample: {ncircles}", ha="center")
    print(ncircles)

    circle = plt.Circle((0, 0), 1, color='white', fill=False)
    ax.add_patch(circle)

    inside = 0
    outside = 0
    plt.pause(2)
    for i  in range(ncircles):
        if not plt.fignum_exists(fig.number):
            break

        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            color = "lime"
            inside += 1
        else:
            color = "red"
            outside += 1
        ax.plot(x,y, marker="o", color=color)
        supposed_pi = 4 * inside / (inside + outside)
        pi_text.set_text(
            rf"$\pi \quad \approx \quad 4 \cdot \frac{{{inside}}}{{{inside}+{outside}}} \approx {supposed_pi:.4f}$"
        )
        plt.pause(0.00001)
        



    print("")
    plt.show()

if __name__ == "__main__":
    main()