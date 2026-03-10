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
    fig = plt.figure(figsize=(7,4.5))
    ax = fig.add_subplot()
    lower_bound = 0
    upper_bound = 10
    ax.set_ylim(lower_bound, upper_bound)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    axbox1 = plt.axes([0.725, 0.01, 0.175, 0.075])
    prompt_box = TextBox(axbox1, "Choose a graph: Linear(1), Quadratic(2), Sine(3), Cosine(4): ")
    def choose(text):
        try:
            n = int(text)
            if n in [1,2,3,4]:
                prompt_box.set_active(False)
                axbox1.set_visible(False)
                match n:
                    case 1:
                        linear()
                    case 2:
                        quadratic()
                    case 3:
                        sine()
                    case 4:
                        cosine()
        except ValueError:
            print("Not a valid integer.")
            prompt_box.set_val("")
            return
        fig.canvas.draw_idle()
    prompt_box.on_submit(choose)
    plt.show()


def linear():
    #implement me
    print("Test1")

def quadratic():
    #implement me too
    print("Test2")

def sine():
    #implement me three
    print("Test3")

def cosine():
    #implement me four
    print("Test4")

def main():
    window()
    print("Nothing so far")


if __name__ == "__main__":
    main()

