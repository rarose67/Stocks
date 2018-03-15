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

    def get_symb(self):
        return self.symbol
        
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
        
    def get_var(self):
        return self.varience

    def get_div(self):
        return self.dividend

    def set_var(self, new_var):
        self.varience = new_var

    def set_div(self, change_in_div):
        self.dividend += change_in_div

    def set_price(self, curr_price):
        self.price = curr_price

    def avg_change(self, start_price, days):
        """Return the average change in the stock's price after a given number of days."""

        return ((self.price - start_price) / days)

    def trading_day(self):
        change = uniform(-(self.varience), self.varience)
        change = round(change, 2)
    
        self.price += change

    def buy_shares(self, num_shares):
        self.shares += num_shares

def quarter(stock, money):
    money += (stock.get_div() / 4 )
    new_shares = (money // stock.get_price())
    stock.buy_shares(new_shares)
    money = money - (new_shares * stock.get_price())
    return money

    
