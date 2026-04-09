"""
Imma probably clean this up later, but this file is basically inspired by LeetCode 121 (Best Time to Buy and Sell Stock).

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




def main():
    print("How many days would you like to simulate?")
    while True:
        try:
            days = int(input("Days: "))
            print(f"You have chosen {days} days")
            break
        except ValueError:
            print("Not valid. Enter a number\n")

if __name__ == "__main__":
    main()