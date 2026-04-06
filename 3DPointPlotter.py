'''
ADD Description later. Simple thingy to learn how to use 3d matplot thingy
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
    plt.show()

def main():
    window()

if __name__ == "__main__":
    main()