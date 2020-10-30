# Given an array of numbers that represent stock prices
# Where each number is the price for a certain day
# Find two days when you should buy and sell your stock for...
# ...the highest profit
# For instance stockBuySell([110, 180, 260, 40, 310, 535, 695])
# The code should produce "buy on day 4 sell on day 7"

def sort_buy_sell(array):
    # Counters, why are they so many lol 🧐
    buycounter = 0
    sellcounter = 0
    counter = 0
    sell = 0
    buy = array[0]
    for count in array:
        counter = counter + 1
        if sell < count:
            sell = count
            sellcounter = counter
        if buy > count:
            buy = count
            buycounter = counter
    print("buy", buy, "sell", sell)
    print("Buy on day", buycounter, "sell on", sellcounter)

# Activating the function


array = [110, 180, 260, 40, 310, 535, 695]
sort_buy_sell(array)
