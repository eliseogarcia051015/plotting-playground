""""
Similar to "function_transformer.py" but instead of being in cartesian coordinates,
this program will handle functions in the polar plane (r = f(\theta)). I think
I want to keep the idea of sliders, but look into how that implementation will look
like given things like petals

Functions:
    1. Rose Curve       r = A sin(Bθ)
    2. Spiral           r = Aθ
    3. Cardioid         r = A(1 + cos(θ))
    4. Cosine Rose      r = A[cos(Bθ)]
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import TextBox
import math

def window():
    lower_bound,upper_bound =-10,10
    fig, ax = plt.subplots(figsize=(7,4.5))
    plt.subplots_adjust(bottom=0.2)
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_ylim(lower_bound, upper_bound)
    ax.set_xlim(lower_bound, upper_bound)
    plt.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    axbox = plt.axes([0.725, 0.05, 0.175, 0.075])
    prompt_box = TextBox(axbox, "Choose a graph: Rose Curve(1), Spiral(2), Cardioid(3), Cosine Rose(4): ")
    options = [1, 2, 3, 4]
    def choose(text):
        try:
            n = int(text)
            if n not in options:
                raise ValueError
        except ValueError:
            print("Enter a valid number (1-4)")
            prompt_box.set_val("")
            return
        prompt_box.set_active(False)
        axbox.set_visible(False)

        if n == 1:
            rose(fig, ax)
        elif n == 2:
            spiral(fig, ax)
        elif n == 3:
            cardioid(fig, ax)
        elif n == 4:
            cosine_rose(fig, ax)

        fig.canvas.draw_idle()
    prompt_box.on_submit(choose)
    plt.show()

#1
def rose(fig,ax):
    print("Nothing so far (1)")

#2
def spiral(fig,ax):
    print("Nothing so far (2)")

#3
def cardioid(fig,ax):
    print("Nothing so far (3)")

#4
def cosine_rose(fig,ax):
    print("Nothing so far (4)")

def main():
    window()

if __name__ == "__main__":
    main()