"""
Prompts the user to choose how many points to plot, then collects y-values
one at a time through a text input interface. Points are plotted sequentially
on a graph with dynamically adjusting axes.
"""


import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from matplotlib.ticker import MaxNLocator


def main() -> None:
    #window figure created
    fig = plt.figure(figsize=(7, 4.5))
    ax = fig.add_subplot()

    #lower/upper bounds vars
    upper_bound = 10
    lower_bound = 0
    ax.set_ylim(lower_bound, upper_bound)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    #value vars
    x_vals = []
    y_vals = []
    current_point = {"index": 0}
    num_of_inputs = {"value": 0}

    plt.subplots_adjust(bottom=0.25)

    #box for getting number of inputs
    axbox1 = plt.axes([0.5, 0.075, 0.4, 0.075])
    prompt_box = TextBox(axbox1, "How many points would you like to plot: ")

    #box for receiving y values
    axbox2 = plt.axes([0.275, 0.075, 0.6, 0.075])
    text_box = TextBox(axbox2, "Point 1: (0, _ ): ")
    axbox2.set_visible(False)
    text_box.set_active(False)


    def set_x(text: str) -> None:
        if num_of_inputs["value"] != 0:
            return
        try:
            n = int(text)
            if n <= 0:
                print("Enter a positive integer.")
                return
        except ValueError:
            print("Not a valid integer.")
            return

        num_of_inputs["value"] = n
        ax.set_xlim(0, n-1)

        prompt_box.set_active(False)
        axbox1.set_visible(False)

        axbox2.set_visible(True)
        text_box.set_active(True)
        fig.canvas.draw_idle()

    def submit_y(text: str) -> None:
        if text.strip() == "":
            return
        try:
            y = float(text)
            if (y%1==0):
                y=int(y)
        except ValueError:
            print("Enter a valid number")
            text_box.set_val("")
            return

        x = current_point["index"]

        x_vals.append(x)
        y_vals.append(y)

        print(f"Point successfully plotted on ({x}, {y})")

        # adjust bounds if needed
        nonlocal lower_bound, upper_bound
        if y > upper_bound:
            upper_bound = y * 1.1
        if y < lower_bound:
            lower_bound = y * 1.1
        ax.set_ylim(lower_bound, upper_bound)

        ax.plot(x_vals, y_vals, marker="o", color="blue")
        text_box.set_val("")
        current_point["index"] += 1

        if current_point["index"] == num_of_inputs["value"]:
            text_box.set_active(False)
            axbox2.set_visible(False)
            plt.subplots_adjust(bottom=0.1)
            fig.canvas.draw_idle()
            ax.set_title("All points plotted!", y=1.05)
            print("All points plotted.")
        else:
            next_x = current_point["index"]
            text_box.label.set_text(f"Point {next_x+1}: ({next_x}, _): ")
            plt.draw()

    #submit and display everything
    prompt_box.on_submit(set_x)
    text_box.on_submit(submit_y)
    plt.show()


if __name__ == "__main__":
    main()