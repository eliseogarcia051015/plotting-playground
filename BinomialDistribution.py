"""
This program visualizes a simplified Galton board. Ballsfall through pins making a random 
left or right move at eachpeg with equal probability. After passing 
through all rows, each ball lands in a bin and stacks on top of previously landed balls. 
As more balls are dropped, the distribution of balls across the bins approaches a binomial
distribution, forming a bell-shaped curve.
"""

import matplotlib.pyplot as plt

class Ball:
    pass 


def main():
    fig, ax = plt.subplots(figsize=(6,6))
    fig.canvas.manager.set_window_title("Galton board")
    plt.xticks([])
    plt.yticks([])

    plt.show()

if __name__ == "__main__":
    main()