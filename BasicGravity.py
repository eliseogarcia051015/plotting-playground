# Try to simulate a ball being dropping 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(4,5))
    fig.canvas.manager.set_window_title("Gravity Simulator")
    ax = fig.add_subplot(111)
    ax.set_xlim(0,2), ax.set_xticks([])
    ax.set_ylim(0,10), ax.set_yticks([])
    


    x = 1        #m
    y0 = 8        #m
    v0 = 0        #m/s
    g = -9.81    #m/s^2
    dt = 0.02    #second/frame
    
    ball = ax.scatter([x], [y0], color = "white", s=100)
    plt.pause(0.75)

    def update(frame):
        t = frame * dt

        y = y0 + v0*t + 0.5*g*t**2
        v = v0 + g*t
        
        if (y<=0):
            y = 0
            print(f"Hit ground at t={t:.2f}s with v={v:.2f} m/s")
            anim.event_source.stop()
        ball.set_offsets([x, y])
        return ball,

    anim = animation.FuncAnimation(fig, update, interval=5, blit=True)
    plt.show()

if __name__ == "__main__":
    main()