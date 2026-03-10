#basic idea before I forget. Open a window, user inters option in the textbox, the it graphs functions
#like linear, quadratic, sine, cosine, maybe more
#There should also be a slider that changes stuff
#linear: y= Ax + B
#sine: y= Asin(Bx)+C
#Quadratic: y = Ax^2 + B
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox
from matplotlib.ticker import MaxNLocator

def window():
    fig, ax = plt.subplots(figsize=(7,4.5))
    plt.subplots_adjust(bottom=0.2)
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    lower_bound = -10
    upper_bound = 10
    ax.set_ylim(lower_bound, upper_bound)
    ax.set_xlim(lower_bound, upper_bound)
    plt.grid(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    axbox1 = plt.axes([0.725, 0.05, 0.175, 0.075])
    prompt_box = TextBox(axbox1, "Choose a graph: Linear(1), Quadratic(2), Sine(3), Cosine(4): ")
    def choose(text):
        try:
                n = int(text)
        except ValueError:
            print("Enter a valid number")
            prompt_box.set_val("")
            return
        prompt_box.set_active(False)
        axbox1.set_visible(False)
        if n == 1:
            linear(fig, ax)
        elif n == 2:
            quadratic(fig, ax)
        elif n == 3:
            sine(fig, ax)
        elif n == 4:
            cosine(fig, ax)
        fig.canvas.draw_idle()
    prompt_box.on_submit(choose)
    plt.show()




def linear(fig,ax):
    #implement me
    ax.set_title("Y = Ax + B", y=1.05)
    print("Test1")

def quadratic(fig, ax):
    #implement me too
    print("Test2")

def sine(fig, ax):
    #implement me three
    print("Test3")

def cosine(fig, ax):
    #implement me four
    print("Test4")

def main():
    window()
    print("Nothing so far")


if __name__ == "__main__":
    main()

