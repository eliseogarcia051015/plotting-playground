"""
This program uses random points inside a square to estimate the value of pi (Monte Carlo Method).
Points that fall inside the inscribed circle are counted, and the ratio of
inside points to total points is used to approximate pi. 
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import TextBox

def main():
    ncircles = 0

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
        try:
            ncircles = int(text)
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
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(-1.1, 1.1)
    ax.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    circle = plt.Circle((0, 0), 1, color='white', fill=False)
    ax.add_patch(circle)
    

    print("")
    plt.show()

if __name__ == "__main__":
    main()