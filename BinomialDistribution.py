"""
This program visualizes a simplified Galton board. Balls fall through pins making a random 
left or right move at each peg with equal probability. After passing 
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
    def __init__(self, start_x=0.0, start_y=1.0):
        self.x = start_x
        self.y = start_y
        self.current_row = 0
        self.current_col = 0
        self.target_x = start_x
        self.target_y = start_y
        self.is_done = False
        
        # Pick the very first target (row 1)
        self.choose_next_target()

    def choose_next_target(self):
        if self.current_row >= ROWS:
            self.is_done = True
            return

        move = random.choice([0, 1])
        
        self.current_row += 1
        self.current_col += move
        
        # Set next target coordinates based on your triangle spacing
        self.target_y = -self.current_row
        self.target_x = self.current_col - (self.current_row * 0.5)

    def update(self):
        # Smoothly interpolate current position toward target position
        if not self.is_done:
            self.x += (self.target_x - self.x) * 0.2
            self.y += (self.target_y - self.y) * 0.2
            
            # If close enough to target, snap and choose the next drop row
            if abs(self.x - self.target_x) < 0.01 and abs(self.y - self.target_y) < 0.01:
                self.x = self.target_x
                self.y = self.target_y
                if self.current_row >= ROWS:
                    self.is_done = True
                else:
                    self.choose_next_target()

class Pin:
    @staticmethod
    def get_pins():
        pins_x = []
        pins_y = []
        for r in range(1, ROWS + 1):
            for c in range(r + 1):
                pins_x.append(c - (r / 2.0))
                pins_y.append(-r)
        return pins_x, pins_y
    
class GaltonBoard:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(7, 7))
        self.fig.canvas.manager.set_window_title("Galton board")
        
        self.ax.set_xlim(-ROWS / 2 - 2, ROWS / 2 + 2)
        self.ax.set_ylim(-ROWS - 4, 2)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Static pins
        pins_x, pins_y = Pin.get_pins()
        self.ax.scatter(pins_x, pins_y, color='black', s=30, zorder=3)
        
        # Bin dividers
        for i in range(ROWS + 2):
            bx = i - 0.5 - (ROWS / 2.0)
            self.ax.vlines(bx, -ROWS - 1, -ROWS - 3.2, color='gray', linestyle='--', alpha=0.6)

        self.bin_counts = [0] * (ROWS + 1)
        self.active_balls = []
        self.stacked_x = []
        self.stacked_y = []

        # Artists for animation
        self.ball_scatter = self.ax.scatter([], [], color='crimson', s=40, zorder=4)
        self.stacked_scatter = self.ax.scatter([], [], color='dodgerblue', s=25, zorder=2)

    def update(self, frame):
        # Spawn a new ball periodically
        if frame % 5 == 0:
            self.active_balls.append(Ball(start_x=0.0, start_y=0.0))

        still_active = []
        for ball in self.active_balls:
            ball.update()
            if ball.is_done:
                # Land into the bin and stack vertically
                bin_idx = ball.current_col
                if 0 <= bin_idx <= ROWS:
                    self.bin_counts[bin_idx] += 1
                    height = self.bin_counts[bin_idx]
                    self.stacked_x.append(bin_idx - (ROWS / 2.0))
                    self.stacked_y.append(-ROWS - 1.1 - (height * 0.12))
            else:
                still_active.append(ball)
        
        self.active_balls = still_active

        # Refresh scatter plots
        if self.active_balls:
            self.ball_scatter.set_offsets([(b.x, b.y) for b in self.active_balls])
        else:
            self.ball_scatter.set_offsets([])

        if self.stacked_x:
            self.stacked_scatter.set_offsets(list(zip(self.stacked_x, self.stacked_y)))

        return self.ball_scatter, self.stacked_scatter

def main():
    board = GaltonBoard()
    ani = animation.FuncAnimation(
        board.fig, 
        board.update, 
        frames=600, 
        interval=30, 
        blit=True, 
        repeat=True
    )
    plt.show()

if __name__ == "__main__":
    main()