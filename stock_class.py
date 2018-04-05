from random import uniform

class Stock:
    """This class represents a stock that is traded daily on the stock market."""

    def __init__(self, init_symb, init_name, init_shares, init_price, init_var, init_div):
        self.symbol = init_symb
        self.name = init_name
        self.shares = init_shares
        self.price = init_price
        self.varience = init_var
        self.dividend = init_div
        self.weekly_start_price = init_price
        self.days_held = 0

    def get_symb(self):
        return self.symbol
        
    def get_name(self):
        return self.name

    def get_shares(self):
        return self.shares

    def get_price(self):
        return self.price
        
    def get_var(self):
        return self.varience

    def get_div(self):
        return self.dividend

    def get_wk_price(self):
        return self.weekly_start_price

    def get_days_held(self):
        return self.days_held

    def set_var(self, new_var):
        self.varience = new_var

    def set_div(self, change_in_div):
        self.dividend += change_in_div

    def set_price(self, curr_price):
        self.price = curr_price

    def set_wk_price(self):
        self.weekly_start_price = self.price

    def avg_change(self, start_price, days):
        """Return the average change in the stock's price after a given number of days."""

        return ((self.price - start_price) / days)

    def trade(self):
        """Simulate a day of trading"""

        change = uniform(-(self.varience), self.varience) #change in price is a random number between the negative a positive variance of the stock price.
        change = round(change, 2)
    
        self.price += change

        #if the stock price becomes negative, reset it to 0. 
        if (self.price < 0):
            self.price = 0.00
        
        self.days_held += 1

    def buy_shares(self, num_shares):
        self.shares += num_shares

def quarter(stock, money):
    """Use stock dividends to buy more shares"""

    money += round(((stock.get_div() / 4 ) * stock.get_shares()), 2)
    new_shares = (money // stock.get_price())
    stock.buy_shares(new_shares)
    print("Bought {0} shares of {1} at ${2}".format(new_shares, stock.get_symb() ,stock.get_price()))
    money = round((money - (new_shares * stock.get_price())), 2)
    return money

def market_open(dotw, date):
    """Determine if the stock market is open"""

    if ((dotw % 6 == 0) or (dotw % 7 == 0) or (date == 1) or (date == 15) or (date == 50) or (date == 89) or (date == 148) or (date == 185) or (date == 246) or (date == 326) or (date == 359)):
        return False
    else:
        return True
    
def main():
    Ford = Stock("F", "Ford", 800, 11.33, 0.50, 0.60)

    money = 0.0
    days = 365
    day_of_the_week = 1
    trading_days_this_week = 0
    new_quarter = False

    for day in range(1, days+1):
        if(market_open(day_of_the_week, day)):
            Ford.trade()
            trading_days_this_week += 1
            
            #Each quarter, buy more shares with the dividends. 
            if(day % 90 == 0) or new_quarter:
                money = quarter(Ford, money)
                new_quarter = False
        else:
            #If the market is closed.
            if(day % 90 == 0):
                new_quarter = True

            if (day_of_the_week % 7 == 0): #If it's Sunday, re-evaluate the daily varience of the stock price.  Also, reset counters. 
                Ford.avg_change(Ford.get_wk_price(), trading_days_this_week)
                Ford.set_wk_price()
                trading_days_this_week = 0
                day_of_the_week = 0

        day_of_the_week += 1


    print("You have", Ford.get_shares(), "shares of", Ford.get_symb(), "at $", Ford.get_price(), "and have $", money, "left to invest.")

if (__name__ == "__main__"):
    main()