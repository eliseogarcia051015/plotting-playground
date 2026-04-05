'''
ADD Description later. Simple thingy to learn how to use 3d matplot thingy
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import TextBox, Slider, Button
import numpy as np


def window():
    ax = plt.figure().add_subplot(projection='3d')
    plt.show()

def main():
    window()

if __name__ == "__main__":
    main()