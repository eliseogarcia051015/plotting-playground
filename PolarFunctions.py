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
from matplotlib.widgets import Slider
from matplotlib.widgets import Button
import numpy as np

def window():
    lower_bound,upper_bound =2*-np.pi,2*np.pi

    fig, ax = plt.subplots(figsize=(7,7))
    fig.canvas.manager.set_window_title("Polar Function Visualizer")
    plt.subplots_adjust(bottom=0.2)

    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_ylim(lower_bound, upper_bound)
    ax.set_xlim(lower_bound, upper_bound)
    plt.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    choose(fig, ax)

    zoom_in_ax = plt.axes([0.05, 0.92, 0.1, 0.05]) 
    zoom_in_button = Button(zoom_in_ax, "+") 
    #implement method

    zoom_out_ax = plt.axes([0.15, 0.92, 0.1, 0.05]) 
    zoom_out_button = Button(zoom_out_ax, "-") 
    #implement method

    reset_ax = plt.axes([0.85, 0.92, 0.1, 0.05]) 
    reset_button = Button(reset_ax, "Reset") 
    reset_button.on_clicked(lambda event: reset(event, fig, ax))

    plt.show()

def choose(fig, ax):
    axbox = plt.axes([0.725, 0.05, 0.175, 0.075])
    prompt_box = TextBox(axbox, "Choose a graph: Spiral(1), Rose Curve(2), Cardioid(3), Cosine Rose(4): ")
    options = [1, 2, 3, 4]
    def cont(text):
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
            spiral(fig, ax)
        elif n == 2:
            rose(fig, ax)
        elif n == 3:
            cardioid(fig, ax)
        elif n == 4:
            cosine_rose(fig, ax)

        fig.canvas.draw_idle()
    prompt_box.on_submit(cont)

def reset(event, fig, ax):
    ax.clear()
    for extra_ax in fig.axes[1:]:
        extra_ax.remove()
    choose(fig, ax)
    fig.canvas.draw_idle()

def PolaRToRect(r, theta):# x = rcos(theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

#1
'''
GOTTA FIX BOUNDS. RIGHT NOW SPIRAL ONLY  GOES UP TO WHAT BOUNDS ARE ALREADY SET IN WINDOW
'''
def spiral(fig,ax):
    ax.set_title("Spiral: r = a + bθ", pad=20)
    A = 0
    B = 1

    theta = np.linspace(0, 2*np.pi, 500)
    r = A + (B*theta)
    x,y = PolaRToRect(r, theta)
    line, = ax.plot(x,y)

    ax_sliderA = plt.axes([0.2, 0.15, 0.6, 0.03])
    fig.sliderA = Slider(ax_sliderA, "A", -3, 3, valinit=A, valstep=0.05)

    ax_sliderB = plt.axes([0.2, 0.1, 0.6, 0.03])
    fig.sliderB = Slider(ax_sliderB, "B", 0, 5, valinit=B)
    
    def update(val):
        A_val = fig.sliderA.val
        B_val = fig.sliderB.val

        r = A_val + (B_val * theta)
        x,y = PolaRToRect(r, theta)

        line.set_xdata(x)
        line.set_ydata(y)
    fig.sliderA.on_changed(update)
    fig.sliderB.on_changed(update)
    

#2
def rose(fig,ax):
    ax.set_title("Rose Curve: r = A sin(Bθ) + C", pad=20)

    theta = np.linspace(0, 2*np.pi, 500)

    A = 1
    B = 1
    C = 0

    r = A * np.sin(B * theta) + C
    x, y = PolaRToRect(r, theta)

    line, = ax.plot(x, y)

    # Sliders
    ax_sliderA = plt.axes([0.2, 0.1, 0.6, 0.03])#magnitude
    fig.sliderA = Slider(ax_sliderA, "A", 0.00, 5, valinit=A, valstep=0.05)

    ax_sliderB = plt.axes([0.2, 0.05, 0.6, 0.03])#rose pdeals
    fig.sliderB = Slider(ax_sliderB, "B", 0, 10, valinit=B, valstep=1)

    ax_sliderC = plt.axes([0.2, 0.0075, 0.6, 0.03])#vertical shift
    fig.sliderC = Slider(ax_sliderC, "C", -4, 4, valinit=C, valstep=0.05)

    def update(val):
        A_val = fig.sliderA.val
        B_val = fig.sliderB.val
        C_val = fig.sliderC.val

        r = A_val * np.sin(B_val * theta) + C_val
        x, y = PolaRToRect(r, theta)

        line.set_xdata(x)
        line.set_ydata(y)
        fig.canvas.draw_idle()

    fig.sliderA.on_changed(update)
    fig.sliderB.on_changed(update)
    fig.sliderC.on_changed(update)

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