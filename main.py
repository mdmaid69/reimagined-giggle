import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue