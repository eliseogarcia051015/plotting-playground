"""
This program visualizes the Hilbert curve, a type of space-filling curve
that maps a one-dimensional line into a two-dimensional area. The curve is
generated recursively, with each iteration increasing its complexity and
level of detail. Despite being a continuous line, the Hilbert curve passes
through every point in a grid without crossing itself.
"""
import matplotlib.pyplot as plt
import math

order = 5

def window(order: int):
    fig,ax = plt.subplots(figsize=(6,6))
    fig.canvas.manager.set_window_title("Hilbert Curve Visualizer")

    print(plotPoints(order))
    plt.show()

def plotPoints(order: int):
    N = int(math.pow(2,order))
    total_points = N * N

    for i in range(total_points):
        print(i)

#order = x, 
#quandrants = math.pow(2, order), 
#total_points = quandrants * quandrants
def main():
    while(True):
        try:
            order = int(input("Enter order: "))
            if order > 0:
                break
            print("Try a positive number")
        except ValueError:
            print(f"Not a number. Try again")
    print(f"order = {order}")

    window(order)
    print("Everything successful")

if __name__ == "__main__":
    main()