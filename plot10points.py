import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def main() -> None:
    fig = plt.figure(figsize=(7, 4.5))
    ax = fig.add_subplot()

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    x_vals = list(range(11))
    y_vals = []

    current_point = {"index": 0}

    plt.subplots_adjust(bottom=0.25)

    axbox = plt.axes([0.2, 0.1, 0.6, 0.075])
    text_box = TextBox(axbox, "Point 1 (0, y): ")

    def submit(text: str) -> None:
        try:
            y = float(text)
        except ValueError:
            print("Please enter a number.")
            text_box.set_val("")
            return

        y_vals.append(y)
        current_point["index"] += 1

        text_box.set_val("")
        
        if current_point["index"] == 11:
            ax.plot(x_vals, y_vals, marker="o")
            plt.draw()
            text_box.set_active(False)
            print("All points plotted.")
        else:
            next_x = current_point["index"]
            text_box.label.set_text(
                f"Point {next_x + 1} ({next_x}, y): "
            )

    text_box.on_submit(submit)

    plt.show()


if __name__ == "__main__":
    main()