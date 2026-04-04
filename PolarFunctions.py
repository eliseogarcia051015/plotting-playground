""""
Similar to "function_transformer.py" but instead of being in cartesian coordinates,
this program will handle functions in the polar plane (r = f(\theta)). I think
I want to keep the idea of sliders, but look into how that implementation will look
like given things like petals

Functions:
    1. Spiral           r = A + Bθ
    2. Rose Curve       r = A sin(Bθ) + C
    3. Cardioid         r = A(1 + cos(θ))
    4. Cosine Rose      r = A[cos(Bθ)]
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import TextBox, Slider, Button
import numpy as np


def window():
    lower_bound,upper_bound =2*-np.pi,2*np.pi

    fig, ax = plt.subplots(figsize=(7,7))
    fig.canvas.manager.set_window_title("Polar Function Visualizer")
    plt.subplots_adjust(bottom=0.2)
    fig.slider_axes = [] 
    fig.choose_ax = None
    fig.prompt_box = None

    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_ylim(lower_bound, upper_bound)
    ax.set_xlim(lower_bound, upper_bound)
    ax.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    choose(fig, ax)

    zoom_in_ax = plt.axes([0.05, 0.92, 0.1, 0.05]) 
    zoom_in_button = Button(zoom_in_ax, "+") 
    zoom_in_button.on_clicked(lambda event: zoom(event, ax, fig, factor=0.75))

    zoom_out_ax = plt.axes([0.15, 0.92, 0.1, 0.05]) 
    zoom_out_button = Button(zoom_out_ax, "-") 
    zoom_out_button.on_clicked(lambda event: zoom(event, ax, fig, factor=1.33))

    reset_ax = plt.axes([0.85, 0.92, 0.1, 0.05]) 
    reset_button = Button(reset_ax, "Reset") 
    reset_button.on_clicked(lambda event: reset(event, fig, ax))
    plt.show()


def choose(fig, ax):
    axbox = plt.axes([0.725, 0.05, 0.175, 0.075])
    fig.choose_ax = axbox
    prompt_box = TextBox(axbox, "Choose a graph: Spiral(1), Rose Curve(2), Cardioid(3), Cosine Rose(4): ")
    fig.prompt_box = prompt_box #reference to it needed for better resetting
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
        
        if getattr(fig, 'choose_ax', None) is not None:
            fig.prompt_box.disconnect_events() #kill listeners
            fig.prompt_box = None
            fig.choose_ax.remove()
            fig.choose_ax = None
        fig.canvas.draw_idle()

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


def zoom(event, ax, fig, factor):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    x_mid = (xlim[0] + xlim[1]) / 2
    y_mid = (ylim[0] + ylim[1]) / 2
    x_range = (xlim[1] - xlim[0]) * factor / 2
    y_range = (ylim[1] - ylim[0]) * factor / 2
    ax.set_xlim(x_mid - x_range, x_mid + x_range)
    ax.set_ylim(y_mid - y_range, y_mid + y_range)
    fig.canvas.draw_idle()


def reset(event, fig, ax):
    if getattr(fig, 'prompt_box', None) is not None:
        fig.prompt_box.disconnect_events()
        fig.prompt_box = None
    if getattr(fig, 'choose_ax', None) is not None:
        fig.choose_ax.remove()
        fig.choose_ax = None
    for sax in getattr(fig, 'slider_axes', []):
        sax.remove()
    fig.slider_axes = []
    for attr in ('sliderA', 'sliderB', 'sliderC'):
        if hasattr(fig, attr):
            delattr(fig, attr)
    ax.clear()
    lower_bound, upper_bound = -2 * np.pi, 2 * np.pi
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_xlim(lower_bound, upper_bound)
    ax.set_ylim(lower_bound, upper_bound)
    ax.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    choose(fig, ax)
    fig.canvas.draw_idle()

def PolaRToRect(r, theta):# x = rcos(theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

#scaling 

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
    line, = ax.plot(x,y, color="steelblue")

    ax_sliderA = plt.axes([0.2, 0.15, 0.6, 0.03])
    fig.sliderA = Slider(ax_sliderA, "A", -3, 3, valinit=A, valstep=0.05)

    ax_sliderB = plt.axes([0.2, 0.1, 0.6, 0.03])
    fig.sliderB = Slider(ax_sliderB, "B", 0, 5, valinit=B)

    fig.slider_axes = [ax_sliderA, ax_sliderB] 
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

    fig.slider_axes = [ax_sliderA, ax_sliderB, ax_sliderC]
    ax.set_title(f"Rose Curve: r = {A}sin({B}θ) + {C}", pad=20)
    def update(val):
        A_val = fig.sliderA.val
        B_val = fig.sliderB.val
        C_val = fig.sliderC.val

        A, B, C = A_val, B_val, C_val
        ax.set_title(f"Rose Curve: r = {A:.2f}sin({B}θ) + {C:.2f}", pad=20)

        r = A_val * np.sin(B_val * theta) + C_val
        x, y = PolaRToRect(r, theta)

        line.set_xdata(x)
        line.set_ydata(y)
        fig.canvas.draw_idle()

    fig.sliderA.on_changed(update)
    fig.sliderB.on_changed(update)
    fig.sliderC.on_changed(update)

#3
def cardioid(fig,ax): # r = a(1 + cos(theta))
    print("Nothing so far (3)")
    ax.set_title("Cardioid: ")

#4
def cosine_rose(fig,ax):
    print("Nothing so far (4)")

def main():
    window()

if __name__ == "__main__":
    main()