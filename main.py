import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue