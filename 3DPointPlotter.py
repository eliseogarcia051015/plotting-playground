'''
Experiments with plotting points in a 3D coordinate system using Matplotlib.
Allows the user to enter x, y, and z coordinates
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import TextBox, Slider, Button
import numpy as np


def window():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    fig.canvas.manager.set_window_title("3D Point Plotter")

    #disable dragging and moving around
    ax._rotate_btn = []   # disables rotation
    ax._zoom_btn = []     # disables zoom
    ax._pan_btn = []      # disables pan
    fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id) 

    coords1 = [x.strip() for x in input("Enter values (x, y, z): ").split(" ")] 
    ax.scatter3D(coords1[0], coords1[1], coords1[2])
    ax.scatter3D(0.0,0.0,0.0)
    plt.show()

def main():
    window()

if __name__ == "__main__":
    main()