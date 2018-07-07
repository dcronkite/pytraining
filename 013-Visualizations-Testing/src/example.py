import pandas as pd


def add_two(num):
    return num + 2


def convert_sas_date(df_column, unit='s'):
    return pd.to_timedelta(df_column, unit=unit) + pd.datetime(1960, 1, 1)


class ShoppingCart:

    def __init__(self, tax_rate=0.1):
        self.items = {}
        self.coupons = {}
        self.tax_rate = tax_rate

    def add_item(self, name, cost, quantity=1):
        self.items[name] = cost * quantity
        # total_cost = cost * quantity
        # self.cost += total_cost

    def add_coupon(self, name, amount):
        self.coupons[name] = amount

    def remove_item(self, name):
        # total_cost = self.items[name]
        # self.cost -= total_cost
        del self.items[name]

    def get_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += self.items[item]
            if item in self.coupons:
                total_cost -= self.coupons[item]
        return total_cost + total_cost * self.tax_rate
