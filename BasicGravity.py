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
    time_txt = ax.text(0.3, 10.7, f'Time: 0.00', animated=True)
    
    x = 1        #m
    y= 8       #m
    v = 0       #m/s
    g = -9.81    #m/s^2
    e = .73    #about the COR for a tennis ball
    t = 0
    dt = 0.02    #second/frame
    
    ball = ax.scatter([x], [y], color = "white", s=100)
    plt.pause(0.75)

    def update(frame):
        nonlocal y, v, t
        t += dt

        v = v + g * dt
        y = y + v * dt

        
        #print(f"vel: {v:.2f} and time:{t}")
        time_txt.set_text(f'Time: {t:.2f}')

        # Bounce condition
        if y <= 0:
            y = 0
            print(f"Hit ground at t={t:.2f}s with v={v:.2f} m/s")
            v = -e * v  # reverse velocity with energy loss

            if abs(v) < 0.2:
                print("Ball stopped.")
                v = 0
                anim.event_source.stop()
        ball.set_offsets([x, y])
        return ball, time_txt

    anim = animation.FuncAnimation(fig, update, interval=5, blit=True)
    plt.show()

if __name__ == "__main__":
    main()