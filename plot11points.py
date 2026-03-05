import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def main() -> None:
    fig = plt.figure(figsize=(7, 4.5))
    ax = fig.add_subplot()

    num_of_inputs = 11

    ax.set_xlim(0, num_of_inputs-1)
    ax.set_ylim(0, 10)

    x_vals = list(range(num_of_inputs))
    y_vals = []

    current_point = {"index": 0}

    plt.subplots_adjust(bottom=0.25)

    axbox = plt.axes([0.2, 0.1, 0.6, 0.075])
    text_box = TextBox(axbox, "Point 1: (0, _ ): ")

    def submit(text: str) -> None:
        if text.strip() == "":
            return
        try:
            x = current_point["index"]
            y = float(text)
            print(f"Point successfully plotted on ({x}, {y})")
        except ValueError:
            print("Please enter a valid number")
            text_box.set_val("")
            fig.canvas.draw_idle()
            return

        y_vals.append(y)
        current_point["index"] += 1

        text_box.set_val("")
        fig.canvas.draw_idle()

        if current_point["index"] == num_of_inputs:
            ax.plot(x_vals, y_vals, marker="o")
            plt.draw()
            text_box.set_active(False)
            print("All points plotted.")
        else:
            next_x = current_point["index"]
            text_box.label.set_text(
                f"Point {next_x + 1}: ({next_x}, _ ): "
            )

    text_box.on_submit(submit)
    plt.show()


if __name__ == "__main__":
    main()