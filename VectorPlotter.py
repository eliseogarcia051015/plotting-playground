"""
Should be similar to point plotter but with vectors instead of pointa
"""

import matplotlib.pyplot as plt

def main():
    fig = plt.figure(figsize=(5,5))
    fig.canvas.manager.set_window_title("Vector Plotter")

    plt.show()

if __name__ == "__main__":
    main