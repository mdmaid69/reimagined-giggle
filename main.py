import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue