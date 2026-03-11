import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox
from matplotlib.ticker import MaxNLocator
import numpy as np


"""
Interactive Function Visualizer

This program opens a graphical window where the user can select a type of
function to graph. After choosing a function, sliders appear that allow the
user to dynamically modify parameters of the function and observe how the
graph changes in real time.

Currently supported functions:
    1. Linear
    2. Quadratic (to be implemented)
    3. Sine (to be implemented)
    4. Cosine (to be implemented)
"""


def window(lower_bound, upper_bound):
    """
    Creates the main plotting window and prompts the user to choose
    a type of function to graph.

    Parameters
    ----------
    lower_bound : int or float
        Minimum value for both the x and y axes.
    upper_bound : int or float
        Maximum value for both the x and y axes.

    Behavior
    --------
    - Initializes the plotting window
    - Displays coordinate axes and grid
    - Prompts the user to select a function via a TextBox
    - Calls the appropriate graphing function based on user input
    """

    fig, ax = plt.subplots(figsize=(7,4.5))
    plt.subplots_adjust(bottom=0.2)
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_ylim(lower_bound, upper_bound)
    ax.set_xlim(lower_bound, upper_bound)
    plt.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    axbox1 = plt.axes([0.725, 0.05, 0.175, 0.075])
    prompt_box = TextBox(axbox1, "Choose a graph: Linear(1), Quadratic(2), Sine(3), Cosine(4): ")
    def choose(text):
        """
        Handles user input from the TextBox and calls the appropriate
        graphing function.
        """
        try:
            n = int(text)
            if n<0:
                raise ValueError("Please enter a valid int")
        except ValueError:
            print("Enter a valid number")
            prompt_box.set_val("")
            return
        prompt_box.set_active(False)
        axbox1.set_visible(False)
        if n == 1:
            linear(fig, ax)
        elif n == 2:
            quadratic(fig, ax)
        elif n == 3:
            sine(fig, ax)
        elif n == 4:
            cosine(fig, ax)
        fig.canvas.draw_idle()
    prompt_box.on_submit(choose)
    plt.show()


def linear(fig,ax):
    """
    Plots a linear function and provides sliders to interactively
    modify its parameters.

    Linear equation:
        y = Ax + B

    Sliders
    -------
    A : controls the slope of the line
    B : controls the vertical shift
    """
    ax.set_title("Linear equation = Ax + B", y=1.05)
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 300)
    A = 1
    B = 0
    y = (A*x) + B
    line, = ax.plot(x,y)

    ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='yellow')
    fig.sliderA = Slider(ax_slider, "A", -3, 3   , valinit=A)

    ax_slider2 = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='red')
    fig.sliderB = Slider(ax_slider2, "B", -5, 5, valinit=B)

    def update(val):
        """
        Updates the graph whenever a slider value changes.
        """
        A_val = fig.sliderA.val
        B_val = fig.sliderB.val

        y = (A_val * x) + B_val
        line.set_ydata(y)
        fig.canvas.draw_idle()

    fig.sliderA.on_changed(update)
    fig.sliderB.on_changed(update)


#called function if prompt equals this, slider transforms function
#Quadratic: y = Ax^2 + B
def quadratic(fig, ax):
    #implement me too
    print("Test2")


#called function if prompt equals this, slider transforms function
#Sine: y = Asin(Bx)+C
def sine(fig, ax):
    #implement me three
    print("Test3")


#called function if prompt equals this, slider transforms function
#Cosine: y= Acos(Bx)+C
def cosine(fig, ax):
    #implement me four
    print("Test4")


#main function
def main():
    window(-10, 10)
    print("Program done")


if __name__ == "__main__":
    main()

