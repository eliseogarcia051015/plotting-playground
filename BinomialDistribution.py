"""
This program visualizes a simplified Galton board. Ballsfall through pins making a random 
left or right move at eachpeg with equal probability. After passing 
through all rows, each ball lands in a bin and stacks on top of previously landed balls. 
As more balls are dropped, the distribution of balls across the bins approaches a binomial
distribution, forming a bell-shaped curve.
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ROWS = 8
BALL_RADIUS = 0.15
STEP_SIZE = 0.20

class Ball:
    def __init__(self, start_x=0.0, start_y=0.0):
        self.x = start_x
        self.y = start_y
        self.current_row = 0
        self.current_col = 0
        self.is_done = False

    def choose_next_target(self):
        if self.current_row >= ROWS:
            self.is_done = True
            return

        move = random.choice([0, 1])
        
        self.current_row += 1
        self.current_col += move
        
        self.target_y = -self.current_row
        self.target_x = self.current_col - (self.current_row * 0.5)

    def update(self):
        # move toward target
        # if arrived, choose next target
        pass

    
class GaltonBoard:
    def create_board():
    
        pass

    def update(frame):
    
        pass

def main():
    fig, ax = plt.subplots(figsize=(6,6))
    fig.canvas.manager.set_window_title("Galton board")
    plt.xticks([])
    plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()

##
# N=x
# pins=x(x+1)/2
# outcomes = x+1
##