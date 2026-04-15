"""
Imma probably clean this up later, but this file is basically inspired by LeetCode 121 (Best Time to Buy and Sell Stock).
----------Leetcode121-----------
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
----------------------------------
The idea is to use numpy to generate random stock prices over time and matplotlib (kinda like a point plotter) to visualize it. 
Each "day" adds a new point to the graph (x = day, y = price).

There might be a button like "Generate next day" that adds the next point. When a new point is added, the line between the previous point and the new one is:
- green if the price went up
- red if the price went down

So visually you can see the trend as it builds.
At the same time, the terminal prints out what the best buy/sell decision would be based on the data so far (like the actual LeetCode problem). 
It keeps updating as more days are added.

The program will probably ask for some input at the start, like:
- how many days to simulate
- the max range for the random prices [0, x]

Example flow:
---------------------------------------------------------------------------------------------------------------------
terminal: Enter how many days to simulate
user: 5

terminal: Enter random numbers range [0, X]
user: x = 10


Day 0
Prices: [7]
*Only point plotted is (0, 7)*
Msg: Not enough info yet to decide when to buy/sell


Day 1
Prices: [7, 6]
*Points: (0,7), (1,6)*
Msg: Don't buy, you would've lost money. Best profit = 0


Day 2
Prices: [7, 6, 4]
*Points: (0,7), (1,6), (2,4)*
Msg: Don't buy, you would've lost money. Best profit = 0


Day 3
Prices: [7, 6, 4, 5]
*Points: (0,7), (1,6), (2,4), (3,5)*
Msg: Buy on Day 2 ($4), sell on Day 3 ($5). Profit = 1


Day 4
Prices: [7, 6, 4, 5, 1]
*Points: (0,7), (1,6), (2,4), (3,5), (4,1)*
Msg: Same best move as before. Profit = 1


Day 5
Prices: [7, 6, 4, 5, 1, 10]
*Points: (0,7), (1,6), (2,4), (3,5), (4,1), (5,10)*
Msg: Buy on Day 4 ($1), sell on Day 5 ($10). Profit = 9


*maybe later add something like having a budget instead of just 1 stock*
"""

import matplotlib
matplotlib.use('TkAgg')  # or 'Agg' if you don't need a window
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


def main():
    print("How many days would you like to simulate?")
    while True:
        try:
            days = int(input("Days: "))
            break
        except ValueError:
            print("Not valid. Enter a number\n")
    while True:
        try:
            limit = int(input("Enter random numbers range: "))
            break
        except ValueError:
            print("Not valid. Enter a number\n")
    print(f"You have chosen {days} days")
    print(f"You have selected [0, {limit}]")
    print("---------"*5)
    window(days, limit)

def window(days, limit):
    plt.ion()
    fig = plt.figure(figsize=(10,10))
    fig.canvas.manager.set_window_title("Stock Market Simulation")
    ax = fig.add_subplot()
    plt.grid(True)

    upper_bound = 10
    lower_bound = 0
    ax.set_xlim(0, days - 1)
    ax.set_ylim(lower_bound, upper_bound)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    rng = np.random.default_rng()
    prices = rng.integers(0,limit+1, size=days)
    all_stocks = []
    for day in range(days):
        curr_stock = prices[:day + 1]
        all_stocks = curr_stock

        print(f"\nDay {day}")
        print(f"Prices: {prices[day]}")
        maxprofit, buydate, selldate = maxProfit(curr_stock)
        if day == 0:
            msg = "Not enough info yet to decide."
        elif maxprofit == 0:
            msg = "Don't buy, no profit possible yet."
        else:
            msg = f"Buy on Day {buydate} (${prices[buydate]}), Sell on Day {selldate} (${prices[selldate]}). Profit = {maxprofit}"
        print(f"This is the highest profit you can make {maxprofit}. Buy on day {buydate}. Sell on day {selldate}") #delete this later
        print(f"Msg: {msg}")


        ax.plot(day, prices[day], marker="o", color="blue")
        if day > 0:
            prev_price = prices[-1]
            color = "green" if prices[day] > prev_price else "red"
            ax.plot([day-1, day], [prev_price, prices[day]], color=color)

        if prices[day] > upper_bound:
            upper_bound = prices[day] * 1.1
        if prices[day] < lower_bound:
            lower_bound = prices[day] * 1.1
        ax.set_ylim(lower_bound, upper_bound)

        plt.show()

        input("Press [enter] to continue \n")
    print(f"Array of all prices: {all_stocks}")



    input("Press enter to end the program")
    #plt.show()

def maxProfit(prices) -> int:
        buy, sell = 0, 1 ##L/R pointers
        maxP, maxB, maxS = 0, 0, 0

        while sell < (len(prices)):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
                maxB = buy
                maxS = sell
            else:
                buy = sell
            sell += 1
        return maxP, maxB, maxS

if __name__ == "__main__":
    main()