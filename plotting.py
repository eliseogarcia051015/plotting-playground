import matplotlib.pyplot as plt
import numpy as np #for creating x values

def open_window():
    """
    Creates a figure and axes object and returns them.
    """
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot()

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 10)

    ax.axhline(0, color='black', linestyle='--')  # horizontal dashed line at y=0
    ax.axvline(0, color='black', linestyle='--')  # vertical dashed line at x=0

    return fig, ax


def equation_1(ax, slope:int, translation: int, color: str) -> None:  
    """
    Docstring: simple y = mx+b line to practice graphing

    Parameters:
    ax: matplotlib.axes.Axes object to plot on
    slope: slope of the line (m)
    translation: y-intercept of the line (b)
    """ 
    x = np.linspace(-10, 10, 100) #(start, end, how many)
    y = slope * x + translation #y = mx + b
    ax.plot(x, y, color=f'{color}', label=f'y = {slope}x + {translation}')
    ax.set_title("Line Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


def euqation_2(ax, slope:int, translation: int, color: str):
    """
    Docstring: simple y = mx^2+b graph

    Parameters:
    ax: matplotlib.axes.Axes object to plot on
    slope: slope of the line (m)
    translation: y-intercept of the line (b)
    """ 
    print("nun")
    x = np.linspace(-10, 10, 100) #(start, end, how many)
    y = slope * (x*x) + translation #y = mx + b
    ax.plot(x, y, color=f'{color}', label=f'y = {slope}x + {translation}')
    ax.set_title("Line Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

def main():
    fig, ax = open_window()
    equation_1(ax, 1, 0, 'blue')
    equation_1(ax, 3, 0, 'black')
    equation_1(ax, -1/2, 0, 'green')
    euqation_2(ax, 1, 0, 'red')
    
    plt.show()

if __name__ == "__main__":
    main()