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
    #implement me
    fig = plt.figure(figsize=(7,4.5))
    ax = fig.add_subplot()
    upper_bound = 10
    lower_bound = 0
    ax.set_ylim(lower_bound, upper_bound)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    axbox1 = plt.axes([0.5, 0.075, 0.4, 0.075])
    prompt_box = TextBox(axbox1, "How many points would you like to plot: ")
    plt.show()


def linear():
    #implement me
    print()

def main():
    window()
    print("Nothing so far")


if __name__ == "__main__":
    main()

