# Try to simulate a ball being dropping 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(4,5))
    fig.canvas.manager.set_window_title("Gravity Simulator")
    ax = fig.add_subplot(111)
    window_y_limit = 10
    ax.set_xlim(0,2), ax.set_xticks([])
    ax.set_ylim(0,window_y_limit), ax.set_yticks([])
    
    x = 1        #m
    y = 8        #m
    v = 0.00     #m/s
    g = -9.81    #m/s^2
    e = .73      #about the COR for a tennis ball
    t = 0.00     #s
    dt = 0.02    #second/frame

    time_txt = ax.text(0, 10.7, f'Time: {t}')
    vel_txt = ax.text(0.7, 10.7, f'Velocity: {v}')
    height_txt = ax.text(1.4, 10.7, f"Height: {y}")
    
    r=0.3 #ball radius
    ball = ax.scatter([x], [y+r], color = "white", edgecolors='blue', s=100)
    plt.pause(1.5)

    def update(frame):
        nonlocal y, v, t
        t += dt

        v = v + g * dt
        y = y + v * dt 
        #print(f"vel: {v:.2f} and time:{t}")

        # Bounce condition
        if y <= 0:
            y = 0
            print(f"Hit ground at t={t:.2f}s with v={v:.2f} m/s")
            v = -e * v  # reverse velocity with energy loss

            if abs(v) < 0.2:
                print("Ball stopped.")
                v = 0
                anim.event_source.stop()
        time_txt.set_text(f'Time: {t:.2f}')
        height_txt.set_text(f'Height: {y:.0f}')
        vel_txt.set_text(f'Velocity: {v:.2f}')
        fig.canvas.draw()
        ball.set_offsets([x, y+r])
        return ball, time_txt

    anim = animation.FuncAnimation(fig, update, interval=5, blit=True)
    plt.show()

if __name__ == "__main__":
    main()