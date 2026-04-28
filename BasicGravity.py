# Try to simulate a ball being dropping 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(4,5))
    fig.canvas.manager.set_window_title("Gravity Simulator")
    ax = fig.add_subplot(111)
    ax.set_xlim(0,1), ax.set_xticks([])
    ax.set_ylim(0,1.2), ax.set_yticks([])
    plt.pause(1)

    x,y = 0.5, 1.1
    SPEEDY = 0.01
    
    ball = ax.scatter([x], [y], color = "white", s=100)

    def update(frame):
        nonlocal y, SPEEDY
        y = y - SPEEDY
        
        ball.set_offsets([0.5, y])
        if (y<0):
            y = 0
            SPEEDY = 0
        return ball,

    anim = animation.FuncAnimation(fig, update, frames=100, interval=1, blit=True)
    plt.show()

if __name__ == "__main__":
    main()